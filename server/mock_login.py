import hash_password
FAKE_USER = {
    "username": "myname",
    "password": hash_password.encode_password("mypass")
    }
