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


    ### Wrong Answers:
    - 1. 
    Public IP address
    Private IP address
    Secondary private IP address

    - 2. 
    Import the third-party SSL/TLS certificate to AWS Secrets Manager, link it with the custom domain name in API Gateway, and then create an MX record in Route 53 for the custom domain name.
    Upload the third-party SSL/TLS certificate directly to the API Gateway stage, and then create a TXT record in Route 53 for the custom domain name.
    Import the third-party SSL/TLS certificate to AWS Systems Manager Parameter Store, link it with the API Gateway stage, and then create an NS record in Route 53.

    - 3. 
    Use an Amazon Route 53 Latency Routing Policy
    Use an Amazon Route 53 Failover Routing Policy
    Use an Amazon Route 53 Geolocation Routing Policy
