import sys, os,bs4,webbrowser,requests

os.chdir("/home/aditya/Desktop")

print("Googling....")
res = requests.get("http://www.google.com/search?q=" + " ".join(sys.argv[1:]))
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,"html.parser")
linkElems = soup.select(".r a")

