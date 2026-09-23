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


    ### Wrong Answers:
    - 1. 
    Use Amazon S3 static website hosting and manually upload site files from each branch using the AWS CLI after every merge.
    Use AWS Elastic Beanstalk to host the sites and configure an EC2-based Jenkins server to deploy on branch merges.
    Use Amazon EC2 instances behind an Application Load Balancer and deploy with AWS CodeDeploy on each merge.

    - 2. 
    Amazon SQS
    AWS Batch
    Amazon SWF

    - 3. 
    Amazon SQS
    Amazon Kinesis Data Streams
    AWS CloudFormation

    - 4. 
    REST API on Amazon API Gateway with separate resources for each data source
    Amazon Kinesis Data Streams consumed by the mobile clients
    Application Load Balancer with separate target groups for each data source
