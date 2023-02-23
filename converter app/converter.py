import PySimpleGUI as sg

layout = [
    [sg.Input(key='-input-'),
     sg.Spin(['km to mile', 'kg to lbs', 'sec to min'], key='-units-'),
     sg.Button('Convert', key='-convert-')],
    [sg.Text('Output', key='-output-')],
]

window = sg.Window('Converter', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-convert-':
        input_value = values['-input-']
        if input_value.isnumeric():
            print("input_value")
            match values['-units-']:
                case 'km to mile':
                    output = round(float(input_value) * 0.6214, 2)
                    output_string = f'{input_value} km are {output} miles.'
                case 'kg to lbs':
                    output = round(float(input_value) * 2.2046, 2)
                    output_string = f'{input_value} kg are {output} pounts.'
                case 'sec to min':
                    output = round(float(input_value) / 60, 2)
                    output_string = f'{input_value} secs are {output} minutes.'
            window['-output-'].update(output_string)
window.close()
