"""
This module provides the functionality around devices
"""

import initialize


def add_device():
    """
    Adds a new device to the VS-CMDB
    :return: True if successful
    """
    pass


def rename_device():
    # devicedat.txt uitlezen en elke line als apart device tonen in een easygui choicebox
    devicedatFile = open(pathToDeviceDat, "r")
    devicesDatLines = devicedatFile.readlines()
    deviceToRename = easygui.choicebox(title="Rename Device", msg="Select the device you want to rename.",
                                       choices=devicesDatLines)
    devicedatFile.close()
    if deviceToRename == None:
        exit()

    # elke regel in de device key scheiden door de komma te vervangen met een nextline
    oldDeviceKey = deviceToRename
    formattedDevice = oldDeviceKey.replace(",", "\n")

    # de eerste regel (de device naam)
    currentDeviceName = formattedDevice.split()[0]

    # nieuwe device naam opvragen van de gebruiker dmv een enter box
    newDeviceName = easygui.enterbox(title="Rename Device", msg="{0}\nHow would you like to name {1}?"
                                     .format(formattedDevice, currentDeviceName))

    # de oude device naam vervangen met de nieuwe device naam
    key = formattedDevice.replace(currentDeviceName, newDeviceName)

    # vervolgens weer de nieuwe device naam combineren tot een key
    newformattedDevice = key.replace("\n", ",")
    removedComma = newformattedDevice[:-1]
    newDeviceKey = removedComma + "\n"

    # de nieuwe key naar devicedat.txt schrijven
    devicedatFile = open(pathToDeviceDat, "r")
    deviceKeys = devicedatFile.read()

    changedDeviceKey = deviceKeys.replace(oldDeviceKey, newDeviceKey)
    devicedatFile = open(pathToDeviceDat, "w")
    devicedatFile.write(changedDeviceKey)
    devicedatFile.close()

    return True


def remove_device():
    """
    Removes a device from the registered devices list
    :return: True if successful
    """
    pass