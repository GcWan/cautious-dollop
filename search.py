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
    return result

def wikiSearch(query):
    link = "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={}&prop=info&inprop=url&format=json"\
        .format(query.replace(" ", "_"))
    result = requests.get(link).json()['query']['search'][0]
    title = result['title']
    pid = result['pageid']
    info = requests.get("https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts"
                        "&exintro&explaintext&redirects=1&titles={}".format(title)).json()
    extract = info['query']['pages'][str(pid)]['extract']
    if "\n" in extract:
        extract = extract[:extract.find("\n")]
    while len(extract) > 1500:
        extract = extract[:extract.rfind(" ")]
    return extract
