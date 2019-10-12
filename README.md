# Crawl google trend data

## Summary

目的是要去抓特定字詞的聲量，了解該字詞在過去一段時間聲量的變化

由於 google trend 會針對聲量數值做正規劃 (將資料調整成 0-100 之間)，加上要抓取的字詞很多，以及 google trend 同時只能抓取 5 個字詞，為了避免字詞聲量之間的基準不一，所以就一次只抓取一個字詞，google trend 參數如下:

- 地區: 根據想了解的國家做篩選 ex: TW
- 時間: 目前是針對過去 5 年
- 類別: 所有類別
- 搜尋類別: 網頁搜尋

## Crawl process

- Step1: 根據開發者工具 (F12) 找尋 URL

    - Network 中 All 可以看到很多 Name，從中找尋 Response 為 json 格式 (通常都是) 且擁有所需的資料，Headers 就會呈現 Request URL 即為要尋找的 URL
    - URL 可能會是以編碼過後的形式呈現，可以透過 unquote or unquote_plus 來解碼

    ```python
    from urllib.parse import unquote, unquote_plus

    # 對符號進行解碼
    print(unquote(URL))
    print(unquote_plus(URL))

    URL = 'https://trends.google.com/trends/api/widgetdata/multiline'
    ```

- Step2: 尋找 request method, 以及 request 時所需要攜帶的參數

    - Header 裡有 Query String Parameters 即為所需邀攜帶的 parameter

    ```python
    county = 'TW'
    search_name = 'dog'

    params = {
        'hl': 'zh-TW',
        'tz': -480,
        'req': {
            "time":"2014-10-12 2019-10-12",
            "resolution":"WEEK",
            "locale":"zh-TW",
            "comparisonItem":[
                {
                    "geo":{"country":"{}".format(county)},"complexKeywordsRestriction":{"keyword":[{"type":"BROAD","value":"{}".format(search_name)}]}}],
                    "requestOptions":{"property":"","backend":"IZG","category":0}
        },
        'token': 'toke from web',
        'tz': -480
    }
    ```

- Step3: 解析所需要的資料，並整理成所需要的格式

## Note

- token 還不會抓取
- time 還無法從網站中抓取

## Reference

- [Python 的 urllib.parse 庫解析 URL](https://blog.csdn.net/xc_zhou/article/details/80907101)

- [Google Trend unofficial api](https://github.com/GeneralMills/pytrends)

