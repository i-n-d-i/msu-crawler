import requests
from urllib.parse import quote, unquote
from queue import Queue
from bs4 import BeautifulSoup
import sys

def checkResponse(page):
    if(page.status_code != 200):
        print("Error, page not found")
        exit(1)

def BFS_one_level(q, destination_link, excptn, file):
    for i in range(q.qsize()):
        link = q.get()
        page = requests.get(link)
        checkResponse(page)
        getLink(q, page, destination_link, excptn, file)

def BFS(q, destination_link, file):
    excptn = []
    print("\nLevel 0:\n")
    BFS_one_level(q, destination_link, excptn, file)
    print("\nLevel 1:\n")
    BFS_one_level(q, destination_link, excptn, file)
    print("\nLevel 2:\n")
    BFS_one_level(q, destination_link, excptn, file)


def getLink(q, page, destination_link, excptn, file):
    doc = BeautifulSoup(page.text, features = 'lxml')
    for link in doc.find_all('a'):
        url = str(link.get('href'))
        url = unquote(url)

        if(url.find('wiki', 1, 5) != -1):
             url = 'https://kk.wikipedia.org' + url
             if(excptn.count(url) == 0):
                if(destination_link == url):
                    print("Destination:")
                    print(url)
                    file.write(url)
                    file.write('\n')
                    exit(1)
                else:
                    print(url)
                file.write(url)
                file.write('\n')
                excptn.append(url)
                q.put(url)
    return

if __name__ == '__main__':
    if(len(sys.argv) != 3):
        print("Error, need more arguments")
        exit(1)

    start_link = unquote(sys.argv[1])
    destination_link = unquote(sys.argv[2])
    file = open('links.txt', 'w')
    q = Queue()
    q.put(start_link)

    BFS(q, destination_link, file)
    file.close()
