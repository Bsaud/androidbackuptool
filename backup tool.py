import PySimpleGUIWx as sg
import os
sg.theme('LightGrey1')
layout = [  [sg.Text('Make sure that your android phone has usb debugging \nenabled in developer options menu and accept the prompt on your phone')],
            [sg.Text('Select backup Location:'), sg.InputText(),sg.FolderBrowse()],
            [sg.Button('Backup'), sg.Button('Restore')]]

# Create the Window
window = sg.Window('Android backup tool', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        window.close()
    elif event == 'Backup':
        try:
            os.system('adb.exe backup -apk -shared -all -f %s/backup.ap' %values[0])
        except:
            sg.Popup('Make sure ADB exists in the same directory as this program!')
    elif event == 'Restore':
        try:
            os.system('adb.exe restore %s/backup.ab' %values[0])
        except:
            sg.Popup('Make sure ADB exists in the same directory as this program!')
