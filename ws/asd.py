import requests,bs4


result = requests.get("https://en.wikipedia.org/wiki/Go_(programming_language)")
soup = bs4.BeautifulSoup(result.text,"lxml")

paragrps = soup.select("p")

print(paragrps[5].getText())