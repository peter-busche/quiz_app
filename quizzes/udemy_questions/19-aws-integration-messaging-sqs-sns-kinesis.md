# Section 19: AWS Integration & Messaging: SQS, SNS & Kinesis ---> [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=427)
    ============================================================================================================================================================
- ### Questions:
    - 1. 
    Messages produced by an application must be pushed to multiple Amazon SQS queues. What is the BEST solution for this requirement?

    - 2. 
    A company needs to ingest several terabytes of data every hour from a large number of distributed sources. The messages are delivered continually 24 hrs a day. Messages must be delivered in real time for security analysis and live operational dashboards.\
    Which approach will meet these requirements?

    - 3. 
    A company runs a decoupled application that uses an Amazon SQS queue. The messages are processed by an AWS Lambda function. The function is not keeping up with the number of messages in the queue. A developer noticed that though the application can process multiple messages per invocation, it is only processing one at a time.
    How can the developer configure the application to process messages more efficiently?

    - 4. 
    A company uses Amazon SQS to decouple an online application that generates memes. The SQS consumers poll the queue regularly to keep throughput high and this is proving to be costly and resource intensive. A Developer has been asked to review the system and propose changes that can reduce costs and the number of empty responses.
    What would be the BEST approach to MINIMIZING cost?

    - 5. 
    A company uses an Amazon Simple Queue Service (SQS) Standard queue for an application. An issue has been identified where applications are picking up messages from the queue that are still being processed causing duplication. What can a Developer do to resolve this issue?

    - 6. 
    A Developer manages a monitoring service for a fleet of IoT sensors in a major city. The monitoring application uses an Amazon Kinesis Data Stream with a group of EC2 instances processing the data. Amazon CloudWatch custom metrics show that the instances a reaching maximum processing capacity and there are insufficient shards in the Data Stream to handle the rate of data flow.
    What course of action should the Developer take to resolve the performance issues?

    - 7. 
    A three tier web application has been deployed on Amazon EC2 instances using Amazon EC2 Auto Scaling. The EC2 instances in the web tier sometimes receive bursts of traffic and the application tier cannot scale fast enough to keep up with messages sometimes resulting in message loss.
    How can a Developer decouple the application to prevent loss of messages?

    - 8. 
    A web application is using Amazon Kinesis Data Streams for ingesting IoT data that is then stored before processing for up to 24 hours.
    How can the Developer implement encryption at rest for data stored in Amazon Kinesis Data Streams?

    - 9. 
    A company is in the process of migrating an application from a monolithic architecture to a microservices-based architecture. The developers need to refactor the application so that the many microservices can asynchronously communicate with each other in a decoupled manner.
    Which AWS services can be used for asynchronous message passing? (Select TWO.)

    - 10. 
    A company is running an order processing system on AWS. Amazon SQS is used to queue orders and an AWS Lambda function processes them. The company recently started noticing a lot of orders are failing to process.
    How can a Developer MOST effectively manage these failures to debug the failed orders later and reprocess them, as necessary?

    - 11. 
    A gaming application displays the results of games in a leaderboard. The leaderboard is updated by 4 KB messages that are retrieved from an Amazon SQS queue. The updates are received infrequently but the Developer needs to minimize the time between the messages arriving in the queue and the leaderboard being updated.
    Which technique provides the shortest delay in updating the leaderboard?

    - 12. 
    A Developer is writing an AWS Lambda function that processes records from an Amazon Kinesis Data Stream. The Developer must write the function so that it sends a notice to Administrators if it fails to process a batch of records.
    How should the Developer write the function?

    - 13. 
    An application uses Amazon Kinesis Data Streams to ingest and process large streams of data records in real time. Amazon EC2 instances consume and process the data using the Amazon Kinesis Client Library (KCL). The application handles the failure scenarios and does not require standby workers. The application reports that a specific shard is receiving more data than expected. To adapt to the changes in the rate of data flow, the “hot” shard is resharded.
    Assuming that the initial number of shards in the Kinesis data stream is 6, and after resharding the number of shards increased to 8, what is the maximum number of EC2 instances that can be deployed to process data from all the shards?

    - 14. 
    A monitoring application that keeps track of a large eCommerce website uses Amazon Kinesis for data ingestion. During periods of peak data rates, the Kinesis stream cannot keep up with the incoming data.
    What step will allow Kinesis data streams to accommodate the traffic during peak hours?

    - 15. 
    A Developer is managing an application that includes an Amazon SQS queue. The consumers that process the data from the queue are connecting in short cycles and the queue often does not return messages. The cost for API calls is increasing. How can the Developer optimize the retrieval of messages and reduce cost?

    - 16. 
    An Amazon Kinesis Data Stream has recently been configured to receive data from sensors in a manufacturing facility. A consumer EC2 instance is configured to process the data every 48 hours and save processing results to an Amazon RedShift data warehouse. Testing has identified a large amount of data is missing. A review of monitoring logs has identified that the sensors are sending data correctly and the EC2 instance is healthy.
    What is the MOST likely explanation for this issue?

    - 17. 
    A Developer needs to run some code using Lambda in response to an event and forward the execution result to another application using a pub/sub notification.
    How can the Developer accomplish this?

    - 18. 
    What does an Amazon SQS delay queue accomplish?

    - 19. 
    To reduce the cost of API actions performed on an Amazon SQS queue, a Developer has decided to implement long polling. Which of the following modifications should the Developer make to the API actions?

    - 20. 
    An application asynchronously invokes an AWS Lambda function. The application has recently been experiencing occasional errors that result in failed invocations. A developer wants to store the messages that resulted in failed invocations such that the application can automatically retry processing them.
    What should the developer do to accomplish this goal with the LEAST operational overhead?

    - 21. 
    An application needs to generate SMS text messages and emails for a large number of subscribers. Which AWS service can be used to send these messages to customers?

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
    Publish the messages to an Amazon SNS topic and subscribe each SQS queue to the topic
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=451)

    - 2. 
    Use Amazon Kinesis Data Streams with Kinesis Client Library to ingest and deliver messages
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=461)

    - 3. 
    Call the ReceiveMessage API to set MaxNumberOfMessages to a value greater than the default of 1.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=446)

    - 4. 
    Set the Imaging queue ReceiveMessageWaitTimeSeconds attribute to 20 seconds
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=444)

    - 5. 
    Increase the VisibilityTimeout API action on the queue
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=440)

    - 6. 
    Increase the EC2 instance size and add shards to the stream
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=463)

    - 7. 
    Add an Amazon SQS queue between the web tier and the application tier
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=431)

    - 8. 
    Enable server-side encryption on Kinesis Data Streams with an AWS KMS CMK
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=462)

    - 9. 
    Amazon SNS
    Amazon SQS
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=455)

    - 10. 
    Implement dead-letter queues for failed orders from the order queue
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=441)

    - 11. 
    Retrieve the messages from the queue using long polling every 15 seconds
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=444)

    - 12. 
    Configure an Amazon SNS topic as an on-failure destination
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=551)

    - 13. 
    8
    https://docs.aws.amazon.com/streams/latest/dev/kinesis-record-processor-scaling.html

    - 14. 
    Increase the shard count of the stream using UpdateShardCount
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=463)

    - 15. 
    Call the ReceiveMessage API with the WaitTimeSeconds parameter set to 20
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=444)

    - 16. 
    Records are retained for 24 hours in the Kinesis Data Stream by default
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=462)

    - 17. 
    Configure a Lambda “on success” destination and route the execution results to Amazon SNS
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=468)

    - 18. 
    Messages are hidden for a configurable amount of time when they are first added to the queue
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=443)

    - 19. 
    Set the ReceiveMessage API with a WaitTimeSeconds of 20
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=444)

    - 20. 
    Configure a redrive policy on an Amazon SQS queue. Set the dead-letter queue as an event source to the Lambda function.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=)

    - 21. 
    Amazon SNS
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=)

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
    Publish the messages to an Amazon Kinesis Data Stream and subscribe each SQS queue to the stream
    Configure a redrive policy on a primary SQS queue that copies each message to the other queues
    Send the messages to an SQS FIFO queue and enable message fan-out to each SQS queue

    - 2. 
    Use Amazon SQS FIFO queues with long polling to ingest and deliver messages
    Use AWS Data Pipeline with hourly batch jobs to ingest and deliver messages
    Use Amazon Kinesis Data Firehose with Amazon S3 and Amazon Athena to ingest and deliver messages

    - 3. 
    Call the ChangeMessageVisibility API to set VisibilityTimeout to a value greater than the default of 30.
    Call the SetQueueAttributes API to set DelaySeconds to a value greater than the default of 0.
    Call the SendMessageBatch API to set MaxNumberOfMessages to a value greater than the default of 1.

    - 4. 
    Set the Imaging queue DelaySeconds attribute to 20 seconds
    Set the Imaging queue VisibilityTimeout attribute to 20 seconds
    Set the Imaging queue ReceiveMessageWaitTimeSeconds attribute to 0 seconds

    - 5. 
    Increase the DelaySeconds API action on the queue
    Decrease the VisibilityTimeout API action on the queue
    Increase the ReceiveMessageWaitTimeSeconds API action on the queue

    - 6. 
    Decrease the EC2 instance size and merge shards in the stream
    Increase the EC2 instance size and merge shards in the stream
    Add more EC2 instances and increase the stream retention period

    - 7. 
    Add an Amazon SNS topic between the web tier and the application tier
    Add an Application Load Balancer between the web tier and the application tier
    Add an Amazon CloudFront distribution between the web tier and the application tier

    - 8. 
    Enable SSE-S3 encryption on Kinesis Data Streams with Amazon S3 managed keys
    Configure TLS on the Kinesis Data Streams endpoint with an AWS ACM certificate
    Attach an encrypted Amazon EBS volume to the Kinesis Data Streams shards

    - 9. 
    Amazon API Gateway
    Amazon ECS
    Amazon RDS

    - 10. 
    Implement delay queues for failed orders from the order queue
    Increase the visibility timeout for failed orders on the order queue
    Enable long polling for failed orders on the order queue

    - 11. 
    Retrieve the messages from the queue using short polling every 15 seconds
    Retrieve the messages from a delay queue using short polling every 10 seconds
    Retrieve the messages from the queue using short polling every 60 seconds

    - 12. 
    Configure an Amazon SNS topic as an on-success destination
    Configure Amazon SES as an on-failure destination
    Configure a CloudWatch Logs log group as an on-failure destination

    - 13. 
    6
    12
    16

    - 14. 
    Increase the retention period of the stream using IncreaseStreamRetentionPeriod
    Merge the shards of the stream using MergeShards
    Enable enhanced fan-out on the stream using RegisterStreamConsumer

    - 15. 
    Call the ReceiveMessage API with the WaitTimeSeconds parameter set to 0
    Call the ReceiveMessage API with the VisibilityTimeout parameter set to 20
    Call the SetQueueAttributes API with the DelaySeconds parameter set to 20

    - 16. 
    Records are deleted from the Kinesis Data Stream as soon as the first consumer reads them
    Amazon Redshift rejects Kinesis records that are older than 24 hours by default
    Server-side encryption on the Kinesis Data Stream prevents the EC2 instance reading records

    - 17. 
    Configure a Lambda “on failure” destination and route the execution results to Amazon SNS
    Configure a Lambda dead-letter queue and route the execution results to Amazon SNS
    Configure a Lambda “on success” destination and route the execution results to Amazon SQS

    - 18. 
    Messages are hidden for a configurable amount of time after they are received by a consumer
    Messages are moved to a separate queue after a configurable number of failed receive attempts
    Consumers wait for a configurable amount of time for messages to arrive before returning a response

    - 19. 
    Set the ReceiveMessage API with a WaitTimeSeconds of 0
    Set the ReceiveMessage API with a VisibilityTimeout of 20
    Set the SendMessage API with a DelaySeconds of 20

    - 20. 
    Configure an Amazon SNS topic as an on-failure destination. Subscribe an email address to the topic to review the failed events.
    Configure the function to write failed events to CloudWatch Logs. Create a metric filter that re-invokes the Lambda function.
    Configure reserved concurrency on the Lambda function. Increase the maximum retry attempts for asynchronous invocation to 10.

    - 21. 
    Amazon SQS
    Amazon MQ
    Amazon Kinesis Data Streams
