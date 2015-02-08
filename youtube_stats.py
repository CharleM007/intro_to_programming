print(str.upper("These results come from nine lines of code with stock Python 3"))
import json
from urllib.request import urlopen
url = "https://gdata.youtube.com/feeds/api/standardfeeds/top_rated?alt=json" 
response = urlopen(url)
contents = response.read()
text = contents.decode('utf8')
data = json.loads(text)
for video in data['feed']['entry'][0:5]:
    print(video['title']['$t'])


print(20*"*")
print(str.upper('''These results come from six lines of Python 3, 
    using the Requests library. There's also some additional formatting
    done to the strings. That's in line 23 of the code.'''))
import requests
url = "https://gdata.youtube.com/feeds/api/standardfeeds/top_rated?alt=json" 
response = requests.get(url)
data = response.json()
for video in data['feed']['entry'][0:5]:
    view_count = int(video['yt$statistics']['viewCount']) #converts viewCount into an int
    print(video['title']['$t'], "with", '{:,}'.format(view_count), "views") #second 1/2 formats the int with thousands separators

