# 🛡️ Auto-Detect & Respond to Cloud Threats Using AWS GuardDuty + SNS Alerts

## 🔍 Overview
This project sets up an automated cloud security response pipeline using:

- **Amazon GuardDuty** to detect threats like port scanning, credential compromise, or unusual activity
- **Amazon SNS** to send real-time alert notifications
- **EventBridge** to route GuardDuty findings
- **(Optional)** AWS Lambda to automatically **quarantine EC2 instances**
- **IAM** to secure access across services

---

## 🧱 Architecture

![Architecture](architecture/guardduty-sns-architecture.png)

> Diagram: GuardDuty triggers EventBridge, which notifies SNS. Lambda optionally stops the affected EC2.

---

## 📁 Folder Structure

```plaintext
guardduty-threat-detection/
├── README.md
├── architecture/
│   └── guardduty-sns-architecture.png
├── eventbridge/
│   └── cloudwatch-event-pattern.json
├── sns/
│   └── sns-setup-instructions.md
├── iam/
│   └── guardduty-sns-lambda-policy.json
├── lambda/
│   └── quarantine-instance.py

🚀 Setup Guide
✅ Step 1: Enable GuardDuty
Go to AWS Console → GuardDuty → Click Enable

Wait for service to initialize and start scanning

✅ Step 2: Create SNS Topic
See sns/sns-setup-instructions.md

✅ Step 3: Create EventBridge Rule
Use the pattern in eventbridge/cloudwatch-event-pattern.json

Target = SNS Topic

✅ Step 4: Add IAM Role
Use the policy in iam/guardduty-sns-lambda-policy.json

Attach it to the Lambda function (if used)

✅ Step 5: (Optional) Deploy Lambda
Deploy lambda/quarantine-instance.py

Triggered via EventBridge

Stops the compromised EC2 instance

🧰 Tools & Services
Tool	Purpose
GuardDuty	Threat Detection
SNS	Alert Delivery
EventBridge	Trigger GuardDuty Alerts
Lambda	Auto-Remediation (optional)
IAM	Secure Permissions

📌 Status
✅ MVP Complete
📊 Optional: Add Power BI dashboard for alert trends
🔁 Improvements coming soon

💼 Author
Wilfredo Rodriguez
AWS | Cloud Security | Automation




