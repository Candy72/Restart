# //This script gets the instance id
# //Marcelle 2022/10/13
import boto3
ec2 = boto3.client('ec2')
response = ec2.describe_instances()
# print(response)
# TODO: only works with one instance
instance_id = response["Reservations"][0]["Instances"][0]["InstanceId"] 
print(f"The instance ID is {instance_id}")