import PySimpleGUI as sg
import pyttsx3

engine = pyttsx3.init()

layout = [
    [sg.Text('Enter text to speak:'),sg.Input(key='-TEXT-'),sg.Button('Speak')],
    [sg.Radio('Male', 'voice', key='-MALE-'), sg.Radio('Female', 'voice', key='-FEMALE-', default=True)],
]

window = sg.Window('Text-to-Speech App', layout,background_color='grey')

while True:
    event, values = window.read()
    if event ==sg.WINDOW_CLOSED: 
        break
    voice=engine.getProperty('voices')
    if event == 'Speak':
        text = values['-TEXT-']
        if text.strip() != '':
            engine.setProperty('voice', voice[0].id if values['-MALE-'] else voice[1].id)
            engine.say(text)
            engine.runAndWait()

window.close()