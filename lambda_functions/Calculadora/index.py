import json

def lambda_handler(event, context):
    params = event.get('queryStringParameters', {})
    num1 = params.get('num1')
    num2 = params.get('num2')
    operador = params.get('operador')
    
    if operador == ' ':
        operador = '+'  # Para evitar tener que escribir %2B

    
    if not num1 or not num2 or not operador:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Los parametros "num1", "num2" y "operador" son obligatorios.'})
        }
    
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Los parametros "num1" y "num2" deben ser números válidos.'})
        }

    if operador not in ['+', '-', '*', '/']:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'El operador debe ser uno de los siguientes: "+", "-", "*", "/"'})
        }

    try:
        if operador == '+':
            resultado = num1 + num2
        elif operador == '-':
            resultado = num1 - num2
        elif operador == '*':
            resultado = num1 * num2
        elif operador == '/':
            if num2 == 0:
                raise ZeroDivisionError
            resultado = num1 / num2
    except ZeroDivisionError:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'La división por cero no está permitida.'})
        }

    return {
        'statusCode': 200,
        'body': json.dumps({'resultado': resultado})
    }
