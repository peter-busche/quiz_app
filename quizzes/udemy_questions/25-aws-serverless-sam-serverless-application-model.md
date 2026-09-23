# Section 25: AWS Serverless: SAM - Serverless Application Model ---> [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=732)
    ============================================================================================================================================================
- ### Questions:
    - 1. 
    The source code for an application is stored in a file named index.js that is in a folder along with a template file that includes the following code:
        AWSTemplateFormatVersion: '2010-09-09'
        Transform: 'AWS::Serverless-2016-10-31'
        Resources:
        LambdaFunctionWithAPI:
        Type: AWS::Serverless::Function
        Properties:
        Handler: index.handler
        Runtime: nodejs12.x
    What does a Developer need to do to prepare the template so it can be deployed using an AWS CLI command?

    - 2. 
    A Developer is using AWS SAM to create a template for deploying a serverless application. The Developer plans deploy an AWS Lambda function and an Amazon DynamoDB table using the template.
    Which resource types should the Developer specify? (Select TWO.)

    - 3. 
    A Developer has created the code for a Lambda function saved the code in a file named lambda_function.py. He has also created a template that named template.yaml. The following code is included in the template file:
        AWSTemplateFormatVersion: '2010-09-09'
        Transform: 'AWS::Serverless-2016-10-31'
        Resources:
        microservicehttpendpointpython3:
        Type: 'AWS::Serverless::Function'
        Properties:
        Handler: lambda_function.lambda_handler
        CodeUri: .
    What commands can the Developer use to prepare and then deploy this template? (Select TWO.)

    - 4. 
    A Developer is using AWS SAM to create a template for deploying a serverless application. The Developer plans deploy a Lambda function using the template.
    Which resource type should the Developer specify?

    - 5. 
    A Developer is looking for a way to use shorthand syntax to express functions, APIs, databases, and event source mappings. The Developer will test using AWS SAM to create a simple Lambda function using Nodejs.12x.
    What is the SIMPLEST way for the Developer to get started with a Hello World Lambda function?

    - 6. 
    A Developer needs to setup a new serverless application that includes AWS Lambda and Amazon API Gateway as part of a single stack. The Developer needs to be able to locally build and test the serverless applications before deployment on AWS.
    Which service should the Developer use?

    - 7. 
    - 8. 
    - 9. 
    - 10. 
    - 11. 
    - 12. 
    - 13. 
    - 14. 
    - 15. 
    - 16. 
    - 17. 
    - 18. 
    - 19. 
    - 20. 
    - 21. 
    - 22. 
    - 23. 
    - 24. 
    - 25. 
    - 26. 
    - 27. 
    - 28. 
    - 29. 


    ### Answers:
    - 1. 
    Run the aws cloudformation package command to upload the source code to an Amazon S3 bucket and produce a modified CloudFormation template
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=735)

    - 2. 
    AWS::Serverless::SimpleTable
    AWS::Serverless:Function
    https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-template-anatomy.html

    - 3. 
    Run aws cloudformation package and then aws cloudformation deploy
    Run sam package and then sam deploy
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=735)

    - 4. 
    AWS::Serverless:Function
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=735)

    - 5. 
    Install the AWS CLI, run aws sam init and use one of the AWS Quick Start Templates
    https://docs.aws.amazon.com/cli/latest/reference/cloudformation/package.html

    - 6. 
    AWS Serverless Application Model (SAM)
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=733)
    - 7. 
    - 8. 
    - 9. 
    - 10. 
    - 11. 
    - 12. 
    - 13. 
    - 14. 
    - 15. 
    - 16. 
    - 17. 
    - 18. 
    - 19. 
    - 20. 
    - 21. 
    - 22. 
    - 23. 
    - 24. 
    - 25. 
    - 26. 
    - 27. 
    - 28. 
    - 29.


    ### Wrong Answers:
    - 1. 
    Run the aws lambda create-function command to upload the source code to an Amazon S3 bucket and produce a modified CloudFormation template
    Run the aws cloudformation validate-template command to upload the source code to an Amazon S3 bucket and produce a modified CloudFormation template
    Run the aws s3 cp command to upload the source code to an Amazon S3 bucket and produce a modified CloudFormation template

    - 2. 
    AWS::Serverless::Api
    AWS::Serverless::LayerVersion
    AWS::Serverless::Application

    - 3. 
    Run aws cloudformation compile and then aws cloudformation deploy
    Run aws cloudformation deploy and then aws cloudformation package
    Run sam init and then sam publish

    - 4. 
    AWS::Serverless::Api
    AWS::Serverless::Application
    AWS::Serverless::SimpleTable

    - 5. 
    Install the AWS CLI, run aws cloudformation package and use one of the AWS Quick Start Templates
    Install the AWS CLI, run aws lambda create-function and use one of the AWS Quick Start Templates
    Install the AWS CLI, run aws sam publish and use one of the Serverless Application Repository templates

    - 6. 
    AWS Elastic Beanstalk
    AWS CodeDeploy
    AWS CloudFormation StackSets
