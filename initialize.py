"""
This module provides the initialization for the application
"""

import os
import password


DEFAULT_USER = "admin"
DEFAULT_PASSWORD = "root"
DEFAULT_GROUP = "administrators"
DEFAULT_DEVICE_TYPE = "server"
detailInfo = "Microsoft Server 2016, 16GB 500GB SSD"
DEFAULT_DEVICE = "{0},domain.users.rotterdam.box1,Dell,ABC-123-DEF,{1}".format(DEFAULT_DEVICE_TYPE,
                                                                               detailInfo)
# Device format: device type, device name, brand, serial or service tag, info detail 1, info detail 2
APPLICATION_TASKS = ["Change password", "Add group", "Add user", "Remove user", "Reset user password",
                     "Add Device", "Remove Device", "Rename Device"]
DEFAULT_TASKS = [APPLICATION_TASKS[0], APPLICATION_TASKS[1], APPLICATION_TASKS[2],
                 APPLICATION_TASKS[3], APPLICATION_TASKS[4]]
DEFAULT_LINKED_GROUP_TASK = "{0},{1},{2},{3},{4},{5}".format(DEFAULT_GROUP,
                                                         DEFAULT_TASKS[0],
                                                         DEFAULT_TASKS[1],
                                                         DEFAULT_TASKS[2],
                                                         DEFAULT_TASKS[3],
                                                         DEFAULT_TASKS[4])

registeredAccounts = {"users": [], "groups": []}
registeredTasks = {DEFAULT_GROUP: []}
registeredDevices = {"devices": []}
applicationSetting = {"path_to_userdat": "", "path_to_groupdat": "", "path_to_taskdat": "",
                      "path_to_grouptaskdat": "", "path_to_devicedat": "",
                      "login_retries": 3,
                      "password_change_retries": 3, "password_minimum_length": 8}


def create_default_userdat(pathToUserDat):
    """
    Creates the default userdat.txt file, which hold the users and related hashes
    The default user: admin password: root
    :param pathToUserDat: The path to the userdat.txt file
    :return: boolean True if the default userdat.txt file was created, no other option
    the program crashes if file was not created successfully
    """
    userdatFile = open(pathToUserDat, 'w')
    userLine = "{0},{1},{2}\n".format(DEFAULT_GROUP, DEFAULT_USER, password.get_hash_from_password(DEFAULT_PASSWORD))
    userdatFile.write(userLine)
    userdatFile.close()

    return True


def is_userdat_file_available(pathToUserDat):
    """
    Test if the userdat.txt file is available
    :param pathToUserDat: The path to the userdat.txt file
    :return: True if the file is available, False if not
    """
    return os.path.isfile(pathToUserDat)


def split_userdat_lines(userdatLines):
    """
    Splits the lines of the userdat.txt line into it's separate components
    :param userdatLines: The lines read from the userdat.txt file
    :return: List with lists containing the separate parts of a userdat.txt line
    """
    users = []
    for userdatLine in userdatLines:
        userInfoParts = userdatLine.strip('\n').split(',')
        users.append(userInfoParts)

    return users


def read_user_database(pathToUserDat):
    """
    Read the file with the user names and hashed passwords
    If the file does not exists a file will be generated with the default
    user: admin and password: root
    :param pathToUserDat: The path to the userdat.txt file
    :return: List containing lists with the group, user names and password hashes
    """
    if not is_userdat_file_available(pathToUserDat):
        create_default_userdat(pathToUserDat)
    else:
        # The userdat.txt exists, continue the function
        pass

    userdatFile = open(pathToUserDat, 'r')
    usersDatLines = userdatFile.readlines()
    userdatFile.close()

    # Create the nested lists by splitting the comma separated parts
    users = split_userdat_lines(usersDatLines)

    return users


def create_default_groupdat(pathToGroupDat):
    """
    Creates the default groupdat.txt file, which hold the available groups
    The default group: administrator
    :param pathToGroupDat: The path to the groupdat.txt file
    :return: boolean True if the default groupdat.txt file was created, no other option
    the program crashes if file was not created successfully
    """
    groupdatFile = open(pathToGroupDat, 'w')
    userLine = "{0}\n".format(DEFAULT_GROUP)
    groupdatFile.write(userLine)
    groupdatFile.close()

    return True


def is_groupdat_file_available(pathToGroupDat):
    """
    Test if the groupdat.txt file is available
    :param pathToGroupDat: The path to the groupdat.txt file
    :return: True if the file is available, False if not
    """
    return os.path.isfile(pathToGroupDat)


def read_group_database(pathToGroupDat):
    """
    Read the file with the groups
    If the file does not exists a file will be generated with the default
    user: admin and password: root
    :param pathToGroupDat: The path to the groupdat.txt file
    :return: List containing the available groups
    """
    if not is_groupdat_file_available(pathToGroupDat):
        create_default_groupdat(pathToGroupDat)
    else:
        # The groupdat.txt exists, continue the function
        pass

    groupdatFile = open(pathToGroupDat, 'r')
    groupsDatLines = groupdatFile.readlines()
    groupdatFile.close()

    groups = []
    for groupDatLine in groupsDatLines:
        groups.append(groupDatLine.strip('\n'))

    # Check if the first equals the default group
    if groups[0] != DEFAULT_GROUP:
        groups.insert(0, DEFAULT_GROUP)

    return groups


def create_default_taskdat(pathToTaskDat):
    """
    Creates the default taskdat.txt file, which hold the users and related hashes
    The default task: administrators,add user, remove user, etc
    :param pathToTaskDat: The path to the taskdat.txt file
    :return: boolean True if the default taskdat.txt file was created, no other option
    the program crashes if file was not created successfully
    """
    taskdatFile = open(pathToTaskDat, 'w')
    for task in DEFAULT_TASKS:
        taskLine = "{0}\n".format(task)
        taskdatFile.write(taskLine)

    taskdatFile.close()

    return True


def is_taskdat_file_available(pathToTaskDat):
    """
    Test if the taskdat.txt file is available
    :param pathToTaskDat: The path to the taskdat.txt file
    :return: True if the file is available, False if not
    """
    return os.path.isfile(pathToTaskDat)


def split_taskdat_lines(taskdatLines):
    """
    Splits the lines of the taskdat.txt line into it's separate components
    :param taskdatLines: The lines read from the taskdat.txt file
    :return: List with lists containing the separate parts of a taskdat.txt line
    """
    tasks = []
    for taskdatLine in taskdatLines:
        taskInfoParts = taskdatLine.strip('\n').split(',')
        tasks.append(taskInfoParts)

    return tasks


def read_task_database(pathToTaskDat):
    """
    Read the file with the associated tasks
    If the file does not exists a file will be generated with the default
    group and tasks
    :param pathToTaskDat: The path to the taskdat.txt file
    :return: List containing lists with the group and associated tasks
    """
    if not is_taskdat_file_available(pathToTaskDat):
        create_default_taskdat(pathToTaskDat)
    else:
        # The taskdat.txt exists, continue the function
        pass

    taskdatFile = open(pathToTaskDat, 'r')
    tasksDatLines = taskdatFile.readlines()
    taskdatFile.close()

    # Create the nested lists by splitting the comma separated parts
    tasks = split_taskdat_lines(tasksDatLines)

    return tasks


def create_default_group_to_task_dat(pathToGroupTaskDat):
    """
    Creates the default grouptaskdat.txt file, which hold the available tasks linked to a group
    The default group to tasks: administrators,Add user, Remove user, etc
    :param pathToGroupTaskDat: The path to the grouptaskdat.txt file
    :return: boolean True if the default grouptaskDat.txt file was created, no other option
    the program crashes if file was not created successfully
    """
    taskdatFile = open(pathToGroupTaskDat, 'w')
    taskLine = "{0}\n".format(DEFAULT_LINKED_GROUP_TASK)
    taskdatFile.write(taskLine)
    taskdatFile.close()

    return True


def is_grouptaskdat_file_available(pathToGroupTaskDat):
    """
    Test if the grouptaskdat.txt file is available
    :param pathToGroupTaskDat: The path to the grouptaskdat.txt file
    :return: True if the file is available, False if not
    """
    return os.path.isfile(pathToGroupTaskDat)


def split_grouptaskdat_lines(groupTaskDatLines):
    """
    Splits the lines of the grouptaskdat.txt line into it's separate components
    :param groupTaskDatLines: The lines read from the grouptaskdat.txt file
    :return: List with lists containing the separate parts of a grouptaskdat.txt line
    """
    groupTasks = []
    for groupTaskDatLine in groupTaskDatLines:
        groupTaskInfoParts = groupTaskDatLine.strip('\n').split(',')
        groupTasks.append(groupTaskInfoParts)

    return groupTasks


def read_grouptask_database(pathToGroupTaskDat):
    """
    Read the file with the group and associated tasks
    If the file does not exists a file will be generated with the default
    group and tasks
    :param pathToGroupTaskDat: The path to the grouptaskdat.txt file
    :return: List containing lists with the group and associated tasks
    """
    if not is_grouptaskdat_file_available(pathToGroupTaskDat):
        create_default_group_to_task_dat(pathToGroupTaskDat)
    else:
        # The grouptaskdat.txt exists, continue the function
        pass

    groupTaskDatFile = open(pathToGroupTaskDat, 'r')
    groupTasksDatLines = groupTaskDatFile.readlines()
    groupTaskDatFile.close()

    # Create the nested lists by splitting the comma separated parts
    groupTasks = split_grouptaskdat_lines(groupTasksDatLines)

    return groupTasks


def initialize_users(pathToUserDat):
    """
    Initialize the users by reading the file with the user names and hashed passwords
    The module global variable will be set
    :param pathToUserDat: Path to the userdat.txt file
    :return: None
    """
    applicationSetting["path_to_userdat"] = pathToUserDat
    registeredAccounts["users"] = read_user_database(pathToUserDat)


def initialize_groups(pathToGroupDat):
    """
    Initialize the users by reading the file with the groups
    The module global variable will be set
    :param pathToGroupDat: Path to the groupdat.txt file
    :return: None
    """
    applicationSetting["path_to_groupdat"] = pathToGroupDat
    registeredAccounts["groups"] = read_group_database(pathToGroupDat)


def initialize_tasks(pathToTaskDat):
    """
    Initialize the tasks by reading the file with the tasks
    The module global variable will be set
    :param pathToTaskDat: Path to the taskdat.txt file
    :return: None
    """
    GROUP = 0

    applicationSetting["path_to_taskdat"] = pathToTaskDat
    taskLines = read_task_database(pathToTaskDat)
    for taskLine in taskLines:
        # Clear old tasks
        registeredTasks[taskLine[GROUP]] = []
        for task in taskLine:
            registeredTasks[taskLine[GROUP]].append(task)

    return None


def initialize_grouptasks(pathToGroupTaskDat):
    """
    Initialize the linked group tasks by reading the file with the group tasks connected
    The module global variable will be set
    :param pathToGroupTaskDat: Path to the grouptaskdat.txt file
    :return: None
    """
    GROUP = 0

    applicationSetting["path_to_grouptaskdat"] = pathToGroupTaskDat
    taskLines = read_grouptask_database(pathToGroupTaskDat)
    for taskLine in taskLines:
        if taskLine[GROUP] not in registeredTasks.keys():
            # The key does not exist, create it
            registeredTasks[taskLine[GROUP]] = []
        else:
            # The key exist add the tasks to the key, which deletes the previous task list
            pass

        # Clear old tasks
        registeredTasks[taskLine[GROUP]] = []
        for task in taskLine[1:]:
            registeredTasks[taskLine[GROUP]].append(task)

    return None


def create_default_devicedat(pathToDeviceDat):
    """
    Creates the default devicedat.txt file, which hold the available devices
    :param pathToDeviceDat: The path to the devicedat.txt file
    :return: boolean True if the default devicedat.txt file was created, no other option
    the program crashes if file was not created successfully
    """
    devicedatFile = open(pathToDeviceDat, 'w')
    deviceLine = "{0}\n".format(DEFAULT_DEVICE)
    devicedatFile.write(deviceLine)
    devicedatFile.close()

    return True


def is_devicedat_file_available(pathToDeviceDat):
    """
    Test if the devicedat.txt file is available
    :param pathToDeviceDat: The path to the devicedat.txt file
    :return: True if the file is available, False if not
    """
    return os.path.isfile(pathToDeviceDat)


def read_device_database(pathToDeviceDat):
    """
    Read the file with the devices
    If the file does not exists a file will be generated with the default
    device: server
    :param pathToDeviceDat: The path to the devicedat.txt file
    :return: List containing the available devices
    """
    if not is_devicedat_file_available(pathToDeviceDat):
        create_default_devicedat(pathToDeviceDat)
    else:
        # The devicedat.txt exists, continue the function
        pass

    devicedatFile = open(pathToDeviceDat, 'r')
    devicesDatLines = devicedatFile.readlines()
    devicedatFile.close()

    return devicesDatLines


def initialize_devices(pathToDeviceDat):
    """
    Initialize the devices by reading the file with the devices
    The module global variable will be set
    :param pathToDeviceDat: Path to the devicedat.txt file
    :return: None
    """
    DEVICE_TYPE = 0
    applicationSetting["path_to_devicedat"] = pathToDeviceDat
    devicesDatLines = read_device_database(pathToDeviceDat)

    # Add the devices to the respective device types
    # Device format: device type, device name, operating system, brand, serial or service tag, internal memory, harddisk
    for deviceDatLine in devicesDatLines:
        deviceLineParts = deviceDatLine.strip('\n').split(',')

        # Create the device type entry
        registeredDevices["devices"].append(deviceLineParts)


def get_registered_users_info():
    """
    Retrieves the list with registered users
    :return: List with lists containing the group, user and the hashed password
    """
    return registeredAccounts["users"]


def get_registered_users():
    """
    Retrieves the list with registered users
    :return: List with users
    """
    USER_NAME = 1
    usersInfo = get_registered_users_info()
    users= []
    for user in usersInfo:
        if len(user) > 1:
            users.append(user[USER_NAME])
        else:
            # No valid user line
            pass

    return users


def get_registered_groups():
    """
    Retrieves the list with registered groups
    :return: List with lists containing the available groups
    """
    return registeredAccounts["groups"]


def get_registered_grouptasks(group):
    """
    Retrieves the list with registered tasks for a given group
    NOTE: There is no check if the group exists
    :return: List with lists containing the available tasks
    """
    return registeredTasks[group]


def get_registered_devices():
    """
    Retrieves the list with the registered devices
    :return: List with lists containing the registered devices
    """
    return registeredDevices["devices"]


def get_max_login_retries():
    """
    Retrieves the maximum number of allowed retries
    :return: integer number of maximum retries
    """
    return applicationSetting["login_retries"]
