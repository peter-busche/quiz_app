# Section 7: My Questions: ELB + ASG ---> [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=92)
    ============================================================================================================================================================
- ### Questions:
    - 1. 
    A team stores shared files on Amazon EFS. Most files are read heavily for a few weeks and then are almost never touched again. The team wants to lower storage costs automatically without changing the application.
    What should they do?

    - 2. 
    A developer needs a low-cost Amazon EFS file system for a development environment. Durability across multiple Availability Zones is not required, and most files are rarely accessed.
    Which EFS configuration is the MOST cost-effective?

    - 3. 
    An application running on an EC2 instance in us-east-1a stores data on an Amazon EBS volume. The application must be moved to an instance in us-east-1b along with its data.
    How can the developer move the EBS volume data to the new Availability Zone?

    - 4. 
    A company runs a WordPress website on dozens of Linux EC2 instances spread across several Availability Zones. All instances must read and write the same website files at the same time.
    Which storage option is the BEST fit?

    - 5. 
    An application running on a single EC2 instance is running out of memory. The developer changes the instance type from t2.micro to t2.large.
    What type of scaling is this?

    - 6. 
    Which statement BEST describes the goal of high availability for an application on AWS?

    - 7. 
    Which of the following are benefits of using a load balancer in front of a fleet of EC2 instances? (Select TWO.)

    - 8. 
    An Application Load Balancer is configured to health check its targets on port 4567 at the route /health. One of the instances responds to the health check with an HTTP 503 status code.
    What will the load balancer do?

    - 9. 
    A company must place a fleet of third-party firewall and intrusion detection virtual appliances in the path of all network traffic entering its VPC.
    Which type of load balancer should be used?

    - 10. 
    An online game uses a custom protocol over UDP and needs to handle millions of requests per second with ultra-low latency.
    Which load balancer should the developer choose?

    - 11. 
    A developer wants the EC2 instances behind an Application Load Balancer to accept HTTP traffic ONLY from the load balancer, and not directly from the internet.
    How should the instance security group be configured?

    - 12. 
    A company is building a microservices application. Requests to example.com/users must go to the users service, and requests to example.com/search must go to the search service. Both services run on separate groups of EC2 instances.
    What is the SIMPLEST way to route this traffic?

    - 13. 
    Which of the following can be registered as targets in an Application Load Balancer target group? (Select TWO.)

    - 14. 
    A developer registers an AWS Lambda function as a target of an Application Load Balancer.
    How does the Lambda function receive the HTTP request?

    - 15. 
    A developer notices that the application logs on the EC2 instances behind an Application Load Balancer only show private IP addresses. The developer also needs to know which protocol (HTTP or HTTPS) the client used to connect to the load balancer.
    Which request header contains this information?

    - 16. 
    A partner company only allows outbound connections to IP addresses on its firewall allowlist. The application they need to connect to runs behind an AWS load balancer.
    Which load balancer should be used so the partner can allowlist fixed IP addresses?

    - 17. 
    A company wants to expose a single static IP address per Availability Zone to its customers but also needs HTTP path-based routing for its application.
    What architecture meets these requirements?

    - 18. 
    Users of a web application behind an Application Load Balancer complain that they keep losing their shopping cart contents because session data is stored in memory on each EC2 instance.
    What is the QUICKEST fix that does not require changes to the application code?

    - 19. 
    A developer is configuring an application-based custom cookie for sticky sessions on an Application Load Balancer.
    Which cookie name is ALLOWED to be used?

    - 20. 
    A developer enables duration-based sticky sessions on an Application Load Balancer.
    What is the name of the cookie that the load balancer generates?

    - 21. 
    A Network Load Balancer spans two Availability Zones. AZ 1 has 2 instances and AZ 2 has 8 instances. The instances in AZ 1 are overloaded.
    What change will distribute requests evenly across all 10 instances, and what is the cost implication?

    - 22. 
    Which statements about cross-zone load balancing are correct? (Select TWO.)

    - 23. 
    A company hosts three websites with different domain names behind a single Application Load Balancer. Each website has its own SSL/TLS certificate.
    What allows the load balancer to present the correct certificate to each client?

    - 24. 
    A company uses a Classic Load Balancer for two websites with different domain names, each with its own SSL certificate. They want to keep serving both over HTTPS.
    What must they do?

    - 25. 
    Some legacy clients connecting to an application behind an HTTPS load balancer only support older versions of SSL/TLS.
    What should the developer configure to allow these clients to connect?

    - 26. 
    An Application Load Balancer is in front of an application whose requests all complete in under 5 seconds. During deployments, instances take a long time to be removed from the target group.
    What should the developer change?

    - 27. 
    What is the default deregistration delay (connection draining) period for an Elastic Load Balancer?

    - 28. 
    Which of the following are functions of an Auto Scaling Group? (Select TWO.)

    - 29. 
    Which of the following is configured in an Auto Scaling Group's launch template?

    - 30. 
    A developer wants the average CPU utilization across an Auto Scaling Group to stay around 40% with minimal configuration.
    Which scaling policy should they use?

    - 31. 
    An e-commerce site gets a predictable spike in traffic every Friday at 5 PM. The developer wants to make sure enough EC2 instances are already running before the spike starts.
    Which scaling policy should they use?

    - 32. 
    A company wants its Auto Scaling Group to add 2 instances when a CloudWatch alarm fires for CPU above 70%, and remove 1 instance when a second alarm fires for CPU below 30%.
    Which type of scaling policy is this?

    - 33. 
    An application behind an Application Load Balancer should keep the number of requests handled by each EC2 instance roughly stable as traffic grows.
    Which metric is the BEST fit for a target tracking scaling policy?

    - 34. 
    After an Auto Scaling Group launches a new instance, it ignores a CloudWatch alarm that is still firing and does not launch another instance for several minutes.
    Why is this happening?

    - 35. 
    Newly launched instances in an Auto Scaling Group take a long time to install software from user data before they can serve traffic.
    What will reduce this configuration time AND allow a shorter cooldown period?

    - 36. 
    A developer has updated the launch template of an Auto Scaling Group with a new AMI and wants to replace all existing EC2 instances, while keeping at least 60% of the instances healthy during the process.
    Which feature should they use?


    ### Answers:
    - 1. 
    Create an EFS lifecycle policy that moves files to EFS Infrequent Access (or Archive) after N days without access
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=92)

    - 2. 
    EFS One Zone-IA
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=92)

    - 3. 
    Take a snapshot of the EBS volume and restore the snapshot to a new volume in us-east-1b
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=93)

    - 4. 
    Amazon EFS, mounted on all instances through mount targets in each AZ
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=94)

    - 5. 
    Vertical scaling (scaling up)
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=97)

    - 6. 
    Run the application in at least 2 Availability Zones so it can survive the loss of a data center
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=99)

    - 7. 
    Expose a single point of access (DNS) to the application
    Provide SSL termination (HTTPS) for the websites
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=102)

    - 8. 
    Mark the instance as unhealthy and stop sending traffic to it
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=104)

    - 9. 
    Gateway Load Balancer
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=117)

    - 10. 
    Network Load Balancer
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=114)

    - 11. 
    Allow inbound HTTP traffic only from the load balancer's security group
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=106)

    - 12. 
    Use one Application Load Balancer with path-based routing rules that send each path to a different target group
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=109)

    - 13. 
    ECS tasks
    Private IP addresses
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=111)

    - 14. 
    The HTTP request is translated into a JSON event
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=111)

    - 15. 
    X-Forwarded-Proto
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=113)

    - 16. 
    Network Load Balancer with an Elastic IP assigned in each AZ
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=114)

    - 17. 
    A Network Load Balancer whose target group is an Application Load Balancer
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=116)

    - 18. 
    Enable sticky sessions (session affinity) on the load balancer
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=119)

    - 19. 
    MYAPPSESSION
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=120)

    - 20. 
    AWSALB
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=120)

    - 21. 
    Enable cross-zone load balancing; you will pay for inter-AZ data transfer
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=122)

    - 22. 
    Cross-zone load balancing is enabled by default on an Application Load Balancer
    There are no inter-AZ data charges for cross-zone load balancing on an Application Load Balancer
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=122)

    - 23. 
    Server Name Indication (SNI)
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=125)

    - 24. 
    Use a separate Classic Load Balancer for each hostname and certificate, or move to an ALB / NLB that supports SNI
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=126)

    - 25. 
    A security policy on the HTTPS listener that supports older SSL/TLS versions
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=124)

    - 26. 
    Lower the deregistration delay on the target group
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=127)

    - 27. 
    300 seconds
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=127)

    - 28. 
    Automatically register new instances with a load balancer
    Re-create an instance if a previous one is terminated or unhealthy
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=128)

    - 29. 
    The AMI, instance type, EC2 user data, security groups, and IAM role
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=131)

    - 30. 
    Target tracking scaling
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=133)

    - 31. 
    Scheduled scaling
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=133)

    - 32. 
    Step scaling
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=133)

    - 33. 
    RequestCountPerTarget
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=135)

    - 34. 
    The Auto Scaling Group is in its cooldown period
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=136)

    - 35. 
    Use a ready-to-use AMI with the software already installed
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=136)

    - 36. 
    Instance Refresh with a minimum healthy percentage of 60%
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=137)


    ### Wrong Answers:
    - 1. 
    Switch the file system to EFS One Zone so files are stored in a single AZ
    Take EBS snapshots of the file system and delete the originals after N days
    Increase the provisioned throughput of the EFS Standard file system

    - 2. 
    EFS Standard
    EFS Standard-IA
    EFS One Zone with provisioned throughput

    - 3. 
    Detach the volume and attach it directly to the instance in us-east-1b
    Enable EBS Multi-Attach so both instances can use the same volume
    Modify the volume's Availability Zone attribute to us-east-1b

    - 4. 
    A gp3 EBS volume attached to each instance
    An io2 EBS volume with Multi-Attach enabled
    EC2 Instance Store volumes on each instance

    - 5. 
    Horizontal scaling (scaling out)
    High availability
    Elasticity

    - 6. 
    Increase the instance size so the application can handle greater loads
    Run as many instances as possible in a single Availability Zone
    Automatically add instances when CPU utilization is high

    - 7. 
    Remove the need to run health checks on instances
    Automatically increase the size of instances under heavy load
    Guarantee that every user is always sent to the same instance

    - 8. 
    Terminate the instance and launch a replacement
    Keep sending traffic but retry failed requests on another instance
    Reboot the instance and wait for it to pass the next health check

    - 9. 
    Network Load Balancer
    Application Load Balancer
    Classic Load Balancer

    - 10. 
    Application Load Balancer
    Classic Load Balancer
    Gateway Load Balancer

    - 11. 
    Allow inbound HTTP traffic from 0.0.0.0/0
    Allow inbound HTTP traffic from the load balancer's public DNS name
    Allow inbound HTTP traffic only from the Elastic IP of the load balancer

    - 12. 
    Use one Classic Load Balancer with listener rules for each path
    Use a Network Load Balancer with a separate listener port for each service
    Use one Classic Load Balancer per service and route with Route 53

    - 13. 
    Public IP addresses
    Amazon S3 buckets
    Other Application Load Balancers

    - 14. 
    The raw TCP packets are forwarded to the function
    The request is sent to the function's function URL over HTTPS
    The request is written to an SQS queue that triggers the function

    - 15. 
    X-Forwarded-For
    X-Forwarded-Port
    X-Forwarded-Host

    - 16. 
    Application Load Balancer with an Elastic IP assigned
    Classic Load Balancer using its fixed hostname
    Application Load Balancer with cross-zone load balancing enabled

    - 17. 
    An Application Load Balancer with an Elastic IP assigned in each AZ
    A Classic Load Balancer with path-based routing
    A Gateway Load Balancer that forwards to an Application Load Balancer

    - 18. 
    Enable cross-zone load balancing on the load balancer
    Increase the deregistration delay on the target group
    Switch to a Network Load Balancer

    - 19. 
    AWSALB
    AWSALBAPP
    AWSALBTG

    - 20. 
    AWSELB
    AWSALBAPP
    AWSALBTG

    - 21. 
    Enable cross-zone load balancing; there is no charge for inter-AZ data
    Enable sticky sessions; there is no additional charge
    Increase the deregistration delay; there is no additional charge

    - 22. 
    Cross-zone load balancing is enabled by default on a Network Load Balancer
    There are charges for inter-AZ data when cross-zone load balancing is enabled on a Classic Load Balancer
    Cross-zone load balancing can only be disabled at the load balancer level on an Application Load Balancer

    - 23. 
    X-Forwarded-Proto header
    Sticky sessions
    Cross-zone load balancing

    - 24. 
    Add both certificates to the same Classic Load Balancer listener and enable SNI
    Install both certificates on each EC2 instance behind the Classic Load Balancer
    Use a wildcard Route 53 record pointing at the Classic Load Balancer

    - 25. 
    Enable SNI on a Classic Load Balancer
    Install the older SSL certificates on each EC2 instance
    Add a second default certificate to the HTTPS listener

    - 26. 
    Increase the deregistration delay to 3600 seconds
    Increase the health check interval on the target group
    Enable cross-zone load balancing

    - 27. 
    60 seconds
    0 seconds
    3600 seconds

    - 28. 
    Increase the instance type of an instance when CPU is high
    Encrypt traffic between clients and instances
    Distribute incoming requests across instances

    - 29. 
    The scaling policies and CloudWatch alarms
    The minimum, maximum, and desired capacity
    The listener rules and SSL certificates of the load balancer

    - 30. 
    Simple scaling
    Scheduled scaling
    Predictive scaling

    - 31. 
    Target tracking scaling
    Step scaling
    Simple scaling based on a CPU CloudWatch alarm

    - 32. 
    Target tracking scaling
    Scheduled scaling
    Predictive scaling

    - 33. 
    CPUUtilization
    Average Network In
    HealthyHostCount

    - 34. 
    The Auto Scaling Group has reached its desired capacity
    The load balancer's deregistration delay is in effect
    The CloudWatch alarm is in the INSUFFICIENT_DATA state

    - 35. 
    Increase the cooldown period to 3600 seconds
    Move the user data script into the scaling policy
    Use a larger instance type in the launch template

    - 36. 
    Scheduled scaling to set the desired capacity to 0 and back
    Connection draining with a deregistration delay of 60%
    Terminate the instances manually and let the ASG replace them
