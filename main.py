from logger import timestamp, event_builder
from func import download_file


def load_to_list():
    _urls = []
    event_builder(timestamp() + 'Loading URLs from file')
    i = 0
    try:
        file_to_read = open("urls.txt", "r")
        for line in file_to_read:
            _urls.append(line.strip())
        file_to_read.close()
    except:
        event_builder(timestamp() + 'Error while loading URLs!')
    finally:
        event_builder(timestamp() + f'Loaded URLs!')
        return _urls


def download(urls):
    event_builder(timestamp() + f'Downloading {len(urls)} objects')
    i = 0
    try:
        for link in urls:
            i = download_file(link, i, len(urls))
    finally:
        event_builder(timestamp() + f'Downloaded {len(urls)} files!')


if __name__ == '__main__':
    urls = load_to_list()
    download(urls)
