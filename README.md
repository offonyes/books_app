# Multithreaded JSON Fetcher
## Prerequisites

- Python 3.12
- Django

## Installation

1. Clone or download the project repository.
2. Install the required dependencies using the provided requirements.txt file:

```py
pip install -r requirements.txt
```
3. After installing the dependencies, run the server to start.
```py
python manage.py runserver
```

## Functions
1. Type http://127.0.0.1:8000/admin
2. To Create super user write:
   ```py
   python manage.py createsuperuser
   ```
3. Or use login admin, password admin


### Books
- Main page 
- ![authors_books_page](https://github.com/offonyes/books_app/blob/main/readme_images/main_page.png)

- `/books/`: View all books available in the bookstore.
- ![authors_books_page](https://github.com/offonyes/books_app/blob/main/readme_images/books_page.png)

- `/books/<book_id>/`: View details of a specific book by its ID.

### Authors

- `/authors/`: View all authors.
- ![authors_page](https://github.com/offonyes/books_app/blob/main/readme_images/authors_page.png)

- `/authors/<author_id>/`: View details of a specific author by its ID.
