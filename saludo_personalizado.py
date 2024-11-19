import json


def lambda_handler(event, context):
    nombre = event.get('queryStringParameters', {}).get('nombre')

    if not nombre:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Falta el parámetro "nombre"'})
        }

    return {
        'statusCode': 200,
        'body': json.dumps({'message': f'Hola, {nombre}!'})
    }