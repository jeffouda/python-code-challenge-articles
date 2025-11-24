from lib.classes.many_to_many import Author, Magazine, Article


class TestMagazine:
    """Class Magazine in many_to_many.py"""

    def test_has_name(self):
        """Magazine is initialized with a name"""
        magazine = Magazine("Vogue", "Fashion")
        assert magazine.name == "Vogue"

    def test_name_is_mutable_string(self):
        """magazine name is mutable string"""
        magazine = Magazine("Vogue", "Fashion")

        # Check that name is of type str
        assert isinstance(magazine.name, str)

        # Check that name can be changed
        magazine.name = "New Vogue"
        assert magazine.name == "New Vogue"

    def test_name_is_valid(self):
        """name is between 2 and 16 characters"""
        # Test valid name
        magazine = Magazine("Vogue", "Fashion")
        assert magazine.name == "Vogue"

        # Test short name
        try:
            Magazine("A", "Fashion")
            assert False, "Short name should raise exception"
        except ValueError:
            assert True
        except Exception as e:
            assert False, f"Unexpected exception: {e}"

        # Test long name
        try:
            Magazine("This is a very long magazine name", "Fashion")
            assert False, "Long name should raise exception"
        except ValueError:
            assert True
        except Exception as e:
            assert False, f"Unexpected exception: {e}"

    def test_has_category(self):
        """Magazine is initialized with a category"""
        magazine = Magazine("Vogue", "Fashion")
        assert magazine.category == "Fashion"

    def test_category_is_mutable_string(self):
        """category is mutable string"""
        magazine = Magazine("Vogue", "Fashion")

        # Check that category is of type str
        assert isinstance(magazine.category, str)

        # Check that category can be changed
        magazine.category = "Lifestyle"
        assert magazine.category == "Lifestyle"

    def test_category_is_valid(self):
        """category is longer than 0 characters"""
        # Test valid category
        magazine = Magazine("Vogue", "Fashion")
        assert magazine.category == "Fashion"

        # Test empty category
        try:
            Magazine("Vogue", "")
            assert False, "Empty category should raise exception"
        except ValueError:
            assert True
        except Exception as e:
            assert False, f"Unexpected exception: {e}"

    def test_has_many_articles(self):
        """magazine has many articles"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author, magazine, "How to wear a tutu with style")
        article_2 = Article(author, magazine, "Dating life in NYC")

        assert len(magazine.articles()) == 2
        assert article_1 in magazine.articles()
        assert article_2 in magazine.articles()

    def test_articles_of_type_article(self):
        """magazine articles are of type Article"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        Article(author, magazine, "How to wear a tutu with style")
        assert isinstance(magazine.articles()[0], Article)

    def test_has_many_contributors(self):
        """magazine has many contributors"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Holmes")
        magazine = Magazine("Vogue", "Fashion")
        Article(author_1, magazine, "How to wear a tutu with style")
        Article(author_2, magazine, "Dating life in NYC")

        assert author_1 in magazine.contributors()
        assert author_2 in magazine.contributors()

    def test_contributors_of_type_author(self):
        """magazine contributors are of type Author"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        Article(author, magazine, "How to wear a tutu with style")
        assert isinstance(magazine.contributors()[0], Author)

    def test_contributors_are_unique(self):
        """magazine contributors are unique"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        Article(author, magazine, "How to wear a tutu with style")
        Article(author, magazine, "Dating life in NYC")

        assert len(set(magazine.contributors())) == len(magazine.contributors())
        assert len(magazine.contributors()) == 1

    def test_article_titles(self):
        """article_titles returns list of titles"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        Article(author, magazine, "How to wear a tutu with style")
        Article(author, magazine, "Dating life in NYC")

        titles = magazine.article_titles()
        assert "How to wear a tutu with style" in titles
        assert "Dating life in NYC" in titles
        assert len(titles) == 2

    def test_no_articles(self):
        """article_titles returns None if no articles"""
        magazine = Magazine("Vogue", "Fashion")
        assert magazine.article_titles() is None

    def test_contributing_authors(self):
        """contributing_authors returns authors with more than 2 articles"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Holmes")
        magazine = Magazine("Vogue", "Fashion")

        # Author 1 has 3 articles
        Article(author_1, magazine, "Article 1")
        Article(author_1, magazine, "Article 2")
        Article(author_1, magazine, "Article 3")

        # Author 2 has 1 article
        Article(author_2, magazine, "Article 4")

        contributing = magazine.contributing_authors()
        assert author_1 in contributing
        assert author_2 not in contributing
        assert len(contributing) == 1

    def test_no_contributing_authors(self):
        """contributing_authors returns None if no authors with >2 articles"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        Article(author, magazine, "How to wear a tutu with style")

        assert magazine.contributing_authors() is None

    def test_top_publisher(self):
        """top_publisher returns magazine with most articles"""
        Magazine.all_magazines.clear()
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        author = Author("Carry Bradshaw")

        # Magazine 1 has 2 articles
        Article(author, magazine_1, "Article 1")
        Article(author, magazine_1, "Article 2")

        # Magazine 2 has 1 article
        Article(author, magazine_2, "Article 3")

        top = Magazine.top_publisher()
        assert top == magazine_1

    def test_no_top_publisher(self):
        """top_publisher returns None if no articles"""
        Magazine.all_magazines.clear()
        assert Magazine.top_publisher() is None
