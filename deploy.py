import boto3

PROJECT = "upb-cloudformation"

cf = boto3.client('cloudformation')

with open('template.yaml', 'r') as file:
    template = file.read()

response= cf.create_stack(
    StackName=PROJECT,
    TemplateBody=template
)

print(response)