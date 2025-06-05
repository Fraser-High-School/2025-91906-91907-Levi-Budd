



import configparser

config = configparser.ConfigParser()

with open('settings.ini', 'w') as configfile:
    config['MATH'] = {
        'difficulty': '4',
        'amount': '10',
        'mode': 'easy',
        'password': '1234'
    }
    config.write(configfile)


config.read('settings.ini')

difficulty = config['MATH']['difficulty']
amount = config['MATH']['amount']
mode = config['MATH']['mode']
password = config['MATH']['password']

print(f"Amount set to: {amount}")
print(f"Difficulty set to: {difficulty}")
print(f"Mode set to: {mode}")
print(f"Password set to: {password}")