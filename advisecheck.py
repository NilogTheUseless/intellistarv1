import requests as re

response = re.get('https://www.localconditions.com/weather-wichita-kansas/67201/alerts.php')
html = response.text
file = open("alerts.txt", "w")
file.write(html)


word = html
if word.find('<h5 class="card-title">Wind Advisory issued') != -1):
  windadvise = false
else:
  windadvise = 

index = open("index.html").read().format(bla-bla='something',
                                        wowo='wawa')

ex.

<h1> Boink {bla-bla:} aaaaaaand {wowo:} </h1>
