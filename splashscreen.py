"""
This module provides the splash screen for the application.
"""
import easygui

def show(version):
    """
    Splash screen which shows the name and current version of the VS-CMDB
    :param: Version number of the application
    :return: None
    """
    displayText = " _   _ _____        _____ ___  ______________ \n"
    displayText += "| | | /  ___|      /  __ \\|  \\/  |  _  \\ ___ \\\n"
    displayText += "| | | \\ `--. ______| /  \\/| .  . | | | | |_/ /\n"
    displayText += "| | | |`--. \______| |    | |\/| | | | | ___ \\\n"
    displayText += "\\ \\_/ /\\__/ /      | \\__/\\| |  | | |/ /| |_/ /\n"
    displayText += " \\___/\\____/        \\____/\\_|  |_/___/ \\____/ \n"
    displayText += "\n"
    displayText += "{0:>38}: {1:>5}\n".format("Version", version)
    displayText += "\n\n"
    displayText += "RAc hogeschool Rotterdam\n"
    displayText += "R.R. Saunders - "
    displayText += "C. Stolk - "
    displayText += "D. Terpstra"
    easygui.msgbox(displayText, title="Starting VS-CMDB")
