# JoanyDoctorAPI

This is a developer API used for commenting on doctors.


SETUP

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
./manage.py runserver


Add username/password for authentication into the API. Two test users have already been added. Feel free to use their usernames (phaedraa, benjamin) when making requests.

USE:

A comment require's a corresponding and valid doctor ID,
a rating (1 - 5), a title, comment text, and the username of
the individual leaving a comment.

Accepted calls include the bellow:

List all comments (GET):
http -v GET http://127.0.0.1:8000/comments/ --auth username:password

Create a comment (POST):**
curl -X POST -d title=<title> -d username=<username> -d text=<text> -d  rating=<rating> -d doctor_id=<doctor_id> -H 'Accept:application/json; indent=4' -u username:password http://127.0.0.1:8000/comments/

** Comment creation will return a list of doctors nearby to the user, ranked by rating/number of ratings

Mark comment inactive:
curl -X DELETE -H 'Accept:application/json; indent=4' -u username:password http://127.0.0.1:8000/comments/<COMMENT_ID>

Get specific comment:
curl -X GET -H 'Accept:application/json; indent=4' -u username:password http://127.0.0.1:8000/comments/<COMMENT_ID>

Update specific comment:
curl -X PUT -d title=<title> -d text=<text> -d  rating=<rating> -H 'Accept:application/json; indent=4' -u username:password http://127.0.0.1:8000/comments/<COMMENT_ID>



QUESTIONS
How would you handle profanity filtering?
I'd use a Natural Language Processing library such as Python's NLTK. As an MVP, you could just filter out set words and replace them with less harsh alternatives.
How would you handle security and authentication?
Require user credentials when making the API request; require authenticiation (username and password)
How would you handle functionality where all comments went through an admin approval phase before going live?
Add a pending state to all comments so that comments with pending are not displayed or used to calculate the doctor ratings. Pending comments would be unpended only upon admin approval, after which their data would be incorporated into corresponding Doctor ratings.
