import requests
import bs4

link='https://www.cricbuzz.com/live-cricket-scores/30505/mi-vs-rcb-48th-match-indian-premier-league-2020'
res = requests.get(link)
soup = bs4.BeautifulSoup(res.text,'html.parser')

details =soup.select('.cb-col .cb-col-100 .cb-col-scores')
for i in details:
     k=str(print(i.getText().strip()))
p=k.replace("  ","\n")
print(k)

