import re

def validate_email(email):
    pattern = '\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*'
    return re.match(pattern, email)