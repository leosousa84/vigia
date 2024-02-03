#! /home/leo/.cache/pypoetry/virtualenvs/vigia-_-xV_upl-py3.10/bin/python
from unicodedata import name
from xml.etree.ElementTree import parse

dic_nmap = {}

tree = parse('/home/leo/scripts/vigia/dados/nmap.xml')
root = tree.getroot()


def parse_xml():
    """
    >>> E necessáro ter o arquivo em formato xml do nmap
    """
    try:
        for i in root.iter('nmaprun'):
            for nmaprun in i:
                if nmaprun.tag == 'host':
                    for hostx in nmaprun:
                        if hostx.tag == 'address':
                            if 'ipv4' in hostx.attrib['addrtype']:
                                dic_nmap['ipv4'] = hostx.attrib['addr']
                                dic_nmap['addrtype'] = hostx.attrib['addrtype']
                        elif hostx.tag == 'ports':
                            for port in hostx:
                                for itens in port:
                                    if 'state' == itens.tag:
                                        dic_nmap['state'] = itens.attrib[
                                            'state'
                                        ]
                                    if 'service' == itens.tag:
                                        try:
                                            dic_nmap['name'] = itens.attrib[
                                                'name'
                                            ]
                                        except Exception as err:
                                            dic_nmap['name'] = False
                                        try:
                                            dic_nmap['version'] = itens.attrib[
                                                'version'
                                            ]
                                        except Exception as err:
                                            dic_nmap['version'] = False
                                        try:
                                            dic_nmap['product'] = itens.attrib[
                                                'product'
                                            ]
                                        except Exception as err:
                                            dic_nmap['product'] = False

                                        print(dic_nmap)

    except Exception as err:
        print(f'Ocorreu um erro: {err}')


def main():
    parse_xml()


if __name__ == '__main__':
    main()
