import use
import preprocess
import os
import json

def handler(event, context):
    try:
        netName = "gan"
        checkpoint = 29471
        modelDir = os.path.join("models", netName)
        (x, msg) = use.main(netName, checkpoint, modelDir, preprocess.fromJson(event))
        return {
            "statusCode": 200,
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
            "body": json.dumps(
                {
                    "classification": "",
                    "error_msg" : str(e)
                }
            )
        }