# 🚀 Automated Daily Quote Emailer (AWS Serverless)

A serverless Python application that automates the delivery of inspirational quotes to your inbox every evening. 

## 🛠️ Tech Stack
- **Compute:** AWS Lambda (Python 3.12)
- **Automation:** Amazon EventBridge (Cron: `30 14 * * ? *`)
- **Communication:** Amazon SES (Simple Email Service)
- **API:** ZenQuotes API

## 📋 Features
- **Scheduled Execution:** Automatically runs at 8:00 PM IST daily.
- **HTML Emails:** Sends professionally formatted emails with custom CSS.
- **Error Handling:** Built-in logging for CloudWatch monitoring.

## ⚙️ Setup Instructions
1. **SES Verification:** Verify your sender and recipient email in the AWS SES Console (ap-south-1).
2. **IAM Permissions:** Grant the Lambda function `ses:SendEmail` permissions.
3. **Environment:** Ensure the `region_name` in the code matches your SES region.

## 📈 Learning Outcomes
- Managing AWS Identity and Access Management (IAM) roles.
- Working with Event-Driven architectures.
- Handling external REST APIs in a serverless environment.
