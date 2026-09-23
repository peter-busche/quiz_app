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
    All at once
    Rolling
    Immutable

    - 2. 
    All at once
    Rolling
    Rolling with additional batch

    - 3. 
    All at once
    Rolling
    Rolling with additional batch

    - 4. 
    In the root of the source bundle
    In the .elasticbeanstalk folder
    In the .platform/hooks folder

    - 5. 
    Use the All at once deployment policy on the existing environment to deploy the new code and update the platform to the newer Node.js version in a single step.
    Enable managed platform updates on the existing environment to upgrade Node.js, and deploy the new code using the All at once deployment policy in the same maintenance window.
    Add an .ebextensions command that upgrades Node.js on each running EC2 instance, then deploy the new code to the existing environment using the All at once deployment policy.

    - 6. 
    Amazon DynamoDB
    AWS CloudFormation
    Amazon EC2 with PostgreSQL installed
