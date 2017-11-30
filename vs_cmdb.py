"""
This is the main start-up file of the VS-CMDB application
"""

import easygui
import splashscreen
import initialize
import users
import login
import switchboard

def handle_login():
    """
    Handles the login procedure
    :return: Logged in user and the group he/she belongs to
    """
    RESULT = 0
    NAME = 1
    loginResult = login.login()
    if loginResult is not None:
        if loginResult[RESULT] == "Success":
            message = "User {0} from {1} group has signed in".format(loginResult[NAME],
                                                                     users.get_group_from_user(loginResult[NAME]))

            return True
        else:
            message = "Error:\nLogin failed. After {0} attempts.\nProgram will be terminated.".format(loginResult[NAME])
            easygui.msgbox(message, title="ERROR")

            return False
    else:
        easygui.msgbox("VS-CMDB stops on user request.", title="INFORMATION")

        return False


def handle_switchboard():
    """
    Handles the switchboard which is the heart of the application
    Until the user quits it keeps coming back to the point
    :return: None
    """
    quit = False
    while (not quit):
        selectedTask = switchboard.select_task()
        if (selectedTask is None) or (selectedTask == "Quit"):
            quit = True
        else:
            switchboard.start_selected_task(selectedTask)

    return None


def main():
    """
    The main loop of the application
    :return: None
    """
    splashscreen.show(0.1)

    # Initialize the application
    initialize.initialize_users(".\\userdat.txt")
    initialize.initialize_groups(".\\groupdat.txt")
    initialize.initialize_tasks(".\\taskdat.txt")
    initialize.initialize_grouptasks(".\\grouptaskdat.txt")
    initialize.initialize_devices(".\\devicedat.txt")

    # Login procedure
    if handle_login():
        # Switchboard
        handle_switchboard()

    else:
        # Login failed, exit the application
        pass

    return None

if __name__ == "__main__":
    main()
else:
    easygui.msgbox("Error:\nThis is the main part of the program and should not be imported as a module.",
                   title="ERROR")
