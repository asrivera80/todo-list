import json
import decimalencoder
import todoList


def translate(event, context):
    # create a response
    item = todoList.get_item(event['pathParameters']['id'])
    translate = str(
        todoList.get_translate(
            item["text"], event['pathParameters']['idioma']
            )
        )
    item["text"] = translate
    print("Pintar Traduccion: \n\r")
    print(
        json.dumps(
            item["text"], cls=decimalencoder.DecimalEncoder, indent=4
            )
        )
    if item:
        response = {
            "statusCode": 200,
            "body": json.dumps(item,
                               cls=decimalencoder.DecimalEncoder)
        }
    else:
        response = {
            "statusCode": 404,
            "body": ""
        }
    return response
