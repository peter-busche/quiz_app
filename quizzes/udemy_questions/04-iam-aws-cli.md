# Section 4: IAM & AWS CLI  ---> [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=21)
    ============================================================================================================================================================
- ### Questions:
    - 1. 
    The following permissions policy is applied to an IAM user account:
        {
        "Version": "2012-10-17",
        "Statement": [{
        "Effect": "Allow",
        "Action": "sqs:*",
        "Resource": "arn:aws:sqs:*:513246782345:staging-queue*"
        }]
        }
    Due to this policy, what Amazon SQS actions will the user be able to perform?

    - 2. 
    An organization has a new AWS account and is setting up IAM users and policies. According to AWS best practices, which of the following strategies should be followed? (Select TWO.)

    - 3. 
    An Amazon DynamoDB table will store authentication credentials for a mobile app. The table must be secured so only a small group of Developers are able to access it.
    How can table access be secured according to this requirement and following AWS best practice?

    - 4. 
    A small team of Developers require access to an Amazon S3 bucket. An admin has created a resource-based policy. Which element of the policy should be used to specify the ARNs of the user accounts that will be granted access?

    - 5. 
    A Developer has noticed some suspicious activity in her AWS account and is concerned that the access keys associated with her IAM user account may have been compromised. What is the first thing the Developer do in should do in this situation?

    - 6. 
    A developer is writing an application for a company. The program needs to access and read the file named "secret-data.xlsx" located in the root directory of an Amazon S3 bucket named "DATA-BUCKET". The company's security policies mandate the enforcement of the principle of least privilege for the IAM policy associated with the application.
    Which IAM policy statement will comply with these security stipulations?

    - 7. 
    A team of Developers require read-only access to an Amazon DynamoDB table. The Developers have been added to a group. What should an administrator do to provide the team with access whilst following the principal of least privilege?

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
    The user will be able to use all Amazon SQS actions, but only for queues with names begin with the string “staging-queue“
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=25)

    - 2. 
    Create standalone policies instead of using inline policies
    Use groups to assign permissions to users
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=36)

    - 3. 
    Attach a permissions policy to an IAM group containing the Developer’s IAM user accounts that grants access to the table
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=36)

    - 4. 
    Principal
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=25)

    - 5. 
    Delete the compromised access keys
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=30)

    - 6. 
    {"Effect": "Allow", "Action": "s3:GetObject", "Resource": "arn:aws:s3:::DATA-BUCKET/secret-data.xlsx"}
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=36)

    - 7. 
    Create a customer managed policy with read only access to DynamoDB and specify the ARN of the table for the “Resource” element. Attach the policy to the group
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=)

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
    The user will be able to use all Amazon SQS actions on all queues in account 513246782345
    The user will be able to create queues named “staging-queue“ but cannot send or receive messages
    The user will be able to use all Amazon SQS actions, but only for a single queue named “staging-queue“

    - 2. 
    Share the root user access keys with administrators who need full access
    Attach inline policies directly to each individual IAM user
    Grant all users the AdministratorAccess managed policy and restrict later

    - 3. 
    Store the Developers’ IAM access keys in the DynamoDB table and validate them on each request
    Attach a resource-based policy to the DynamoDB table that lists each Developer’s IAM access key ID
    Share the root user credentials with the Developers and enable MFA on the root account

    - 4. 
    Resource
    Action
    Condition

    - 5. 
    Change the password for the IAM user account
    Enable MFA on the IAM user account
    Open a support case with AWS Support

    - 6. 
    {"Effect": "Allow", "Action": "s3:GetObject", "Resource": "arn:aws:s3:::DATA-BUCKET/*"}
    {"Effect": "Allow", "Action": "s3:*", "Resource": "arn:aws:s3:::DATA-BUCKET/secret-data.xlsx"}
    {"Effect": "Allow", "Action": "s3:GetObject", "Resource": "arn:aws:s3:::DATA-BUCKET"}

    - 7. 
    Attach the AmazonDynamoDBFullAccess AWS managed policy to the group so the Developers can read the table
    Create an inline policy with read only access to DynamoDB and embed a copy of it in each Developer’s IAM user
    Create a customer managed policy with read only access to DynamoDB and specify “*” for the “Resource” element. Attach the policy to the group
