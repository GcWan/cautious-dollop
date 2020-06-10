from googlesearch import search


def googleSearch(query):
    for r in search(query, tld='ca', lang='en', num=1, start=0, stop=1, pause=2.0):
        return r
