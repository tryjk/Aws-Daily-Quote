import json
import boto3
import urllib.request

def lambda_handler(event, context):
    # 1. Fetch a random fact from a public API
    api_url = "https://uselessfacts.jsph.pl/random.json?language=en"
    response = urllib.request.urlopen(api_url)
    data = json.loads(response.read().decode())
    fact = data['text']
    
    # 2. Setup the SES client
    # Note: Ensure your region matches where you verified your email
    ses = boto3.client('ses', region_name='ap-south-1') 
    
    # 3. Define the email details
    SENDER = "your-email-address"
    RECIPIENT = "Your-email-address"
    SUBJECT = "Your Daily Dose of Knowledge"
    BODY_TEXT = f"Good morning! Here is your fact for today:\n\n{fact}"
    
    # 4. Send the email
    try:
        ses.send_email(
            Source=SENDER,
            Destination={'ToAddresses': [RECIPIENT]},
            Message={
                'Subject': {'Data': SUBJECT},
                'Body': {'Text': {'Data': BODY_TEXT}}
            }
        )
        return {"statusCode": 200, "body": "Email sent successfully!"}
    except Exception as e:
        print(e)
        return {"statusCode": 500, "body": "Error sending email"}
