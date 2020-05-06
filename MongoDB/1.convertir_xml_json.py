# -*- coding: utf-8 -*-

import xmltodict
import json

with open('dblp.xml', encoding='utf-8') as in_file:
    xml = in_file.read()
    xml_dict = xmltodict.parse(xml)

    # xml2=xml.replace('&Ouml;','Ö')
    # print('DESPUES: ', xml.replace('&Ouml;','Ö'))

    with open('jsondata.json', 'w', encoding='utf-8') as out_file:
        json.dump(xml_dict, out_file)

    print('terminado')