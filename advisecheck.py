import requests as re

response = re.get('https://www.localconditions.com/weather-wichita-kansas/67201/alerts.php')
html = response.text
index = open("index.html").read().format(bla-bla='something',
                                        wowo='wawa')

ex.

<h1> Boink {bla-bla:} aaaaaaand {wowo:} </h1>
