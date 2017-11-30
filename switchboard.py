"""
This module provides the switchboard functionality for the application
The switchboard shows all the options available or the currently logged in user
"""

import easygui
import users
import initialize
import password
import groups
import devices


def handle_task_selection(tasks):
    """
    Handles the GUI dialog on which the user can select a task to perform
    The task quit will be added
    :param tasks: The tasks that are available to the current user
    :return: String the name of the selected task or None if the user cancels
    """
    selectedTask = None
    updatedTasks = tasks[:]
    updatedTasks.append("Quit")

    selectedTask = easygui.choicebox("Select the task you'd like to perform: {0}".format(users.currentUser),
                                     title="Switchboard", choices=updatedTasks)

    return selectedTask


def select_task():
    """
    Let the user select a task to perform from the tasks available to him/her
    :return: string with the selected task
    """
    currentUser = users.get_current_logged_in_user()
    currentGroup = users.get_group_from_user(currentUser)
    tasks = initialize.get_registered_grouptasks(currentGroup)

    return handle_task_selection(tasks)


def start_selected_task(nameOfTask):
    """
    Starts the selected task
    :param nameOfTask: The name of the user selected task
    :return: None
    """
    NAME = 0
    PASSWORD = 1
    if nameOfTask == "Change password":
        # Start the change password task
        password.change_password(users.currentUser)
    elif nameOfTask == "Add group":
        # Start add group task
        newGroup = groups.add_group()
        groups.add_tasks(newGroup)
    elif nameOfTask == "Add user":
        # Start add user task
        newUserInfo = users.add_user()
        if newUserInfo is not None:
            users.add_user_to_group(newUserInfo[NAME], newUserInfo[PASSWORD])
        else:
            # The user canceled
            pass
    elif nameOfTask == "Reset user password":
        # Start reset user password
        password.reset_user_password()
    elif nameOfTask == "Remove user":
        # Remove user
        users.remove_user()
    elif nameOfTask == "Add Device":
        # Add device
        devices.add_device()
    elif nameOfTask == "Rename Device":
        # Rename device
        devices.rename_device()
    elif nameOfTask == "Remove Device":
        # Remove device
        devices.remove_device()
    else:
        easygui.msgbox("Task: {0} has not been implemented.".format(nameOfTask))

    return None


