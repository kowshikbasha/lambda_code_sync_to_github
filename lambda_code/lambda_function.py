import json

def lambda_handler(event, context):
    """
    A simple AWS Lambda function that greets a user by name.
    It expects a JSON payload in the event like: {"name": "YourName"}
    """
    
    # Safely get the 'name' from the event body.
    # The event body is a string, so we need to parse it as JSON.
    try:
        body = json.loads(event['body'])
        name = body.get('name', 'World')  # Use a default value of 'World' if 'name' is not provided.
    except (json.JSONDecodeError, KeyError):
        # Handle cases where the event body is not valid JSON or the 'body' key is missing.
        name = 'World'

    # Create the personalized greeting message.
    message = f'Hello, {name}!'

    # Return a JSON object with the status code and a JSON-formatted body.
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps({'message': message})
    }