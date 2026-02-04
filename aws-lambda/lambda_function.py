import json

def lambda_handler(event, context):
    name = event.get("name", "User")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": f"Hello {name}, response from AWS Lambda"
        })
    }
