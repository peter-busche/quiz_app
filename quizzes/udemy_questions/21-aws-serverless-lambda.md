# Section 21: AWS Serverless: Lambda ---> [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=527)
    ============================================================================================================================================================
- ### Questions:
    - 1. A developer is creating an AWS Serverless Application Model (AWS SAM) template. It includes several AWS Lambda functions, an Amazon S3 bucket, and an Amazon CloudFront distribution. One Lambda function, running on Lambda@Edge, is integrated with the CloudFront distribution, while the S3 bucket serves as an origin for the distribution.
    However, upon deploying the AWS SAM blueprint in the us-west-1 Region, the stack's creation fails.
    What could be the possible reason for this failure?

    - 2. 
    An engineer is constructing an AWS Lambda function and intends to log specific key events that transpire during the function's execution. To correlate the events with a particular function invocation, the engineer is looking to incorporate a unique identifier.
    The following code segment has been added to the Lambda function:
    function handler (event, context) {
    }

    - 3. 
    A Developer is creating an AWS Lambda function that will process data from an Amazon Kinesis data stream. The function is expected to be invoked 50 times per second and take 100 seconds to complete each request.
    What MUST the Developer do to ensure the functions runs without errors?

    - 4. 
    A Developer is designing a cloud native application. The application will use several AWS Lambda functions that will process items that the functions read from an event source. Which AWS services are supported for Lambda event source mappings? (Select THREE.)

    - 5. 
    A company is deploying a new serverless application with an AWS Lambda function. A developer ran some test invocations using the AWS CLI. The function is invoking correctly and returning a success message, but not log data is being generated in Amazon CloudWatch Logs. The developer waited for 15 minutes but the log data is not showing up.
    What is the most likely explanation for this issue?

    - 6. 
    A company is creating a serverless application that uses AWS Lambda functions. The developer has written the code to initialize the AWS SDK outside of the Lambda handler function.
    What is PRIMARY benefit of this action?

    - 7. 
    An application uses Amazon API Gateway, an AWS Lambda function and a DynamoDB table. The developer requires that another Lambda function is triggered when an item lifecycle activity occurs in the DynamoDB table.
    How can this be achieved?

    - 8. 
    A company is planning to use AWS CodeDeploy to deploy a new AWS Lambda function
    What are the MINIMUM properties required in the 'resources' section of the AppSpec file for CodeDeploy to deploy the function successfully?

    - 9. 
    A Developer must deploy a new AWS Lambda function using an AWS CloudFormation template.
    Which procedures will deploy a Lambda function? (Select TWO.)

    - 10. 
    An AWS Lambda function requires several environment variables with secret values. The secret values should be obscured in the Lambda console and API output even for users who have permission to use the key.
    What is the best way to achieve this outcome and MINIMIZE complexity and latency?

    - 11. 
    A Developer needs to write some code to invoke an AWS Lambda function using the AWS Command Line Interface (CLI). Which option must be specified to cause the function to be invoked asynchronously? 

    - 12. 
    A company is running an application built on AWS Lambda functions. One Lambda function has performance issues when it has to download a 50 MB file from the internet every execution. This function is called multiple times a second.
    What solution would give the BEST performance increase?

    - 13. 
    An application uses AWS Lambda to process many files. The Lambda function takes approximately 3 minutes to process each file and does not return any important data. A Developer has written a script that will invoke the function using the AWS CLI.
    What is the FASTEST way to process all the files?

    - 14. 
    A serverless application is used to process customer information and outputs a JSON file to an Amazon S3 bucket. AWS Lambda is used for processing the data. The data is sensitive and should be encrypted.
    How can a Developer modify the Lambda function to ensure the data is encrypted before it is uploaded to the S3 bucket?

    - 15. 
    A Developer has updated an AWS Lambda function and published a new version. To ensure the code is working as expected the Developer needs to initially direct a percentage of traffic to the new version and gradually increase this over time. It is important to be able to rollback if there are any issues reported.
    What is the BEST way the Developer can implement the migration to the new version SAFELY?

    - 16. 
    A Developer has written some code that will connect and pull information from several hundred websites. The code needs to run on a daily schedule and execution time will be less than 60 seconds.
    Which AWS service will be most suitable and cost-effective?

    - 17. 
    A developer is in the process of revising multiple AWS Lambda functions and notes that these functions utilize the same bespoke libraries. The developer intends to centralize these libraries, implement updates with minimal effort, and keep the libraries version controlled.
    Which solution aligns with these needs while requiring the least development effort?

    - 18. 
    Based on the following AWS CLI command the resulting output, what has happened here?
        $ aws lambda invoke --function-name MyFunction --invocation-type Event --payload ewogICJrZXkxIjogInZhbHVlMSIsCiAgImtleTIiOiAidmFsdWUyIiwKICAia2V5MyI6ICJ2YWx1ZTMiCn0= response.json
        {
        "StatusCode": 202
        }

    - 19. 
    A Developer has setup an Amazon Kinesis Data Stream with 6 shards to ingest a maximum of 2000 records per second. An AWS Lambda function has been configured to process these records. In which order will these records be processed?

    - 20. 
    A Developer has created an AWS Lambda function in a new AWS account. The function is expected to be invoked 40 times per second and the execution duration will be around 100 seconds. What MUST the Developer do to ensure there are no errors?

    - 21. 
    Based on the following AWS CLI command the resulting output, what has happened here?
        $ aws lambda invoke --function-name MyFunction --payload ewogICJrZXkxIjogInZhbHVlMSIsCiAgImtleTIiOiAidmFsdWUyIiwKICAia2V5MyI6ICJ2YWx1ZTMiCn0= response.json
        {
        "StatusCode": 200
        }

    - 22. 
    A Development team are deploying an AWS Lambda function that will be used by a production application. The function code will be updated regularly, and new versions will be published. The development team do not want to modify application code to point to each new version.
    How can the Development team setup a static ARN that will point to the latest published version?

    - 23. 
    A Developer created an AWS Lambda function for a serverless application. The Lambda function has been executing for several minutes and the Developer cannot find any log data in CloudWatch Logs.
    What is the MOST likely explanation for this issue?

    - 24. 
    A Developer has created a serverless function that processes log files. The function should be invoked once every 15 minutes. How can the Developer automatically invoke the function using serverless services?

    - 25. 
    - 26. 
    - 27. 
    - 28. 
    - 29. 
    - 30. 
    - 31. 
    - 32. 
    - 33. 
    - 34. 
    - 35. 
    - 36. 
    - 37. 
    - 38. 
    - 39. 
    - 40. 
    - 41. 
    - 42. 
    - 43. 
    - 44. 
    - 45. 
    - 46. 
    - 47. 
    - 48. 
    - 49. 
    - 50. 

    ### Answers:
    - 1. 
    Lambda@Edge functions can only be deployed in the us-east-1 Region.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=567)

    - 2. 
    Use context.awsRequestId within the function to fetch the unique identifier associated with each invocation.
    https://docs.aws.amazon.com/lambda/latest/dg/nodejs-context.html

    - 3. 
    Contact AWS and request to increase the limit for concurrent executions. This calculation is 50 x 100 = 5,000. 3000 – US West (Oregon), US East (N. Virginia), Europe (Ireland).
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=580)

    - 4. 
    Amazon DynamoDB
    Amazon Simple Queue Service (SQS)
    Amazon Kinesis
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=549)         *Event Source Mapping vs Event Notifications

    - 5. 
    The function execution role does not have permission to write log data to CloudWatch Logs.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=562)

    - 6. 
    Takes advantage of execution environment reuse.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=575)

    - 7. 
    Enable a DynamoDB stream and trigger the Lambda function synchronously from the stream
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=549)

    - 8. 
    name, alias, currentversion, and targetversion
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=595)
    
    - 9. 
    Create an AWS::Lambda::Function resource in the template, then write the code directly inside the CloudFormation template
    Upload a ZIP file containing the function code to Amazon S3, then add a reference to it in an AWS::Lambda::Function resource in the template
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=587)

    - 10. 
    Encrypt the secret values client-side using encryption helpers
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=561)

    - 11. 
    Set the –invocation-type option to Event
    https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html

    - 12. 
    Cache the file in the /tmp directory
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=576)

    - 13. 
    Invoke the Lambda function asynchronously with the invocation type Event and process the files in parallel
    https://aws.amazon.com/blogs/architecture/understanding-the-different-ways-to-invoke-lambda-functions/

    - 14. 
    Use the GenerateDataKey API, then use the data key to encrypt the file using the Lambda code
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=561)

    - 15. 
    Create an Alias, assign the current and new versions and use traffic shifting to assign a percentage of traffic to the new version
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=593)

    - 16. 
    AWS Lambda
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=568)

    - 17. 
    Create a Lambda layer including all the custom libraries.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=577)

    - 18. 
    An AWS Lambda function has been invoked asynchronously and has completed successfully. 202-ASYNC.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=544)

    - 19. 
    Lambda will receive each record in the exact order it was placed into the shard. There is no guarantee of order across shards.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=550)

    - 20. 
    Contact AWS Support to increase the concurrent execution limits. 40*100sec=4000 > 1000 limit
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=580)

    - 21. 
    An AWS Lambda function has been invoked synchronously and has completed successfully. 200-SYNC.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=537)

    - 22. 
    Setup an Alias that will point to the latest version.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=593)

    - 23. 
    The execution role for the Lambda function is missing permissions to write log data to the CloudWatch Logs
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=559)

    - 24. 
    Create an Amazon CloudWatch Events rule that is scheduled to run and invoke the function
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=546)

    - 25. 
    - 26. 
    - 27. 
    - 28. 
    - 29. 
    - 30. 
    - 31. 
    - 32. 
    - 33. 
    - 34. 
    - 35. 
    - 36. 
    - 37. 
    - 38. 
    - 39. 
    - 40. 
    - 41. 
    - 42. 
    - 43. 
    - 44. 
    - 45. 
    - 46. 
    - 47. 
    - 48. 
    - 49. 
    - 50.


    ### Wrong Answers:
    - 1. 
    Lambda@Edge functions cannot be defined in AWS SAM templates and must be created in the Lambda console.
    CloudFront distributions cannot use an S3 bucket located in the us-west-1 Region as an origin.
    AWS SAM templates cannot deploy more than one Lambda function within a single stack.

    - 2. 
    Use context.functionVersion within the function to fetch the unique identifier associated with each invocation.
    Use context.logStreamName within the function to fetch the unique identifier associated with each invocation.
    Use context.invokedFunctionArn within the function to fetch the unique identifier associated with each invocation.

    - 3. 
    Configure reserved concurrency of 5,000 on the function without changing the account limit for concurrent executions.
    Increase the number of shards in the Kinesis data stream to 50 so each shard invokes one function per second.
    Configure an Amazon SQS dead-letter queue on the function to capture invocations that exceed the concurrency limit.

    - 4. 
    Amazon Simple Notification Service (SNS)
    Amazon Simple Storage Service (S3)
    Amazon API Gateway

    - 5. 
    CloudWatch Logs only receives Lambda log data when the function is invoked from the Lambda console.
    The function has not been configured with an Amazon CloudWatch Logs subscription filter.
    The function execution role does not have permission to write trace data to AWS X-Ray.

    - 6. 
    Reduces the size of the deployment package uploaded to Lambda.
    Increases the maximum timeout available to the function.
    Removes the need for IAM credentials within the execution environment.

    - 7. 
    Enable DynamoDB Accelerator (DAX) and trigger the Lambda function from the DAX cluster
    Configure a DynamoDB global table and trigger the Lambda function asynchronously from the replica table
    Enable Time to Live on the DynamoDB table and configure it to invoke the Lambda function when items change

    - 8. 
    name, alias, and targetversion
    name, runtime, handler, and codeuri
    name, alias, currentversion, and hooks

    - 9. 
    Upload the function code to an AWS CodeCommit repository, then add a reference to it in an AWS::Lambda::Function resource in the template
    Upload a ZIP file containing the function code to an Amazon EFS file system, then add a reference to it in an AWS::Lambda::Function resource in the template
    Create an AWS::Lambda::EventSourceMapping resource in the template, then write the code directly inside the CloudFormation template

    - 10. 
    Store the secret values as plaintext environment variables and rely on default encryption at rest
    Encrypt the secret values with the default AWS managed key for Lambda (aws/lambda)
    Store the secret values as tags on the Lambda function and restrict access to the tags

    - 11. 
    Set the –invocation-type option to RequestResponse
    Set the –invocation-type option to DryRun
    Set the –log-type option to Tail

    - 12. 
    Store the file in an Amazon EBS volume attached to the function
    Store the file contents in a Lambda environment variable
    Write the file to the /opt directory at runtime

    - 13. 
    Invoke the Lambda function synchronously with the invocation type RequestResponse and process the files sequentially
    Invoke the Lambda function with the invocation type DryRun and process the files in parallel
    Configure provisioned concurrency and invoke the function with the invocation type RequestResponse one file at a time

    - 14. 
    Enable SSE-S3 default encryption on the S3 bucket so the file is encrypted after it is uploaded
    Add an S3 bucket policy that denies PutObject requests without the x-amz-server-side-encryption header
    Use the Decrypt API to generate a plaintext key, then use that key to encrypt the file using the Lambda code

    - 15. 
    Update the $LATEST version with the new code and use weighted Amazon Route 53 records to shift a percentage of traffic
    Create a Lambda layer containing the new code and attach it to a percentage of the function invocations
    Point the application directly at the new version ARN and use reserved concurrency to limit its share of traffic

    - 16. 
    Amazon EC2
    AWS Elastic Beanstalk
    Amazon EMR

    - 17. 
    Package the custom libraries in each function's deployment package and update them individually.
    Create a Lambda alias that includes the custom libraries for all the functions.
    Store the custom libraries in Lambda environment variables shared across the functions.

    - 18. 
    An AWS Lambda function has been invoked synchronously and has completed successfully.
    An AWS Lambda function has been invoked with a dry run and the parameters were validated.
    An AWS Lambda function has been invoked synchronously and returned a throttling error.

    - 19. 
    Lambda will receive each record in the exact order it was placed into the stream, across all shards.
    Lambda will receive records in random order within each shard, but in exact order across shards.
    Lambda will receive records in last-in, first-out (LIFO) order within each shard.

    - 20. 
    Configure reserved concurrency of 4,000 on the function without changing the account limit.
    Configure an Amazon SQS dead-letter queue to capture the throttled invocations.
    Publish a new version and configure an alias to spread the invocations across versions.

    - 21. 
    An AWS Lambda function has been invoked asynchronously and has completed successfully.
    An AWS Lambda function has been invoked with a dry run and the parameters were validated.
    An AWS Lambda function has been invoked synchronously and the event was queued for later processing.

    - 22. 
    Setup a Lambda layer that will point to the latest version.
    Setup an environment variable that will point to the latest version.
    Setup a resource-based policy that will point to the latest version.

    - 23. 
    The resource-based policy for the Lambda function is missing permissions for CloudWatch Logs to invoke it
    The Lambda function has not been configured with AWS X-Ray active tracing enabled
    CloudWatch Logs only receives log data after the Lambda function execution has fully completed

    - 24. 
    Create an Amazon SQS queue with a 15-minute delivery delay that invokes the function
    Configure an Amazon S3 lifecycle rule that runs every 15 minutes and invokes the function
    Set the function timeout to 15 minutes so that the function re-invokes itself automatically

