import logging
from json import loads

import boto3

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
boto3.set_stream_logger('botocore', level=logging.DEBUG)
logger.info('Loading function')

client = boto3.client('dynamodb')
table = 'dynamodb-product-stack-DemoTable-1F1E0UEKYGSUR'


def put_products(product):
    try:

        client.put_item(
            TableName=table,
            Item={
                'id': {'S': 'OLJCESPC7Z'},
                'name': {'S': 'Vintage Typewriter'},
                'description': {'S': 'This typewriter looks good in your living room.'},
                'picture': {'S': '/static/img/products/typewriter.jpg'},
                'priceUsd': {
                    'M': {
                        'currencyCode': {
                            'S': 'USD'
                        },
                        'units': {
                            'N': '67'
                        },
                        'nanos': {
                            'N': '990000000'
                        }
                    }
                },
                'categories': {'SS': ['vintage']}
            }
        )
        logger.info('{} method successful'.format(''))
        logger.debug('Event payload: {}'.format(''))
    except Exception as e:
        logger.error(e)
        # return -1
    else:
        logger.error('Unsupported method \'{}\''.format(''))


def main():
    put_products('')


if __name__ == '__main__':
    main()
