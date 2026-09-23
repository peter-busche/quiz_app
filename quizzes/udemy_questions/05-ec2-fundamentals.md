# Section 5: EC2 Fundamentals ---> [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=39)
    ============================================================================================================================================================
- ### Questions:
    - 1. 
    A Developer must run a shell script on Amazon EC2 Linux instances each time they are launched by an Amazon EC2 Auto Scaling group. What is the SIMPLEST way to run the script?

    - 2. 
    An organization is hosting a website on an Amazon EC2 instance in a public subnet. The website should allow public access for HTTPS traffic on TCP port 443 but should only accept SSH traffic on TCP port 22 from a corporate address range accessible over a VPN.
    Which security group configuration will support both requirements?

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
    Add the script to the user data when creating the launch configuration
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=42)

    - 2. 
    Allow traffic to port 443 from 0.0.0.0/0 and allow traffic to port 22 from 192.168.0.0/16.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=51)

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


    ### Wrong Answers:
    - 1. 
    Add the script to the instance metadata when creating the launch configuration
    Use AWS CodeDeploy to run the script as an AfterInstall hook on each launch
    Create an Amazon EventBridge rule that invokes the script from AWS Lambda on each launch

    - 2. 
    Allow traffic to port 443 from 0.0.0.0/0 and deny traffic to port 22 from 0.0.0.0/0.
    Allow traffic to port 22 from 0.0.0.0/0 and allow traffic to port 443 from 192.168.0.0/16.
    Allow traffic to ports 22 and 443 from 0.0.0.0/0.
