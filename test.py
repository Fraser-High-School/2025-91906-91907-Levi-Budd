



import configparser

config = configparser.ConfigParser()

with open('settings.ini', 'w') as configfile:
    config['settings'] = {
        'difficulty': '4',
        'amount': '10',
        'mode': 'easy',
        'password': '1234'
    }
    config.write(configfile)


config.read('settings.ini')

difficulty = config['settings']['difficulty']
amount = config['settings']['amount']
mode = config['settings']['mode']
password = config['settings']['password']

print(f"Amount set to: {amount}")
print(f"Difficulty set to: {difficulty}")
print(f"Mode set to: {mode}")
print(f"Password set to: {password}")