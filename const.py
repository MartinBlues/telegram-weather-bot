#const
TOKEN = '5847037531:AAH_X56YsWm9UxXpAyaIbcjtfJhRR5q1nco'

URL = 'https://api.telegram.org/bot{token}/{method}'

UPDATE_METH = 'getUpdates'
SEND_METH = 'sendMessage'

MY_ID = 465651213

UPDATE_ID_FILE_PATH = 'update_id'

with open(UPDATE_ID_FILE_PATH) as file:
    data = file.readline()
    if data:
        data = int(data)
    UPDATE_ID = data


WEATHER_TOKEN = 'aae94af6a073e74747c98712f6202b52'

WEATHER_URL = 'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}'