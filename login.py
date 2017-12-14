"""
This module provides the login, user authentication, verification and authorization
"""

import initialize
import users
import password


def login():
    """
    User can login to the application and with the proper credentials they get access
    :return: List with string 'Success' if successful, followed by the user name
    or list with string 'Failure' if not successful and the number of attempts
    or None when the user cancels
    """
    return "Success"
