import json

def lambda_handler(event, context):
    try:
        # Parsear el cuerpo de la solicitud
        body = json.loads(event.get('body', '{}'))
        texto = body.get('texto', '')

        if not texto:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'El parámetro "texto" es obligatorio'})
            }

        palabras = len(texto.split())
        caracteres = len(texto)
        texto_mayusculas = texto.upper()

        return {
            'statusCode': 200,
            'body': json.dumps({
                'palabras': palabras,
                'caracteres': caracteres,
                'texto_mayusculas': texto_mayusculas
            })
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Error procesando la solicitud', 'detalle': str(e)})
        }
