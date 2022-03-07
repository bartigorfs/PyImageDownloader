import datetime
import urllib.request

URLS = []


def getTime():
    now = datetime.datetime.now()
    current_time = now.strftime("%H_%M_%S")
    return current_time


def loadToList():
    print('Loading URLs from file')
    urls = []
    fileToRead = open("urls.txt", "r")
    for line in fileToRead:
        urls.append(line.strip())
    fileToRead.close()
    print(f'Loaded! Files loaded: {len(urls)}')
    return urls


def download():
    print(f'Downloading {len(URLS)} objects')
    i = 0
    while i < len(URLS):
        img = urllib.request.urlopen(URLS[i]).read()
        out = open(f"IMG\IMG_{getTime()}.jpg","wb")
        out.write(img)
        out.close()
        i += 1
        print(f'Downloaded {i} from {len(URLS)}')


if __name__ == '__main__':
    URLS = loadToList()
    download()

