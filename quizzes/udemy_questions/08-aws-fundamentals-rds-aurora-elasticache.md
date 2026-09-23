# Section 8: AWS Fundamentals: RDS + Aurora + ElastiCache ---> [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=138)
    ============================================================================================================================================================
- ### Questions:
    - 1. 
    An eCommerce application uses an Amazon RDS database with Amazon ElastiCache in front. Stock volume data is updated dynamically in listings as sales are made. Customers have complained that occasionally the stock volume data is incorrect, and they end up purchasing items that are out of stock. A Developer has checked the front end and indeed some items display the incorrect stock count.
    What could be causing this issue?

    - 2. 
    A Developer is creating a database solution using an Amazon ElastiCache caching layer. The solution must provide strong consistency to ensure that updates to product data are consistent between the backend database and the ElastiCache cache. Low latency performance is required for all items in the database.
    Which cache writing policy will satisfy these requirements?

    - 3. 
    A developer needs to implement a caching layer in front of an Amazon RDS database. If the caching layer fails, it is time consuming to repopulate cached data so the solution should be designed for maximum uptime. Which solution is best for this scenario?

    - 4. 
    An online retail application developer is planning to migrate to AWS to accommodate a future surge in traffic. Currently, a web server, which hosts the web application and manages session state in memory, and a separate server hosting a MySQL database for order details, are used.
    During peak traffic, memory usage on the web server reaches its limit, leading to considerable slowdowns. As part of the migration plan, the developer intends to use Amazon EC2 instances with an Auto Scaling group and an Application Load Balancer for the web server.
    What other changes can the developer implement to enhance application performance?

    - 5. 
    A multimedia streaming service wants to migrate its user authentication system to AWS. The system keeps user session data during an active session, which is crucial for seamless user experience. The new system needs to be fault-tolerant, highly scalable natively, and any service disruption must not affect user experience.
    What is the best option to store the user session data?

    - 6. 
    A Developer is building a three-tier web application that must be able to handle a minimum of 10,000 requests per minute. The requirements state that the web tier should be completely stateless while the application maintains session state data for users.
    How can the session state data be maintained externally, whilst keeping latency at the LOWEST possible value?

    - 7. 
    A review of Amazon CloudWatch metrics shows that there are a high number of reads taking place on a primary database built on Amazon Aurora with MySQL. What can a developer do to improve the read scaling of the database? (Select TWO.)

    - 8. 
    A Development team is involved with migrating an on-premises MySQL database to Amazon RDS. The database usage is very read-heavy. The Development team wants re-factor the application code to achieve optimum read performance for queries.
    How can this objective be met?

    - 9. 
    A web application runs on a fleet of Amazon EC2 instances in an Auto Scaling group behind an Application Load Balancer (ALB). A developer needs a store for session data so it can be reliably served across multiple requests.
    Where is the best place to store the session data?

    - 10. 
    An organization handles data that requires high availability in its relational database. The main headquarters for the organization is in Virginia with smaller offices located in California. The main headquarters uses the data more frequently than the smaller offices. How should the developer configure their databases to meet high availability standards?

    - 11. 
    An ecommerce company manages a storefront that uses an Amazon API Gateway API which exposes an AWS Lambda function. The Lambda functions processes orders and stores the orders in an Amazon RDS for MySQL database. The number of transactions increases sporadically during marketing campaigns, and then goes close to zero during quite times.
    How can a developer increase the elasticity of the system MOST cost-effectively?

    - 12. 
    A critical application is hosted on AWS exposed by an HTTP API through Amazon API Gateway. The API is integrated with an AWS Lambda function and the application data is housed in an Amazon RDS for PostgreSQL DB instance, featuring 2 vCPUs and 16 GB of RAM.
    The company has been receiving customer complaints about occasional HTTP 500 Internal Server Error responses from some API calls during unpredictable peak usage times. Amazon CloudWatch Logs has recorded "connection limit exceeded" errors. The company wants to ensure resilience in the application, with no unscheduled downtime for the database.
    Which solution would best fit these requirements?

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
    The cache is not being invalidated when the stock volume data is changed.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=154)

    - 2. 
    Use a write-through caching strategy.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=160)

    - 3. 
    Implement Amazon ElastiCache Redis
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=156)

    - 4. 
    Use Amazon ElastiCache for Memcached to store and manage session data, while utilizing Amazon RDS for MySQL DB instance for application data storage.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=156)

    - 5. 
    Store the user session data in Amazon ElastiCache.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=155)

    - 6. 
    Create an Amazon ElastiCache Redis cluster, then implement session handling at the application level to leverage the cluster for session data storage
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=153)

    - 7. 
    Create a separate Aurora MySQL cluster and configure binlog replication.
    Create Aurora Replicas in same cluster as the primary database instance.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=147)

    - 8. 
    Add a connection string to use an Amazon RDS read replica for read queries
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=140)

    - 9. 
    Write the data to an Amazon ElastiCache cluster.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=155)

    - 10. 
    Create an Aurora database with the primary database in Virginia and specify the failover to the Aurora replica in another AZ in Virginia.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=145)

    - 11. 
    Migrate from Amazon RDS to Amazon Aurora MySQL. Use an Aurora Auto Scaling policy to scale read replicas based on average connections of Aurora Replicas.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=)

    - 12. 
    Use Amazon RDS Proxy and update the Lambda function to connect to the proxy.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=152)

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
    The cache is using a write-through strategy when the stock volume data is changed.
    The ElastiCache cluster is not configured with Multi-AZ replication.
    The Amazon RDS database is not configured with a Multi-AZ standby instance.

    - 2. 
    Use a lazy loading caching strategy.
    Use a cache-aside strategy with a long TTL.
    Use a write-around caching strategy.

    - 3. 
    Implement Amazon ElastiCache Memcached
    Implement Amazon DynamoDB Accelerator (DAX)
    Implement an Amazon RDS read replica

    - 4. 
    Use sticky sessions on the Application Load Balancer to store session data in memory on the EC2 instances.
    Store session data on Amazon EBS volumes attached to the EC2 instances, while utilizing Amazon RDS for MySQL DB instance for application data storage.
    Use Amazon CloudFront to cache session data at edge locations, while utilizing Amazon RDS for MySQL DB instance for application data storage.

    - 5. 
    Store the user session data in the memory of the EC2 instances.
    Store the user session data on an Amazon EBS volume.
    Store the user session data in Amazon S3 Glacier.

    - 6. 
    Enable sticky sessions on the Elastic Load Balancer to keep session data on the web tier instances
    Create an Amazon RDS MySQL database, then implement session handling at the application level to leverage the database for session data storage
    Create an Amazon S3 bucket, then implement session handling at the application level to leverage the bucket for session data storage

    - 7. 
    Increase the instance size of the primary database instance only.
    Enable Multi-AZ on the Aurora cluster to serve reads from the standby.
    Place an Amazon CloudFront distribution in front of the Aurora cluster.

    - 8. 
    Add a connection string to use the Amazon RDS Multi-AZ standby instance for read queries
    Enable Amazon RDS Multi-AZ and send all queries to the primary endpoint
    Add Amazon DynamoDB Accelerator (DAX) in front of the Amazon RDS database

    - 9. 
    Write the data to the root EBS volume of the EC2 instance.
    Write the data to the instance store of the EC2 instance.
    Enable sticky sessions on the ALB and store the data in memory.

    - 10. 
    Create an RDS database with the primary database in California and a read replica in the same AZ in California.
    Create an Aurora database with the primary database in California and specify the failover to the Aurora replica in Virginia.
    Create an RDS database in a single AZ in Virginia and take daily automated snapshots copied to California.

    - 11. 
    Migrate from Amazon RDS to Amazon Aurora MySQL. Use a scheduled scaling policy on the Lambda function to add provisioned concurrency.
    Increase the instance size of the Amazon RDS for MySQL database. Enable Multi-AZ to scale read traffic during campaigns.
    Migrate from Amazon RDS to Amazon EC2 instances running MySQL. Use an EC2 Auto Scaling group to add instances based on CPU utilization.

    - 12. 
    Increase the reserved concurrency of the Lambda function to handle more connections.
    Enable Multi-AZ on the RDS DB instance and update the Lambda function to connect to the standby.
    Add an Amazon ElastiCache cluster and update the Lambda function to connect to the cache.
