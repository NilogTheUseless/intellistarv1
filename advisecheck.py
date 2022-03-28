import requests as re

response = re.get('https://www.localconditions.com/weather-wichita-kansas/67201/alerts.php')
html = response.text

dfgh = open('alerts.txt', 'w')

dfgh.write(html)
dfgh.close()
