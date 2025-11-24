from lib.classes.many_to_many import Author, Magazine, Article


class TestArticle:
    """Class Article in many_to_many.py"""

    def test_has_title(self):
        """Article is initialized with a title"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article = Article(author, magazine, "How to wear a tutu with style")
        assert article.title == "How to wear a tutu with style"

    def test_title_is_immutable_string(self):
        """title is an immutable string"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article = Article(author, magazine, "How to wear a tutu with style")

        # Check that title is of type str
        assert isinstance(article.title, str)

        # Check that title cannot be changed
        try:
            article.title = "New Title"
            assert False, "Title should not be mutable"
        except AttributeError:
            assert True
        except Exception as e:
            assert False, f"Unexpected exception: {e}"

    def test_title_is_valid(self):
        """title is between 5 and 50 characters inclusive"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")

        # Test valid title
        article = Article(author, magazine, "How to wear a tutu with style")
        assert article.title == "How to wear a tutu with style"

        # Test short title
        try:
            Article(author, magazine, "Hi")
            assert False, "Short title should raise exception"
        except ValueError:
            assert True
        except Exception as e:
            assert False, f"Unexpected exception: {e}"

        # Test long title
        try:
            Article(
                author,
                magazine,
                "This title is way too long and exceeds the maximum allowed characters for an article title",
            )
            assert False, "Long title should raise exception"
        except ValueError:
            assert True
        except Exception as e:
            assert False, f"Unexpected exception: {e}"

    def test_has_an_author(self):
        """article has an author"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article = Article(author, magazine, "How to wear a tutu with style")
        assert article.author == author

    def test_author_of_type_author(self):
        """author is of type Author"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article = Article(author, magazine, "How to wear a tutu with style")
        assert isinstance(article.author, Author)

    def test_has_a_magazine(self):
        """article has a magazine"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article = Article(author, magazine, "How to wear a tutu with style")
        assert article.magazine == magazine

    def test_magazine_of_type_magazine(self):
        """magazine is of type Magazine"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article = Article(author, magazine, "How to wear a tutu with style")
        assert isinstance(article.magazine, Magazine)
