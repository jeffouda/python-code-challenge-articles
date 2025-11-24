class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if len(name) <= 0:
            raise ValueError("Name must be longer than 0 characters")
        self._name = name
        self._articles = []  # Internal cache

    @property
    def name(self):
        return self._name

    def articles(self):
        """Returns a list of all articles the author has written"""
        return self._articles

    def magazines(self):
        """Returns a unique list of magazines for which the author has contributed to"""
        unique_magazines = set()
        for article in self._articles:
            unique_magazines.add(article.magazine)
        return list(unique_magazines)

    def add_article(self, magazine, title):
        """Creates a new Article instance and associates it with that author and magazine"""
        new_article = Article(self, magazine, title)
        return new_article

    def topic_areas(self):
        """Returns a unique list of categories of the magazines the author has contributed to"""
        if not self._articles:
            return None

        categories = set()
        for article in self._articles:
            categories.add(article.magazine.category)
        return list(categories)


class Magazine:
    all_magazines = []

    def __init__(self, name, category):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if len(name) < 2 or len(name) > 16:
            raise ValueError("Name must be between 2 and 16 characters")
        if not isinstance(category, str):
            raise ValueError("Category must be a string")
        if len(category) <= 0:
            raise ValueError("Category must be longer than 0 characters")

        self._name = name
        self._category = category
        self._articles = []
        Magazine.all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if len(value) < 2 or len(value) > 16:
            raise ValueError("Name must be between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise ValueError("Category must be a string")
        if len(value) <= 0:
            raise ValueError("Category must be longer than 0 characters")
        self._category = value

    def articles(self):
        """Returns a list of all the articles the magazine has published"""
        return self._articles

    def contributors(self):
        """Returns a unique list of authors who have written for this magazine"""
        authors = set()
        for article in self._articles:
            authors.add(article.author)
        return list(authors)

    def article_titles(self):
        """Returns a list of titles of all articles written for that magazine"""
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        """Returns a list of authors who have written more than 2 articles for the magazine"""
        if not self._articles:
            return None

        author_count = {}
        for article in self._articles:
            author = article.author
            author_count[author] = author_count.get(author, 0) + 1

        result = []
        for author, count in author_count.items():
            if count > 2:
                result.append(author)

        return result if result else None

    @classmethod
    def top_publisher(cls):
        """Returns the Magazine instance with the most articles"""
        if not cls.all_magazines:
            return None

        top_magazine = None
        max_articles = 0

        for magazine in cls.all_magazines:
            article_count = len(magazine.articles())
            if article_count > max_articles:
                max_articles = article_count
                top_magazine = magazine

        return top_magazine


class Article:
    def __init__(self, author, magazine, title):
        self._author = None
        self._magazine = None
        self._title = None

        self.author = author
        self.magazine = magazine
        self.title = title

        # Add this article to author's and magazine's lists
        author._articles.append(self)
        magazine._articles.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise ValueError("Title must be a string")
        if len(value) < 5 or len(value) > 50:
            raise ValueError("Title must be between 5 and 50 characters")
        if hasattr(self, "_title") and self._title is not None:
            raise AttributeError("Title cannot be changed after instantiation")
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise ValueError("Author must be an instance of Author class")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise ValueError("Magazine must be an instance of Magazine class")
        self._magazine = value
