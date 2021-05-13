import json 

def handler(event, context):


    try:
        # TODO decode video
        video_bytes = event['body'].encode('utf-8')
        # TODO run model 
        

        return {
            'statusCode': 200,
            'body': json.dumps(
                {
                    "predicted_label": 'placeholder',
                }
            )
        }

    except Exception as e:
        return {
            'statusCode': 502,
            'body': json.dumps(
                {
                    "predicted_label": 'placeholder',
                    "error_msg" : str(e)
                }
            )
        }
