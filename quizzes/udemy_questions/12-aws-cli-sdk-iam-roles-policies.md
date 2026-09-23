# Section 12: AWS CLI, SDK, IAM Roles & Policies ---> [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=238)
    ============================================================================================================================================================
- ### Questions:
    - 1. 
    An application writes items to an Amazon DynamoDB table. As the application scales to thousands of instances, calls to the DynamoDB API generate occasional ThrottlingException errors. The application is coded in a language incompatible with the AWS SDK.
    How should the error be handled?

    - 2. 
    A programmer is creating an application that requires signed requests (Signature Version 4) for invoking other AWS services. Having constructed a canonical request, created the string to sign, and calculated the signing information, which strategies can the programmer apply to finalize a signed request? (Select TWO.)

    - 3. 
    A Developer is trying to make API calls using AWS SDK. The IAM user credentials used by the application require multi-factor authentication for all API calls.
    Which method should the Developer use to access the multi-factor authentication protected API?

    - 4. 
    A Developer is creating an AWS Lambda function that generates a new file each time it runs. Each new file must be checked into an AWS CodeCommit repository hosted in the same AWS account.
    How should the Developer accomplish this?

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
    Add exponential backoff to the application logic
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=245)

    - 2. 
    Incorporate the signature into an HTTP header called "Authorization".
    Insert the signature into a query string parameter referred to as "X-Amz-Signature".
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=247)

    - 3. 
    GetSessionToken
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=241)

    - 4. 
    Use an AWS SDK to instantiate a CodeCommit client. Invoke the put_file method to add the file to the repository
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=243)
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=601)

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
    Increase the provisioned write capacity of the table after each error
    Retry the failed requests immediately in a tight loop until they succeed
    Add Amazon DynamoDB Accelerator (DAX) to cache the write requests

    - 2. 
    Incorporate the signature into an HTTP header called "X-Amz-Security-Token".
    Insert the signature into a query string parameter referred to as "X-Amz-Credential".
    Incorporate the signature into an HTTP header called "Content-MD5".

    - 3. 
    GetFederationToken
    AssumeRoleWithWebIdentity
    GetCallerIdentity

    - 4. 
    Use an AWS SDK to instantiate an Amazon S3 client. Invoke the put_object method to add the file to the repository
    Use an AWS SDK to instantiate a CodeBuild client. Invoke the start_build method to add the file to the repository
    Use an AWS SDK to instantiate a CodePipeline client. Invoke the put_job_success_result method to add the file to the repository
