# Combined: Difficult Questions
    ============================================================================================================================================================
- ### Questions:
    - 1. 
    A critical application is hosted on AWS exposed by an HTTP API through Amazon API Gateway. The API is integrated with an AWS Lambda function and the application data is housed in an Amazon RDS for PostgreSQL DB instance, featuring 2 vCPUs and 16 GB of RAM.
    The company has been receiving customer complaints about occasional HTTP 500 Internal Server Error responses from some API calls during unpredictable peak usage times. Amazon CloudWatch Logs has recorded "connection limit exceeded" errors. The company wants to ensure resilience in the application, with no unscheduled downtime for the database.
    Which solution would best fit these requirements?

    - 2. 
    An ecommerce company manages a storefront that uses an Amazon API Gateway API which exposes an AWS Lambda function. The Lambda functions processes orders and stores the orders in an Amazon RDS for MySQL database. The number of transactions increases sporadically during marketing campaigns, and then goes close to zero during quite times.
    How can a developer increase the elasticity of the system MOST cost-effectively?

    - 3. 
    An organization handles data that requires high availability in its relational database. The main headquarters for the organization is in Virginia with smaller offices located in California. The main headquarters uses the data more frequently than the smaller offices. How should the developer configure their databases to meet high availability standards?

    - 4. 
    A Developer is creating a database solution using an Amazon ElastiCache caching layer. The solution must provide strong consistency to ensure that updates to product data are consistent between the backend database and the ElastiCache cache. Low latency performance is required for all items in the database.
    Which cache writing policy will satisfy these requirements?

    - 5. 
    An application uses an Amazon RDS database. The company requires that the performance of database reads is improved, and they want to add a caching layer in front of the database. The cached data must be encrypted, and the solution must be highly available.
    Which solution will meet these requirements?

    - 6. 
    In the process of developing an application, a software engineer deploys an Amazon API Gateway REST API within the us-west-2 Region. The plan is to use Amazon CloudFront and a custom domain name for the API, using an SSL/TLS certificate acquired from a third-party provider.
    What is the appropriate strategy for configuring the custom domain name?

    - 7. 
    An application uses Amazon EC2 instances, AWS Lambda functions and an Amazon SQS queue. The Developer must ensure all communications are within an Amazon VPC using private IP addresses. How can this be achieved? (Select TWO.)

    - 8. 
    An application reads data from Amazon S3 and makes 55,000 read requests per second. A Developer must design the storage solution to ensure the performance requirements are met cost-effectively.
    How can the storage be optimized to meet these requirements?

    - 9. 
    A company uses an Amazon S3 bucket to store a large number of sensitive files relating to eCommerce transactions. The company has a policy that states that all data written to the S3 bucket must be encrypted.
    How can a Developer ensure compliance with this policy?

    - 10. 
    A business is providing its clients read-only permissions to items within an Amazon S3 bucket, utilizing IAM permissions to limit access to this S3 bucket. Clients are only permitted to access their specific files. Regulatory compliance necessitates the enforcement of in-transit encryption during communication with Amazon S3.
    What solution will fulfill these criteria?

    - 11. 
    An independent software vendor (ISV) uses Amazon S3 and Amazon CloudFront to distribute software updates. They would like to provide their premium customers with access to updates faster. What is the MOST efficient way to distribute these updates only to the premium customers? (Select TWO.)

    - 12. 
    An application uses an Auto Scaling group of Amazon EC2 instances, an Application Load Balancer (ALB), and an Amazon Simple Queue Service (SQS) queue. An Amazon CloudFront distribution caches content for global users. A Developer needs to add in-transit encryption to the data by configuring end-to-end SSL between the CloudFront Origin and the end users.
    How can the Developer meet this requirement? (Select TWO.)

    - 13. 
    An online retail platform uses the AWS SDK for Python (Boto3) on the frontend to handle user authentication through AWS Security Token Service (AWS STS). The platform stores its digital assets in an Amazon S3 bucket and delivers them using an Amazon CloudFront distribution, which uses the S3 bucket as its origin.
    Currently, the application holds its role credentials in plaintext within a Python file in the application code. The platform developers are looking to improve security by creating a mechanism that enables the application to retrieve user credentials without embedding any credentials in the application code.
    What solution would meet these requirements?

    - 14. 
    A developer is updating an Amazon ECS app that uses an ALB with two target groups and a single listener. The developer has an AppSpec file in an S3 bucket and an AWS CodeDeploy deployment group tied to the ALB and AppSpec file. The developer needs to use an AWS Lambda function for update validation before deployment.
    Which solution meets these requirements?

    - 15. 
    A Developer has created a task definition that includes the following JSON code:
        "placementStrategy": [
        {
        "field": "attribute:ecs.availability-zone",
        "type": "spread"
        },
        {
        "field": "instanceId",
        "type": "spread"
        }
        ]
    What is the effect of this task placement strategy?

    - 16. 
    A Development team wants to run their container workloads on Amazon ECS. Each application container needs to share data with another container to collect logs and metrics.
    What should the Development team do to meet these requirements?

    - 17. 
    A Development team are developing a micro-services application that will use Docker containers on Amazon ECS. There will be 6 distinct services included in the architecture. Each service requires specific permissions to various AWS services.
    What is the MOST secure way to grant the services the necessary permissions?

    - 18. 
    A media company uses Amazon EC2 instances managed by AWS Elastic Beanstalk to run its high-traffic website. The engineering team needs to introduce a new feature, which requires upgrading the underlying platform to a newer version of Node.js. The deployment of the new code and the platform upgrade need to happen without causing any downtime.
    Which strategy should the team adopt to fulfill these requirements?

    - 19. 
    A business operates a web app on Amazon EC2 instances utilizing a bespoke Amazon Machine Image (AMI). They employ AWS CloudFormation for deploying their app, which is currently active in the us-east-1 Region. However, their goal is to extend the deployment to the us-west-1 Region.
    During an initial attempt to create an AWS CloudFormation stack in us-west-1, the action fails, and an error message indicates that the AMI ID does not exist. A developer is tasked with addressing this error through a method that minimizes operational complexity.
    Which action should the developer take?

    - 20. 
    A company runs a decoupled application that uses an Amazon SQS queue. The messages are processed by an AWS Lambda function. The function is not keeping up with the number of messages in the queue. A developer noticed that though the application can process multiple messages per invocation, it is only processing one at a time.
    How can the developer configure the application to process messages more efficiently?

    - 21. 
    A Developer manages a monitoring service for a fleet of IoT sensors in a major city. The monitoring application uses an Amazon Kinesis Data Stream with a group of EC2 instances processing the data. Amazon CloudWatch custom metrics show that the instances a reaching maximum processing capacity and there are insufficient shards in the Data Stream to handle the rate of data flow.
    What course of action should the Developer take to resolve the performance issues?

    - 22. 
    A Developer is writing an AWS Lambda function that processes records from an Amazon Kinesis Data Stream. The Developer must write the function so that it sends a notice to Administrators if it fails to process a batch of records.
    How should the Developer write the function?

    - 23. 
    An application uses Amazon Kinesis Data Streams to ingest and process large streams of data records in real time. Amazon EC2 instances consume and process the data using the Amazon Kinesis Client Library (KCL). The application handles the failure scenarios and does not require standby workers. The application reports that a specific shard is receiving more data than expected. To adapt to the changes in the rate of data flow, the “hot” shard is resharded.
    Assuming that the initial number of shards in the Kinesis data stream is 6, and after resharding the number of shards increased to 8, what is the maximum number of EC2 instances that can be deployed to process data from all the shards?

    - 24. 
    A Developer needs to run some code using Lambda in response to an event and forward the execution result to another application using a pub/sub notification.
    How can the Developer accomplish this?

    - 25. 
    An application asynchronously invokes an AWS Lambda function. The application has recently been experiencing occasional errors that result in failed invocations. A developer wants to store the messages that resulted in failed invocations such that the application can automatically retry processing them.
    What should the developer do to accomplish this goal with the LEAST operational overhead?

    - 26. 
    An application collects data from sensors in a manufacturing facility. The data is stored in an Amazon SQS Standard queue by an AWS Lambda function and an Amazon EC2 instance processes the data and stores it in an Amazon RedShift data warehouse. A fault in the sensors’ software is causing occasional duplicate messages to be sent. Timestamps on the duplicate messages show they are generated within a few seconds of the primary message.
    How can a Developer prevent duplicate data being stored in the data warehouse?

    - 27. 
    A developer is creating a multi-tier web application. The front-end will place messages in an Amazon SQS queue for the back-end to process. Each job includes a file that is 1GB in size. What MUST the developer do to ensure this works as expected?

    - 28. 
    An application is instrumented to generate traces using AWS X-Ray and generates a large amount of trace data. A Developer would like to use filter expressions to filter the results to specific key-value pairs added to custom subsegments.
    How should the Developer add the key-value pairs to the custom subsegments?

    - 29. 
    An application has been instrumented to use the AWS X-Ray SDK to collect data about the requests the application serves. The Developer has set the user field on segments to a string that identifies the user who sent the request.
    How can the Developer search for segments associated with specific users?

    - 30. 
    An AWS developer is building an application that processes sensitive personally identifiable information (PII). The application operates on AWS Lambda and writes diagnostic data to Amazon CloudWatch Logs. However, the developer wants to ensure that PII is not accidentally stored in CloudWatch Logs.
    What strategy should the developer adopt to ensure this?

    - 31. 
    A media organization utilizes an Amazon API Gateway REST API endpoint to disseminate updates from an internal Content Management System (CMS) to Amazon EventBridge. An EventBridge rule is set up to monitor these updates and control content syndication in a primary AWS account. The organization now wants to extend the reach of these updates across several affiliate AWS accounts.
    How can the developer accomplish this without altering the configuration of the CMS?

    - 32. 
    A company is running a Docker application on Amazon ECS. The application must scale based on user load in the last 15 seconds.
    How should the Developer instrument the code so that the requirement can be met?

    - 33. 
    An application serves customers in several different geographical regions. Information about the location users connect from is written to logs stored in Amazon CloudWatch Logs. The company needs to publish an Amazon CloudWatch custom metric that tracks connections for each location.
    Which approach will meet these requirements?

    - 34. 
    A developer is creating an AWS Serverless Application Model (AWS SAM) template. It includes several AWS Lambda functions, an Amazon S3 bucket, and an Amazon CloudFront distribution. One Lambda function, running on Lambda@Edge, is integrated with the CloudFront distribution, while the S3 bucket serves as an origin for the distribution.
        However, upon deploying the AWS SAM blueprint in the us-west-1 Region, the stack's creation fails.
        What could be the possible reason for this failure?

    - 35. 
    A company is planning to use AWS CodeDeploy to deploy a new AWS Lambda function
    What are the MINIMUM properties required in the 'resources' section of the AppSpec file for CodeDeploy to deploy the function successfully?

    - 36. 
    An AWS Lambda function requires several environment variables with secret values. The secret values should be obscured in the Lambda console and API output even for users who have permission to use the key.
    What is the best way to achieve this outcome and MINIMIZE complexity and latency?

    - 37. 
    A serverless application is used to process customer information and outputs a JSON file to an Amazon S3 bucket. AWS Lambda is used for processing the data. The data is sensitive and should be encrypted.
    How can a Developer modify the Lambda function to ensure the data is encrypted before it is uploaded to the S3 bucket?

    - 38. 
    A Developer is creating an AWS Lambda function to process a stream of data from an Amazon Kinesis Data Stream. When the Lambda function parses the data and encounters a missing field, it exits the function with an error. The function is generating duplicate records from the Kinesis stream. When the Developer looks at the stream output without the Lambda function, there are no duplicate records.
    What is the reason for the duplicates?

    - 39. 
    A Developer created an AWS Lambda function and then attempted to add an on failure destination but received the following error:
    The function's execution role does not have permissions to call SendMessage on arn:aws:sqs:us-east-1:515148212435:FailureDestination
    How can the Developer resolve this issue MOST securely?

    - 40. 
    An engineer is constructing a web-based application that uses Amazon DynamoDB for storing data. The data is distributed across two tables: 'authors' and 'books'. The 'authors' table uses 'authorName' as its partition key, while the 'books' table has 'bookTitle' as the partition key and 'authorName' as the sort key.
        The application requires the ability to fetch multiple books and authors simultaneously in a single database operation for effective performance. The engineer is seeking a solution that maximizes application efficiency and reduces network traffic.
        What strategy should the engineer employ to achieve these requirements?

    - 41. 
    A Developer has added a Global Secondary Index (GSI) to an existing Amazon DynamoDB table. The GSI is used mainly for read operations whereas the primary table is extremely write-intensive. Recently, the Developer has noticed throttling occurring under heavy write activity on the primary table. However, the write capacity units on the primary table are not fully utilized.
    What is the best explanation for why the writes are being throttled on the primary table?

    - 42. 
    A gaming company is building an application to track the scores for their games using an Amazon DynamoDB table. Each item in the table is identified by a partition key (user_id) and a sort key (game_name). The table also includes the attribute “TopScore”. 
    A Developer has been asked to write a leaderboard application to display the highest achieved scores for each game (game_name), based on the score identified in the “TopScore” attribute.
    What process will allow the Developer to extract results MOST efficiently from the DynamoDB table?

    - 43. 
    A gaming application stores scores for players in an Amazon DynamoDB table that has four attributes: user_id, user_name, user_score, and user_rank. The users are allowed to update their names only. A user is authenticated by web identity federation.
    Which set of conditions should be added in the policy attached to the role for the dynamodb:PutItem API call?

    - 44. 
    A Developer is troubleshooting an issue with a DynamoDB table. The table is used to store order information for a busy online store and uses the order date as the partition key. During busy periods writes to the table are being throttled despite the consumed throughput being well below the provisioned throughput.
    According to AWS best practices, how can the Developer resolve the issue at the LOWEST cost?

    - 45. 
    A developer is creating a serverless application that will use a DynamoDB table. The average item size is 9KB. The application will make 4 strongly consistent reads/sec, and 2 standard write/sec. How many RCUs/WCUs are required?

    - 46. 
    A Developer is creating a serverless application that uses an Amazon DynamoDB table. The application must make idempotent, all-or-nothing operations for multiple groups of write actions.
    Which solution will meet these requirements?

    - 47. 
    A developer is responsible for a business critical application that uses Amazon DynamoDB as its main data repository. This DynamoDB table holds millions of records and handles high volumes of requests. The developer must implement near-real time processing on the records as soon as they are inserted or modified in the DynamoDB table.
    What's the most efficient way to introduce this capability with MINIMUM modification to the existing application code?

    - 48. 
    A Development team are creating a financial trading application. The application requires sub-millisecond latency for processing trading requests. Amazon DynamoDB is used to store the trading data. During load testing the Development team found that in periods of high utilization the latency is too high and read capacity must be significantly over-provisioned to avoid throttling.
    How can the Developers meet the latency requirements of the application?

    - 49. 
    An Amazon API Gateway API developer aims to integrate request validation in a production setting but wants to test it before deployment. Which of the following methods offers the least operational overhead for testing via a tool by sending test requests?

    - 50. 
    A company wants to implement authentication for its new REST service using Amazon API Gateway. To authenticate the calls, each request must include HTTP headers with a client ID and user ID. These credentials must be compared to authentication data in an Amazon DynamoDB table.
    What MUST the company do to implement this authentication in API Gateway?

    - 51. 
    A software organization has developed a new feature in its serverless application hosted on AWS. This feature involves an AWS Lambda function that gets invoked by an Amazon API Gateway API. Currently, the API uses a specific Lambda alias to invoke the Lambda function. The organization wants to roll out this new feature to a select group of users for beta testing without affecting the application's existing users.
    What would be the most efficient approach to meet these requirements?

    - 52. 
    An online multiplayer game employs Amazon API Gateway WebSocket APIs with an HTTP backend. The game developer needs to add a feature that identifies players with unstable connections who repeatedly join and leave the game. The developer also wants the ability to disconnect such players from the game.
    What two modifications should the developer implement in the game to fulfill these requirements? (Select TWO.)

    - 53. 
    A firm intends to utilize AWS CodeDeploy to deploy an application to Amazon Elastic Container Service (Amazon ECS). While deploying an updated version of the application, the company's initial requirement is to direct 10% of active traffic to the updated application version. Following a 15-minute interval, all remaining active traffic must be rerouted to the updated application.
    Which predefined CodeDeploy configuration aligns with these needs?

    - 54. 
    A Developer needs to access AWS CodeCommit over SSH. The SSH keys configured to access AWS CodeCommit are tied to a user with the following permissions:
        {
        "version": "2012-10-17"
        "Statement": [
        {
        "Effect": "Allow",
        "Action": [
        "codecommit:BatchGetRepositories",
        "codecommit:Get*"
        "codecommit:List*",
        "codecommit:GitPull"
        ],
        "Resource": "*"
        }
        ]
        }
        The Developer needs to create/delete branches.
    Which specific IAM permissions need to be added based on the principle of least privilege?

    - 55. 
    A Developer is deploying an Amazon ECS update using AWS CodeDeploy. In the appspec.yaml file, which of the following is a valid structure for the order of hooks that should be specified?

    - 56. 
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

    - 57. 
    A Developer is creating a web application that will be used by employees working from home. The company uses a SAML directory on-premises for storing user information. The Developer must integrate with the SAML directory and authorize each employee to access only their own data when using the application.
    Which approach should the Developer take?

    - 58. 
    A customer requires a serverless application with an API which mobile clients will use. The API will have both and AWS Lambda function and an Amazon DynamoDB table as data sources. Responses that are sent to the mobile clients must contain data that is aggregated from both of these data sources.
    The developer must minimize the number of API endpoints and must minimize the number of API calls that are required to retrieve the necessary data.
    Which solution should the developer use to meet these requirements?

    - 59. 
    A company is using an AWS Step Functions state machine. When testing the state machine errors were experienced in the Step Functions task state machine. To troubleshoot the issue a developer requires that the state input be included along with the error message in the state output.
    Which coding practice can preserve both the original input and the error for the state?

    - 60. 
    An application running on a fleet of EC2 instances use the AWS SDK for Java to copy files into several AWS buckets using access keys stored in environment variables. A Developer has modified the instances to use an assumed IAM role with a more restrictive policy that allows access to only one bucket.
    However, after applying the change the Developer logs into one of the instances and is still able to write to all buckets. What is the MOST likely explanation for this situation?

    - 61. 
    An application that processes financial transactions receives thousands of transactions each second. The transactions require end-to-end encryption, and the application implements this by using the AWS KMS GenerateDataKey operation. During operation the application receives the following error message:
    “You have exceeded the rate at which you may call KMS. Reduce the frequency of your calls.
    (Service: AWSKMS; Status Code: 400; Error Code: ThrottlingException; Request ID: <ID>”
    Which actions are best practices to resolve this error? (Select TWO.)

    - 62. 
    An application is running on a cluster of Amazon EC2 instances. The application has received an error when trying to read objects stored within an Amazon S3 bucket. The bucket is encrypted with server-side encryption and AWS KMS managed keys (SSE-KMS). The error is as follows:
    Service: AWSKMS; Status Code: 400, Error Code: ThrottlingException
    Which combination of steps should be taken to prevent this failure? (Select TWO.)

    - 63. 
    A large quantity of sensitive data must be encrypted. A Developer will use a custom CMK to generate the encryption key. The key policy currently looks like this:
        {
        "Sid": "Allow Key Usage",
        "Effect": "Allow",
        "Principal": {"AWS": [
        "arn:aws:iam::111122223333:user/CMKUser"
        ]},
        "Action": [
        "kms:Encrypt",
        "kms:Decrypt",
        "kms:ReEncrypt*",
        "kms:DescribeKey"
        ],
        "Resource": "*"
        }
    What API action must be added to the key policy?

    - 64. 
    An international research organization holds a wide range of data across several Amazon S3 buckets. They recently received an alert indicating potential exposure of sensitive financial data via a public-facing web portal. The developer's job is to trace all potential data leakage points across their AWS infrastructure.
    What is the most effective strategy for this task?

    - 65. 
    A developer is running queries on Hive-compatible partitions in Athena using DDL but is facing time out issues. What is the most effective and efficient way to prevent this from continuing to happen?


    ### Answers:
    - 1. 
    Use Amazon RDS Proxy and update the Lambda function to connect to the proxy.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=152)
    [Source: 08-aws-fundamentals-rds-aurora-elasticache.md #12](../udemy_questions/08-aws-fundamentals-rds-aurora-elasticache.md)

    - 2. 
    Migrate from Amazon RDS to Amazon Aurora MySQL. Use an Aurora Auto Scaling policy to scale read replicas based on average connections of Aurora Replicas.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=)
    [Source: 08-aws-fundamentals-rds-aurora-elasticache.md #11](../udemy_questions/08-aws-fundamentals-rds-aurora-elasticache.md)

    - 3. 
    Create an Aurora database with the primary database in Virginia and specify the failover to the Aurora replica in another AZ in Virginia.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=145)
    [Source: 08-aws-fundamentals-rds-aurora-elasticache.md #10](../udemy_questions/08-aws-fundamentals-rds-aurora-elasticache.md)

    - 4. 
    Use a write-through caching strategy.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=160)
    [Source: 08-aws-fundamentals-rds-aurora-elasticache.md #2](../udemy_questions/08-aws-fundamentals-rds-aurora-elasticache.md)

    - 5. 
    Amazon ElastiCache for Redis in cluster mode.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=)
    [Source: 08-aws-fundamentals-rds-aurora-elasticache.md #14](../udemy_questions/08-aws-fundamentals-rds-aurora-elasticache.md)

    - 6. 
    Import the third-party SSL/TLS certificate to AWS Certificate Manager (ACM), link it with the custom domain name in API Gateway, and then create an alias (A) record in Route 53 for the custom domain name.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=195)
    [Source: 09-route-53.md #2](../udemy_questions/09-route-53.md)

    - 7. 
    Add the AWS Lambda function to the VPC
    Create a VPC endpoint for Amazon SQS
    [Source: 10-vpc-fundamentals.md #5](../udemy_questions/10-vpc-fundamentals.md)

    - 8. 
    Create at least 10 prefixes and split the files across the prefixes.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=257)
    [Source: 13-advanced-amazon-s3.md #1](../udemy_questions/13-advanced-amazon-s3.md)

    - 9. 
    Create an S3 bucket policy that denies any S3 Put request that does not include the x-amz-server-side-encryption
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=270)
    [Source: 14-amazon-s3-security.md #1](../udemy_questions/14-amazon-s3-security.md)

    - 10. 
    Update the S3 bucket policy to include a condition that requires aws:SecureTransport for all actions.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=269)
    [Source: 14-amazon-s3-security.md #7](../udemy_questions/14-amazon-s3-security.md)

    - 11. 
    Create a signed URL with access to the content and distribute it to the premium customers
    Create an origin access identity (OAI) and associate it with the distribution and configure permissions
    [Source: 14-amazon-s3-security.md #8](../udemy_questions/14-amazon-s3-security.md)

    - 12. 
    Configure the Origin Protocol Policy
    Configure the Viewer Protocol Policy
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=283)
    https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html
    [Source: 15-cloudfront.md #1](../udemy_questions/15-cloudfront.md)

    - 13. 
    Integrate a Lambda@Edge function with the CloudFront distribution. Trigger the function upon each viewer request. Give the execution role of the function the required permissions to interact with AWS STS. Shift all SDK calls from the frontend to this function.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=567)
    [Source: 15-cloudfront.md #4](../udemy_questions/15-cloudfront.md)

    - 14. 
    Add a listener to the ALB. Update the AppSpec file to link the Lambda function to the BeforeAllowTraffic lifecycle hook.
    https://docs.aws.amazon.com/codedeploy/latest/userguide/reference-appspec-file.html
    [Source: 16-ecs-ecr-fargate-docker-in-aws.md #9](../udemy_questions/16-ecs-ecr-fargate-docker-in-aws.md)

    - 15. 
    It distributes tasks evenly across Availability Zones and then distributes tasks evenly across the instances within each Availability Zone
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=)
    [Source: 16-ecs-ecr-fargate-docker-in-aws.md #12](../udemy_questions/16-ecs-ecr-fargate-docker-in-aws.md)

    - 16. 
    Create one task definition. Specify both containers in the definition. Mount a shared volume between those two containers
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=339)
    [Source: 16-ecs-ecr-fargate-docker-in-aws.md #13](../udemy_questions/16-ecs-ecr-fargate-docker-in-aws.md)

    - 17. 
    Create six separate IAM roles, each containing the required permissions for the associated ECS service, then configure each ECS task definition to reference the associated IAM role
    [Source: 16-ecs-ecr-fargate-docker-in-aws.md #16](../udemy_questions/16-ecs-ecr-fargate-docker-in-aws.md)

    - 18. 
    Implement Blue/Green (CNAME Swap) deployment using Elastic Beanstalk. Prepare a separate environment with the new version of Node.js and the new code, and once testing is complete, swap the CNAMEs of the two environments.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=378)
    [Source: 17-aws-elastic-beanstalk.md #5](../udemy_questions/17-aws-elastic-beanstalk.md)

    - 19. 
    Copy the AMI from the us-east-1 Region to the us-west-1 Region and use the new AMI ID in the CloudFormation template. Dont have to rebuild AMI this way.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=379)
    [Source: 18-aws-cloudformation.md #4](../udemy_questions/18-aws-cloudformation.md)

    - 20. 
    Call the ReceiveMessage API to set MaxNumberOfMessages to a value greater than the default of 1.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=446)
    [Source: 19-aws-integration-messaging-sqs-sns-kinesis.md #3](../udemy_questions/19-aws-integration-messaging-sqs-sns-kinesis.md)

    - 21. 
    Increase the EC2 instance size and add shards to the stream
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=463)
    [Source: 19-aws-integration-messaging-sqs-sns-kinesis.md #6](../udemy_questions/19-aws-integration-messaging-sqs-sns-kinesis.md)

    - 22. 
    Configure an Amazon SNS topic as an on-failure destination
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=551)
    [Source: 19-aws-integration-messaging-sqs-sns-kinesis.md #12](../udemy_questions/19-aws-integration-messaging-sqs-sns-kinesis.md)

    - 23. 
    8
    https://docs.aws.amazon.com/streams/latest/dev/kinesis-record-processor-scaling.html
    [Source: 19-aws-integration-messaging-sqs-sns-kinesis.md #13](../udemy_questions/19-aws-integration-messaging-sqs-sns-kinesis.md)

    - 24. 
    Configure a Lambda “on success” destination and route the execution results to Amazon SNS
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=468)
    [Source: 19-aws-integration-messaging-sqs-sns-kinesis.md #17](../udemy_questions/19-aws-integration-messaging-sqs-sns-kinesis.md)

    - 25. 
    Configure a redrive policy on an Amazon SQS queue. Set the dead-letter queue as an event source to the Lambda function.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=)
    [Source: 19-aws-integration-messaging-sqs-sns-kinesis.md #20](../udemy_questions/19-aws-integration-messaging-sqs-sns-kinesis.md)

    - 26. 
    Use a FIFO queue and configure the Lambda function to add a message deduplication token to the message body
    [Source: 19-aws-integration-messaging-sqs-sns-kinesis.md #22](../udemy_questions/19-aws-integration-messaging-sqs-sns-kinesis.md)

    - 27. 
    Store the large files in Amazon S3 and use the SQS Extended Client Library for Java to manage SQS messages
    [Source: 19-aws-integration-messaging-sqs-sns-kinesis.md #25](../udemy_questions/19-aws-integration-messaging-sqs-sns-kinesis.md)

    - 28. 
    Add annotations to the custom subsegments
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=509)
    [Source: 20-aws-monitoring-audit-cloudwatch-x-ray-and-cloudtrail.md #2](../udemy_questions/20-aws-monitoring-audit-cloudwatch-x-ray-and-cloudtrail.md)

    - 29. 
    By using the GetTraceSummaries API with a filter expression
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=513)
    [Source: 20-aws-monitoring-audit-cloudwatch-x-ray-and-cloudtrail.md #5](../udemy_questions/20-aws-monitoring-audit-cloudwatch-x-ray-and-cloudtrail.md)

    - 30. 
    Configure Amazon CloudWatch Logs data protection to detect and mask PII in log events (using managed data identifiers) before the data is stored.
    https://digitalcloud.training/amazon-cloudwatch/
    [Source: 20-aws-monitoring-audit-cloudwatch-x-ray-and-cloudtrail.md #8](../udemy_questions/20-aws-monitoring-audit-cloudwatch-x-ray-and-cloudtrail.md)

    - 31. 
    Implement an EventBridge event bus in the affiliate AWS accounts to create a rule that matches events and forwards them from the main account.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=496)
    [Source: 20-aws-monitoring-audit-cloudwatch-x-ray-and-cloudtrail.md #12](../udemy_questions/20-aws-monitoring-audit-cloudwatch-x-ray-and-cloudtrail.md)

    - 32. 
    Create a high-resolution custom Amazon CloudWatch metric for user activity data, then publish data every 5 seconds
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=474)
    [Source: 20-aws-monitoring-audit-cloudwatch-x-ray-and-cloudtrail.md #13](../udemy_questions/20-aws-monitoring-audit-cloudwatch-x-ray-and-cloudtrail.md)

    - 33. 
    Create a CloudWatch metric filter to extract metrics from the log files with location as a dimension.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=)
    [Source: 20-aws-monitoring-audit-cloudwatch-x-ray-and-cloudtrail.md #17](../udemy_questions/20-aws-monitoring-audit-cloudwatch-x-ray-and-cloudtrail.md)

    - 34. 
    Lambda@Edge functions can only be deployed in the us-east-1 Region.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=567)
    [Source: 21-aws-serverless-lambda.md #1](../udemy_questions/21-aws-serverless-lambda.md)

    - 35. 
    name, alias, currentversion, and targetversion
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=595)
    [Source: 21-aws-serverless-lambda.md #8](../udemy_questions/21-aws-serverless-lambda.md)

    - 36. 
    Encrypt the secret values client-side using encryption helpers
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=561)
    [Source: 21-aws-serverless-lambda.md #10](../udemy_questions/21-aws-serverless-lambda.md)

    - 37. 
    Use the GenerateDataKey API, then use the data key to encrypt the file using the Lambda code
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=561)
    [Source: 21-aws-serverless-lambda.md #14](../udemy_questions/21-aws-serverless-lambda.md)

    - 38. 
    The Lambda function did not handle the error, and the Lambda service attempted to reprocess the data
    [Source: 21-aws-serverless-lambda.md #31](../udemy_questions/21-aws-serverless-lambda.md)

    - 39. 
    Create a customer managed policy with all read/write permissions to SQS and attach the policy to the function’s execution role
    [Source: 21-aws-serverless-lambda.md #32](../udemy_questions/21-aws-serverless-lambda.md)

    - 40. 
    Utilize the DynamoDB BatchGetItem operation to fetch multiple items from both tables in a single network round trip.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=623)
    [Source: 22-aws-serverless-dynamodb.md #2](../udemy_questions/22-aws-serverless-dynamodb.md)

    - 41. 
    The write capacity units on the GSI are under provisioned
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=632)
    [Source: 22-aws-serverless-dynamodb.md #6](../udemy_questions/22-aws-serverless-dynamodb.md)

    - 42. 
    Create a global secondary index with a partition key of “game_name” and a sort key of “TopScore” and get the results based on the score attribute.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=632)
    [Source: 22-aws-serverless-dynamodb.md #8](../udemy_questions/22-aws-serverless-dynamodb.md)

    - 43. 
    "Condition": {
        "ForAllValues:StringEquals": {
            "dynamodb:LeadingKeys": [
                "${www.amazon.com:user_id}"
            ],
                "dynamodb:Attributes": [
                "user_name"
            ]
        }
    }
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=625)
    [Source: 22-aws-serverless-dynamodb.md #9](../udemy_questions/22-aws-serverless-dynamodb.md)

    - 44. 
    Add a random number suffix to the partition key values
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=)
    [Source: 22-aws-serverless-dynamodb.md #14](../udemy_questions/22-aws-serverless-dynamodb.md)

    - 45. 
    12 RCU and 18 WCU
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=612)
    [Source: 22-aws-serverless-dynamodb.md #17](../udemy_questions/22-aws-serverless-dynamodb.md)

    - 46. 
    Update the items in the table using the TransactWriteltems operation to group the changes.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=644)
    [Source: 22-aws-serverless-dynamodb.md #23](../udemy_questions/22-aws-serverless-dynamodb.md)

    - 47. 
    Use AWS Lambda triggered by DynamoDB Streams to process the documents.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=)
    [Source: 22-aws-serverless-dynamodb.md #29](../udemy_questions/22-aws-serverless-dynamodb.md)

    - 48. 
    Use Amazon DynamoDB Accelerator (DAX) to cache the data
    [Source: 22-aws-serverless-dynamodb.md #35](../udemy_questions/22-aws-serverless-dynamodb.md)

    - 49. 
    Modify the existing API to include request validation, deploy this to a new API Gateway stage, test it, then deploy it to the production stage.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=666)
    [Source: 23-aws-serverless-api-gateway.md #3](../udemy_questions/23-aws-serverless-api-gateway.md)

    - 50. 
    Implement an AWS Lambda authorizer that references the DynamoDB authentication table
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=690)
    [Source: 23-aws-serverless-api-gateway.md #6](../udemy_questions/23-aws-serverless-api-gateway.md)

    - 51. 
    Create a new version of the Lambda function. Build a new stage on API Gateway integrated with this new Lambda version. Utilize this new API Gateway stage for beta testing.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=666)
    [Source: 23-aws-serverless-api-gateway.md #11](../udemy_questions/23-aws-serverless-api-gateway.md)

    - 52. 
    Implement $connect and $disconnect routes in the backend service.
    Add logic to track the player's connection status using Amazon DynamoDB in the backend service.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=698)
    https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-route-keys-connect-disconnect.html
    [Source: 23-aws-serverless-api-gateway.md #12](../udemy_questions/23-aws-serverless-api-gateway.md)

    - 53. 
    CodeDeployDefault.ECSCanary10Percent15Minutes
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=724)
    [Source: 24-aws-cicd-codecommit-codepipeline-codebuild-codedeploy.md #7](../udemy_questions/24-aws-cicd-codecommit-codepipeline-codebuild-codedeploy.md)

    - 54. 
    “codecommit:CreateBranch” and “codecommit:DeleteBranch”
    https://docs.aws.amazon.com/cli/latest/reference/codecommit/index.html#cli-aws-codecommit
    [Source: 24-aws-cicd-codecommit-codepipeline-codebuild-codedeploy.md #14](../udemy_questions/24-aws-cicd-codecommit-codepipeline-codebuild-codedeploy.md)

    - 55. 
    BeforeInstall > AfterInstall > AfterAllowTestTraffic > BeforeAllowTraffic > AfterAllowTraffic
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=718)
    https://docs.aws.amazon.com/codedeploy/latest/userguide/reference-appspec-file-structure-hooks.html
    [Source: 24-aws-cicd-codecommit-codepipeline-codebuild-codedeploy.md #16](../udemy_questions/24-aws-cicd-codecommit-codepipeline-codebuild-codedeploy.md)

    - 56. 
    Run the aws cloudformation package command to upload the source code to an Amazon S3 bucket and produce a modified CloudFormation template
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=735)
    [Source: 25-aws-serverless-sam-serverless-application-model.md #1](../udemy_questions/25-aws-serverless-sam-serverless-application-model.md)

    - 57. 
    Use an Amazon Cognito identity pool, federate with the SAML provider, and use a trust policy with an IAM condition key to limit employee access.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=)
    [Source: 27-cognito-cognito-user-pools-cognito-identity-pools-cognito-sync.md #8](../udemy_questions/27-cognito-cognito-user-pools-cognito-identity-pools-cognito-sync.md)

    - 58. 
    GraphQL API on AWS AppSync
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=795)
    [Source: 28-other-serverless-step-functions-appsync.md #4](../udemy_questions/28-other-serverless-step-functions-appsync.md)

    - 59. 
    Use ResultPath in a Catch statement to include the original input with the error.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=789)
    [Source: 28-other-serverless-step-functions-appsync.md #5](../udemy_questions/28-other-serverless-step-functions-appsync.md)

    - 60. 
    The AWS credential provider looks for instance profile credentials last
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=812)
    [Source: 29-advanced-identity.md #1](../udemy_questions/29-advanced-identity.md)

    - 61. 
    Create a local cache using the AWS Encryption SDK and the LocalCryptoMaterialsCache feature.
    Create a case in the AWS Support Center to increase the quota for the account.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=843)
    [Source: 30-aws-security-encryption-kms-encryption-sdk-ssm-parameter-store-iam-sts.md #2](../udemy_questions/30-aws-security-encryption-kms-encryption-sdk-ssm-parameter-store-iam-sts.md)

    - 62. 
    Perform error retries with exponential backoff in the application code
    Contact AWS support to request an AWS KMS rate limit increase
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=843)
    [Source: 30-aws-security-encryption-kms-encryption-sdk-ssm-parameter-store-iam-sts.md #5](../udemy_questions/30-aws-security-encryption-kms-encryption-sdk-ssm-parameter-store-iam-sts.md)

    - 63. 
    kms:GenerateDataKey
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=837)
    [Source: 30-aws-security-encryption-kms-encryption-sdk-ssm-parameter-store-iam-sts.md #6](../udemy_questions/30-aws-security-encryption-kms-encryption-sdk-ssm-parameter-store-iam-sts.md)

    - 64. 
    Implement Amazon Macie and apply the SensitiveData:S3Object/financial finding type across all S3 buckets to automatically identify potential exposure of sensitive financial data.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=886)
    [Source: 31-aws-other-services.md #1](../udemy_questions/31-aws-other-services.md)

    - 65. 
    Use the MSCK REPAIR TABLE command to update the metadata in the catalog.
    https://docs.aws.amazon.com/athena/latest/ug/msck-repair-table.html
    [Source: 99-other.md #7](../udemy_questions/99-other.md)


    ### Wrong Answers:
    - 1. 
    Increase the reserved concurrency of the Lambda function to handle more connections.
    Enable Multi-AZ on the RDS DB instance and update the Lambda function to connect to the standby.
    Add an Amazon ElastiCache cluster and update the Lambda function to connect to the cache.

    - 2. 
    Migrate from Amazon RDS to Amazon Aurora MySQL. Use a scheduled scaling policy on the Lambda function to add provisioned concurrency.
    Increase the instance size of the Amazon RDS for MySQL database. Enable Multi-AZ to scale read traffic during campaigns.
    Migrate from Amazon RDS to Amazon EC2 instances running MySQL. Use an EC2 Auto Scaling group to add instances based on CPU utilization.

    - 3. 
    Create an RDS database with the primary database in California and a read replica in the same AZ in California.
    Create an Aurora database with the primary database in California and specify the failover to the Aurora replica in Virginia.
    Create an RDS database in a single AZ in Virginia and take daily automated snapshots copied to California.

    - 4. 
    Use a lazy loading caching strategy.
    Use a cache-aside strategy with a long TTL.
    Use a write-around caching strategy.

    - 5. 
    Amazon ElastiCache for Memcached with multiple nodes.
    Amazon RDS read replicas in the same Availability Zone.
    Amazon ElastiCache for Redis with cluster mode disabled and a single node.

    - 6. 
    Import the third-party SSL/TLS certificate to AWS Secrets Manager, link it with the custom domain name in API Gateway, and then create an MX record in Route 53 for the custom domain name.
    Upload the third-party SSL/TLS certificate directly to the API Gateway stage, and then create a TXT record in Route 53 for the custom domain name.
    Import the third-party SSL/TLS certificate to AWS Systems Manager Parameter Store, link it with the API Gateway stage, and then create an NS record in Route 53.

    - 7. 
    Create a NAT gateway so that the Lambda function can reach Amazon SQS
    Attach an internet gateway to the VPC for the EC2 instances to reach SQS
    Create a VPC peering connection between the VPC and the Amazon SQS service

    - 8. 
    Store all the files under a single prefix to maximize request throughput.
    Enable Amazon S3 Transfer Acceleration on the bucket.
    Move the files to the S3 Glacier Flexible Retrieval storage class.

    - 9. 
    Create an S3 bucket policy that denies any S3 Get request that does not include the x-amz-server-side-encryption
    Enable S3 Versioning and MFA Delete on the bucket to protect the data
    Create an S3 bucket policy that denies any request where aws:SecureTransport is false

    - 10. 
    Update the S3 bucket policy to include a condition that requires s3:x-amz-server-side-encryption for all actions.
    Enable default encryption with SSE-KMS on the S3 bucket for all objects.
    Enable S3 Object Lock on the bucket in compliance mode for all objects.

    - 11. 
    Make the S3 bucket public and share the object URLs with the premium customers
    Create a separate CloudFront distribution with a lower price class for premium customers
    Enable S3 Transfer Acceleration on the bucket and share the endpoint with premium customers

    - 12. 
    Configure the Cache Behavior TTL settings
    Configure the Price Class of the distribution
    Configure Origin Access Control on the SQS queue

    - 13. 
    Move the role credentials from the Python file into environment variables in the frontend application code. Continue to call AWS STS from the frontend using the SDK.
    Store the role credentials in a public object in the S3 origin bucket. Configure the frontend to download the credentials through the CloudFront distribution before each SDK call.
    Add the role credentials as custom headers on the CloudFront distribution origin. Configure the frontend to read the headers and pass them to AWS STS on each request.

    - 14. 
    Add a listener to the ALB. Update the AppSpec file to link the Lambda function to the AfterAllowTraffic lifecycle hook.
    Add a target group to the ALB. Update the AppSpec file to link the Lambda function to the ValidateService lifecycle hook.
    Remove a target group from the ALB. Update the AppSpec file to link the Lambda function to the ApplicationStart lifecycle hook.

    - 15. 
    It distributes tasks randomly across Availability Zones and then places tasks on the instance with the least available memory
    It places all tasks in a single Availability Zone and then spreads them evenly across the instances in that zone
    It distributes tasks evenly across instances first and then balances the remaining tasks across Availability Zones

    - 16. 
    Create two task definitions, one for each container, and mount a shared Amazon EBS volume between the tasks
    Create one task definition for each container and configure them to share data using an Amazon SQS queue
    Create one task definition with both containers and enable awsvpc networking so they share the same file system

    - 17. 
    Create a single IAM role containing the permissions for all six services and attach it to the ECS container instance profile
    Create six separate IAM users with access keys and store the keys as environment variables in each ECS task definition
    Create a single IAM role containing the permissions for all six services and configure every ECS task definition to reference it

    - 18. 
    Use the All at once deployment policy on the existing environment to deploy the new code and update the platform to the newer Node.js version in a single step.
    Enable managed platform updates on the existing environment to upgrade Node.js, and deploy the new code using the All at once deployment policy in the same maintenance window.
    Add an .ebextensions command that upgrades Node.js on each running EC2 instance, then deploy the new code to the existing environment using the All at once deployment policy.

    - 19. 
    Create a new CloudFormation stack in us-east-1 with the Region parameter set to us-west-1 to reuse the same AMI ID.
    Share the AMI from the us-east-1 Region with the us-west-1 Region using AMI launch permissions and keep the same AMI ID.
    Rebuild the custom AMI from scratch in the us-west-1 Region and hard-code the new AMI ID into all templates.

    - 20. 
    Call the ChangeMessageVisibility API to set VisibilityTimeout to a value greater than the default of 30.
    Call the SetQueueAttributes API to set DelaySeconds to a value greater than the default of 0.
    Call the SendMessageBatch API to set MaxNumberOfMessages to a value greater than the default of 1.

    - 21. 
    Decrease the EC2 instance size and merge shards in the stream
    Increase the EC2 instance size and merge shards in the stream
    Add more EC2 instances and increase the stream retention period

    - 22. 
    Configure an Amazon SNS topic as an on-success destination
    Configure Amazon SES as an on-failure destination
    Configure a CloudWatch Logs log group as an on-failure destination

    - 23. 
    6
    12
    16

    - 24. 
    Configure a Lambda “on failure” destination and route the execution results to Amazon SNS
    Configure a Lambda dead-letter queue and route the execution results to Amazon SNS
    Configure a Lambda “on success” destination and route the execution results to Amazon SQS

    - 25. 
    Configure an Amazon SNS topic as an on-failure destination. Subscribe an email address to the topic to review the failed events.
    Configure the function to write failed events to CloudWatch Logs. Create a metric filter that re-invokes the Lambda function.
    Configure reserved concurrency on the Lambda function. Increase the maximum retry attempts for asynchronous invocation to 10.

    - 26. 
    Use a Standard queue and configure the Lambda function to add a message deduplication ID to the message attributes
    Increase the visibility timeout of the Standard queue to be longer than the time between duplicate messages
    Configure a dead-letter queue to capture duplicate messages before they are processed by the EC2 instance

    - 27. 
    Increase the maximum message size of the SQS queue to 1GB
    Split each file into 256KB chunks and send them as a batch of SQS messages
    Compress the files and store them in the SQS message body using the SQS Extended Client Library for Java

    - 28. 
    Add metadata to the custom subsegments
    Add sampling rules to the custom subsegments
    Add dimensions to the custom subsegments

    - 29. 
    By using the BatchGetTraces API with a filter expression
    By using the GetServiceGraph API with a filter expression
    By using the PutTraceSegments API with a filter expression

    - 30. 
    Configure a CloudWatch Logs metric filter to detect PII in log events and delete the matching events after the data is stored.
    Enable AWS KMS encryption on the CloudWatch Logs log group so that PII in log events is masked before the data is stored.
    Configure Amazon Macie to scan the CloudWatch Logs log group directly and mask PII in log events before the data is stored.

    - 31. 
    Configure the CMS to publish the updates directly to the default event bus in each affiliate AWS account.
    Create an EventBridge archive in the main account and replay the archived events into each affiliate AWS account.
    Create an additional API Gateway REST API in each affiliate account and point the CMS to these new endpoints.

    - 32. 
    Create a standard-resolution custom Amazon CloudWatch metric for user activity data, then publish data every 5 seconds
    Create a high-resolution custom Amazon CloudWatch metric for user activity data, then publish data every 60 seconds
    Enable detailed monitoring on the Amazon ECS cluster for user activity data, then publish data every 5 seconds

    - 33. 
    Create a CloudWatch Logs subscription filter to stream the log files to Kinesis with location as a partition key.
    Create a CloudWatch alarm on the log group to count connections with location as a dimension.
    Create a CloudWatch Logs Insights query to aggregate the log files with location as a dimension.

    - 34. 
    Lambda@Edge functions cannot be defined in AWS SAM templates and must be created in the Lambda console.
    CloudFront distributions cannot use an S3 bucket located in the us-west-1 Region as an origin.
    AWS SAM templates cannot deploy more than one Lambda function within a single stack.

    - 35. 
    name, alias, and targetversion
    name, runtime, handler, and codeuri
    name, alias, currentversion, and hooks

    - 36. 
    Store the secret values as plaintext environment variables and rely on default encryption at rest
    Encrypt the secret values with the default AWS managed key for Lambda (aws/lambda)
    Store the secret values as tags on the Lambda function and restrict access to the tags

    - 37. 
    Enable SSE-S3 default encryption on the S3 bucket so the file is encrypted after it is uploaded
    Add an S3 bucket policy that denies PutObject requests without the x-amz-server-side-encryption header
    Use the Decrypt API to generate a plaintext key, then use that key to encrypt the file using the Lambda code

    - 38. 
    Amazon Kinesis Data Streams delivers each record at least twice by default
    The Lambda function's reserved concurrency is set too high, causing records to be read in parallel
    The Kinesis stream's retention period is too short, causing records to be republished

    - 39. 
    Add a resource-based policy to the Lambda function granting SQS permission to invoke it
    Attach the AdministratorAccess managed policy to the function's execution role
    Add a permission to the SQS queue policy allowing the Lambda service principal full access

    - 40. 
    Utilize the DynamoDB Query operation to fetch multiple items from both tables in a single network round trip.
    Utilize the DynamoDB Scan operation with a filter expression to fetch multiple items from both tables in a single network round trip.
    Utilize the DynamoDB GetItem operation to fetch multiple items from both tables in a single network round trip.

    - 41. 
    The write capacity units on the primary table are under provisioned
    The read capacity units on the GSI are under provisioned
    The DynamoDB Streams shard for the primary table is throttling write requests

    - 42. 
    Create a local secondary index with a sort key of “TopScore” and get the results based on the score attribute.
    Scan the table with a filter on “game_name” and sort the results by “TopScore” in the application.
    Create a global secondary index with a partition key of “TopScore” and a sort key of “game_name” and get the results based on the score attribute.

    - 43. 
    "Condition": { "ForAllValues:StringEquals": { "dynamodb:LeadingKeys": [ "${www.amazon.com:user_id}" ], "dynamodb:Attributes": [ "user_name", "user_score", "user_rank" ] } }
    "Condition": { "ForAllValues:StringNotEquals": { "dynamodb:LeadingKeys": [ "${www.amazon.com:user_id}" ], "dynamodb:Attributes": [ "user_name" ] } }
    "Condition": { "ForAllValues:StringEquals": { "dynamodb:LeadingKeys": [ "${www.amazon.com:user_name}" ], "dynamodb:Attributes": [ "user_id" ] } }

    - 44. 
    Increase the provisioned write capacity units on the table
    Enable DynamoDB Accelerator (DAX) to cache the write requests
    Add a global secondary index on the order date attribute

    - 45. 
    6 RCU and 18 WCU
    12 RCU and 9 WCU
    9 RCU and 36 WCU

    - 46. 
    Update the items in the table using the BatchWriteItem operation to group the changes.
    Update the items in the table using the TransactGetItems operation to group the changes.
    Update the items in the table using conditional PutItem calls with the ReturnValues parameter.

    - 47. 
    Use a scheduled AWS Lambda function that scans the table every minute to find new records.
    Modify the application to publish every write to an Amazon SQS queue for processing.
    Use DynamoDB Accelerator (DAX) to capture item-level changes and process them.

    - 48. 
    Use Amazon ElastiCache for Memcached in front of DynamoDB with lazy loading
    Enable DynamoDB auto scaling to handle the increased read capacity
    Use strongly consistent reads to reduce the read latency

    - 49. 
    Deploy the API with request validation directly to the production stage and monitor Amazon CloudWatch Logs for validation errors.
    Create a new AWS account, rebuild the entire API with request validation, and test it using AWS X-Ray traces before migrating.
    Export the API as an OpenAPI file, import it into a local API emulator on an EC2 instance, and test request validation there.

    - 50. 
    Configure an Amazon Cognito user pool authorizer that references the DynamoDB authentication table
    Use IAM authorization and add the client ID and user ID to an IAM policy for each caller
    Enable API keys on the method and store the client ID and user ID in a usage plan

    - 51. 
    Update the existing Lambda alias to point to the new function version. Keep using the existing API Gateway stage for beta testing.
    Publish the new code to the $LATEST version of the Lambda function. Point the production API Gateway stage at $LATEST for beta testing.
    Create a new Lambda function in a different Region. Update the production API Gateway stage to invoke it directly for beta testing.

    - 52. 
    Implement a $default route only and let API Gateway track connection status automatically.
    Configure an API Gateway usage plan to throttle players with unstable connections.
    Enable API Gateway caching on the WebSocket API to store each player's connection status.

    - 53. 
    CodeDeployDefault.ECSLinear10PercentEvery3Minutes
    CodeDeployDefault.ECSCanary10Percent5Minutes
    CodeDeployDefault.ECSAllAtOnce

    - 54. 
    “codecommit:Put*” and “codecommit:Update*”
    “codecommit:GitPush” and “codecommit:Update*”
    “codecommit:*”

    - 55. 
    ApplicationStop > BeforeInstall > AfterInstall > ApplicationStart > ValidateService
    BeforeAllowTraffic > AfterAllowTraffic
    BeforeInstall > AfterAllowTestTraffic > AfterInstall > AfterAllowTraffic > BeforeAllowTraffic

    - 56. 
    Run the aws lambda create-function command to upload the source code to an Amazon S3 bucket and produce a modified CloudFormation template
    Run the aws cloudformation validate-template command to upload the source code to an Amazon S3 bucket and produce a modified CloudFormation template
    Run the aws s3 cp command to upload the source code to an Amazon S3 bucket and produce a modified CloudFormation template

    - 57. 
    Create an IAM user for each employee and attach a policy that limits access to their own data.
    Use an Amazon Cognito identity pool with unauthenticated access enabled and a single shared IAM role for all employees.
    Use AWS STS GetSessionToken with the on-premises SAML credentials and attach a resource-based policy to each object.

    - 58. 
    REST API on Amazon API Gateway with separate resources for each data source
    Amazon Kinesis Data Streams consumed by the mobile clients
    Application Load Balancer with separate target groups for each data source

    - 59. 
    Use OutputPath in a Retry statement to include the original input with the error.
    Use InputPath in a Catch statement to include the original input with the error.
    Use ResultSelector in a Retry statement to include the original input with the error.

    - 60. 
    The IAM role policy changes take up to 24 hours to propagate to running instances
    The AWS credential provider looks for instance profile credentials first
    The AWS SDK for Java ignores IAM roles and only supports access keys

    - 61. 
    Replace GenerateDataKey calls with direct kms:Encrypt calls for each transaction payload.
    Enable automatic key rotation on the KMS key used by the application.
    Create a second KMS key in the same Region and alternate calls between the two keys.

    - 62. 
    Enable automatic key rotation on the AWS KMS key
    Increase the instance size of the EC2 instances in the cluster
    Enable S3 Transfer Acceleration on the bucket

    - 63. 
    kms:CreateKey
    kms:GenerateRandom
    kms:EnableKeyRotation

    - 64. 
    Implement Amazon GuardDuty and apply the Recon:IAMUser/UserPermissions finding type across all S3 buckets to automatically identify potential exposure of sensitive financial data.
    Implement Amazon Inspector and run a network reachability assessment across all S3 buckets to automatically identify potential exposure of sensitive financial data.
    Implement AWS Trusted Advisor and run the S3 bucket permissions check to automatically classify sensitive financial data within all S3 objects.

    - 65. 
    Use the ALTER TABLE ADD PARTITION command for every partition on each query.
    Use the DROP TABLE command and recreate the table before each query.
    Increase the Athena query timeout limit in the workgroup settings.
