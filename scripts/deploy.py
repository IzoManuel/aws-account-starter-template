import boto3
import json
import os

def deploy_stack(stack_name, template_file, parameters_file):
    with open(template_file, 'r') as template:
        template_body = template.read()

    try:
        with open(parameters_file, 'r') as params:
            parameters = json.load(params)
            if not parameters:
                parameters = []
    except json.JSONDecodeError:
        parameters = []

    cloudformation = boto3.client('cloudformation')

    response = cloudformation.create_stack(
        StackName=stack_name,
        TemplateBody=template_body,
        Parameters=parameters,
        Capabilities=['CAPABILITY_NAMED_IAM']
    )

    print(f"Stack {stack_name} creation initiated.")
    return response

if __name__ == "__main__":
    # Adjust paths to be relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    template_file = os.path.join(script_dir, '../templates/main.yml')
    parameters_file = os.path.join(script_dir, '../parameters/security-params.json')

    stack_name = "security-stack"
    deploy_stack(stack_name, template_file, parameters_file)
