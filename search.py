from bs4 import BeautifulSoup


def googleSearch(terms):
    url = "https://www.google.ca/search?q={}".format("%20".join(terms))
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="html.parser")
    result = soup.find('div', class_='Z0LcW XcVN5d')
    return(result.text)

query = "When was Obama Born?"
response = requests.get("https://www.google.ca/search?q="+"%20".join(query.split()))
soup = BeautifulSoup(response.text, features="html.parser")
result = soup.find('div', class_='BNeawe iBp4i AP7Wnd')
print('testing 1 2 3')
