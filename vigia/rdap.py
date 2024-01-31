#! /home/leo/.cache/pypoetry/virtualenvs/vigia-_-xV_upl-py3.10/bin/python
import requests
import json

url = 'businesscorp.com.br'
dic_rdap = {}


def parse():
    """
    >>> E realizado um get na api e retorna um json
    """
    try:
        response = requests.get('http://rdap.registro.br/domain/' + url)
        if response.status_code == 200:
            json_rdap = json.loads(response.text)
            dic_rdap['domain'] = json_rdap['handle']
            for i in json_rdap['nameservers']:
                dic_rdap['nameserver'] = i['ldhName']
                dic_rdap['dono'] = json_rdap['entities'][0]['vcardArray'][1][
                    2
                ][3]
                dic_rdap['reponsavel'] = json_rdap['entities'][1][
                    'vcardArray'
                ][1][2][3]
                print(dic_rdap)
    except Exception as err:
        print(f'Ocorreu um erro: {err}')


def dump_json():
    """
    >>> E realizado um dump da api e gera um arquivo json
    """
    response = requests.get('http://rdap.registro.br/domain/' + url)
    try:
        if response.status_code == 200:
            json_rdap = json.loads(response.text)
            with open('output.json', 'w') as json_file:
                json.dump(json_rdap, json_file, indent=2)
    except Exception as err:
        print(f'Ocorreu um erro: {err}')


def main():
    parse()


if __name__ == '__main__':
    main()
