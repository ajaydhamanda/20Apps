import PySimpleGUI as sg
from debugpy.common.timestamp import current

sg.theme('BlueMono')
sg.set_options(font = 'Franklin 20', button_element_size=(5, 3))
button_size = (6,3)
layout = [
    [sg.Text('', font = 'Franklin 14', justification = 'center', expand_x = True, pad =(10,40), key = 'text')],
    [sg.Button('Clear', size = (13,3)), sg.Button('=', expand_x=True)],
    [sg.Button(7, size = button_size), sg.Button(8, size = button_size), sg.Button(9, size = button_size), sg.Button('+', size = button_size)],
    [sg.Button(4, size = button_size), sg.Button(5, size = button_size), sg.Button(6, size = button_size), sg.Button('-', size = button_size)],
    [sg.Button(1, size = button_size), sg.Button(2, size = button_size), sg.Button(3, size = button_size), sg.Button('*', size = button_size)],
    [sg.Button(0, size = button_size), sg.Button('.', expand_x= True ), sg.Button('/', size = button_size)]
]

window = sg.Window('Calculator', layout)

current_number = []
full_operation = []

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        current_number.append(event)
        num_string = ''.join(current_number)
        print(num_string)
        window['text'].update(num_string)

    if event in ['+', '-', '*', '/']:
        full_operation.append(''.join(current_number))
        current_number = []
        full_operation.append(event)
        window['text'].update('')

    if event == '=':
        full_operation.append(''.join(current_number))
        result = eval(''.join(full_operation))
        window['text'].update(result)
        full_operation = []

    if event == 'Clear':
        current_number = []
        full_operation = []
        window['text'].update('')

window.close()