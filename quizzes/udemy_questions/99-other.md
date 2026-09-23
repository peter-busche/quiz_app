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
    Run the aws ec2 create-instance-profile command
    Run the aws sts assume-role command
    Run the aws iam create-service-linked-role command

    - 2. 
    An IAM permissions boundary in the master account
    A resource-based policy on each AWS service
    An AWS Config rule

    - 3. 
    Amazon SQS
    AWS AppConfig
    Amazon ElastiCache

    - 4. 
    Deploy the web tier and application tier on a single large EC2 instance with an Elastic IP address
    Implement Amazon RDS Multi-AZ for both the web tier and the application tier
    Create a single EC2 Dedicated Host for both the web tier and application tier

    - 5. 
    Amazon Route 53
    AWS Direct Connect
    Amazon SQS

    - 6. 
    Create an IAM policy in the member account with an explicit deny for each individual user and role
    Remove the FullAWSAccess SCP from the member account
    Create a permissions boundary for every IAM role in the member account
