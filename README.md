# JoanyDoctorAPI

This is a developer API used for commenting on doctors.

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