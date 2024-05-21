from flask import Flask, request, make_response
import re

app = Flask(__name__)

morse = {
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        ".": ".-.-.-",
        ",": "--..--",
        "?": "..--..",
        "'": ".---.",
        "!": "-.-.--",
        "-": "-....-",
        "/": "-..-.",
        "@": ".--.-.",
        "(": "-.--.",
        ")": "-.--.-",
        ":": "---...",
        ";": "-.-.-.",
        "=": "-...-",
        "+": ".-.-.",
        "_": "..--.-",
        '"': ".-..-.",
        "$": "...-..-"
        }

def morse_to_english(input):
    result = []
    morse_list = input.split()
    for item in morse_list:
        if item == '/':
            result.append(' ')
        for key, value in morse.items():
            if value == item:
                result.append(key)
    return ''.join(result)

def english_to_morse(input):
    result = []
    for char in input:
        if char in morse:
            result.append(morse[char])
        elif char == ' ':
            result.append('/')
        else:
            return f"Character '{char}' cannot be translated to Morse code."
    return ' '.join(result)

@app.route('/', methods=['GET'])
def welcome():
    welcome_text = '''

# To translate english into morse code
$ curl -L -d 'input=Hello World!' morse.freaks.dev

# To translate morse code into english
$ curl -L -d 'input=.... . .-.. .-.. --- / .-- --- .-. .-.. -.. -.-.--' morse.freaks.dev

'''
    response = make_response(welcome_text, 200)
    response.mimetype = "text/plain"
    return response

@app.route('/', methods=['POST'])
def get_input():
    input = request.form.get('input')
    pattern = r'^[\.\-/ ]*$'
    if bool(re.match(pattern, input)):
        return morse_to_english(input)
    return english_to_morse(input.lower())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
