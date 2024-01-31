#! /home/leo/.cache/pypoetry/virtualenvs/vigia-_-xV_upl-py3.10/bin/python
import json

dic_sublist3r = {}


def parse():
    """
    >>> E necessáro ter o arquivo em formato txt do sublist3r
    """
    try:
        with open('/home/leo/scripts/vigia/dados/sublist3r.txt') as file:
            for line in file:
                dic_sublist3r['subdomain'] = line.rstrip('\n')
                print(dic_sublist3r)
    except Exception as err:
        print(f'Ocorreu um erro: {err}')


def main():
    parse()


if __name__ == '__main__':
    main()
