"""drf-spectacular api schemas"""
from drf_spectacular.utils import OpenApiExample

# Return example of Logins(General or Social)
TOKEN_WITH_USER_LOGIN_SUCCESS_RESPONSE_EXAMPLE = OpenApiExample(
    response_only=True,
    name="Success Example",
    value={
        "accessToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
        ".eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUyMjE3Mjg0LCJpYXQiOjE2NTIyMTAwODQsImp0aSI6IjA0ODY3"
        "NjA2NTIzMzRmMDhiN2Q3MTc2NjQ0NTg3YjI3IiwidXNlcl9pZCI6Mjl9.CDOzt"
        "k-o6jvEbfdzAouTAgIypzFgAcm4jbRzzGeDais",
        "refreshToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
        ".eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1MjIzMTY4NCwiaW"
        "F0IjoxNjUyMjEwMDg0LCJqdGkiOiIwNjUxZjdlNGJlMDY0ZjEzYWY5MjU2ZGIyN"
        "GVlNTVkNiIsInVzZXJfaWQiOjI5fQ.ael6_7GMvE39X6qESW__gikrLrbQAeYTtAllWmN_sYc",
        "user": {
            "nickname": "Ongot",
            "name": "ongot",
            "email": "ongot@123.com",
            "cellPhoneNumber": "010-1111-1111",
            "profileImageUrl": "https://upload.wikimedia.org/wikipedia/"
            "commons/thumb/a/ab/Swagger-logo.png/150px-Swagger"
            "-logo.png",
            "birthday": "1998-01-01",
            "isActive": True,
            "isVerified": True,
        },
    },
)
