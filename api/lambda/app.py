import use
import preprocess
import os
import json

def handler(event, context):
    try:
        netName = "gan"
        checkpoint = 29471
        modelDir = os.getenv("MODEL_DIR", "./models/gan") # local env default to ./models
        #modelDir = '/opt/ml/models/gan/'
        # bucket = event['Records'][0]['s3']['bucket']['name']
        # key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')

        #modelDir = os.path.join("models", netName)
        print("start")
        (x, msg) = use.main(netName, checkpoint, modelDir, preprocess.fromJson(event))
        return {
            "statusCode": 200,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            "body": json.dumps(
                {
                    "classification": str(x),
                    "explanation": msg
                }
            )
        }
    except Exception as e:
        return {
            "statusCode": 502,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            "body": json.dumps(
                {
                    "classification": "",
                    "error_msg" : str(e)
                }
            )
        }