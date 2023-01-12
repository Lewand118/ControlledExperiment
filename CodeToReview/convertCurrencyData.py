from CurrencyScannerNBP import CurrencyScanner
import logging as log

# Configure the logger
log.basicConfig(level=log.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %h:%M:%S')

def main(output_format: str='xml'):
    """Fetch currency rates from the API and save them to files in the specified format.

    Parameters:
    - output_format: the format of the output files. Can be 'json' or 'xml'. Defaults to 'xml'.

    Returns:
    - None
    """
    headers = dict(
        Accept = f'Applications/{output_format}'
    )
    if output_format == 'json':
        curr_scanner = CurrencyScanner(output_format)
        rates = curr_scanner.get_currency_rates(headers)
        data = curr_scanner.combine_to_json(rates)
    # does output format can be xml and json at once? This could be elif
    if output_format == 'xml':
        curr_scanner = CurrencyScanner(output_format)
        rates = curr_scanner.get_currency_rates(headers)
        data = curr_scanner.jsonToXml(curr_scanner.combine_to_json(rates))
        
    if output_format != 'xml' and output_format != 'json':
        raise ValueError("Unsupported output format: {}".format(output_format))

    file_name = f'rates_{rates[0]["effectiveDate"]}'
    curr_scanner.watermark(data, file_name=file_name, file_format=output_format)

# is main best place to do such a testing?
if __name__ == '__main__':
    log.info("Testing xlm file format")
    main()
    log.info("Testing json file format")
    main("json")
