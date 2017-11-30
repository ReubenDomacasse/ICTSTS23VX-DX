"""
This module provides the functionality around users
"""

import initialize
import password


currentUser = None


def get_group_from_user(user):
    """
    Retrieves the group the user belongs to
    :param user: User from which you would like to know the group
    :return: string the group to which the user is assigned or None if the user does not exists
    """
    pass


def get_hash_from_user(user):
    """
    Retrieves the hash of the user
    :param user: User from which you would like to know the hash
    :return: string the hash of the users password or None if the user does not exists
    """
    pass


def set_current_logged_in_user(user):
    """
    Set the new currently logged on user
    :param user: The user name of the user currently logged in
    :return: None
    """
    global currentUser

    currentUser = user

    return None


def get_current_logged_in_user():
    """
    Retrieves the currently succesfully logged on user
    :return: string with the user name
    """
    return currentUser


def add_user_to_group(userName, password):
    """
    Add the new user to a group
    :param userName: The user that needs to be added to a group
    :param password: Password of the user
    :return: True if successful, False if not and None if the user cancels
    """
    pass


def add_user():
    """
    Adds a new user to the application
    :return: List containing the user name and password, an empty list in the creation was
     not successful or None if the user canceled
    """
    pass


def remove_user():
    """
    Removes a user from the registered users list
    :return: True if successful
    """
    pass