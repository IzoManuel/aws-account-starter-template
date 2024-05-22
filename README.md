
# AWS Security Setup with CloudFormation

This repository contains AWS CloudFormation templates and Python scripts to enforce security best practices, including setting up IAM roles and enforcing Multi-Factor Authentication (MFA) for IAM users. These resources are designed to be used in a bootcamp setting to ensure that all participants have a secure and consistent AWS environment.

## CloudFormation Templates

### IAM Roles

The `iam-roles.yaml` template creates IAM roles with specific policies for EC2 and Lambda.

**Resources Created:**
- `EC2Role`: IAM role for EC2 instances.
- `LambdaExecutionRole`: IAM role for Lambda functions.

### MFA Enforcement

The `mfa.yaml` template enforces MFA for IAM users by creating a group (`MFAEnforcedGroup`) and a policy (`MFAUserPolicy`) that denies access to users not using MFA.

**Resources Created:**
- `MFAEnforcedGroup`: IAM group with policies to enforce MFA.
- `MFAUserPolicy`: Policy attached to the group to enforce MFA requirements.

## Parameters

### Security Parameters

The `security-params.json` file provides parameter values for the security-related CloudFormation templates.

## Scripts

### Deployment Script

The `deploy.py` script is used to deploy the CloudFormation stack. It reads the template and parameters files and creates the necessary AWS resources.

### Validation Script

The `validate.py` script validates the CloudFormation template to ensure it is correctly formatted and can be deployed.

### Deletion Script

The `delete.py` script deletes the CloudFormation stack and all associated resources.

## Getting Started

### Prerequisites

- AWS account
- AWS CLI configured with your credentials
- Python installed

### Setting Up

1. Clone this repository to your local machine.
2. Navigate to the `scripts` directory.
3. Run the `deploy.py` script to deploy the CloudFormation stack.
4. Add users to the `MFAEnforcedGroup` to enforce MFA.
5. Attach the `EC2Role` and `LambdaExecutionRole` to your EC2 instances and Lambda functions, respectively.

## Monitoring and Managing Costs

- Use AWS Free Tier resources where possible.
- Set up AWS Budgets and Cost Alerts to monitor usage and receive notifications.
- Regularly check and delete unused resources to avoid unnecessary charges.

## Conclusion

By following this setup, you can ensure a secure and cost-effective AWS environment for your bootcamp participants. The provided templates and scripts help enforce best practices and streamline the setup process. If you have any questions or need further assistance, please refer to the AWS documentation or reach out for support.
