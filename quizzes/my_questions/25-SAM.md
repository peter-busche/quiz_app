# Section 25: My Questions: SAM - Serverless Application Model ---> [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=732)
    ============================================================================================================================================================
- ### Questions:
    - 1. 
    A developer opens a YAML template and needs to confirm it is an AWS SAM template rather than a plain CloudFormation template.
    Which line identifies it as a SAM template?

    - 2. 
    Which statements about AWS SAM are correct? (Select TWO.)

    - 3. 
    A developer wants to define a Lambda function, an API Gateway REST API, and a simple DynamoDB table in a SAM template.
    Which set of resource types should be used?

    - 4. 
    A developer runs the SAM CLI to deploy an application. In what order do the following steps happen?

    - 5. 
    When a developer runs sam deploy, where is the zipped application code uploaded before the CloudFormation stack is updated?

    - 6. 
    Under the hood, how does sam deploy apply changes to the CloudFormation stack?

    - 7. 
    A developer is iterating on Lambda function code and wants each code change to reach AWS in seconds, without waiting for a CloudFormation deployment.
    Which command should they use?

    - 8. 
    A developer wants the SAM CLI to watch the project for file changes and automatically push them to AWS as they are saved.
    Which command does this?

    - 9. 
    When sam sync --watch detects a change, how does it decide what to do?

    - 10. 
    A SAM project contains many resources. A developer wants to push a code change for ONLY the function with logical ID HelloWorldLambdaFunction.
    Which command should they run?

    - 11. 
    Which statement about sam sync --code is correct?

    - 12. 
    A Lambda function defined in a SAM template needs to create, read, update, and delete items in a DynamoDB table. The developer wants to grant these permissions with the least effort.
    What should they use?

    - 13. 
    A Lambda function in a SAM template must read messages from an Amazon SQS queue.
    Which SAM policy template grants this permission?

    - 14. 
    A Lambda function in a SAM template only needs read-only access to objects in an S3 bucket.
    Which SAM policy template is the BEST fit?

    - 15. 
    Which AWS service does SAM natively use to gradually shift traffic to a new version of a Lambda function?

    - 16. 
    A developer adds AutoPublishAlias: live to a Lambda function in a SAM template.
    What happens when new code is deployed?

    - 17. 
    A developer wants SAM to send 10% of traffic to the new version of a Lambda function for 10 minutes, then shift the rest.
    Which setting should they configure?

    - 18. 
    During a SAM deployment using CodeDeploy traffic shifting, the developer wants the deployment to roll back automatically if the new Lambda version causes errors, and wants to run validation tests before and after traffic is shifted. (Select TWO.)

    - 19. 
    A developer wants to run automated integration tests locally against an endpoint that emulates the AWS Lambda service.
    Which command should they use?

    - 20. 
    A developer wants to run a Lambda function locally ONCE with a test payload and exit when the invocation completes.
    Which command should they use?

    - 21. 
    A developer's function makes calls to AWS services. When running sam local invoke, the calls fail because they are using the wrong AWS account.
    What should the developer do?

    - 22. 
    A developer wants to test a Lambda function locally with a realistic S3 "put object" event but does not want to write the JSON payload by hand.
    Which command should they use?

    - 23. 
    A developer wants to run a local HTTP server that hosts all the API Gateway endpoints and Lambda functions in their SAM template, with function changes reloaded automatically.
    Which command should they use?

    - 24. 
    A team deploys the same SAM application to dev and prod environments with different parameters. They want to avoid typing the parameters on every deployment.
    What should they use?

    - 25. 
    A SAM template has 15 Lambda functions that all use the same runtime, memory size, timeout, and environment variables. The developer wants to avoid repeating these properties on every function.
    What should they use?

    - 26. 
    Several Lambda functions in a SAM application share the same third-party libraries. The developer wants to package these libraries once and reuse them across the functions.
    Which SAM resource type should they use?

    - 27. 
    A developer wants to define an AWS Step Functions state machine in a SAM template, and have SAM automatically generate IAM permissions for the Lambda functions it calls using policy templates.
    Which SAM resource type should they use?

    - 28. 
    A Lambda function in a SAM template must be invoked for every batch of messages that arrives in an Amazon SQS queue.
    How should this be configured in the SAM template?

    - 29. 
    A developer wants a Lambda function defined in a SAM template to run every day at midnight UTC.
    How should this be configured?

    - 30. 
    A developer wants AWS X-Ray tracing turned on for every Lambda function in a SAM template.
    What is the SIMPLEST way to do this?

    - 31. 
    A company wants to share a reusable SAM application (for example, a standard log-processing function) with other teams and AWS accounts, and let them deploy it with a few parameters.
    Which service should they publish it to?

    - 32. 
    A SAM template includes an application from the AWS Serverless Application Repository using the AWS::Serverless::Application resource. The deployment fails because of a missing capability.
    Which capability must be acknowledged?

    - 33. 
    A developer wants a REST API defined in a SAM template to only allow requests from users who are signed in to an Amazon Cognito user pool.
    What should the developer configure?

    - 34. 
    A team wants to quickly generate a CI/CD pipeline configuration (for example, AWS CodePipeline) with separate stages for deploying their SAM application to test and production accounts.
    Which SAM CLI command helps with this?


    ### Answers:
    - 1. 
    Transform: 'AWS::Serverless-2016-10-31'
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=734)

    - 2. 
    SAM generates complex CloudFormation from a simple SAM YAML template
    SAM can run Lambda, API Gateway, and DynamoDB locally
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=733)

    - 3. 
    AWS::Serverless::Function, AWS::Serverless::Api, AWS::Serverless::SimpleTable
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=734)

    - 4. 
    sam build, then sam package (optional) to zip and upload the code to S3, then sam deploy to create and execute a CloudFormation change set
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=735)

    - 5. 
    An Amazon S3 bucket
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=735)

    - 6. 
    It creates and executes a CloudFormation change set
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=735)

    - 7. 
    sam sync --code
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=737)

    - 8. 
    sam sync --watch
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=737)

    - 9. 
    If the changes include configuration it runs sam sync; if the changes are code only it runs sam sync --code
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=737)

    - 10. 
    sam sync --code --resource-id HelloWorldLambdaFunction
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=737)

    - 11. 
    It updates code using service APIs and bypasses CloudFormation, without updating infrastructure
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=736)

    - 12. 
    The DynamoDBCrudPolicy SAM policy template
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=738)

    - 13. 
    SQSPollerPolicy
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=738)

    - 14. 
    S3ReadPolicy
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=738)

    - 15. 
    AWS CodeDeploy
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=739)

    - 16. 
    SAM publishes a new version of the function with the latest code and points the "live" alias to it
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=740)

    - 17. 
    A DeploymentPreference with a Canary type (for example, Canary10Percent10Minutes)
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=740)

    - 18. 
    Add CloudWatch Alarms to the DeploymentPreference to trigger a rollback
    Add PreTraffic and PostTraffic hook Lambda functions to the DeploymentPreference
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=739)

    - 19. 
    sam local start-lambda
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=741)

    - 20. 
    sam local invoke
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=741)

    - 21. 
    Pass the correct --profile option to the SAM CLI
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=741)

    - 22. 
    sam local generate-event s3 put, piped into sam local invoke -e -
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=742)

    - 23. 
    sam local start-api
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=742)

    - 24. 
    A samconfig.toml file with a section per environment, deployed with sam deploy --config-env dev (or prod)
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=743)

    - 25. 
    The Globals section of the SAM template
    https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-template-anatomy-globals.html

    - 26. 
    AWS::Serverless::LayerVersion
    https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-layerversion.html

    - 27. 
    AWS::Serverless::StateMachine
    https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-statemachine.html

    - 28. 
    Add an event of Type: SQS (with the queue ARN and a BatchSize) under the function's Events property
    https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-sqs.html

    - 29. 
    Add an event of Type: Schedule (an Amazon EventBridge rule) with a cron expression under the function's Events property
    https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-schedule.html

    - 30. 
    Set Tracing: Active for Function in the Globals section
    https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-function.html#sam-function-tracing

    - 31. 
    AWS Serverless Application Repository
    https://docs.aws.amazon.com/serverlessrepo/latest/devguide/what-is-serverlessrepo.html

    - 32. 
    CAPABILITY_AUTO_EXPAND
    https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-template-nested-applications.html

    - 33. 
    A Cognito user pool authorizer in the Auth property of the AWS::Serverless::Api resource
    https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-api-cognitoauthorizer.html

    - 34. 
    sam pipeline init --bootstrap
    https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-generating-example-ci-cd.html


    ### Wrong Answers:
    - 1. 
    AWSTemplateFormatVersion: '2010-09-09'
    Transform: 'AWS::Include'
    Type: 'AWS::Serverless::Application'

    - 2. 
    SAM templates are written in a proprietary format that CloudFormation cannot read
    SAM templates cannot use CloudFormation Outputs, Mappings, or Parameters
    SAM can only deploy Lambda functions and no other AWS resources

    - 3. 
    AWS::Lambda::Function, AWS::ApiGateway::RestApi, AWS::DynamoDB::GlobalTable
    AWS::Serverless::Lambda, AWS::Serverless::Gateway, AWS::Serverless::Table
    AWS::Serverless::Function, AWS::Serverless::HttpApi, AWS::Serverless::DynamoDBTable

    - 4. 
    sam deploy, then sam build to compile the code, then sam package to upload the code to S3
    sam package to upload the code to CodeCommit, then sam deploy to call the Lambda UpdateFunctionCode API
    sam init, then sam sync --code to create a new CloudFormation stack from scratch

    - 5. 
    An AWS CodeCommit repository
    An Amazon ECR repository
    The /tmp directory of the Lambda function

    - 6. 
    It deletes the existing stack and creates a new one
    It calls the Lambda UpdateFunctionCode API directly for every resource
    It triggers an AWS CodePipeline pipeline that runs sam build

    - 7. 
    sam deploy --guided
    sam local invoke
    sam package

    - 8. 
    sam local start-api
    sam deploy --watch
    sam build --use-container

    - 9. 
    It always runs a full sam deploy with a CloudFormation change set
    It always runs sam sync --code, even when configuration changes
    It only reloads the function locally and never deploys to AWS

    - 10. 
    sam sync --code --resource AWS::Serverless::Function
    sam deploy --resource-id HelloWorldLambdaFunction
    sam local invoke HelloWorldLambdaFunction

    - 11. 
    It updates both code and infrastructure through a CloudFormation change set
    It only works for functions running locally with sam local start-lambda
    It uploads code to S3 and waits for the next scheduled CloudFormation deployment

    - 12. 
    The AmazonDynamoDBFullAccess managed policy attached to the developer's IAM user
    The DynamoDBReadPolicy SAM policy template
    A DynamoDB resource-based policy on the table

    - 13. 
    SQSSendMessagePolicy
    SNSPublishMessagePolicy
    S3ReadPolicy

    - 14. 
    S3CrudPolicy
    S3FullAccessPolicy
    DynamoDBReadPolicy

    - 15. 
    AWS CodePipeline
    AWS CodeBuild
    Amazon Route 53 weighted routing

    - 16. 
    SAM overwrites the $LATEST version and deletes the alias
    SAM creates a new Lambda function with a different name for each deployment
    SAM sends 100% of traffic to $LATEST and publishes a version only on rollback

    - 17. 
    A DeploymentPreference with an AllAtOnce type
    A DeploymentPreference with a Linear type (for example, Linear10PercentEvery1Minute)
    ReservedConcurrentExecutions set to 10 on the new version

    - 18. 
    Enable sam sync --watch to roll back automatically
    Add AWS Config rules to the Lambda alias
    Set the function's Timeout property to 10 minutes

    - 19. 
    sam local invoke
    sam local start-api
    sam local generate-event

    - 20. 
    sam local start-lambda
    sam local start-api
    sam sync --code

    - 21. 
    Add the credentials to the SAM template's Globals section
    Run sam local invoke with the --region option only
    Add the AWS account ID to samconfig.toml under the Resources section

    - 22. 
    sam local start-api --event s3
    sam build --event s3 put
    sam sync --code --event s3 put

    - 23. 
    sam local start-lambda
    sam local invoke
    sam deploy --local

    - 24. 
    A separate SAM template file for every environment
    Environment variables in the Globals section of the template
    The --guided flag on every sam deploy

    - 25. 
    The Mappings section of the template
    A SAM policy template
    The Outputs section of the template

    - 26. 
    AWS::Serverless::Application
    AWS::Serverless::SimpleTable
    AWS::Serverless::Function with a larger CodeUri

    - 27. 
    AWS::Serverless::Application
    AWS::Serverless::Function with a StepFunctions event
    AWS::StepFunctions::Activity

    - 28. 
    Add an SQSPollerPolicy to the function and write polling code in the handler
    Add an event of Type: SNS pointing to the queue ARN
    Configure the SQS queue's redrive policy to point to the Lambda function

    - 29. 
    Add an event of Type: SQS with a DelaySeconds of 86400
    Set the function's Timeout property to 86400 seconds
    Use sam sync --watch with a cron expression

    - 30. 
    Add the AWSXRayDaemonWriteAccess policy to the developer's IAM user
    Run sam local start-lambda with the --tracing flag
    Add an event of Type: XRay to each function

    - 31. 
    Amazon ECR Public Gallery
    AWS CodeArtifact
    AWS Marketplace

    - 32. 
    CAPABILITY_NAMED_IAM
    CAPABILITY_RESOURCE_POLICY
    CAPABILITY_SERVERLESS

    - 33. 
    An IAM policy template such as CognitoReadPolicy on the Lambda function
    An API key and usage plan on the AWS::Serverless::Api resource
    A resource-based policy on the Cognito user pool

    - 34. 
    sam init --pipeline
    sam deploy --guided
    sam sync --watch
