import requests as re

response = re.get('https://www.localconditions.com/weather-wichita-kansas/67201/alerts.php')
html = response.text
file = open("alerts.txt", "w")
file.write(html)

if '<h5 class="card-title">Wind Advisory issued' in html:
  windadvise = 'Wind Advisory is in effect for our area.'
  print(windadvise)
  index = open("index.html").read().format(windadvise='Wind Advisory is in effect for our area')
else:
  windadvise = 'Operation: FAILED'
  print(windadvise)
  index = open("index.html").read().format(windadvise='')
