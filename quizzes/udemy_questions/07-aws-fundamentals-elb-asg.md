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
    Install SSL certificates on each of the EC2 instances
    Configure the Elastic Load Balancer for TCP pass-through on port 443
    Enable SSL on the EC2 instances’ Elastic Block Store volumes

    - 2. 
    Launch additional EC2 instances manually when CPU utilization is high
    Use an Elastic Load Balancer with cross-zone load balancing enabled
    Use Amazon EC2 Spot Instances with a fixed instance count

    - 3. 
    Network Load Balancer with sticky sessions enabled.
    Classic Load Balancer with TCP listeners and connection draining enabled.
    Application Load Balancer with cross-zone load balancing enabled.

    - 4. 
    Install SSL certificates on the EC2 instances
    Configure the Elastic Load Balancer with TCP pass-through to the instances
    Configure end-to-end encryption between the load balancer and the instances

    - 5. 
    Configure the HTTP server to add the x-forwarded-proto request header to the logs.
    Enable access logging on the ALB and store the logs on the EC2 instances.
    Configure the HTTP server to log the source IP address of each TCP connection.
