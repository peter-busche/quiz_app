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


    ### Wrong Answers:
    - 1. 
    The IAM role policy changes take up to 24 hours to propagate to running instances
    The AWS credential provider looks for instance profile credentials first
    The AWS SDK for Java ignores IAM roles and only supports access keys

    - 2. 
    Use the AWS IAM simulate-principal-policy API to decode the message
    Use the AWS KMS decrypt API to decode the message
    Use the AWS CloudTrail lookup-events API to decode the message

    - 3. 
    Create an IAM user in the Production account and share its access keys with the developer
    Use the sts:GetSessionToken API with the Development account credentials to access Production
    Add the developer's Development IAM user to an IAM group in the Production account
