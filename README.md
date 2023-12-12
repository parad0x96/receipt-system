# Usage
1. Create a virtualenv
2. Install dependencies
    ```pip install -r requirements.txt ```
3. Run the migrations
  ```python manage.py migrate ```
4. Create a superuser
  ```python manage.py createsuperuser```
5. Run the server
  ```python manage.py runserver```
6. Go to `http://127.0.0.1:8000/api/signup` to register to the website, you'll be automatically logged in.
7. Test the website.