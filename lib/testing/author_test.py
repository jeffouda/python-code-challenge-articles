from lib.classes.many_to_many import Author, Magazine, Article


class TestAuthor:
    """Class Author in many_to_many.py"""

    def test_has_name(self):
        """Author is initialized with a name"""
        author = Author("Carry Bradshaw")
        assert author.name == "Carry Bradshaw"

    def test_name_is_immutable_string(self):
        """author name is immutable string"""
        author = Author("Carry Bradshaw")

        # Check that name is of type str
        assert isinstance(author.name, str)

        # Check that name cannot be changed
        try:
            author.name = "New Name"
            assert False, "Name should not be mutable"
        except AttributeError:
            assert True
        except Exception as e:
            assert False, f"Unexpected exception: {e}"

    def test_name_is_valid(self):
        """name is longer than 0 characters"""
        # Test valid name
        author = Author("Carry Bradshaw")
        assert author.name == "Carry Bradshaw"

        # Test empty name
        try:
            Author("")
            assert False, "Empty name should raise exception"
        except ValueError:
            assert True
        except Exception as e:
            assert False, f"Unexpected exception: {e}"

    def test_has_many_articles(self):
        """author has many articles"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author, magazine, "How to wear a tutu with style")
        article_2 = Article(author, magazine, "Dating life in NYC")

        assert len(author.articles()) == 2
        assert article_1 in author.articles()
        assert article_2 in author.articles()

    def test_articles_of_type_articles(self):
        """author articles are of type Article"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        Article(author, magazine, "How to wear a tutu with style")
        assert isinstance(author.articles()[0], Article)

    def test_has_many_magazines(self):
        """author has many magazines"""
        author = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        Article(author, magazine_1, "How to wear a tutu with style")
        Article(author, magazine_2, "Carrara Marble")

        assert magazine_1 in author.magazines()
        assert magazine_2 in author.magazines()

    def test_magazines_of_type_magazine(self):
        """author magazines are of type Magazine"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        Article(author, magazine, "How to wear a tutu with style")
        assert isinstance(author.magazines()[0], Magazine)

    def test_magazines_are_unique(self):
        """author magazines are unique"""
        author = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        Article(author, magazine_1, "How to wear a tutu with style")
        Article(author, magazine_1, "How to be single and happy")
        Article(author, magazine_2, "Carrara Marble")

        assert len(set(author.magazines())) == len(author.magazines())
        assert len(author.magazines()) == 2

    def test_add_article(self):
        """add_article method creates a new article for the author"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article = author.add_article(magazine, "How to wear a tutu with style")

        assert isinstance(article, Article)
        assert article in author.articles()
        assert article in magazine.articles()
        assert article.author == author
        assert article.magazine == magazine

    def test_topic_areas(self):
        """topic_areas returns unique list of categories"""
        author = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        Article(author, magazine_1, "How to wear a tutu with style")
        Article(author, magazine_2, "Carrara Marble")

        topic_areas = author.topic_areas()
        assert "Fashion" in topic_areas
        assert "Architecture" in topic_areas
        assert len(topic_areas) == 2

    def test_no_articles(self):
        """topic_areas returns None if author has no articles"""
        author = Author("Carry Bradshaw")
        assert author.topic_areas() is None
