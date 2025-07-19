# SNS Setup Instructions

Follow these steps to create the SNS topic that will be triggered by GuardDuty findings:

1. Open the AWS Console → Go to **Amazon SNS**
2. Click **Create topic**
   - Type: `Standard`
   - Name: `guardduty-threat-alerts`
3. After creating the topic, click **Create subscription**
   - Protocol: `Email`
   - Endpoint: `your-email@example.com` (replace with your email)
4. Check your email inbox and confirm the subscription to receive alerts.
5. This topic will later be used as the target in an EventBridge rule.
