import easygui

msg = "Enter your device information" #Koptekst
title = "Add Device" #Titel venster
fieldNames = ["Type:", "Domain:", "User:", "Plaats:", "Merk:", "Serienummer:", "Software:", "RAM:", "Opslag:","HDD TYPE:"] #Veldnamen

fieldValues = easygui.multenterbox(msg, title, fieldNames)

# Controleer de velden
while 1:  # Doorgaan tot laatste venster
    if fieldValues == None:
        break
    errmsg = ""

    # Zoeken naar lege velden
    for i in range(len(fieldNames)):
        if fieldValues[i].strip() == "":
            errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])

    if errmsg == "": # Geen problemen gevonden
        with open("devicedat.txt", "a") as f:
            print(fieldValues, file=f)
        break
    else: #foutmelding weergeven
        fieldValues = easygui.multenterbox(errmsg, title, fieldNames, fieldValues)