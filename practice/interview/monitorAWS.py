import boto3
import resp

#client = boto3.client('cloudformation')：创建一个 CloudFormation 服务的客户端实例，用于调用该服务的 API。
client = boto3.client('cloudformation')#CloudFormation 控制台 → Stack 列表中看到的名称；
status = resp['Stacks'][0]['StackStatus']
print("Current Stack status:", status)
paginator = client.get_paginator('describe_stack_events')

