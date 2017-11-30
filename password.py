"""
This module provides the password related functionality for the application
"""

import hashlib
import easygui
import users
import initialize


def get_hash_from_password(userPassword):
    """
    Creates a hash, SHA256 format, from the provided password
    :param userPassword: The password for which the SHA256 hash should be created
    :return: string containing the hash (digest) value
    """
    hashedPassword = hashlib.sha256(userPassword)
    hashDigest = hashedPassword.hexdigest()

    return hashDigest


def change_password(user):
    """
    Change the password for the given user
    The user must exist in order to change the password
    :param user: The user for which we need to change the password
    :return: True if this was successful
    """
    pass


def reset_user_password():
    """
    Reset the user his/her password
    :return: True if successful
    """
    pass
