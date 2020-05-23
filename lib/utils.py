import json
import os


def load_credentials_to_environment(content, keys):
    content = json.loads(content)
    for k in keys:
        os.environ[f'TWITTER_{k.upper()}'] = content[k.lower()]


def read_credentials_from_file(file_path, keys):
    try:
        with open(file_path, 'rt') as f:
            content = ''
            for l in f.readlines():
                content += l
            load_credentials_to_environment(content, keys)
    except Exception as e:
        print(e)
