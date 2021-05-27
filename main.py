from urllib.request import urlopen
from bs4 import BeautifulSoup as BS4


URL = 'https://www.deezer.com/br/playlist/6985689604'


def main():

    html = urlopen(URL)
    soup = BS4(html, 'html.parser')
    track_list = soup.find('div', {"class": "datagrid"})
    tracks = track_list.find_all("a")
    for track in tracks:
        track_name = track.find("span", {"itemprop": "name"})
        if track_name != None:
            track_name = str(track_name).split('>')
            track_name = str(track_name[1]).split('<')
            print(track_name[0])




if __name__ == '__main__':
    main()
