This project is a Django-based REST API for a social media platform.

Clone the repository
Create a virtual environment and activate it
Install the requirements:
pip install -r requirements.txt

Apply migrations:
python manage.py makemigrations
python manage.py migrate

Run the development server:
python manage.py runserver


User Authentication


To register a new user, send a POST request to /api/accounts/register/ with the following data:
{
  "username": "your_username",
  "password": "your_password",
  "password2": "your_password",
  "email": "your_email@example.com",
  "first_name": "Your",
  "last_name": "Name"
}


To login and receive an authentication token, send a POST request to /api/accounts/login/ with the following data:
{
  "username": "your_username",
  "password": "your_password"
}


The custom user model extends Django's AbstractUser and includes the following additional fields:

bio: TextField for user biography
profile_picture: ImageField for user profile picture
followers: ManyToManyField for user followers


You can use tools like Postman or curl to test the API endpoints. Make sure to include the authentication token in the header for protected routes:
Authorization: Token your_auth_token