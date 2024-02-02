import re
#regular expression


def validate_email(email):
    if(len(email)>7):
        return bool(re.match("([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"),email)