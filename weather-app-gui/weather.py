import PySimpleGUI as sg
from bs4 import BeautifulSoup as bs
import requests


def get_weather_data(location):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.50"
    url = f"https://www.google.com/search?q=weather+{location.replace(' ','')}"
    session = requests.session()
    session.headers['User-Agent'] = user_agent
    html = session.get(url)

    soup = bs(html.text, "html.parser")
    name = soup.find('div', attrs = {'id': 'wob_loc'}).BBwThe
    time = soup.find('div', attrs = {'id': 'wob_dts'}).text
    weather =  soup.find('span', attrs = {'id': 'wob_dc'}).text
    temp =  soup.find('span', attrs = {'id': 'wob_tm'}).text
    return name, time, weather, temp


weather_column = sg.Column([
    [sg.Image('', key='Image')]],
    key='-LEFT-')

info_column = sg.Column([
    [sg.Text('', key="Location", font = 'Helvetica 30', background_color = '#FF0000', text_color='#FFFFFF', pad = 0, visible=False)],
    [sg.Text('', key="Time", font = 'Helvetica 30', text_color='#FFFFFF', background_color='#FF0000', pad = 0, visible=False)],
    [sg.Text('', key="Temperature", font = 'Helvetica 30', background_color = '#FF0000', pad=(0,10), justification = 'center', visible=False)]
    ])

layout = [
    [sg.Input(expand_x=True, key='-input-'), sg.Button('Enter', border_width = 0)],
    [weather_column, info_column]
]

window = sg.Window('Weather App', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == 'Enter':
        name, time, weather, temp = get_weather_data(values["-input-"])

        window['Location'].update(name, visible= True)
        window['Time'].update(time.split(' ')[0], visible= True)
        window['Temperature'].update(f'{temp} \u2103 ({weather})', visible= True)

        # sun
        if weather in ('Sun', 'Sunny', 'Clear', 'Clear with periodic clouds', 'Mostly sunny'):
            window['Image'].update('Weather/sunny.png')

        # part sun
        if weather in ('Partly Sunny', 'Mostly Sunny', 'Partly cloudy', 'Mostly cloudy', 'Cloudy', 'Overcast'):
            window['Image'].update('Weather/partcloud.png')

        # rain
        if weather in ('Rain', 'Chance of Rain', 'Light Rain', 'Showers', 'Scattered Showers', 'Rain and Snow', 'Hail'):
            window['Image'].update('Weather/rain.png')

        # thunder
        if weather in ('Scattered Thunderstorms', 'Chance of Storm', 'Storm', 'Thunderstorm', 'Chance of TStorm'):
            window['Image'].update('Weather/thunder.png')

        # foggy
        if weather in ('Mist', 'Dust', 'Fog', 'Smoke', 'Haze', 'Flurries'):
            window['Image'].update('Weather/fog.png')

        # snow
        if weather in ('Freezing Drizzle', 'Chance of Snow', 'Sleet', 'Snow', 'Icy', 'Snow Showers'):
            window['Image'].update('Weather/snow.png')

window.close()
