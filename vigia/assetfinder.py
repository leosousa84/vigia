#! /home/leo/.cache/pypoetry/virtualenvs/vigia-_-xV_upl-py3.10/bin/python
import json

dic_assetfinder = {}


def parse():
    """
    >>> E necessáro ter o arquivo em formato txt do assetfinder
    """
    try:
        with open('/home/leo/scripts/vigia/dados/assetfinder.txt') as file:
            for line in file:
                dic_assetfinder['subdomain'] = line.rstrip('\n')
                print(dic_assetfinder)
    except Exception as err:
        print(f'Ocorreu um erro: {err}')


def main():
    parse()


if __name__ == '__main__':
    main()
