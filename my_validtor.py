import re


def validate_email(email):
    regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    return re.match(regex, email) is not None


def length_check(string, len1, op1):
    match op1:
        case 1:  # check if string is equal to len1
            if len(string) == len1:
                return True
            else:
                return False
        case 2:  # check if string is greater than or equal to len1
            if len(string) >= len1:
                return True
            else:
                return False
        case 3:  # check if string is less than or equal to len1
            if len(string) <= len1:
                return True
            else:
                return False


def password_validator(password, pref_length):
    pattern = r"^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$\!%*?&]{8,}$"
    # check if password is between the required length
    if range_check(len(password), 0, pref_length):
        return True
    # Checks if the password matches the pattern
    if re.match(password, pattern):
        return True
    else:
        return False


def presence_check(string):
    pass


def range_check(num, min, max):
    return min <= num <= max  # check if num is inbetween the min and max


def data_type_check(myData, myType):
    if type(myData) == myType:
        return True
    else:
        return False
