#! /home/leo/.cache/pypoetry/virtualenvs/vigia-_-xV_upl-py3.10/bin/python
import json

dic_subfinder = {}


def parse():
    """
    >>> E necessáro ter o arquivo em formato json do subfinder
    """
    try:
        with open('/home/leo/scripts/vigia/dados/subfinder.json') as json_file:
            for line in json_file:
                jsonline = json.loads(line)
                dic_subfinder['subdomain'] = jsonline['host']
                dic_subfinder['source'] = jsonline['source']
                print(dic_subfinder)
    except Exception as err:
        print(f'Ocorreu um erro: {err}')


def main():
    parse()


if __name__ == '__main__':
    main()
