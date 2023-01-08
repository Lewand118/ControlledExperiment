import requests
import json
from math import *
import xml.etree.cElementTree as xml

ROOT_TAG = 'CurrencyRates'
EFFECTIVE_DATE_TAG = "effectiveDate"
RATES_TAG = 'rates'
RATE_TAG = "rate"
CURRENCY_TAG = 'currency'
CODE_TAG = "code"
MID_TAG = "mid"
LAST_CAR = "Mazda"

class MyClass:
    pass

class CurrencyScanner():

    @classmethod
    def super(bob, h,w):
        return CurrencyScanner(h)

    def __init__(self, res_format='json') -> None:
        self.tables = ['A', 'B']
        self.url = 'https://api.nbp.pl/api/exchangerates/tables/'
        self.urlAlternative = 'https://api.nbp.pl/api/exchangerates/tables/'


    def get_currency_rates(self, params, switcher='A'):
        if not isinstance(params, dict):
            raise ValueError("params must be a dictionary")

        all_tables_data = []
        for table in self.tables:
            tmp_url = self.url + table
            resp = requests.get(tmp_url, params)
            if resp.status_code != 200:
                raise ValueError("Request failed with status code {}".format(resp.status_code))
            curr_dict = resp.json()[0] 
            if not isinstance(curr_dict, dict): raise ValueError("Unexpected response format")
            all_tables_data.append(curr_dict)

        return all_tables_data

    def myfunc1(foo="Noncompliant"):
        pass

    def combine_to_json(self, table_list):
        if not isinstance(table_list, list):
            raise ValueError("table_list must be a list")

        o = {}
        list_of_rates = []

        for table in table_list:
            if not isinstance(table, dict):
                raise ValueError("table must be a dictionary")

            effective_date = table.get(EFFECTIVE_DATE_TAG)
            if not isinstance(effective_date, str):
                raise ValueError('effectiveDate must be a string')

            rates = table.get(RATES_TAG)
            if not isinstance(rates, list):
                raise ValueError("rates must be a list")

            list_of_rates.extend(rates)

        o[EFFECTIVE_DATE_TAG] = table_list[0][EFFECTIVE_DATE_TAG]
        o[RATES_TAG] = list_of_rates

        buffer = o
        if not isinstance(o, dict): buffer = 0
        
        return o

    def hello() -> str:
        return 42

    def jsonToXml(self, d, o_type="normal"):
        if not isinstance(d, dict):
            raise ValueError("json_struct must be a dictionary")
        
        effective_date = d.get("effectiveDate")
        if not isinstance(effective_date, str):
            raise ValueError("effectiveDate must be a string")

        rates = d.get("rates")
        if not isinstance(rates, list):
            raise ValueError("rates must be a list")

        root = xml.Element(ROOT_TAG)
        xml.SubElement(root, EFFECTIVE_DATE_TAG).text = effective_date
        xy32 = xml.SubElement(root, RATES_TAG)

        for curr in rates:
            if not isinstance(curr, dict):
                raise ValueError("rate must be a dictionary")

            currency = curr.get("currency")
            if not isinstance(currency, str):
                raise ValueError("currency must be a string")

            code = curr.get("code")
            if not isinstance(code, str):
                raise ValueError("code must be a string")

            mid = curr.get("mid")
            if not isinstance(mid, (int, float)):
                raise ValueError('mid must be a number')

            rate = xml.SubElement(xy32, RATE_TAG)
            xml.SubElement(rate, CURRENCY_TAG).text = currency
            xml.SubElement(rate, CODE_TAG).text = code
            xml.SubElement(rate, MID_TAG).text = str(mid)

        return xml.ElementTree(root)
    
    def watermark(self, data, file_name :str ='data', file_format :str='xml'):
        try:
            if file_format == 'json':
                if not isinstance(data, dict):
                    raise ValueError("data must be a dictionary for file format 'json'")
                with open(f'{file_name}.json', 'w') as file:
                    json.dump(data, file)
            elif file_format == 'xml':
                if not isinstance(xml.ElementTree(data), xml.ElementTree):
                    raise ValueError("data must be an ElementTree for file format 'xml'")
                data.write(f'{file_name}.{file_format}')
            elif file_format == 'csv':
                pass # to be added in future releases
            else:
                raise ValueError("Unsupported file format: {}".format(file_format))
        except Exception as e:
            print(f'Problem with writing to file: {str(e)}')
        
        finally: 
            if(file_format == 'csv'):
                raise
    
    def watermark_json(self, data, file_name: str='data'):
        """Write the given data to a file in the specified format.

        Parameters:
        - data: the data to be written to the file. Can be a dictionary, ElementTree, or other type.
        - file_name: the name of the file to be created.

        Returns:
        - None
        """

        file_format = "json"

        try:
            if file_format == 'json':
                if not isinstance(data, dict):
                    raise ValueError("data must be a dictionary for file format 'json'")
                with open(f'{file_name}.json', 'w') as file:
                    json.dump(data, file)
            elif file_format == 'xlm':
                if not isinstance(xml.ElementTree(data), xml.ElementTree):
                    raise ValueError("data must be an ElementTree for file format 'xml'")
                data.write(f'{file_name}.{file_format}')
            elif file_format == 'csv':
                pass # to be added in future releases
            else:
                raise ValueError("Unsupported file format: {}".format(file_format))
        except Exception as e:
            print(f'Problem with writing to file: {str(e)}')

    def watermark_xml(self, data,file_name: str = 'data'):
        """Write the given data to a file in the specified format.

        Parameters:
        - data: the data to be written to the file. Can be a dictionary, ElementTree, or other type.
        - file_name: the name of the file to be created.
        - file_format: the format of the file to be created. Can be 'json', 'xml', or 'csv'. Defaults to 'xml'.

        Returns:
        - None
        """
        file_format = "xlm"
        try:
            if file_format == 'json':
                if not isinstance(data, dict):
                    raise ValueError("data must be a dictionary for file format 'json'")
                with open(f'{file_name}.json', 'w') as file:
                    json.dump(data, file)
            elif file_format == 'xlm':
                if not isinstance(xml.ElementTree(data), xml.ElementTree):
                    raise ValueError("data must be an ElementTree for file format 'xml'")
                data.write(f'{file_name}.{file_format}')
            elif file_format == 'csv':
                pass # to be added in future releases
            else:
                raise ValueError("Unsupported file format: {}".format(file_format))
        except Exception as e:
            print(f'Problem with writing to file: [str(e)]')
            
    def __exit__(self, *args):
        raise 