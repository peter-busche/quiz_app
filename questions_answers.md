# Section 4: IAM & AWS CLI  ---> [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=21)
    ============================================================================================================================================================
- ### Questions:
    - 1. 
    The following permissions policy is applied to an IAM user account:
        {
        "Version": "2012-10-17",
        "Statement": [{
        "Effect": "Allow",
        "Action": "sqs:*",
        "Resource": "arn:aws:sqs:*:513246782345:staging-queue*"
        }]
        }
    Due to this policy, what Amazon SQS actions will the user be able to perform?

    - 2. 
    An organization has a new AWS account and is setting up IAM users and policies. According to AWS best practices, which of the following strategies should be followed? (Select TWO.)

    - 3. 
    An Amazon DynamoDB table will store authentication credentials for a mobile app. The table must be secured so only a small group of Developers are able to access it.
    How can table access be secured according to this requirement and following AWS best practice?

    - 4. 
    A small team of Developers require access to an Amazon S3 bucket. An admin has created a resource-based policy. Which element of the policy should be used to specify the ARNs of the user accounts that will be granted access?

    - 5. 
    A Developer has noticed some suspicious activity in her AWS account and is concerned that the access keys associated with her IAM user account may have been compromised. What is the first thing the Developer do in should do in this situation?

    - 6. 
    A developer is writing an application for a company. The program needs to access and read the file named "secret-data.xlsx" located in the root directory of an Amazon S3 bucket named "DATA-BUCKET". The company's security policies mandate the enforcement of the principle of least privilege for the IAM policy associated with the application.
    Which IAM policy statement will comply with these security stipulations?

    - 7. 
    A team of Developers require read-only access to an Amazon DynamoDB table. The Developers have been added to a group. What should an administrator do to provide the team with access whilst following the principal of least privilege?

    - 8. 
    A Developer has lost their access key ID and secret access key for programmatic access. What should the Developer do?

    - 9. 
    A company is reviewing their security practices. According to AWS best practice, how should access keys be managed to improve security? (Select TWO.)

    - 10. 
    The manager of a development team is setting up a shared S3 bucket for team members. The manager would like to use a single policy to allow each user to have access to their objects in the S3 bucket. Which feature can be used to generalize the policy?

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
    The user will be able to use all Amazon SQS actions, but only for queues with names begin with the string “staging-queue“
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=25)

    - 2. 
    Create standalone policies instead of using inline policies
    Use groups to assign permissions to users
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=36)

    - 3. 
    Attach a permissions policy to an IAM group containing the Developer’s IAM user accounts that grants access to the table
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=36)

    - 4. 
    Principal
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=25)

    - 5. 
    Delete the compromised access keys
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=30)

    - 6. 
    {"Effect": "Allow", "Action": "s3:GetObject", "Resource": "arn:aws:s3:::DATA-BUCKET/secret-data.xlsx"}
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=36)

    - 7. 
    Create a customer managed policy with read only access to DynamoDB and specify the ARN of the table for the “Resource” element. Attach the policy to the group
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=)

    - 8. 
    Disable and delete the user's access key and generate a new set

    - 9. 
    Delete all access keys for the root account IAM user
    Use different access keys for different applications

    - 10. 
    Variable

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


# Section 5: EC2 Fundamentals ---> [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=39)
    ============================================================================================================================================================
- ### Questions:
    - 1. 
    A Developer must run a shell script on Amazon EC2 Linux instances each time they are launched by an Amazon EC2 Auto Scaling group. What is the SIMPLEST way to run the script?

    - 2. 
    An organization is hosting a website on an Amazon EC2 instance in a public subnet. The website should allow public access for HTTPS traffic on TCP port 443 but should only accept SSH traffic on TCP port 22 from a corporate address range accessible over a VPN.
    Which security group configuration will support both requirements?

    - 3. 
    A Developer is writing code to run in a cron job on an Amazon EC2 instance that sends status information about the application to Amazon CloudWatch.
    Which method should the Developer use?

    - 4. 
    A Developer will be launching several Docker containers on a new Amazon ECS cluster using the EC2 Launch Type. The containers will all run a web service on port 80.
    What is the EASIEST way the Developer can configure the task definition to ensure the web services run correctly and there are no port conflicts on the host instances?

    - 5. 
    A Developer has code running on Amazon EC2 instances that needs read-only access to an Amazon DynamoDB table.
    What is the MOST secure approach the Developer should take to accomplish this task?

    - 6. 
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
    Add the script to the user data when creating the launch configuration
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=42)

    - 2. 
    Allow traffic to port 443 from 0.0.0.0/0 and allow traffic to port 22 from 192.168.0.0/16.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=51)

    - 3. 
    Use the unified CloudWatch agent to publish custom metrics.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=)

    - 4. 
    Specify port 80 for the container port and port 0 for the host port
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=109)

    - 5. 
    Use an IAM role with an AmazonDynamoDBReadOnlyAccess policy applied to the EC2 instances

    - 6. 
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


# Section 6: EC2 Instance Storage ---> [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=72)
    ============================================================================================================================================================
- ### Questions:
    - 1. 
    - 2. 
    - 3. 
    - 4. 
    - 5. 
    - 6. 
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
    - 2. 
    - 3. 
    - 4. 
    - 5. 
    - 6. 
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


# Section 7: AWS Fundamentals: ELB + ASG ---> [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=92)
    ============================================================================================================================================================
- ### Questions:
    - 1. 
    A company is running a web application on Amazon EC2 behind an Elastic Load Balancer (ELB). The company is concerned about the security of the web application and would like to secure the application with SSL certificates. The solution should not have any performance impact on the EC2 instances.
    What steps should be taken to secure the web application? (Select TWO.)

    - 2. 
    An application is being migrated into the cloud. The application is stateless and will run on a fleet of Amazon EC2 instances. The application should scale elastically. How can a Developer ensure that the number of instances available is sufficient for current demand?

    - 3. 
    A corporation plans to deploy an application on AWS utilizing an Elastic Load Balancer that operates with HTTP/HTTPS listeners. The application must have the ability to retrieve client IP addresses.
    Which load-balancing solution would satisfy these needs?

    - 4. 
    An organization needs to add encryption in-transit to an existing website running behind an Elastic Load Balancer. The website’s Amazon EC2 instances are CPU-constrained and therefore load on their CPUs should not be increased. What should be done to secure the website? (Select TWO.)

    - 5. 
    A developer must identify the public IP addresses of clients connecting to Amazon EC2 instances behind a public Application Load Balancer (ALB). The EC2 instances run an HTTP server that logs all requests to a log file.
    How can the developer ensure the client public IP addresses are captured in the log files on the EC2 instances?

    - 6. 
    An application includes multiple Auto Scaling groups of Amazon EC2 instances. Each group corresponds to a different subdomain of example.com, including forum.example.com and myaccount.example.com. An Elastic Load Balancer will be used to distribute load from a single HTTPS listener.
    Which type of Elastic Load Balancer MUST a Developer use in this scenario?

    - 7. 
    An Auto Scaling Group (ASG) of Amazon EC2 instances is being created for processing messages from an Amazon SQS queue. To ensure the EC2 instances are cost-effective a Developer would like to configure the ASG to maintain aggregate CPU utilization at 70%.
    Which type of scaling policy should the Developer choose?

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
    Add an SSL certificate to the Elastic Load Balancer
    Configure the Elastic Load Balancer for SSL termination
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=123)

    - 2. 
    Create a launch configuration and use Amazon EC2 Auto Scaling
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=128)

    - 3. 
    Application Load Balancer with X-Forwarded-For headers enabled.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=113)

    - 4. 
    Configure an Elastic Load Balancer with SSL termination
    Configure SSL certificates on an Elastic Load Balancer
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=123)

    - 5. 
    Configure the HTTP server to add the x-forwarded-for request header to the logs.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=)

    - 6. 
    Application Load Balancer

    - 7. 
    Target Tracking Scaling Policy

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
    An e-commerce web application that shares session state on-premises is being migrated to AWS. The application must be fault tolerant, natively highly scalable, and any service interruption should not affect the user experience.
    What is the best option to store the session state?

    - 14. 
    An application uses an Amazon RDS database. The company requires that the performance of database reads is improved, and they want to add a caching layer in front of the database. The cached data must be encrypted, and the solution must be highly available.
    Which solution will meet these requirements?

    - 15. 
    A developer is updating an Amazon Aurora MySQL database to allow more clients to connect. What database parameter needs to be updated to support a higher number of client connections?

    - 16. 
    An Amazon ElastiCache cluster has been placed in front of a large Amazon RDS database. To reduce cost the ElastiCache cluster should only cache items that are actually requested. How should ElastiCache be optimized?

    - 17. 
    An Amazon RDS database is experiencing a high volume of read requests that are slowing down the database. Which fully managed, in-memory AWS database service can assist with offloading reads from the RDS database?

    - 18. 
    A company is migrating an application with a website and MySQL database to the AWS Cloud. The company require the application to be refactored so it offers high availability and fault tolerance.
    How should a Developer refactor the application? (Select TWO.)

    - 19. 
    A retail organization stores stock information in an Amazon RDS database. An application reads and writes data to the database. A Developer has been asked to provide read access to the database from a reporting application in another region.
    Which configuration would provide BEST performance for the reporting application without impacting the performance of the main database?

    - 20. 
    A company is migrating an on-premises web application to AWS. The web application runs on a single server and stores session data in memory. On AWS the company plan to implement multiple Amazon EC2 instances behind an Elastic Load Balancer (ELB). The company want to refactor the application so that data is resilient if an instance fails and user downtime is minimized.
    Where should the company move session data to MOST effectively reduce downtime and make users’ session data more fault tolerant?

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
    Store the session state in Amazon ElastiCache
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=)

    - 14. 
    Amazon ElastiCache for Redis in cluster mode.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=)

    - 15. 
    max_connections
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=)

    - 16. 
    Use a lazy loading caching strategy

    - 17. 
    Amazon ElastiCache Redis

    - 18. 
    Migrate the website to an Auto Scaling group of EC2 instances across multiple AZs and use an Elastic Load Balancer
    Migrate the MySQL database to an Amazon RDS Multi-AZ deployment

    - 19. 
    Implement a cross-region read replica in the region where the reporting application will run

    - 20. 
    An Amazon ElastiCache for Redis cluster

    - 21. 
    - 22. 
    - 23. 
    - 24. 
    - 25. 
    - 26. 
    - 27. 
    - 28. 
    - 29. 


# Section 9: Route 53 ---> [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=165)
    ============================================================================================================================================================
- ### Questions:
    - 1. 
    A website is running on a single Amazon EC2 instance. A Developer wants to publish the website on the Internet and is creating an A record on Amazon Route 53 for the website’s public DNS name.
    What type of IP address MUST be assigned to the EC2 instance and used in the A record to ensure ongoing connectivity?

    - 2. 
    In the process of developing an application, a software engineer deploys an Amazon API Gateway REST API within the us-west-2 Region. The plan is to use Amazon CloudFront and a custom domain name for the API, using an SSL/TLS certificate acquired from a third-party provider.
    What is the appropriate strategy for configuring the custom domain name?

    - 3. 
    A Developer manages a website running behind an Elastic Load Balancer in the us-east-1 region. The Developer has recently deployed an identical copy of the website in us-west-1 and needs to send 20% of the traffic to the new site.
    How can the Developer achieve this requirement?

    - 4. 
    - 5. 
    - 6. 
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
    Elastic IP address
    https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.html
    https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html

    - 2. 
    Import the third-party SSL/TLS certificate to AWS Certificate Manager (ACM), link it with the custom domain name in API Gateway, and then create an alias (A) record in Route 53 for the custom domain name.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=195)

    - 3. 
    Use an Amazon Route 53 Weighted Routing Policy
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=180)

    - 4. 
    - 5. 
    - 6. 
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


# Section 10: VPC Fundamentals ---> [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=196)
    ============================================================================================================================================================
- ### Questions:
    - 1. 
    A financial application is hosted on an Auto Scaling group of EC2 instance with an Elastic Load Balancer. A Developer needs to capture information about the IP traffic going to and from network interfaces in the VPC.
    How can the Developer capture this information?

    - 2. 
    An AWS Lambda function must be connected to an Amazon VPC private subnet that does not have Internet access. The function also connects to an Amazon DynamoDB table. What MUST a Developer do to enable access to the DynamoDB table?

    - 3. 
    An organization is selling memorabilia that is illegal in specific countries. How can a developer restrict access to the website to countries where the memorabilia are illegal?

    - 4. 
    A company is deploying a static website hosted from an Amazon S3 bucket. The website must support encryption in-transit for website visitors.
    Which combination of actions must the Developer take to meet this requirement? (Select TWO.)

    - 5. 
    An application uses Amazon EC2 instances, AWS Lambda functions and an Amazon SQS queue. The Developer must ensure all communications are within an Amazon VPC using private IP addresses. How can this be achieved? (Select TWO.)

    - 6. 
    A Developer is creating an application that uses Amazon EC2 instances and must be highly available and fault tolerant. How should the Developer configure the VPC?

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
    Create a flow log in the VPC and publish data to Amazon S3
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=203)

    - 2. 
    Configure a VPC endpoint
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=205)

    - 3. 
    Create a Web ACL in AWS WAF with a rule that matches the specified countries and blocks access.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=201)

    - 4. 
    - 5. 
    Add the AWS Lambda function to the VPC
    Create a VPC endpoint for Amazon SQS

    - 6. 
    Create a subnet in each availability zone in the region

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

# Section 11: Amazon S3 Introduction ---> [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=213)
    ============================================================================================================================================================
- ### Questions:
    - 1. 
    An application exports files which must be saved for future use but are not frequently accessed. Compliance requirements necessitate redundant retention of data across AWS regions. Which solution is the MOST cost-effective for these requirements?

    - 2. 
    An application that is being migrated to AWS and refactored requires a storage service. The storage service should provide a standards-based REST web service interface and store objects based on keys.
    Which AWS service would be MOST suitable?

    - 3. 
    A Developer is creating a serverless website with content that includes HTML files, images, videos, and JavaScript (client-side scripts).
    Which combination of services should the Developer use to create the website?

    - 4. 
    - 5. 
    - 6. 
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
    Amazon S3 with Cross-Region Replication (CRR)
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=228)

    - 2. 
    Amazon S3

    - 3. 
    Amazon S3 and Amazon CloudFront

    - 4. 
    - 5. 
    - 6. 
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


# Section 12: AWS CLI, SDK, IAM Roles & Policies ---> [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=238)
    ============================================================================================================================================================
- ### Questions:
    - 1. 
    An application writes items to an Amazon DynamoDB table. As the application scales to thousands of instances, calls to the DynamoDB API generate occasional ThrottlingException errors. The application is coded in a language incompatible with the AWS SDK.
    How should the error be handled?

    - 2. 
    A programmer is creating an application that requires signed requests (Signature Version 4) for invoking other AWS services. Having constructed a canonical request, created the string to sign, and calculated the signing information, which strategies can the programmer apply to finalize a signed request? (Select TWO.)

    - 3. 
    A Developer is trying to make API calls using AWS SDK. The IAM user credentials used by the application require multi-factor authentication for all API calls.
    Which method should the Developer use to access the multi-factor authentication protected API?

    - 4. 
    A Developer is creating an AWS Lambda function that generates a new file each time it runs. Each new file must be checked into an AWS CodeCommit repository hosted in the same AWS account.
    How should the Developer accomplish this?

    - 5. 
    - 6. 
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
    Add exponential backoff to the application logic
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=245)

    - 2. 
    Incorporate the signature into an HTTP header called "Authorization".
    Insert the signature into a query string parameter referred to as "X-Amz-Signature".
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=247)

    - 3. 
    GetSessionToken
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=241)

    - 4. 
    Use an AWS SDK to instantiate a CodeCommit client. Invoke the put_file method to add the file to the repository
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=243)
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=601)

    - 5. 
    - 6. 
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


# Section 13: Advanced Amazon S3 ---> [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=248)
    ============================================================================================================================================================
- ### Questions:
    - 1. 
    An application reads data from Amazon S3 and makes 55,000 read requests per second. A Developer must design the storage solution to ensure the performance requirements are met cost-effectively.
    How can the storage be optimized to meet these requirements?

    - 2. 
    Data must be loaded into an application each week for analysis. The data is uploaded to an Amazon S3 bucket from several offices around the world. Latency is slowing the uploads and delaying the analytics job. What is the SIMPLEST way to improve upload times?

    - 3. 
    An organization has an Amazon S3 bucket containing premier content that they intend to make available to only paid subscribers of their website. The objects in the S3 bucket are private to prevent inadvertent exposure of the premier content to non-paying website visitors.
    How can the organization provide only paid subscribers the ability to download the premier content in the S3 bucket?

    - 4. 
    A company has a global presence and managers must submit large quantities of reporting data to an Amazon S3 bucket located in the us-east-1 region on weekly basis. Uploads have been slow recently, how can you improve data throughput and upload times?

    - 5. 
    - 6. 
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
    Create at least 10 prefixes and split the files across the prefixes.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=257)

    - 2. 
    Upload using Amazon S3 Transfer Acceleration
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=258)

    - 3. 
    Generate a pre-signed object URL for the premier content file when a paid subscriber requests a download

    - 4. 
    Enable S3 Transfer Acceleration on the S3 bucket

    - 5. 
    - 6. 
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


# Section 14: Amazon S3 Security ---> [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=261)
    ============================================================================================================================================================
- ### Questions:
    - 1. 
    A company uses an Amazon S3 bucket to store a large number of sensitive files relating to eCommerce transactions. The company has a policy that states that all data written to the S3 bucket must be encrypted.
    How can a Developer ensure compliance with this policy?

    - 2. 
    A company has transferred some of its confidential documents to a private Amazon S3 bucket that is not publicly accessible. Now, the company intends to build a serverless application that allows its staff to securely share these files with others.
    Which AWS service should the company utilize to ensure secure file sharing and access?

    - 3. 
    A static website is hosted on Amazon S3 using the bucket name of dctlabs.com. Some HTML pages on the site use JavaScript to download images that are located in the bucket https://dctlabsimages.s3.amazonaws.com/. Users have reported that the images are not being displayed.
    What is the MOST likely cause?

    - 4. 
    You run an ad-supported photo sharing website using Amazon S3 to serve photos to visitors of your site. At some point you find out that other sites have been linking to the photos on your site, causing loss to your business.
    What is an effective method to mitigate this?

    - 5. 
    An application is running on a fleet of EC2 instances running behind an Elastic Load Balancer (ELB). The EC2 instances session data in a shared Amazon S3 bucket. Security policy mandates that data must be encrypted in transit.
    How can the Developer ensure that all data that is sent to the S3 bucket is encrypted in transit?

    - 6. 
    The development team is experiencing issues with their application hosted on Amazon EC2 instances, as they are unable to connect to an Amazon S3 bucket during test runs.
    What should be the appropriate measures to resolve this issue? (Select TWO.)

    - 7. 
    A business is providing its clients read-only permissions to items within an Amazon S3 bucket, utilizing IAM permissions to limit access to this S3 bucket. Clients are only permitted to access their specific files. Regulatory compliance necessitates the enforcement of in-transit encryption during communication with Amazon S3.
    What solution will fulfill these criteria?

    - 8. 
    An independent software vendor (ISV) uses Amazon S3 and Amazon CloudFront to distribute software updates. They would like to provide their premium customers with access to updates faster. What is the MOST efficient way to distribute these updates only to the premium customers? (Select TWO.)

    - 9. 
    A Java based application generates email notifications to customers using Amazon SNS. The emails must contain links to access data in a secured Amazon S3 bucket. What is the SIMPLEST way to maintain security of the bucket whilst allowing the customers to access specific objects?

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
    Create an S3 bucket policy that denies any S3 Put request that does not include the x-amz-server-side-encryption
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=270)

    - 2. 
    S3 presigned URLs
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=277)

    - 3. 
    Cross Origin Resource Sharing is not enabled on the dctlabsimages bucket
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=271)

    - 4. 
    Remove public read access and use signed URLs with expiry dates
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=277)

    - 5. 
    Create an S3 bucket policy that denies traffic where SecureTransport is false
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=269)

    - 6. 
    Verify the IAM roles attached to the EC2 instances and ensure they have the necessary permissions to access the S3 bucket.
    Check the bucket policies for the Amazon S3 bucket and confirm that they permit access from the EC2 instances.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=270)

    - 7. 
    Update the S3 bucket policy to include a condition that requires aws:SecureTransport for all actions.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=269)

    - 8. 
    Create a signed URL with access to the content and distribute it to the premium customers
    Create an origin access identity (OAI) and associate it with the distribution and configure permissions

    - 9. 
    Use the AWS SDK for Java with GeneratePresignedUrlRequest to create a presigned URL

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


# Section 15: CloudFront ---> [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=281)
    ============================================================================================================================================================
- ### Questions:
    - 1. 
    An application uses an Auto Scaling group of Amazon EC2 instances, an Application Load Balancer (ALB), and an Amazon Simple Queue Service (SQS) queue. An Amazon CloudFront distribution caches content for global users. A Developer needs to add in-transit encryption to the data by configuring end-to-end SSL between the CloudFront Origin and the end users.
    How can the Developer meet this requirement? (Select TWO.)

    - 2. 
    A company is using Amazon CloudFront to provide low-latency access to a web application to its global users. The organization must encrypt all traffic between users and CloudFront, and all traffic between CloudFront and the web application.
    How can these requirements be met? (Select TWO.)

    - 3. 
    A website is being delivered using Amazon CloudFront and a Developer recently modified some images that are displayed on website pages. Upon testing the changes, the Developer noticed that the new versions of the images are not displaying.
    What should the Developer do to force the new images to be displayed?

    - 4. 
    An online retail platform uses the AWS SDK for Python (Boto3) on the frontend to handle user authentication through AWS Security Token Service (AWS STS). The platform stores its digital assets in an Amazon S3 bucket and delivers them using an Amazon CloudFront distribution, which uses the S3 bucket as its origin.
    Currently, the application holds its role credentials in plaintext within a Python file in the application code. The platform developers are looking to improve security by creating a mechanism that enables the application to retrieve user credentials without embedding any credentials in the application code.
    What solution would meet these requirements?

    - 5. 
    A company is deploying a static website hosted from an Amazon S3 bucket. The website must support encryption in-transit for website visitors.
    Which combination of actions must the Developer take to meet this requirement? (Select TWO.)

    - 6. 
    A company use Amazon CloudFront to deliver application content to users around the world. A Developer has made an update to some files in the origin however users have reported that they are still getting the old files.
    How can the Developer ensure that the old files are replaced in the cache with the LEAST disruption?

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
    Configure the Origin Protocol Policy
    Configure the Viewer Protocol Policy
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=283)
    https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html

    - 2. 
    Set the Origin Protocol Policy to “HTTPS Only”
    Set the Viewer Protocol Policy to “HTTPS Only” or “Redirect HTTP to HTTPS”
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=283)
    https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html

    - 3. 
    Invalidate the old versions of the images on the edge caches
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=294)

    - 4. 
    Integrate a Lambda@Edge function with the CloudFront distribution. Trigger the function upon each viewer request. Give the execution role of the function the required permissions to interact with AWS STS. Shift all SDK calls from the frontend to this function.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=567)

    - 5. 
    Create an Amazon CloudFront distribution. Set the S3 bucket as an origin.
    Configure an Amazon CloudFront distribution with an SSL/TLS certificate.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=)

    - 6. 
    Invalidate the files from the edge caches

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


# Section 16: ECS, ECR & Fargate - Docker in AWS ---> [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=312)
    ============================================================================================================================================================
- ### Questions:
    - 1. 
    A developer plan to deploy an application on Amazon ECS that uses the AWS SDK to make API calls to Amazon DynamoDB. In the development environment the application was configured with access keys. The application is now ready for deployment to a production cluster.
    How should the developer configure the application to securely authenticate to AWS services?

    - 2. 
    An application is running on an Amazon EC2 Linux instance. The instance needs to make AWS API calls to several AWS services. What is the MOST secure way to provide access to the AWS services with MINIMAL management overhead?

    - 3. 
    AWS CodeBuild builds code for an application, creates a Docker image, pushes the image to Amazon Elastic Container Registry (ECR), and tags the image with a unique identifier.
    If the Developers already have AWS CLI configured on their workstations, how can the Docker images be pulled to the workstations? 

    - 4. 
    A Developer is creating a service on Amazon ECS and needs to ensure that each task is placed on a different container instance.
    How can this be achieved?

    - 5. 
    A Developer is deploying an application using Docker containers on Amazon ECS. One of the containers runs a database and should be placed on instances in the “databases” task group.
    What should the Developer use to control the placement of the database task?

    - 6. 
    A Developer has created a task definition that includes the following JSON code:
        "placementConstraints": [
        {
        "expression": "task:group == databases",
        "type": "memberOf"
        }
        ]
    What will be the effect for tasks using this task definition?

    - 7. 
    A Developer is migrating Docker containers to Amazon ECS. A large number of containers will be deployed across some newly deployed ECS containers instances using the same instance type. High availability is provided within the microservices architecture. Which task placement strategy requires the LEAST configuration for this scenario?

    - 8. 
    An application deployed on AWS Elastic Beanstalk experienced increased error rates during deployments of new application versions, resulting in service degradation for users. The Development team believes that this is because of the reduction in capacity during the deployment steps. The team would like to change the deployment policy configuration of the environment to an option that maintains full capacity during deployment while using the existing instances.
    Which deployment policy will meet these requirements while using the existing instances?

    - 9. 
    A developer is updating an Amazon ECS app that uses an ALB with two target groups and a single listener. The developer has an AppSpec file in an S3 bucket and an AWS CodeDeploy deployment group tied to the ALB and AppSpec file. The developer needs to use an AWS Lambda function for update validation before deployment.
    Which solution meets these requirements?

    - 10. 
    A Developer is deploying an application in a microservices architecture on Amazon ECS. The Developer needs to choose the best task placement strategy to MINIMIZE the number of instances that are used. Which task placement strategy should be used?

    - 11. 
    A company runs many microservices applications that use Docker containers. The company are planning to migrate the containers to Amazon ECS. The workloads are highly variable and therefore the company prefers to be charged per running task.
    Which solution is the BEST fit for the company’s requirements?

    - 12. 
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

    - 13. 
    A Development team wants to run their container workloads on Amazon ECS. Each application container needs to share data with another container to collect logs and metrics.
    What should the Development team do to meet these requirements?

    - 14. 
    A company is deploying a microservices application on AWS Fargate using Amazon ECS. The application has environment variables that must be passed to a container for the application to initialize.
    How should the environment variables be passed to the container?

    - 15. 
    A company runs many microservices applications that use Docker containers. The company are planning to migrate the containers to Amazon ECS. The workloads are highly variable and therefore the company prefers to be charged per running task.
    Which solution is the BEST fit for the company’s requirements?

    - 16. 
    A Development team are developing a micro-services application that will use Docker containers on Amazon ECS. There will be 6 distinct services included in the architecture. Each service requires specific permissions to various AWS services.
    What is the MOST secure way to grant the services the necessary permissions?

    - 17. 
    A Developer has created a task definition that includes the following JSON code:
    "placementConstraints": [
        {
        "expression": "attribute:ecs.instance-type =~ t2.*",
        "type": "memberOf"
        }
    ]
    What will be the effect for tasks using this task definition?

    - 18. 
    A Developer is migrating Docker containers to Amazon ECS. A large number of containers will be deployed onto an existing ECS cluster that uses container instances of different instance types.
    Which task placement strategy can be used to minimize the number of container instances used based on available memory?

    - 19. 
    A developer is building a Docker application on Amazon ECS that will use an Application Load Balancer (ALB). The developer needs to configure the port mapping between the host port and container port. Where is this setting configured?

    - 20. 
    A developer has created a Docker image and uploaded it to an Amazon Elastic Container Registry (ECR) repository. How can the developer pull the image to his workstation using the docker client?

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
    Configure an ECS task IAM role for the application to use.
        - Instance Profile vs Task Execution Role vs Task Role
        - The IAM role (Task Role) lives in IAM and is referenced by the ECS Task Definition

    - 2. 
    Use EC2 instance profiles
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=321)

    - 3. 
    Run the output of the following: aws ecr get-login-password, and then run: docker pull REPOSITORY URI : TAG
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=348)

    - 4. 
    Use a task placement constraint
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=346)

    - 5. 
    Task Placement Constraint
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=340)

    - 6. 
    They will be placed on container instances in the “databases” task group
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=346)

    - 7. 
    random
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=343)

    - 8. 
    Rolling with additional batch
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=365)

    - 9. 
    Add a listener to the ALB. Update the AppSpec file to link the Lambda function to the BeforeAllowTraffic lifecycle hook.
    https://docs.aws.amazon.com/codedeploy/latest/userguide/reference-appspec-file.html

    - 10. 
    binpack
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=)

    - 11. 
    Amazon ECS with the Fargate launch type
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=)

    - 12. 
    It distributes tasks evenly across Availability Zones and then distributes tasks evenly across the instances within each Availability Zone
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=)

    - 13. 
    Create one task definition. Specify both containers in the definition. Mount a shared volume between those two containers
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=339)

    - 14. 
    Use advanced container definition parameters and define environment variables under the environment parameter within the task definition.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=516)

    - 15. 
    Amazon ECS with the Fargate launch type

    - 16. 
    Create six separate IAM roles, each containing the required permissions for the associated ECS service, then configure each ECS task definition to reference the associated IAM role

    - 17. 
    They will be placed only on container instances using the T2 instance type

    - 18. 
    binpack

    - 19. 
    Task definition

    - 20. 
    Run aws ecr get-login-password use the output to login in then issue a docker pull command specifying the image name using registry/repository[:tag]

    - 21. 
    - 22. 
    - 23. 
    - 24. 
    - 25. 
    - 26. 
    - 27. 
    - 28. 
    - 29. 


# Section 17: AWS Elastic Beanstalk ---> [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=354)
    ============================================================================================================================================================
- ### Questions:
    - 1. A Developer has completed some code updates and needs to deploy the updates to an Amazon Elastic Beanstalk environment. The environment includes twelve Amazon EC2 instances and there can be no reduction in application performance and availability during the update.
    Which deployment policy is the most cost-effective choice to suit these requirements?

    - 2. 
    A developer is planning the deployment of a new version of an application to AWS Elastic Beanstalk. The new version of the application should be deployed only to new EC2 instances.
    Which deployment methods will meet these requirements? (Select TWO.)
    
    - 3. 
    A Developer has completed some code updates and needs to deploy the updates to an Amazon Elastic Beanstalk environment. Due to the criticality of the application, the ability to quickly roll back must be prioritized of any other considerations.
    Which deployment policy should the Developer choose?

    - 4. 
    A Developer needs to configure an Elastic Load Balancer that is deployed through AWS Elastic Beanstalk. Where should the Developer place the load-balancer.config file in the application source bundle?

    - 5. 
    A media company uses Amazon EC2 instances managed by AWS Elastic Beanstalk to run its high-traffic website. The engineering team needs to introduce a new feature, which requires upgrading the underlying platform to a newer version of Node.js. The deployment of the new code and the platform upgrade need to happen without causing any downtime.
    Which strategy should the team adopt to fulfill these requirements?

    - 6. 
    An application on-premises uses Linux servers and a relational database using PostgreSQL. The company will be migrating the application to AWS and require a managed service that will take care of capacity provisioning, load balancing, and auto-scaling.
    Which combination of services should the Developer use? (Select TWO.)

    - 7. 
    A Developer is creating a new web application that will be deployed using AWS Elastic Beanstalk from the AWS Management Console. The Developer is about to create a source bundle which will be uploaded using the console.
    Which of the following are valid requirements for creating the source bundle? (Select TWO.)

    - 8. 
    A company has a website that is developed in PHP and WordPress and is launched using AWS Elastic Beanstalk. There is a new version of the website that needs to be deployed in the Elastic Beanstalk environment. The company cannot tolerate having the website offline if an update fails. Deployments must have minimal impact and rollback as soon as possible.
    What deployment method should be used?

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
    Rolling with additional batch
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=365)

    - 2. 
    Immutable
    Blue/green
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=366)

    - 3. 
    Immutable
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=366)

    - 4. 
    In the .ebextensions folder
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=373)

    - 5. 
    Implement Blue/Green (CNAME Swap) deployment using Elastic Beanstalk. Prepare a separate environment with the new version of Node.js and the new code, and once testing is complete, swap the CNAMEs of the two environments.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=378)

    - 6. 
    Amazon RDS with PostrgreSQL
    AWS Elastic Beanstalk
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=357)

    - 7. 
    Must not include a parent folder or top-level directory.
    Must not exceed 512 MB.

    - 8. 
    Immutable

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


# Section 18: AWS CloudFormation ---> [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=379)
    ============================================================================================================================================================
- ### Questions:
    - 1. 
    To include objects defined by the AWS Serverless Application Model (SAM) in an AWS CloudFormation template, in addition to Resources, what section MUST be included in the document root?

    - 2. 
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

    - 3. 
    How can a Developer view a summary of proposed changes to an AWS CloudFormation stack without implementing the changes in production?

    - 4. 
    A business operates a web app on Amazon EC2 instances utilizing a bespoke Amazon Machine Image (AMI). They employ AWS CloudFormation for deploying their app, which is currently active in the us-east-1 Region. However, their goal is to extend the deployment to the us-west-1 Region.
    During an initial attempt to create an AWS CloudFormation stack in us-west-1, the action fails, and an error message indicates that the AMI ID does not exist. A developer is tasked with addressing this error through a method that minimizes operational complexity.
    Which action should the developer take?

    - 5. 
    - 6. 
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
    Transform
    https://digitalcloud.training/aws-sam/

    - 2. 


    - 3. 
    Create a Change Set
    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.html

    - 4. 
    Copy the AMI from the us-east-1 Region to the us-west-1 Region and use the new AMI ID in the CloudFormation template. Dont have to rebuild AMI this way.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=379)

    - 5. 
    - 6. 
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
    An application collects data from sensors in a manufacturing facility. The data is stored in an Amazon SQS Standard queue by an AWS Lambda function and an Amazon EC2 instance processes the data and stores it in an Amazon RedShift data warehouse. A fault in the sensors’ software is causing occasional duplicate messages to be sent. Timestamps on the duplicate messages show they are generated within a few seconds of the primary message.
    How can a Developer prevent duplicate data being stored in the data warehouse?

    - 23. 
    An application will ingest data at a very high throughput from several sources and stored in an Amazon S3 bucket for subsequent analysis. Which AWS service should a Developer choose for this requirement?

    - 24. 
    A solution requires a serverless service for receiving streaming data and loading it directly into an Amazon Elasticsearch datastore. Which AWS service would be suitable for this requirement?

    - 25. 
    A developer is creating a multi-tier web application. The front-end will place messages in an Amazon SQS queue for the back-end to process. Each job includes a file that is 1GB in size. What MUST the developer do to ensure this works as expected?

    - 26. 
    A mobile application runs as a serverless application on AWS. A Developer needs to create a push notification feature that sends periodic message to subscribers. How can the Developer send the notification from the application?

    - 27. 
    A monitoring application that keeps track of a large eCommerce website uses Amazon Kinesis for data ingestion. During periods of peak data rates, the producers are not making best use of the available shards.
    What step will allow the producers to better utilize the available shards and increase write throughput to the Kinesis data stream? 

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
    Use a FIFO queue and configure the Lambda function to add a message deduplication token to the message body

    - 23. 
    Amazon Kinesis Data Firehose

    - 24. 
    Amazon Kinesis Data Firehose

    - 25. 
    Store the large files in Amazon S3 and use the SQS Extended Client Library for Java to manage SQS messages

    - 26. 
    Publish a notification to an Amazon SNS Topic

    - 27. 
    Install the Kinesis Producer Library (KPL) for ingesting data into the stream

    - 28. 
    - 29. 

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
    A critical application runs on an Amazon EC2 instance. A Developer has configured a custom Amazon CloudWatch metric that monitors application availability with a data granularity of 1 second. The Developer must be notified within 30 seconds if the application experiences any issues.
    What should the Developer do to meet this requirement?

    - 19. 
    A Developer has recently created an application that uses an AWS Lambda function, an Amazon DynamoDB table, and also sends notifications using Amazon SNS. The application is not working as expected and the Developer needs to analyze what is happening across all components of the application.
    What is the BEST way to analyze the issue?

    - 20. 
    A Development team manage a hybrid cloud environment. They would like to collect system-level metrics from on-premises servers and Amazon EC2 instances. How can the Development team collect this information MOST efficiently?

    - 21. 
    A Development team wants to instrument their code to provide more detailed information to AWS X-Ray than simple outgoing and incoming requests. This will generate large amounts of data, so the Development team wants to implement indexing so they can filter the data.
    What should the Development team do to achieve this?

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
    Configure a high-resolution CloudWatch alarm and use Amazon SNS to send the alert.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=)

    - 19. 
    Enable X-Ray tracing for the Lambda function
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=)

    - 20. 
    Install the CloudWatch agent on the on-premises servers and EC2 instances

    - 21. 
    Add annotations to the segment document

    - 22. 
    - 23. 
    - 24. 
    - 25. 
    - 26. 
    - 27. 
    - 28. 
    - 29. 

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
    A Developer is writing an imaging microservice on AWS Lambda. The service is dependent on several libraries that are not available in the Lambda runtime environment.
    Which strategy should the Developer follow to create the Lambda deployment package?

    - 26. 
    A developer has deployed an application on AWS Lambda. The application uses Python and must generate and then upload a file to an Amazon S3 bucket. The developer must implement the upload functionality with the least possible change to the application code.
    Which solution BEST meets these requirements?

    - 27. 
    A serverless application uses an AWS Lambda function to process Amazon S3 events. The Lambda function executes 20 times per second and takes 20 seconds to complete each execution.
    How many concurrent executions will the Lambda function require?

    - 28. 
    A company has an application that logs all information to Amazon S3. Whenever there is a new log file, an AWS Lambda function is invoked to process the log files. The code works, gathering all of the necessary information. However, when checking the Lambda function logs, duplicate entries with the same request ID are found.
    What is the BEST explanation for the duplicate entries?

    - 29. 
    The Lambda function needs to write this data to an Amazon DynamoDB table. After deploying the function, the developer notices that the write operations to the DynamoDB table occasionally fail due to throttling.
    What should the developer do to reduce the likelihood of these throttling issues without significantly over-provisioning the DynamoDB table's write capacity?

    - 30. 
    A Developer is creating multiple AWS Lambda functions that will be using an external library that is not included in the standard Lambda libraries. What is the BEST way to make these libraries available to the functions?

    - 31. 
    A Developer is creating an AWS Lambda function to process a stream of data from an Amazon Kinesis Data Stream. When the Lambda function parses the data and encounters a missing field, it exits the function with an error. The function is generating duplicate records from the Kinesis stream. When the Developer looks at the stream output without the Lambda function, there are no duplicate records.
    What is the reason for the duplicates?

    - 32. 
    A Developer created an AWS Lambda function and then attempted to add an on failure destination but received the following error:
    The function's execution role does not have permissions to call SendMessage on arn:aws:sqs:us-east-1:515148212435:FailureDestination
    How can the Developer resolve this issue MOST securely?

    - 33. 
    A serverless application uses an AWS Lambda function, Amazon API Gateway API and an Amazon DynamoDB table. The Lambda function executes 10 times per second and takes 3 seconds to complete each execution.
    How many concurrent executions will the Lambda function require?

    - 34. 
    An application will generate thumbnails from objects uploaded to an Amazon S3 bucket. The Developer has created the bucket configuration and the AWS Lambda function and has formulated the following AWS CLI command:
    aws lambda add-permission --function-name CreateThumbnail --principal s3.amazonaws.com --statement-id s3invoke --action "lambda:InvokeFunction" --source-arn arn:aws:s3:::digitalcloudbucket-source --source-account 523107438921
    What will be achieved by running the AWS CLI command?

    - 35. 
    A Developer wants the ability to roll back to a previous version of an AWS Lambda function in the event of errors caused by a new deployment.
    How can the Developer achieve this with MINIMAL impact on users?

    - 36. 
    An application resizes images that are uploaded to an Amazon S3 bucket. Amazon S3 event notifications are used to trigger an AWS Lambda function that resizes the images. The processing time for each image is less than one second. A large amount of images are expected to be received in a short burst of traffic. How will AWS Lambda accommodate the workload?

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
    Create a ZIP file with the source code and all dependent libraries.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=585)

    - 26. 
    Use the AWS SDK for Python that is installed in the Lambda execution environment
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=)

    - 27. 
    400
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=)

    - 28. 
    The Lambda function failed, and the Lambda service retried the invocation with a delay
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=)

    - 29. 
    Implement exponential backoff in the Lambda function's error handling code to retry failed write operations.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=)

    - 30. 
    Create a layer in Lambda that includes the external library

    - 31. 
    The Lambda function did not handle the error, and the Lambda service attempted to reprocess the data

    - 32. 
    Create a customer managed policy with all read/write permissions to SQS and attach the policy to the function’s execution role

    - 33. 
    30

    - 34. 
    The Amazon S3 service principal (s3.amazonaws.com) will be granted permissions to perform the lambda:InvokeFunction action

    - 35. 
    Change the application to use an alias that points to the current version. Deploy the new version of the code. Update the alias to direct 10% of users to the newly deployed version. If too many errors are encountered, send 100% of traffic to the previous version

    - 36. 
    Lambda will scale out and execute the requests concurrently
    
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
    An application uses an Amazon DynamoDB table that is 50 GB in size and provisioned with 10,000 read capacity units (RCUs) per second. The table must be scanned during non-peak hours when normal traffic consumes around 5,000 RCUs. The Developer must scan the whole table in the shortest possible time whilst ensuring the normal workload is not affected.
    How would the Developer optimize this scan cost-effectively?

    - 28. 
    A company has a large Amazon DynamoDB table which they scan periodically so they can analyze several attributes. The scans are consuming a lot of provisioned throughput. What technique can a Developer use to minimize the impact of the scan on the table's provisioned throughput?

    - 29. 
    A developer is responsible for a business critical application that uses Amazon DynamoDB as its main data repository. This DynamoDB table holds millions of records and handles high volumes of requests. The developer must implement near-real time processing on the records as soon as they are inserted or modified in the DynamoDB table.
    What's the most efficient way to introduce this capability with MINIMUM modification to the existing application code?

    - 30. 
    A serverless application uses Amazon API Gateway, AWS Lambda and DynamoDB. The application writes statistical data that is constantly received from sensors. The data is analyzed soon after it is written to the database and is then not required.
    What is the EASIEST method to remove stale data and optimize database size?

    - 31. 
    A company is building an application to track athlete performance using an Amazon DynamoDB table. Each item in the table is identified by a partition key (user_id) and a sort key (sport_name). The table design is shown below:
    • Partition key: user_id
    • Sort Key: sport_name
    • Attributes: score, score_datetime
    A Developer is asked to write a leaderboard application to display the top performers (user_id) based on the score for each sport_name.
    What process will allow the Developer to extract results MOST efficiently from the DynamoDB table?

    - 32. 
    A Developer is creating an application that will utilize an Amazon DynamoDB table for storing session data. The data being stored is expected to be around 4.5KB in size and the application will make 20 eventually consistent reads/sec, and 12 standard writes/sec.
    How many RCUs/WCUs are required?

    - 33. 
    A nightly batch job loads 1 million new records in to a DynamoDB table. The records are only needed for one hour, and the table needs to be empty by the next night’s batch job.
    Which is the MOST efficient and cost-effective method to provide an empty table?

    - 34. 
    A Developer is creating a social networking app for games that uses a single Amazon DynamoDB table. All users’ saved game data is stored in the single table, but users should not be able to view each other’s data.
    How can the Developer restrict user access so they can only view their own data?

    - 35. 
    A Development team are creating a financial trading application. The application requires sub-millisecond latency for processing trading requests. Amazon DynamoDB is used to store the trading data. During load testing the Development team found that in periods of high utilization the latency is too high and read capacity must be significantly over-provisioned to avoid throttling.
    How can the Developers meet the latency requirements of the application?

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
    600 Read Capacity Units
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
    Use the Parallel Scan API operation and limit the rate.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=)

    - 28. 
    Set a smaller page size for the scan
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=621)

    - 29. 
    Use AWS Lambda triggered by DynamoDB Streams to process the documents.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=)

    - 30. 
    Enable the TTL attribute and add expiry timestamps to items

    - 31. 
    Create a global secondary index with a partition key of sport_name and a sort key of score, and get the results

    - 32. 
    20 RCU and 60 WCU

    - 33. 
    Create and then delete the table after the task has completed

    - 34. 
    Restrict access to specific items based on certain primary key values

    - 35. 
    Use Amazon DynamoDB Accelerator (DAX) to cache the data

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

# Section 23: AWS Serverless: API Gateway ---> [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=656)
- ### Questions:
    - 1. 
    A company is releasing an updated version of its APIs for its new mobile application, which uses Amazon API Gateway. The developers aim to gradually and seamlessly roll out the new version of APIs.
    What is the MOST straightforward method for them to introduce the new API version to a subset of users through API Gateway?

    - 2. 
    A customer requires a schema-less, key/value database that can be used for storing customer orders. Which type of AWS database is BEST suited to this requirement?

    - 3. 
    An Amazon API Gateway API developer aims to integrate request validation in a production setting but wants to test it before deployment. Which of the following methods offers the least operational overhead for testing via a tool by sending test requests?

    - 4. 
    A Development team are creating a new REST API that uses Amazon API Gateway and AWS Lambda. To support testing there need to be different versions of the service. What is the BEST way to provide multiple versions of the REST API?

    - 5. 
    A legacy service has an XML-based SOAP interface. The Developer wants to expose the functionality of the service to external clients with the Amazon API Gateway. Which technique will accomplish this?

    - 6. 
    A company wants to implement authentication for its new REST service using Amazon API Gateway. To authenticate the calls, each request must include HTTP headers with a client ID and user ID. These credentials must be compared to authentication data in an Amazon DynamoDB table.
    What MUST the company do to implement this authentication in API Gateway?

    - 7. 
    A company is creating a REST service using an Amazon API Gateway with AWS Lambda integration. The service must run different versions for testing purposes.
    What would be the BEST way to accomplish this?

    - 8. 
    A set of APIs are exposed to customers using Amazon API Gateway. These APIs have caching enabled on the API Gateway. Customers have asked for an option to invalidate this cache for each of the APIs.
    What action can be taken to allow API customers to invalidate the API Cache?

    - 9. 
    A company is providing APIs as a web-based service to allow anonymous access to daily updated statistical data, using Amazon API Gateway and AWS Lambda for API development. The service's popularity has grown, and the company aims to improve the API responsiveness.
    What measure should the company undertake to fulfill this objective?

    - 10. 
    A Developer has deployed an AWS Lambda function and an Amazon DynamoDB table. The function code returns data from the DynamoDB table when it receives a request. The Developer needs to implement a front end that can receive HTTP GET requests and proxy the request information to the Lambda function.
    What is the SIMPLEST and most COST-EFFECTIVE solution?

    - 11. 
    A software organization has developed a new feature in its serverless application hosted on AWS. This feature involves an AWS Lambda function that gets invoked by an Amazon API Gateway API. Currently, the API uses a specific Lambda alias to invoke the Lambda function. The organization wants to roll out this new feature to a select group of users for beta testing without affecting the application's existing users.
    What would be the most efficient approach to meet these requirements?

    - 12. 
    An online multiplayer game employs Amazon API Gateway WebSocket APIs with an HTTP backend. The game developer needs to add a feature that identifies players with unstable connections who repeatedly join and leave the game. The developer also wants the ability to disconnect such players from the game.
    What two modifications should the developer implement in the game to fulfill these requirements? (Select TWO.)

    - 13. 
    A company runs a legacy application that uses an XML-based SOAP interface. The company needs to expose the functionality of the service to external customers and plans to use Amazon API Gateway.
    How can a Developer configure the integration?

    - 14. 
    A company has created a set of APIs using Amazon API Gateway and exposed them to partner companies. The APIs have caching enabled for all stages. The partners require a method of invalidating the cache that they can build into their applications.
    What can the partners use to invalidate the API cache?

    - 15. 
    A startup is developing a prototype for a news aggregator application. This application will display the latest news for a specific industry and provide a RESTful API endpoint that clients can invoke. Where feasible, the application should leverage AWS's caching features to reduce the load on the backend service. The backend of the application is expected to handle a modest amount of traffic, primarily during testing periods.
    Which method would be the most cost-effective for the developer to implement this REST endpoint?

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
    - 1. Utilize the canary release deployment feature in API Gateway. Configure the canarySettings to redirect a portion of the API traffic.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=667)

    - 2. Amazon DynamoDB
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=607)

    - 3. 
    Modify the existing API to include request validation, deploy this to a new API Gateway stage, test it, then deploy it to the production stage.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=666)

    - 4. 
    Deploy the API versions as unique stages with unique endpoints and use stage variables to provide further context
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=666)

    - 5. 
    Create a RESTful API with the API Gateway; transform the incoming JSON into a valid XML message for the SOAP interface using mapping templates
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=672)

    - 6. 
    Implement an AWS Lambda authorizer that references the DynamoDB authentication table
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=690)

    - 7. 
    Deploy the API version as unique stages with unique endpoints and use stage variables to provide further context
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=663)

    - 8. 
    Ask customers to pass an HTTP header called Cache-Control:max-age=0
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=678)

    - 9. 
    Activate caching in API Gateway.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=667)

    - 10. 
    Implement an API Gateway API with Lambda proxy integration
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=669)

    - 11. 
    Create a new version of the Lambda function. Build a new stage on API Gateway integrated with this new Lambda version. Utilize this new API Gateway stage for beta testing.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=666)

    - 12. 
    Implement $connect and $disconnect routes in the backend service.
    Add logic to track the player's connection status using Amazon DynamoDB in the backend service.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=698)
    https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-route-keys-connect-disconnect.html

    - 13. 
    Create a RESTful API using Amazon API Gateway. Transform the incoming JSON into a valid XML message for the SOAP interface using mapping templates.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=672)

    - 14. 
    They can pass the HTTP header Cache-Control: max-age=0
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=678)

    - 15. 
    Utilize AWS API Gateway with an AWS Lambda function as the backend and enable caching in API Gateway.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=)

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

# Section 24: AWS CICD: CodeCommit, CodePipeline, CodeBuild, CodeDeploy ---> [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=700)
    ============================================================================================================================================================
- ### Questions:
    - 1. 
    A team of Developers are building a continuous integration and delivery pipeline using AWS Developer Tools. Which services should they use for running tests against source code and installing compiled code on their AWS resources? (Select TWO.)

    - 2. 
    An engineer wishes to share a software project they've developed with their team members for review. The shared application code needs to be preserved over time, with multiple versions and batch modifications being tracked. What is the most appropriate AWS service for this purpose?

    - 3. 
    A developer must deploy an update to Amazon ECS using AWS CodeDeploy. The deployment should expose 10% of live traffic to the new version. Then after a period of time, route all remaining traffic to the new version.
    Which ECS deployment should the company use to meet these requirements?

    - 4. 
    A company needs a version control system for collaborative software development. The solution must include support for batches of changes across multiple files and parallel branching.
    Which AWS service will meet these requirements?

    - 5. 
    A developer is creating a microservices application that includes and AWS Lambda function. The function generates a unique file for each execution and must commit the file to an AWS CodeCommit repository.
    How should the developer accomplish this?

    - 6. 
    A company uses continuous integration and continuous delivery (CI/CD) systems. A Developer needs to automate the deployment of a software package to Amazon EC2 instances as well as to on-premises virtual servers.
    Which AWS service can be used for the software deployment?

    - 7. 
    A firm intends to utilize AWS CodeDeploy to deploy an application to Amazon Elastic Container Service (Amazon ECS). While deploying an updated version of the application, the company's initial requirement is to direct 10% of active traffic to the updated application version. Following a 15-minute interval, all remaining active traffic must be rerouted to the updated application.
    Which predefined CodeDeploy configuration aligns with these needs?

    - 8. 
    A Development team is creating a microservices application running on Amazon ECS. The release process workflow of the application requires a manual approval step before the code is deployed into the production environment.
    What is the BEST way to achieve this using AWS CodePipeline?

    - 9. 
    A team of Developers have been assigned to a new project. The team will be collaborating on the development and delivery of a new application and need a centralized private repository for managing source code. The repository should support updates from multiple sources. Which AWS service should the development team use?

    - 10. 
    A Developer is deploying an update to a serverless application that includes AWS Lambda using the AWS Serverless Application Model (SAM). The traffic needs to move from the old Lambda version to the new Lambda version gradually, within the shortest period of time.
    Which deployment configuration is MOST suitable for these requirements?

    - 11. 
    A Developer has joined a team and needs to connect to the AWS CodeCommit repository using SSH. What should the Developer do to configure access using Git?

    - 12. 
    A company needs a fully-managed source control service that will work in AWS. The service must ensure that revision control synchronizes multiple distributed repositories by exchanging sets of changes peer-to-peer. All users need to work productively even when not connected to a network.
    Which source control service should be used?

    - 13. 
    A development team require a fully-managed source control service that is compatible with Git.
    Which service should they use?

    - 14. 
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

    - 15. 
    A Development team have moved their continuous integration and delivery (CI/CD) pipeline into the AWS Cloud. The team is leveraging AWS CodeCommit for management of source code. The team need to compile their source code, run tests, and produce software packages that are ready for deployment.
    Which AWS service can deliver these outcomes?

    - 16. 
    A Developer is deploying an Amazon ECS update using AWS CodeDeploy. In the appspec.yaml file, which of the following is a valid structure for the order of hooks that should be specified?

    - 17. 
    A Developer is deploying an AWS Lambda update using AWS CodeDeploy. In the appspec.yaml file, which of the following is a valid structure for the order of hooks that should be specified?

    - 18. 
    A company has implemented AWS CodePipeline to automate its release pipelines. The Development team is writing an AWS Lambda function that will send notifications for state changes of each of the actions in the stages.
    Which steps must be taken to associate the Lambda function with the event source?

    - 19. 
    A developer is using AWS CodeBuild to build an application into a Docker image. The buildspec file is used to run the application build. The developer needs to push the Docker image to an Amazon ECR repository only upon the successful completion of each build.

    - 20. 
    A Development team would use a GitHub repository and would like to migrate their application code to AWS CodeCommit.
    What needs to be created before they can migrate a cloned repository to CodeCommit over HTTPS?

    - 21. 
    A Developer has used a third-party tool to build, bundle, and package a software package on-premises. The software package is stored in a local file system and must be deployed to Amazon EC2 instances.
    How can the application be deployed onto the EC2 instances?

    - 22. 
    A Developer is setting up a code update to Amazon ECS using AWS CodeDeploy. The Developer needs to complete the code update quickly. Which of the following deployment types should the Developer use?

    - 23. 
    A serverless application composed of multiple Lambda functions has been deployed. A developer is setting up AWS CodeDeploy to manage the deployment of code updates. The developer would like a 10% of the traffic to be shifted to the new version in equal increments, 10 minutes apart.
    Which setting should be chosen for configuring how traffic is shifted?

    - 24. 
    A Developer needs to update an Amazon ECS application that was deployed using AWS CodeDeploy. What file does the Developer need to update to push the change through CodeDeploy?

    - 25. 
    A Developer is deploying an Amazon EC2 update using AWS CodeDeploy. In the appspec.yml file, which of the following is a valid structure for the order of hooks that should be specified?

    - 26. 
    A Developer is creating an AWS Lambda function that will process medical images. The function is dependent on several libraries that are not available in the Lambda runtime environment. Which strategy should be used to create the Lambda deployment package?

    - 27. 
    - 28. 
    - 29. 


    ### Answers:
    - 1. 
    AWS CodeBuild for running tests against source code
    AWS CodeDeploy for installing compiled code on their AWS resources
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=709)

    - 2. 
    AWS CodeCommit
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=706)

    - 3. 
    Blue/green with canary
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=724)

    - 4. 
    AWS CodeCommit
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=706)

    - 5. 
    Use an AWS SDK to instantiate a CodeCommit client. Invoke the PutFile method to add the file to the repository and execute a commit with CreateCommit.
    https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/codecommit/AWSCodeCommitClient.html

    - 6. 
    AWS CodeDeploy
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=718)

    - 7. 
    CodeDeployDefault.ECSCanary10Percent15Minutes
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=724)

    - 8. 
    Use an approval action in a stage before deployment
    https://docs.aws.amazon.com/codepipeline/latest/userguide/approvals.html

    - 9. 
    AWS CodeCommit
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=706)

    - 10. 
    CodeDeployDefault.LambdaCanary10Percent5Minutes
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=)

    - 11. 
    Generate an SSH public and private key. Upload the public key to the Developer’s IAM account
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=707)

    - 12. 
    AWS CodeCommit
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=705)

    - 13. 
    AWS CodeCommit
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=705)

    - 14. 
    “codecommit:CreateBranch” and “codecommit:DeleteBranch”
    https://docs.aws.amazon.com/cli/latest/reference/codecommit/index.html#cli-aws-codecommit

    - 15. 
    AWS CodeBuild
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=713)

    - 16. 
    BeforeInstall > AfterInstall > AfterAllowTestTraffic > BeforeAllowTraffic > AfterAllowTraffic
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=718)
    https://docs.aws.amazon.com/codedeploy/latest/userguide/reference-appspec-file-structure-hooks.html

    - 17. 
    BeforeAllowTraffic > AfterAllowTraffic
    https://docs.aws.amazon.com/codedeploy/latest/userguide/reference-appspec-file-structure-hooks.html

    - 18. 
    Create an Amazon CloudWatch Events rule that uses CodePipeline as an event source
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=712)

    - 19. 
    Add a post_build phase to the buildspec file that uses the commands block to push the Docker image.
    https://docs.aws.amazon.com/codebuild/latest/userguide/sample-docker.html
    https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html

    - 20. 
    A set of Git credentials generated with IAM
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=707)

    - 21. 
    Upload the bundle to an Amazon S3 bucket and specify the S3 location when doing a deployment using AWS CodeDeploy.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=)

    - 22. 
    Blue/green

    - 23. 
    Linear

    - 24. 
    appspec.yml

    - 25. 
    BeforeInstall > AfterInstall > ApplicationStart > ValidateService

    - 26. 
    Create a ZIP file with the source code and all dependent libraries

    - 27. 
    - 28. 
    - 29. 

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
    A Developer is creating a script to automate the deployment process for a serverless application. The Developer wants to use an existing AWS Serverless Application Model (SAM) template for the application.
    What should the Developer use for the project? (Select TWO.)

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
    Call sam package to create the deployment package. Call sam deploy to deploy the package afterward.
    Call aws cloudformation package to create the deployment package. Call aws cloudformation deploy to deploy the package afterward.

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

# Section 26: Cloud Development Kit (CDK) ---> [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=744)
    ============================================================================================================================================================
- ### Questions:
    - 1. 
    - 2. 
    - 3. 
    - 4. 
    - 5. 
    - 6. 
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
    - 2. 
    - 3. 
    - 4. 
    - 5. 
    - 6. 
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

# Section 27: Cognito: Cognito User Pools, Cognito Identity Pools & Cognito Sync ---> [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=757)
    ============================================================================================================================================================
- ### Questions:
    - 1. 
    A company is creating an application that will require users to access AWS services and allow them to reset their own passwords. Which of the following would allow the company to manage users and authorization while allowing users to reset their own passwords?

    - 2. 
    A Developer has created an Amazon Cognito user pool and configured a domain for it. The Developer wants to add sign-up and sign-in pages to an app with a company logo.
    What should the Developer do to meet these requirements?

    - 3. 
    An application developer is crafting a new software product. To streamline the registration process, they want new users to be able to set up their accounts using their existing social media profiles.
    Which AWS service or feature would be the most appropriate for achieving this goal?

    - 4. 
    A development team are creating a mobile application that customers will use to receive notifications and special offers. Users will not be required to log in.
    What is the MOST efficient method to grant users access to AWS resources?

    - 5. 
    A mobile application has hundreds of users. Each user may use multiple devices to access the application. The Developer wants to assign unique identifiers to these users regardless of the device they use.
    Which of the following methods should be used to obtain unique identifiers?

    - 6. 
    A Developer is writing a web application that allows users to view images from an Amazon S3 bucket. The users will log in with their Amazon login, as well as Facebook and/or Google accounts.
    How can the Developer provide this authentication capability?

    - 7. 
    A Developer is creating a banking application that will be used to view financial transactions and statistics. The application requires multi-factor authentication to be added to the login protocol.
    Which service should be used to meet this requirement?
     
    - 8. 
    A Developer is creating a web application that will be used by employees working from home. The company uses a SAML directory on-premises for storing user information. The Developer must integrate with the SAML directory and authorize each employee to access only their own data when using the application.
    Which approach should the Developer take?

    - 9. 
    A mobile application has thousands of users. Each user may use multiple devices to access the application. The Developer wants to assign unique identifiers to these users regardless of the device they use.
    Which of the below is the BEST method to obtain unique identifiers?

    - 10. 
    A website delivers images stored in an Amazon S3 bucket. The site uses Amazon Cognito-enabled and guest users without logins need to be able to view the images from the S3 bucket..
    How can a Developer enable access for guest users to the AWS resources?

    - 11. 
    A developer is designing a web application that will be used by thousands of users. The users will sign up using their email addresses and the application will store attributes for each user.
    Which service should the developer use to enable users to sign-up for the web application?

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
    Amazon Cognito user pools and identity pools
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=757)

    - 2. 
    Customize the Amazon Cognito hosted web UI and add the company logo.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=779)

    - 3. 
    Amazon Cognito User Pools
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=759)

    - 4. 
    Use Amazon Cognito to associate unauthenticated users with an IAM role that has limited access to resources
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=775)

    - 5. 
    Implement developer-authenticated identities by using Amazon Cognito, and get credentials for these identities
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=775)

    - 6. 
    Use Amazon Cognito with web identity federation
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=772)

    - 7. 
    Amazon Cognito User Pool with MFA
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=759)
    
    - 8. 
    Use an Amazon Cognito identity pool, federate with the SAML provider, and use a trust policy with an IAM condition key to limit employee access.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=)

    - 9. 
    Implement developer-authenticated identities by using Amazon Cognito and get credentials for these identities

    - 10. 
    Create a new identity pool, enable access to unauthenticated identities, and grant access to AWS resources

    - 11. 
    Amazon Cognito user pool

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


# Section 28: Other Serverless: Step Functions & AppSync ---> [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=781)
    ============================================================================================================================================================
- ### Questions:
    - 1. 
    A company wants a serverless solution for phased release of static websites hosted on various version control systems. Deployments should be triggered by Git branch merges and all data exchange should be over HTTPS.
    Which option offers the LOWEST operational overhead?

    - 2. 
    A company currently runs a number of legacy automated batch processes for system update management and operational activities. The company are looking to refactor these processes and require a service that can coordinate multiple AWS services into serverless workflows.
    What is the MOST suitable service for this requirement?

    - 3. 
    An IT automation architecture uses many AWS Lambda functions invoking one another as a large state machine. The coordination of this state machine is legacy custom code that breaks easily.
    Which AWS Service can help refactor and manage the state machine?

    - 4. 
    A customer requires a serverless application with an API which mobile clients will use. The API will have both and AWS Lambda function and an Amazon DynamoDB table as data sources. Responses that are sent to the mobile clients must contain data that is aggregated from both of these data sources.
    The developer must minimize the number of API endpoints and must minimize the number of API calls that are required to retrieve the necessary data.
    Which solution should the developer use to meet these requirements?

    - 5. 
    A company is using an AWS Step Functions state machine. When testing the state machine errors were experienced in the Step Functions task state machine. To troubleshoot the issue a developer requires that the state input be included along with the error message in the state output.
    Which coding practice can preserve both the original input and the error for the state?

    - 6. 
    A legacy application is being refactored into a microservices architecture running on AWS. The microservice will include several AWS Lambda functions. A Developer will use AWS Step Functions to coordinate function execution.
    How should the Developer proceed?

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
    Use AWS Amplify for hosting, connect corresponding repository branches, and initiate deployments by merging changes to the needed branch.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=800)
    
    - 2. 
    AWS Step Functions
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=782)

    - 3. 
    AWS Step Functions
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=782)

    - 4. 
    GraphQL API on AWS AppSync
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=795)

    - 5. 
    Use ResultPath in a Catch statement to include the original input with the error.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=789)

    - 6. 
    Create a state machine using the Amazon States Language

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

# Section 29: Advanced Identity ---> [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=804)
    ============================================================================================================================================================
- ### Questions:
    - 1. 
    An application running on a fleet of EC2 instances use the AWS SDK for Java to copy files into several AWS buckets using access keys stored in environment variables. A Developer has modified the instances to use an assumed IAM role with a more restrictive policy that allows access to only one bucket.
    However, after applying the change the Developer logs into one of the instances and is still able to write to all buckets. What is the MOST likely explanation for this situation?

    - 2. 
    A Developer received the following error when attempting to launch an Amazon EC2 instance using the AWS CLI.
        An error occurred (UnauthorizedOperation) when calling the RunInstances operation: You are not authorized to perform this operation. Encoded authorization failure message: VNVaHFdCohROkbyT_rIXoRyNTp7vXFJCqnGiwPuyKnsSVf-WSSGK_06H3vKnrkUa3qx5D40hqj9HEG8kznr04Acmi6lvc8m51tfqtsomFSDylK15x96ZrxMW7MjDJLrMkM0BasPvy8ixo1wi6X2b0C-J1ThyWU9IcrGd7WbaRDOiGbBhJtKs1z01WSn2rVa5_7sr5PwEK-ARrC9y5Pl54pmeF6wh7QhSv2pFO0y39WVBajL2GmByFmQ4p8s-6Lcgxy23b4NJdJwWOF4QGxK9HcKof1VTVZ2oIpsI-dH6_0t2DI0BTwaIgmaT7ldontI1p7OGz-3wPgXm67x2NVNgaK63zPxjYNbpl32QuXLKUKNlB9DdkSdoLvsuFIvf-lQOXLPHnZKCWMqrkI87eqKHYpYKyV5c11TIZTAJ3MntTGO_TJ4U9ySYvTzU2LgswYOtKF_O76-13fryGG5dhgOW5NxwCWBj6WT2NSJvqOeLykAFjR_ET4lM6Dl1XYfQITWCqIzlvlQdLmHJ1jqjp4gW56VcQCdqozLv2UAg8IdrZIXd0OJ047RQcvvN1IyZN0ElL7dR6RzAAQrftoKMRhZQng6THZs8PZM6wep6-yInzwfg8J5_FW6G_PwYqO-4VunVtJSTzM_F_8kojGlRmzqy7eCk5or__bIisUoslw
    What action should the Developer perform to make this error more human-readable?

    - 3. 
    A developer has a user account in the Development AWS account. He has been asked to modify resources in a Production AWS account. What is the MOST secure way to provide temporary access to the developer?

    - 4. 
    - 5. 
    - 6. 
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
    The AWS credential provider looks for instance profile credentials last
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=812)

    - 2. 
    Use the AWS STS decode-authorization-message API to decode the message
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=805)

    - 3.   
    Create a cross-account access role, and use sts:AssumeRole API to get short-lived credentials
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=805)

    - 4. 
    - 5. 
    - 6. 
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

# Section 30: AWS Security & Encryption: KMS, Encryption SDK, SSM Parameter Store, IAM & STS ---> [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=826)
    ============================================================================================================================================================
- ### Questions:
    - 1. 
    An application runs on a fleet of Amazon EC2 instances and stores data in a Microsoft SQL Server database hosted on Amazon RDS. The developer wants to avoid storing database connection credentials the application code. The developer would also like a solution that automatically rotates the credentials.
    What is the MOST secure way to store and access the database credentials?

    - 2. 
    An application that processes financial transactions receives thousands of transactions each second. The transactions require end-to-end encryption, and the application implements this by using the AWS KMS GenerateDataKey operation. During operation the application receives the following error message:
    “You have exceeded the rate at which you may call KMS. Reduce the frequency of your calls.
    (Service: AWSKMS; Status Code: 400; Error Code: ThrottlingException; Request ID: <ID>”
    Which actions are best practices to resolve this error? (Select TWO.)

    - 3. 
    A Developer is storing sensitive documents in Amazon S3. The documents must be encrypted at rest and company policy mandates that the encryption keys must be rotated annually. What is the EASIEST way to achieve this?

    - 4. 
    An application will use AWS Lambda and an Amazon RDS database. The Developer needs to secure the database connection string and enable automatic rotation every 30 days. What is the SIMPLEST way to achieve this requirement?

    - 5. 
    An application is running on a cluster of Amazon EC2 instances. The application has received an error when trying to read objects stored within an Amazon S3 bucket. The bucket is encrypted with server-side encryption and AWS KMS managed keys (SSE-KMS). The error is as follows:
    Service: AWSKMS; Status Code: 400, Error Code: ThrottlingException
    Which combination of steps should be taken to prevent this failure? (Select TWO.)

    - 6. 
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

    - 7. 
    An organization is developing a data processing application that is hosted on AWS Lambda and utilizes a PostgreSQL database on Amazon RDS. The security team mandates a policy that requires rotating database credentials every week.
    What strategy should the developer adopt to manage the database credentials for the application?

    - 8. 
    A healthcare service wants to exchange patient data securely with a partner organization through an HTTP API endpoint provided by the partner. The healthcare service has the requisite API key for accessing the HTTP API. The service needs a solution to manage the API key through code.
    Which method will fulfill these requirements with maximum security?

    - 9. 
    A company needs to encrypt a large quantity of data. The data encryption keys must be generated from a dedicated, tamper-resistant hardware device.
    To deliver these requirements, which AWS service should the company use?

    - 10. 
    A developer is working on an application that must save hundreds of sensitive files. The application needs to encrypt each file using a unique key before storing it.
    What should the developer do to implement this in the application?

    - 11. 
    An organization has encrypted a large quantity of data. To protect their data encryption keys they are planning to use envelope encryption. Which of the following processes is a correct implementation of envelope encryption?

    - 12. 
    A company has sensitive data that must be encrypted. The data is made up of 1 GB objects and there is a total of 150 GB of data.
    What is the BEST approach for a Developer to encrypt the data using AWS KMS?

    - 13. 
    A company has hired a team of remote Developers. The Developers need to work programmatically with AWS resources from their laptop computers.
    Which security components MUST the Developers use to authenticate? (Select TWO.)

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
    Use AWS Secrets Manager to store the credentials. Retrieve the credentials from Secrets Manager as needed.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=859)

    - 2. 
    Create a local cache using the AWS Encryption SDK and the LocalCryptoMaterialsCache feature.
    Create a case in the AWS Support Center to increase the quota for the account.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=843)

    - 3. 
    Use AWS KMS with automatic key rotation
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=832)

    - 4. 
    Store a secret in AWS Secrets Manager and enable automatic rotation every 30 days
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=859)

    - 5. 
    Perform error retries with exponential backoff in the application code
    Contact AWS support to request an AWS KMS rate limit increase
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=843)

    - 6. 
    kms:GenerateDataKey
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=837)

    - 7. 
    Deploy AWS Secrets Manager to store database credentials and set up automatic weekly rotation.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=859)

    - 8. 
    Use AWS Secrets Manager to store and retrieve the API key.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=859)

    - 9. 
    AWS CloudHSM
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=849)

    - 10. 
    Use the AWS KMS GenerateDataKey API to acquire a data key, use the data key to encrypt the data, and store both the encrypted data key and the data.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=837)

    - 11. 
    Encrypt plaintext data with a data key and then encrypt the data key with a top-level plaintext master key.

    - 12. 
    Make a GenerateDataKey API call that returns a plaintext key and an encrypted copy of a data key. Use the plaintext key to encrypt the data

    - 13. 
    Access key ID
    Secret Access Key

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


# Section 31: AWS Other Services ---> [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=871)
    ============================================================================================================================================================
- ### Questions:
    - 1. 
    An international research organization holds a wide range of data across several Amazon S3 buckets. They recently received an alert indicating potential exposure of sensitive financial data via a public-facing web portal. The developer's job is to trace all potential data leakage points across their AWS infrastructure.
    What is the most effective strategy for this task?

    - 2. 
    A developer is looking to verify that redirects are performing as expected. What is the most efficient way that the developer can access the web logs and perform an analysis on them?

    - 3. 
    A developer is partitioning data using Athena to improve performance when performing queries. What are two things the analyst can do that would counter any benefit of using partitions? (Select TWO.)

    - 4. 
    An organization is launching a new service that will use an IoT device. How can secure communication protocols be established over the internet to ensure the security of the IoT devices during the launch?

    - 5. 
    A company is migrating to the AWS Cloud and needs to build a managed Public Key Infrastructure (PKI) using AWS services. The solution must support the following features:
        - IAM integration.
        - Auditing with AWS CloudTrail.
        - Private certificates.
        - Subordinate certificate authorities (CAs).
    Which solution should the company use to meet these requirements?

    - 6. 
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
    Implement Amazon Macie and apply the SensitiveData:S3Object/financial finding type across all S3 buckets to automatically identify potential exposure of sensitive financial data.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=886)

    - 2. 
    Store the logs in a S3 bucket and use Athena to run SQL queries.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=877)

    - 3. 
    Segmenting data too finely.
    Skewing data heavily to one partition value.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=878)

    - 4. 
    Use AWS Certificate Manager (ACM) to provide TLS secured communications to IoT devices and deploy X.509 certificates in the IoT environment.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=884)

    - 5. 
    AWS Private Certificate Authority.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=885)

    - 6. 
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







# OTHER:
    ============================================================================================================================================================
- ### Questions:
    - 1. 
    A Developer needs to create an instance profile for an Amazon EC2 instance using the AWS CLI. How can this be achieved? (Select THREE.)

    - 2. 
    A team of Developers require access to an AWS account that is a member account in AWS Organizations. The administrator of the master account needs to restrict the AWS services, resources, and API actions that can be accessed by the users in the account.
    What should the administrator create?

    - 3. 
    A company is developing a game for the Android and iOS platforms. The mobile game will securely store user game history and other data locally on the device. The company would like users to be able to use multiple mobile devices and synchronize data between devices.
    Which service can be used to synchronize the data across mobile devices without the need to create a backend application?

    - 4. 
    A three-tier application is being migrated from an on-premises data center. The application includes an Apache Tomcat web tier, an application tier running on Linux, and a MySQL back end. A Developer must refactor the application to run on the AWS cloud. The cloud-based application must be fault tolerant and elastic.
    How can the Developer refactor the web tier and application tier? (Select TWO.)

    - 5. 
    A company provides a large number of services on AWS to customers. The customers connect to one or more services directly and the architecture is becoming complex. How can the architecture be refactored to provide a single interface for the services?

    - 6. 
    A Developer needs to restrict all users and roles from using a list of API actions within a member account in AWS Organizations. The Developer needs to deny access to a few specific API actions.
    What is the MOST efficient way to do this?

    - 7. 
    A developer is running queries on Hive-compatible partitions in Athena using DDL but is facing time out issues. What is the most effective and efficient way to prevent this from continuing to happen?
    
    - 8. 
    A company will be hiring a large number of Developers for a series of projects. The Develops will bring their own devices to work and the company want to ensure consistency in tooling. The Developers must be able to write, run, and debug applications with just a browser, without needing to install or maintain a local Integrated Development Environment (IDE).
    Which AWS service should the Developers use?

    - 9. 
    A Developer is publishing custom metrics for Amazon EC2 using the Amazon CloudWatch CLI. The Developer needs to add further context to the metrics being published by organizing them by EC2 instance and Auto Scaling Group.
    What should the Developer add to the CLI command when publishing the metrics using put-metric-data 

    - 10. 
    A manufacturing company is creating a new RESTful API that their customers can use to query the status of orders. The endpoint for customer queries will be https://www.manufacturerdomain.com/status/customerID
    Which of the following application designs will meet the requirements? (Select TWO.)

    - 11. 
    A company has released a new application on AWS. The company are concerned about security and require a tool that can automatically assess applications for exposure, vulnerabilities, and deviations from best practices.
    Which AWS service should they use?

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
    Run the aws ec2 associate-instance-profile command
    Run the aws iam create-instance-profile command
    Run the aws iam add-role-to-instance-profile command

    - 2. 
    A Service Control Policy (SCP) 
    https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html
    https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_about-scps.html

    - 3. 
    Amazon Cognito
    https://docs.aws.amazon.com/cognito/latest/developerguide/synchronizing-data.html

    - 4. 
    Create an Auto Scaling group of EC2 instances for both the web tier and application tier
    Implement an Elastic Load Balancer for both the web tier and the application tier
    https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html
    https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-auto-scaling.html

    - 5. 
    Amazon API Gateway
    https://aws.amazon.com/api-gateway/features/

    - 6. 
    Create a deny list and specify the API actions to deny
    https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scp.html

    - 7. 
    Use the MSCK REPAIR TABLE command to update the metadata in the catalog.
    https://docs.aws.amazon.com/athena/latest/ug/msck-repair-table.html

    - 8. 
    AWS Cloud9

    - 9. 
    The --dimensions parameter

    - 10. 
    Elastic Load Balancing; Amazon EC2
    Amazon API Gateway; AWS Lambda

    - 11. 
    Amazon Inspector

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







