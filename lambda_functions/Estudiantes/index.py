import json
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
tabla_estudiantes = dynamodb.Table('Estudiantes')

def lambda_handler(event, context):
    id_estudiante = event.get('queryStringParameters', {}).get('id')
    
    if not id_estudiante:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Falta el parámetro "id" en la URL'})
        }

    try:
        # consulta
        response = tabla_estudiantes.get_item(Key={'id': id_estudiante})
        
        if 'Item' not in response:
            return {
                'statusCode': 404,
                'body': json.dumps({'error': 'Estudiante no encontrado'})
            }
        
        estudiante = response['Item']
        return {
            'statusCode': 200,
            'body': json.dumps(estudiante)
        }
    
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
