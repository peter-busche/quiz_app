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
    Enable AWS CloudTrail and publish data to Amazon S3
    Enable Elastic Load Balancer access logs and publish data to Amazon S3
    Enable AWS Config and publish data to Amazon S3

    - 2. 
    Attach an Internet Gateway
    Configure a VPC peering connection
    Attach an Elastic IP address

    - 3. 
    Create a network ACL in the VPC with a rule that matches the specified countries and denies access.
    Create a security group with a rule that matches the specified countries and denies access.
    Create an Amazon Route 53 weighted routing policy that sends traffic from the specified countries to a blank page.
