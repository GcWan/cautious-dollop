from googlesearch import search
import requests


def googleSearch(query):
    for r in search(query, tld='ca', lang='en', num=1, start=0, stop=1, pause=2.0):
        return r


def translate(query, target):
    url = "https://systran-systran-platform-for-language-processing-v1.p.rapidapi.com" \
          "/translation/text/translate"
    querystring = {"source": "auto", "target": target, "input": query}
    headers = {
        'x-rapidapi-host': "systran-systran-platform-for-language-processing-v1.p.rapidapi.com",
        'x-rapidapi-key': "8bef51c08bmsh96dc3702341e39ep14a15bjsn19a83064d62d"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    try:
        result = response.json()['outputs'][0]['output']
    except:
        result = ""
    return(result)
