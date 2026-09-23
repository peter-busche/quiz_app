# Section 20: AWS Monitoring & Audit: CloudWatch, X-Ray and CloudTrail ---> [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=469)
    ============================================================================================================================================================
- ### Questions:
    - 1. 
    A Development team has deployed several applications running on an Auto Scaling fleet of Amazon EC2 instances. The Operations team have asked for a display that shows a key performance metric for each application on a single screen for monitoring purposes.
    What steps should a Developer take to deliver this capability using Amazon CloudWatch?

    - 2. 
    An application is instrumented to generate traces using AWS X-Ray and generates a large amount of trace data. A Developer would like to use filter expressions to filter the results to specific key-value pairs added to custom subsegments.
    How should the Developer add the key-value pairs to the custom subsegments?

    - 3. 
    An application uses both Amazon EC2 instances and on-premises servers. The on-premises servers are a critical component of the application, and a developer wants to collect metrics and logs from these servers. The developer would like to use Amazon CloudWatch.
    How can the developer accomplish this?

    - 4. 
    A Developer wants to debug an application by searching and filtering log data. The application logs are stored in Amazon CloudWatch Logs. The Developer creates a new metric filter to count exceptions in the application logs. However, no results are returned from the logs.
    What is the reason that no filtered results are being returned?

    - 5. 
    An application has been instrumented to use the AWS X-Ray SDK to collect data about the requests the application serves. The Developer has set the user field on segments to a string that identifies the user who sent the request.
    How can the Developer search for segments associated with specific users?
    

    - 6. 
    A company is migrating several applications to the AWS cloud. The security team has strict security requirements and mandate that a log of all API calls to AWS resources must be maintained.

    Which AWS service should be used to record this information for the security team?

    - 7. 
    A serverless application uses Amazon API Gateway an AWS Lambda function and a Lambda authorizer function. There is a failure with the application and a developer needs to trace and analyze user requests that pass through API Gateway through to the back end services.
    Which AWS service is MOST suitable for this purpose?

    - 8. 
    An AWS developer is building an application that processes sensitive personally identifiable information (PII). The application operates on AWS Lambda and writes diagnostic data to Amazon CloudWatch Logs. However, the developer wants to ensure that PII is not accidentally stored in CloudWatch Logs.
    What strategy should the developer adopt to ensure this?

    - 9. 
    A development team have deployed a new application and users have reported some performance issues. The developers need to enable monitoring for specific metrics with a data granularity of one second. How can this be achieved?

    - 10. 
    A security officer has requested that a Developer enable logging for API actions for all AWS regions to a single Amazon S3 bucket.
    What is the EASIEST way for the Developer to achieve this requirement?

    - 11. 
    A developer is debugging an application by sifting through log data stored in Amazon CloudWatch Logs. A fresh metric filter has been established to identify exceptions in these logs. Yet, the logs are not returning any results filtered through the new metric.
    What could be the reason behind the absence of filtered results?

    - 12. 
    A media organization utilizes an Amazon API Gateway REST API endpoint to disseminate updates from an internal Content Management System (CMS) to Amazon EventBridge. An EventBridge rule is set up to monitor these updates and control content syndication in a primary AWS account. The organization now wants to extend the reach of these updates across several affiliate AWS accounts.
    How can the developer accomplish this without altering the configuration of the CMS?

    - 13. 
    A company is running a Docker application on Amazon ECS. The application must scale based on user load in the last 15 seconds.
    How should the Developer instrument the code so that the requirement can be met?

    - 14. 
    An application runs on Amazon EC2 and generates log files. A Developer needs to centralize the log files so they can be queried and retained. What is the EASIEST way for the Developer to centralize the log files?

    - 15. 
    Every time an Amazon EC2 instance is launched, certain metadata about the instance should be recorded in an Amazon DynamoDB table. The data is gathered and written to the table by an AWS Lambda function.
    What is the MOST efficient method of invoking the Lambda function?

    - 16. 
    An application is being instrumented to send trace data using AWS X-Ray. A Developer needs to upload segment documents using JSON-formatted strings to X-Ray using the API. Which API action should the developer use?

    - 17. 
    An application serves customers in several different geographical regions. Information about the location users connect from is written to logs stored in Amazon CloudWatch Logs. The company needs to publish an Amazon CloudWatch custom metric that tracks connections for each location.
    Which approach will meet these requirements?

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
    Create a custom namespace with a unique metric name for each application.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=472)

    - 2. 
    Add annotations to the custom subsegments
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=509)

    - 3. 
    Install the CloudWatch agent on the on-premises servers and specify IAM credentials with permissions to CloudWatch.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=484)

    - 4. 
    CloudWatch Logs only publishes metric data for events that happen after the filter is created
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=486)

    - 5. 
    By using the GetTraceSummaries API with a filter expression
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=513)

    - 6. 
    AWS CloudTrail
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=519)

    - 7. 
    AWS X-Ray
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=504)

    - 8. 
    Configure Amazon CloudWatch Logs data protection to detect and mask PII in log events (using managed data identifiers) before the data is stored.
    https://digitalcloud.training/amazon-cloudwatch/

    - 9. 
    Create custom metrics and configure them as high resolution
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=474)

    - 10. 
    Create an AWS CloudTrail trail and apply it to all regions, configure logging to a single S3 bucket
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=519)

    - 11. 
    CloudWatch Logs only publish metric data for events that occur after the filter has been established.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=486)

    - 12. 
    Implement an EventBridge event bus in the affiliate AWS accounts to create a rule that matches events and forwards them from the main account.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=496)

    - 13. 
    Create a high-resolution custom Amazon CloudWatch metric for user activity data, then publish data every 5 seconds
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=474)

    - 14. 
    Install the Amazon CloudWatch Logs agent and collect the logs from the instances
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=484)

    - 15. 
    Create a CloudWatch Event with an event pattern looking for EC2 state changes and a target set to use the Lambda function
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=488)

    - 16. 
    The PutTraceSegments API action
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=512)

    - 17. 
    Create a CloudWatch metric filter to extract metrics from the log files with location as a dimension.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=)

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
    Create a CloudWatch Logs metric filter with a unique log group for each application.
    Create a CloudWatch alarm for each application and publish them to an SNS topic.
    Enable detailed monitoring on the Auto Scaling group for each application.

    - 2. 
    Add metadata to the custom subsegments
    Add sampling rules to the custom subsegments
    Add dimensions to the custom subsegments

    - 3. 
    Install the AWS X-Ray daemon on the on-premises servers and specify IAM credentials with permissions to CloudWatch.
    Enable CloudWatch detailed monitoring for the on-premises servers from the Amazon CloudWatch console.
    Configure VPC Flow Logs to collect metrics and logs from the on-premises servers over AWS Direct Connect.

    - 4. 
    CloudWatch Logs only publishes metric data for events that match an existing CloudWatch alarm
    CloudWatch Logs only publishes metric data for log groups encrypted with an AWS KMS key
    Metric filters only return results after a log group retention period has been configured

    - 5. 
    By using the BatchGetTraces API with a filter expression
    By using the GetServiceGraph API with a filter expression
    By using the PutTraceSegments API with a filter expression

    - 6. 
    Amazon CloudWatch
    AWS Config
    Amazon Inspector

    - 7. 
    AWS CloudTrail
    AWS Config
    Amazon Inspector

    - 8. 
    Configure a CloudWatch Logs metric filter to detect PII in log events and delete the matching events after the data is stored.
    Enable AWS KMS encryption on the CloudWatch Logs log group so that PII in log events is masked before the data is stored.
    Configure Amazon Macie to scan the CloudWatch Logs log group directly and mask PII in log events before the data is stored.

    - 9. 
    Enable detailed monitoring on the EC2 instances
    Create custom metrics and configure them as standard resolution
    Use CloudWatch Logs Insights with a one-second query interval

    - 10. 
    Create an AWS CloudTrail trail in each region, configure logging to a separate S3 bucket per region
    Enable AWS Config in all regions and configure the delivery channel to a single S3 bucket
    Enable VPC Flow Logs in all regions and configure logging to a single S3 bucket

    - 11. 
    CloudWatch Logs only publish metric data after the log group has been exported to Amazon S3.
    Metric filters only evaluate log events that are sent by the CloudWatch unified agent.
    The metric filter must be associated with a CloudWatch alarm before results are published.

    - 12. 
    Configure the CMS to publish the updates directly to the default event bus in each affiliate AWS account.
    Create an EventBridge archive in the main account and replay the archived events into each affiliate AWS account.
    Create an additional API Gateway REST API in each affiliate account and point the CMS to these new endpoints.

    - 13. 
    Create a standard-resolution custom Amazon CloudWatch metric for user activity data, then publish data every 5 seconds
    Create a high-resolution custom Amazon CloudWatch metric for user activity data, then publish data every 60 seconds
    Enable detailed monitoring on the Amazon ECS cluster for user activity data, then publish data every 5 seconds

    - 14. 
    Install the AWS X-Ray daemon and collect the logs from the instances
    Enable EC2 detailed monitoring and collect the logs from the instances
    Create an AWS CloudTrail trail and collect the logs from the instances

    - 15. 
    Configure the EC2 service as an event source mapping for the Lambda function with a batch size of 1
    Create a scheduled CloudWatch Event that invokes the Lambda function every minute to poll the DescribeInstances API
    Subscribe the Lambda function to the default Amazon SNS topic that EC2 publishes to for instance launches

    - 16. 
    The PutTelemetryRecords API action
    The BatchGetTraces API action
    The GetTraceSummaries API action

    - 17. 
    Create a CloudWatch Logs subscription filter to stream the log files to Kinesis with location as a partition key.
    Create a CloudWatch alarm on the log group to count connections with location as a dimension.
    Create a CloudWatch Logs Insights query to aggregate the log files with location as a dimension.
