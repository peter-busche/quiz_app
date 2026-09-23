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
    Use a task placement constraint distinctInstance.
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
    Configure the access keys as environment variables in the ECS task definition.
    Store the access keys in the container image used by the ECS task.
    Configure an ECS task execution IAM role for the application to use.

    - 2. 
    Store access keys in the ~/.aws/credentials file
    Store access keys in the instance user data
    Hard code access keys in the application code

    - 3. 
    Run the output of the following: aws ecr describe-images, and then run: docker pull REPOSITORY URI : TAG
    Run the output of the following: aws ecr get-login-password, and then run: docker push REPOSITORY URI : TAG
    Run the output of the following: aws ecr create-repository, and then run: docker build REPOSITORY URI : TAG

    - 4. 
    Use a binpack task placement strategy
    Use a random task placement strategy
    Use an ECS service Auto Scaling policy

    - 5. 
    Task Placement Strategy
    ECS Service Auto Scaling
    Container Instance Draining

    - 6. 
    They will be placed on container instances not in the “databases” task group
    They will be spread evenly across all Availability Zones in the “databases” task group
    They will be placed only on the same container instance as other “databases” tasks

    - 7. 
    binpack
    spread
    distinctInstance

    - 8. 
    All at once
    Rolling
    Immutable

    - 9. 
    Add a listener to the ALB. Update the AppSpec file to link the Lambda function to the AfterAllowTraffic lifecycle hook.
    Add a target group to the ALB. Update the AppSpec file to link the Lambda function to the ValidateService lifecycle hook.
    Remove a target group from the ALB. Update the AppSpec file to link the Lambda function to the ApplicationStart lifecycle hook.

    - 10. 
    random
    spread
    distinctInstance

    - 11. 
    Amazon ECS with the EC2 launch type
    Amazon ECS with Reserved Instances for container instances
    Amazon ECS with the EC2 launch type on Dedicated Hosts
