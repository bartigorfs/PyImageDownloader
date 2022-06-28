from datetime import datetime


def logger(err: object):
    if err:
        file = open("error_log.txt", "a")
        file.write(
            f'Error while downloading! Error Code: {err.code};  ErrorReason: {err.reason}; Error URL: {err.url}; '
            f'ErrorArgs: {err.args}; '
            f'ErrorHeaders: {err.headers}')
        file.close()


def timestamp():
    return f'[{datetime.now().strftime("%d/%m %H:%M:%S")}] '


def event_builder(string: str):
    file = open("event_log.txt", "a")
    file.write(string + "\n")
    file.close()
    return print(string)
