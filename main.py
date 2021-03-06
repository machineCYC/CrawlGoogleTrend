import requests
import urllib
import conf

URL = 'https://trends.google.com/trends/api/widgetdata/multiline'

county = 'TW'
search_name = 'dog'

params = {
    'hl': 'zh-TW',
    'tz': -480,
    'req': {
        "time":"2014-10-12 2019-10-12",
        "resolution":"WEEK",
        "locale":"zh-TW",
        "comparisonItem":[{"geo":{"country":"{}".format(county)},"complexKeywordsRestriction":{"keyword":[{"type":"BROAD","value":"{}".format(search_name)}]}}],"requestOptions":{"property":"","backend":"IZG","category":0}
    },
    'token': conf.token,
    'tz': -480
}
params = urllib.parse.urlencode(params).encode('utf-8')
s = requests.session()

response = s.get(URL, params=params)
print(response)