# Section 30: AWS Security & Encryption: KMS, Encryption SDK, SSM Parameter Store, IAM & STS ---> [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=826)
    ============================================================================================================================================================
- ### Questions:
    - 1. 
    An application runs on a fleet of Amazon EC2 instances and stores data in a Microsoft SQL Server database hosted on Amazon RDS. The developer wants to avoid storing database connection credentials the application code. The developer would also like a solution that automatically rotates the credentials.
    What is the MOST secure way to store and access the database credentials?

    - 2. 
    An application that processes financial transactions receives thousands of transactions each second. The transactions require end-to-end encryption, and the application implements this by using the AWS KMS GenerateDataKey operation. During operation the application receives the following error message:
    “You have exceeded the rate at which you may call KMS. Reduce the frequency of your calls.
    (Service: AWSKMS; Status Code: 400; Error Code: ThrottlingException; Request ID: <ID>”
    Which actions are best practices to resolve this error? (Select TWO.)

    - 3. 
    A Developer is storing sensitive documents in Amazon S3. The documents must be encrypted at rest and company policy mandates that the encryption keys must be rotated annually. What is the EASIEST way to achieve this?

    - 4. 
    An application will use AWS Lambda and an Amazon RDS database. The Developer needs to secure the database connection string and enable automatic rotation every 30 days. What is the SIMPLEST way to achieve this requirement?

    - 5. 
    An application is running on a cluster of Amazon EC2 instances. The application has received an error when trying to read objects stored within an Amazon S3 bucket. The bucket is encrypted with server-side encryption and AWS KMS managed keys (SSE-KMS). The error is as follows:
    Service: AWSKMS; Status Code: 400, Error Code: ThrottlingException
    Which combination of steps should be taken to prevent this failure? (Select TWO.)

    - 6. 
    A large quantity of sensitive data must be encrypted. A Developer will use a custom CMK to generate the encryption key. The key policy currently looks like this:
        {
        "Sid": "Allow Key Usage",
        "Effect": "Allow",
        "Principal": {"AWS": [
        "arn:aws:iam::111122223333:user/CMKUser"
        ]},
        "Action": [
        "kms:Encrypt",
        "kms:Decrypt",
        "kms:ReEncrypt*",
        "kms:DescribeKey"
        ],
        "Resource": "*"
        }
    What API action must be added to the key policy?

    - 7. 
    An organization is developing a data processing application that is hosted on AWS Lambda and utilizes a PostgreSQL database on Amazon RDS. The security team mandates a policy that requires rotating database credentials every week.
    What strategy should the developer adopt to manage the database credentials for the application?

    - 8. 
    A healthcare service wants to exchange patient data securely with a partner organization through an HTTP API endpoint provided by the partner. The healthcare service has the requisite API key for accessing the HTTP API. The service needs a solution to manage the API key through code.
    Which method will fulfill these requirements with maximum security?

    - 9. 
    A company needs to encrypt a large quantity of data. The data encryption keys must be generated from a dedicated, tamper-resistant hardware device.
    To deliver these requirements, which AWS service should the company use?

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
    Use AWS Secrets Manager to store the credentials. Retrieve the credentials from Secrets Manager as needed.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=859)

    - 2. 
    Create a local cache using the AWS Encryption SDK and the LocalCryptoMaterialsCache feature.
    Create a case in the AWS Support Center to increase the quota for the account.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=843)

    - 3. 
    Use AWS KMS with automatic key rotation
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=832)

    - 4. 
    Store a secret in AWS Secrets Manager and enable automatic rotation every 30 days
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=859)

    - 5. 
    Perform error retries with exponential backoff in the application code
    Contact AWS support to request an AWS KMS rate limit increase
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=843)

    - 6. 
    kms:GenerateDataKey
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=837)

    - 7. 
    Deploy AWS Secrets Manager to store database credentials and set up automatic weekly rotation.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=859)

    - 8. 
    Use AWS Secrets Manager to store and retrieve the API key.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=859)

    - 9. 
    AWS CloudHSM
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=849)

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
    Store the credentials in an encrypted configuration file on each EC2 instance and rotate them with a cron job.
    Store the credentials in EC2 user data and retrieve them from the instance metadata service as needed.
    Store the credentials as environment variables in the AMI and rebuild the AMI to rotate them.

    - 2. 
    Replace GenerateDataKey calls with direct kms:Encrypt calls for each transaction payload.
    Enable automatic key rotation on the KMS key used by the application.
    Create a second KMS key in the same Region and alternate calls between the two keys.

    - 3. 
    Use SSE-C and upload new customer-provided keys with each request annually
    Use AWS CloudHSM and write a custom script to rotate the keys
    Use AWS Systems Manager Parameter Store with a SecureString rotation policy

    - 4. 
    Store a SecureString parameter in Systems Manager Parameter Store and enable automatic rotation every 30 days
    Store the connection string in Lambda environment variables and enable automatic rotation every 30 days
    Store the connection string in an encrypted Amazon S3 object and enable S3 Lifecycle rotation every 30 days

    - 5. 
    Enable automatic key rotation on the AWS KMS key
    Increase the instance size of the EC2 instances in the cluster
    Enable S3 Transfer Acceleration on the bucket

    - 6. 
    kms:CreateKey
    kms:GenerateRandom
    kms:EnableKeyRotation

    - 7. 
    Store the database credentials in Lambda environment variables and redeploy the function weekly.
    Store the database credentials as a SecureString in Parameter Store and set up automatic weekly rotation.
    Hardcode the database credentials in the function code and update them manually each week.

    - 8. 
    Store the API key in the application source code and encrypt the repository.
    Store the API key in Lambda environment variables in plaintext.
    Store the API key in an Amazon S3 object with a public read ACL.

    - 9. 
    AWS Key Management Service (AWS KMS)
    AWS Secrets Manager
    AWS Certificate Manager
