Small testing project on creation social network

!!! only for development !!!

Using API

1. Runserver on 8000
2. Get authorization token http://127.0.0.1:8000/api/token/ POST Username: admin Password: Qaz.1975
3. Then using 'access' part of json that put in bearer token part of request
4. Posting new user http://127.0.0.1:8000/api/users/ POST with JSON 
{
    "username": " ",
    "email": "  ",
    "password": " "
}
5. Posting new post http://127.0.0.1:8000/api/posts/ POST with JSON
{
    "content": "  ",
    "post_image": "way to your image" or omit
}
6. Posting a vote http://127.0.0.1:8000/api/posts/ POST with JSON
{
    "post": <id>,
    "up_vote"/"down_vote: true
}
7. Getting analytics by upvotes GET
http://127.0.0.1:8000/api/analytics/?date_from=<YYYY_MM_DD>&date_to=<YYYY_MM_DD>
8. Getting info about user's activity GET
http://127.0.0.1:8000/api/user-activity/