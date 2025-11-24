# Code Explanation: Magazine Domain Model

This document provides a comprehensive explanation of the code in this project, which implements a Magazine domain model with Authors, Magazines, and Articles.

## Project Structure

```
lib/
├── classes/
│   └── many_to_many.py  # Main classes: Author, Magazine, Article
├── testing/
│   ├── article_test.py  # Tests for Article class
│   ├── author_test.py   # Tests for Author class
│   ├── magazine_test.py # Tests for Magazine class
│   └── conftest.py      # Pytest configuration
├── debug.py             # Debugging script with ipdb
└── __pycache__/         # Python bytecode cache
```

## Domain Model Overview

The project implements a many-to-many relationship between Authors and Magazines through Articles:

- **Author**: Represents a writer who can contribute to multiple magazines
- **Magazine**: Represents a publication that can have multiple authors
- **Article**: Represents a piece of writing that connects an author to a magazine

## Class Details

### Author Class

**Purpose**: Represents an author who writes articles for magazines.

**Key Features**:

- Immutable name (set at initialization, cannot be changed)
- Maintains a list of all articles written by the author
- Can add new articles to magazines
- Provides methods to get associated magazines and topic areas

**Properties**:

- `name`: Read-only string property (immutable)

**Methods**:

- `articles()`: Returns list of all articles by this author
- `magazines()`: Returns unique list of magazines the author has contributed to
- `add_article(magazine, title)`: Creates and returns a new Article
- `topic_areas()`: Returns unique list of magazine categories the author has written for

### Magazine Class

**Purpose**: Represents a magazine publication.

**Key Features**:

- Mutable name and category (can be changed after creation)
- Maintains a list of all published articles
- Tracks all magazine instances for class-level operations
- Provides contributor and article analysis methods

**Properties**:

- `name`: Mutable string property (2-16 characters)
- `category`: Mutable string property (non-empty)

**Methods**:

- `articles()`: Returns list of all articles in this magazine
- `contributors()`: Returns unique list of authors who have written for this magazine
- `article_titles()`: Returns list of article titles or None if no articles
- `contributing_authors()`: Returns authors with more than 2 articles
- `top_publisher()` (class method): Returns magazine with most articles

### Article Class

**Purpose**: Represents an individual article connecting an author to a magazine.

**Key Features**:

- Immutable title, author, and magazine (set at initialization)
- Automatically registers itself with the author and magazine upon creation

**Properties**:

- `title`: Read-only string property (5-50 characters, immutable)
- `author`: Read-only Author property (immutable)
- `magazine`: Read-only Magazine property (immutable)

## Relationships

### Many-to-Many Relationship

- Authors can write for multiple magazines
- Magazines can have multiple authors
- Articles serve as the junction table connecting authors to magazines

### Data Flow

1. Author and Magazine instances are created independently
2. Article creation links an Author to a Magazine
3. Articles are automatically added to the author's and magazine's internal lists

## Validation and Error Handling

All classes include comprehensive input validation:

- **Type checking**: Ensures correct data types for all inputs
- **Length validation**: Enforces minimum and maximum lengths for strings
- **Immutability**: Prevents changes to immutable properties after initialization
- **Relationship validation**: Ensures Author and Magazine instances are valid

## Testing

The project includes comprehensive unit tests covering:

- Initialization and property validation
- Relationship methods
- Edge cases (empty lists, invalid inputs)
- Business logic (contributing authors, top publisher)

Tests use pytest framework and are organized by class in separate test files.

## Usage Example

```python
# Create instances
author = Author("John Doe")
magazine = Magazine("Tech Weekly", "Technology")

# Create article (links author and magazine)
article = author.add_article(magazine, "The Future of AI")

# Access relationships
print(author.articles())  # [Article instance]
print(magazine.contributors())  # [Author instance]
print(article.title)  # "The Future of AI"
```

## Key Design Decisions

1. **Immutability**: Certain properties (Author.name, Article.title, etc.) are immutable to maintain data integrity
2. **Automatic Registration**: Articles automatically register with their author and magazine
3. **Class-level Tracking**: Magazine class tracks all instances for aggregate methods
4. **Validation at Initialization**: Input validation occurs during object creation rather than through setters
5. **Property Decorators**: Use of @property for controlled access to attributes

## Running the Code

- Install dependencies: `pipenv install`
- Run tests: `pytest`
- Debug interactively: `python lib/debug.py`
