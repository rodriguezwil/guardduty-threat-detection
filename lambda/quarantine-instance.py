import boto3
import json

def lambda_handler(event, context):
    print("Received event: ", json.dumps(event))

    # Extract instance ID from GuardDuty finding
    detail = event.get("detail", {})
    resource = detail.get("resource", {}).get("instanceDetails", {})
    instance_id = resource.get("instanceId")

    if not instance_id:
        print("No instance ID found in the GuardDuty finding.")
        return

    ec2 = boto3.client('ec2')

    try:
        print(f"Attempting to stop EC2 instance: {instance_id}")
        ec2.stop_instances(InstanceIds=[instance_id])
        print(f"Instance {instance_id} has been stopped.")
    except Exception as e:
        print(f"Failed to stop instance {instance_id}: {str(e)}")
