import urllib.request
import uuid
from urllib.error import HTTPError
from logger import logger, timestamp, event_builder


def download_file(url, i, length):
    try:
        img = urllib.request.urlopen(url).read()
        out = open(f"{uuid.uuid4()}.jpg", "wb")
        out.write(img)
        out.close()
        i = i + 1
    except HTTPError as err:
        event_builder(timestamp() + f'Error while downloading! Error code: {err.code}  ErrorURL: {err.url} ')
        logger(err)
        pass
    finally:
        event_builder(timestamp() + f'Downloaded {i} of {length}')
        return i


def read_file():
    print('0')
