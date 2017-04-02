from datetime import datetime
from urllib import request
from urllib.error import URLError, HTTPError
from xml.etree import ElementTree


cbrf_url = "http://www.cbr.ru/scripts/XML_daily.asp?date_req={format_string}"


def search_valute_in_xmltree(char_code, xml_tree):
    for valute in xml_tree:
        for attr in valute:
            if attr.tag == "CharCode":
                if attr.text == char_code:
                    nominal = 1
                    value = 0.0
                    for b in valute:
                        if b.tag == "Value":
                            data = b.text
                            data = data.replace(",", ".")
                            value = float(data)
                        if b.tag == "Nominal":
                            nominal = int(b.text)
                        value = round(float(value / nominal), 8)
                    return dict(CharCode=char_code, Value=value)
    try:
        raise ValueError("\"{charcode}\" char-code not found".format(charcode=char_code))
    except Exception as error:
        print('Caught this error: ' + repr(error))


def get_value(char_code, date=datetime.now()):
    url = cbrf_url.format(
        format_string=date.strftime("%d/%m/%Y")
    )
    try:
        o = request.urlopen(url=url)
        xml = o.read().decode('cp1251')
        xmltree = ElementTree.fromstring(xml)
        data = search_valute_in_xmltree(char_code, xmltree)
        return data['Value']

    except HTTPError as e:
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
    except URLError as e:
        print('We failed to reach a server.')
        print('Reason: ', e.reason)


def get_values(chars, date=datetime.now()):
    url = cbrf_url.format(
        format_string=date.strftime("%d/%m/%Y")
    )
    try:
        returned_data = []
        o = request.urlopen(url=url)
        xml = o.read().decode('cp1251')
        val_curs = ElementTree.fromstring(xml)
        for searching_valute in chars:
            returned_data.append(search_valute_in_xmltree(searching_valute, val_curs))
        return returned_data

    except HTTPError as e:
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
    except URLError as e:
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
