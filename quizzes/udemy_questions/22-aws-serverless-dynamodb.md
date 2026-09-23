# Section 22: AWS Serverless: DynamoDB ---> [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=602)
    ============================================================================================================================================================
- ### Questions:
    - 1. A Developer is creating a DynamoDB table for storing application logs. The table has 5 write capacity units (WCUs). The Developer needs to configure the read capacity units (RCUs) for the table. Which of the following configurations represents the most efficient use of throughput?

    - 2. An engineer is constructing a web-based application that uses Amazon DynamoDB for storing data. The data is distributed across two tables: 'authors' and 'books'. The 'authors' table uses 'authorName' as its partition key, while the 'books' table has 'bookTitle' as the partition key and 'authorName' as the sort key.
    The application requires the ability to fetch multiple books and authors simultaneously in a single database operation for effective performance. The engineer is seeking a solution that maximizes application efficiency and reduces network traffic.
    What strategy should the engineer employ to achieve these requirements?

    - 3. 
    A development team manage a high-traffic e-Commerce site with dynamic pricing that is updated in real-time. There have been incidents where multiple updates occur simultaneously and cause an original editor’s updates to be overwritten. How can the developers ensure that overwriting does not occur?

    - 4. 
    A company runs an application on a fleet of web servers running on Amazon EC2 instances. The web servers are behind an Elastic Load Balancer (ELB) and use an Amazon DynamoDB table for storing session state. A Developer has been asked to implement a mechanism for automatically deleting session state data that is older than 24 hours.
    What is the SIMPLEST solution to this requirement?

    - 5. 
    A Developer is designing a fault-tolerant environment where client sessions will be saved. How can the Developer ensure that no sessions are lost if an Amazon EC2 instance fails?

    - 6. 
    A Developer has added a Global Secondary Index (GSI) to an existing Amazon DynamoDB table. The GSI is used mainly for read operations whereas the primary table is extremely write-intensive. Recently, the Developer has noticed throttling occurring under heavy write activity on the primary table. However, the write capacity units on the primary table are not fully utilized.
    What is the best explanation for why the writes are being throttled on the primary table?

    - 7. 
    An application is using Amazon DynamoDB as its data store and needs to be able to read 100 items per second as strongly consistent reads. Each item is 5 KB in size.
    What value should be set for the table's provisioned throughput for reads?

    - 8. 
    A gaming company is building an application to track the scores for their games using an Amazon DynamoDB table. Each item in the table is identified by a partition key (user_id) and a sort key (game_name). The table also includes the attribute “TopScore”. 
    A Developer has been asked to write a leaderboard application to display the highest achieved scores for each game (game_name), based on the score identified in the “TopScore” attribute.
    What process will allow the Developer to extract results MOST efficiently from the DynamoDB table?

    - 9. 
    A gaming application stores scores for players in an Amazon DynamoDB table that has four attributes: user_id, user_name, user_score, and user_rank. The users are allowed to update their names only. A user is authenticated by web identity federation.
    Which set of conditions should be added in the policy attached to the role for the dynamodb:PutItem API call?

    - 10. 
    A company is migrating a stateful web service into the AWS cloud. The objective is to refactor the application to realize the benefits of cloud computing. How can the Developer leading the project refactor the application to enable more elasticity? (Select TWO.)

    - 11. 
    A Developer is working on an AWS Lambda function that accesses Amazon DynamoDB. The Lambda function must retrieve an item and update some of its attributes or create the item if it does not exist. The Lambda function has access to the primary key.
    Which IAM permission should the Developer request for the Lambda function to achieve this functionality?

    - 12. 
    A Developer recently created an Amazon DynamoDB table. The table has the following configuration:
        table name: table1
        primary partition key: userid (string)
        primary sort key: - 
    The Developer attempted to add two items for userid “user0001” with unique timestamps and received an error for the second item stating: “The conditional request failed”.
    What MUST the Developer do to resolve the issue?

    - 13. 
    An application is using Amazon DynamoDB as its data store and needs to be able to read 200 items per second as eventually consistent reads. Each item is 12 KB in size.
    What value should be set for the table's provisioned throughput for reads?

    - 14. 
    A Developer is troubleshooting an issue with a DynamoDB table. The table is used to store order information for a busy online store and uses the order date as the partition key. During busy periods writes to the table are being throttled despite the consumed throughput being well below the provisioned throughput.
    According to AWS best practices, how can the Developer resolve the issue at the LOWEST cost?

    - 15. 
    A company stores session information for a serverless application in an Amazon DynamoDB table. The company requires an automated process to eliminate outdated items from the table.
    What is the most straightforward and lowest cost method to accomplish this?

    - 16. 
    A company manages an application that stores data in an Amazon DynamoDB table. The company need to keep a record of all new changes made to the DynamoDB table in another table within the same AWS region. What is the MOST suitable way to deliver this requirement?

    - 17. 
    A developer is creating a serverless application that will use a DynamoDB table. The average item size is 9KB. The application will make 4 strongly consistent reads/sec, and 2 standard write/sec. How many RCUs/WCUs are required?

    - 18. 
    An application needs to read up to 100 items at a time from an Amazon DynamoDB. Each item is up to 100 KB in size and all attributes must be retrieved.
    What is the BEST way to minimize latency?

    - 19. 
    An application scans an Amazon DynamoDB table once per day to produce a report. The scan is performed in non-peak hours when production usage uses around 50% of the provisioned throughput.
    How can you MINIMIZE the time it takes to produce the report without affecting production workloads? (Select TWO.)

    - 20. 
    A Developer wants to find a list of items in a global secondary index from an Amazon DynamoDB table.
    Which DynamoDB API call can the Developer use in order to consume the LEAST number of read capacity units?

    - 21. 
    A Developer needs to return a list of items in a global secondary index from an Amazon DynamoDB table.
    Which DynamoDB API call can the Developer use in order to consume the LEAST number of read capacity units?

    - 22. 
    An application writes items to an Amazon DynamoDB table. As the application scales to thousands of instances, calls to the DynamoDB API generate occasional ThrottlingException errors. The application is coded in a language that is incompatible with the AWS SDK.
    What can be done to prevent the errors from occurring?

    - 23. 
    A Developer is creating a serverless application that uses an Amazon DynamoDB table. The application must make idempotent, all-or-nothing operations for multiple groups of write actions.
    Which solution will meet these requirements?

    - 24. 
    A Developer is designing a fault-tolerant application that will use Amazon EC2 instances and an Elastic Load Balancer. The Developer needs to ensure that if an EC2 instance fails session data is not lost. How can this be achieved?

    - 25. 
    A developer is setting up the primary key for an Amazon DynamoDB table that logs a company's purchases from various suppliers. Each transaction is recorded with these attributes: supplierId, transactionTime, item, and unitCost.
    Which primary key configuration will be valid in this case?

    - 26. 
    A Developer needs to scan a full DynamoDB 50GB table within non-peak hours. About half of the strongly consistent RCUs are typically used during non-peak hours and the scan duration must be minimized.
    How can the Developer optimize the scan execution time without impacting production workloads?

    - 27. 
    - 28. 
    - 29. 


    ### Answers:
    - 1. 
    Eventually consistent reads of 15 RCUs reading items that are 1 KB in size. (120/2)*(1/4)=15rcu (eventually consistent + small items = more reads per RCU).
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=614)

    - 2. 
    Utilize the DynamoDB BatchGetItem operation to fetch multiple items from both tables in a single network round trip.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=623)

    - 3. 
    Use conditional writes. Concurrent writes will overwrite the original editors updates.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=649)

    - 4. 
    Add an attribute with the expiration time; enable the Time To Live feature based on that attribute
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=642)

    - 5. 
    Use Amazon DynamoDB to perform scalable session handling
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=647)

    - 6. 
    The write capacity units on the GSI are under provisioned
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=632)

    - 7. 
    200 Read Capacity Units.    100*(8kb/4kb)=200 RCUs
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=646)

    - 8. 
    Create a global secondary index with a partition key of “game_name” and a sort key of “TopScore” and get the results based on the score attribute.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=632)

    - 9. 
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

    - 10. 
    Store the session state in an Amazon DynamoDB table
    Use an Elastic Load Balancer and Auto Scaling Group
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=647)

    - 11. 
    “dynamodb:UpdateItem”, “dynamodb:GetItem”, and “dynamodb:PutItem”
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=618)

    - 12. 
    Recreate the table with a composite key consisting of userid and timestamp
    https://aws.amazon.com/blogs/database/choosing-the-right-dynamodb-partition-key/

    - 13. 
    300 Read Capacity Units
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=)

    - 14. 
    Add a random number suffix to the partition key values
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=)

    - 15. 
    Use Amazon DynamoDB Time to Live (TTL) to automatically delete old items.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=642)

    - 16. 
    Use Amazon DynamoDB streams
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=638)

    - 17. 
    12 RCU and 18 WCU
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=612)

    - 18. 
    Use BatchGetItem
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=623)

    - 19. 
    Use the Limit parameter
    Use a Parallel Scan API operation
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=621)

    - 20. 
    Query operation using eventually-consistent reads
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=613)

    - 21. 
    Query operation using eventually-consistent reads
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=613)

    - 22. 
    Add exponential backoff to the application logic
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=616)

    - 23. 
    Update the items in the table using the TransactWriteltems operation to group the changes.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=644)

    - 24. 
    Use Amazon DynamoDB to perform scalable session handling
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=)

    - 25. 
    A composite primary key with supplierId as the partition key and transactionTime as the sort key.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=)

    - 26. 
    Use parallel scans while limiting the rate
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=)

    - 27. 
    - 28. 
    - 29.


    ### Wrong Answers:
    - 1. 
    Strongly consistent reads of 5 RCUs reading items that are 4 KB in size.
    Eventually consistent reads of 5 RCUs reading items that are 4 KB in size.
    Strongly consistent reads of 15 RCUs reading items that are 1 KB in size.

    - 2. 
    Utilize the DynamoDB Query operation to fetch multiple items from both tables in a single network round trip.
    Utilize the DynamoDB Scan operation with a filter expression to fetch multiple items from both tables in a single network round trip.
    Utilize the DynamoDB GetItem operation to fetch multiple items from both tables in a single network round trip.

    - 3. 
    Use strongly consistent reads before each update.
    Use DynamoDB Streams to replay the original editor's updates.
    Use BatchWriteItem to group concurrent updates together.

    - 4. 
    Enable DynamoDB Streams with a 24-hour retention period so that old items are deleted automatically
    Configure an Amazon S3 lifecycle policy on the table to expire items after 24 hours
    Enable point-in-time recovery on the table with a 24-hour retention window

    - 5. 
    Use Elastic Load Balancer sticky sessions to perform session handling
    Store session data on the instance store volume of each EC2 instance
    Use Amazon EBS snapshots to perform periodic session data backups

    - 6. 
    The write capacity units on the primary table are under provisioned
    The read capacity units on the GSI are under provisioned
    The DynamoDB Streams shard for the primary table is throttling write requests

    - 7. 
    100 Read Capacity Units
    125 Read Capacity Units
    500 Read Capacity Units

    - 8. 
    Create a local secondary index with a sort key of “TopScore” and get the results based on the score attribute.
    Scan the table with a filter on “game_name” and sort the results by “TopScore” in the application.
    Create a global secondary index with a partition key of “TopScore” and a sort key of “game_name” and get the results based on the score attribute.

    - 9. 
    "Condition": { "ForAllValues:StringEquals": { "dynamodb:LeadingKeys": [ "${www.amazon.com:user_id}" ], "dynamodb:Attributes": [ "user_name", "user_score", "user_rank" ] } }
    "Condition": { "ForAllValues:StringNotEquals": { "dynamodb:LeadingKeys": [ "${www.amazon.com:user_id}" ], "dynamodb:Attributes": [ "user_name" ] } }
    "Condition": { "ForAllValues:StringEquals": { "dynamodb:LeadingKeys": [ "${www.amazon.com:user_name}" ], "dynamodb:Attributes": [ "user_id" ] } }

    - 10. 
    Store the session state on Amazon EBS volumes attached to the instances
    Use Elastic Load Balancer sticky sessions to retain session state
    Use a larger Amazon EC2 instance type to handle more sessions

    - 11. 
    “dynamodb:GetRecords”, “dynamodb:BatchGetItem”, and “dynamodb:DescribeTable”
    “dynamodb:Scan”, “dynamodb:DeleteItem”, and “dynamodb:ListTables”
    “dynamodb:UpdateTable”, “dynamodb:GetItem”, and “dynamodb:CreateTable”

    - 12. 
    Increase the write capacity units on the table to allow both items to be written
    Add a global secondary index with timestamp as the sort key to the existing table
    Use the BatchWriteItem operation to insert both items in a single request

    - 13. 
    150 Read Capacity Units
    1200 Read Capacity Units
    2400 Read Capacity Units

    - 14. 
    Increase the provisioned write capacity units on the table
    Enable DynamoDB Accelerator (DAX) to cache the write requests
    Add a global secondary index on the order date attribute

    - 15. 
    Use Amazon DynamoDB Streams to automatically delete old items.
    Use Amazon DynamoDB point-in-time recovery to automatically delete old items.
    Use Amazon DynamoDB Auto Scaling to automatically delete old items.

    - 16. 
    Use Amazon DynamoDB Accelerator (DAX)
    Use Amazon DynamoDB global tables
    Use Amazon DynamoDB point-in-time recovery

    - 17. 
    6 RCU and 18 WCU
    12 RCU and 9 WCU
    9 RCU and 36 WCU

    - 18. 
    Use GetItem in a loop
    Use Scan with a filter expression
    Use Query with a projection expression

    - 19. 
    Use strongly consistent reads
    Set the Select parameter to ALL_ATTRIBUTES
    Increase the page size to 16 MB

    - 20. 
    Query operation using strongly-consistent reads
    Scan operation using eventually-consistent reads
    GetItem operation using eventually-consistent reads

    - 21. 
    Scan operation using strongly-consistent reads
    Query operation using strongly-consistent reads
    BatchGetItem operation using eventually-consistent reads

    - 22. 
    Add immediate retries without any delay to the application logic
    Enable DynamoDB Streams on the table to buffer the write requests
    Enable DynamoDB Accelerator (DAX) to absorb the write traffic

    - 23. 
    Update the items in the table using the BatchWriteItem operation to group the changes.
    Update the items in the table using the TransactGetItems operation to group the changes.
    Update the items in the table using conditional PutItem calls with the ReturnValues parameter.

    - 24. 
    Use Elastic Load Balancer sticky sessions to retain session data
    Store the session data on the instance store of each EC2 instance
    Use Amazon EBS snapshots to perform session data backups

    - 25. 
    A simple primary key with supplierId as the partition key.
    A composite primary key with item as the partition key and unitCost as the sort key.
    A simple primary key with unitCost as the partition key.

    - 26. 
    Use parallel scans without limiting the rate
    Use sequential scans with strongly consistent reads
    Use a Query operation with eventually consistent reads

