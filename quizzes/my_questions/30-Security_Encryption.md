# Section 30: My Questions: Security & Encryption: KMS, Encryption SDK, SSM Parameter Store ---> [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=826)
    ============================================================================================================================================================
- ### Questions:
    - 1. 
    A company requires that data be encrypted by the client before it is uploaded, and that the storage server is NEVER able to decrypt it.
    Which type of encryption is this?

    - 2. 
    A developer needs to encrypt a 10 MB file using AWS KMS.
    Which KMS API should they use?

    - 3. 
    What is the maximum size of data that can be encrypted directly with the KMS Encrypt API?

    - 4. 
    An application needs a data key that will be used to encrypt data at some later time, not right away.
    Which KMS API is the BEST fit?

    - 5. 
    Users outside of AWS, who cannot call the KMS API, must be able to encrypt data that only the company can decrypt.
    Which type of KMS key should be used?

    - 6. 
    Which statements about KMS key rotation are correct? (Select TWO.)

    - 7. 
    An encrypted EBS snapshot in eu-west-2 is copied to ap-southeast-2. What happens to its encryption?

    - 8. 
    A company wants to share an encrypted EBS snapshot with another AWS account. The snapshot is encrypted with a customer managed KMS key.
    What must be done to the KMS key?

    - 9. 
    An application makes many KMS calls and starts receiving ThrottlingException errors. (Select TWO.)

    - 10. 
    A company uses SSE-KMS on an S3 bucket with millions of objects and wants to reduce KMS API calls and costs by up to 99%.
    What should they enable?

    - 11. 
    A company must manage its own encryption keys entirely, on dedicated, single-tenant hardware that AWS does not control.
    Which service should they use?

    - 12. 
    A developer stores configuration for dev and prod Lambda functions in SSM Parameter Store under /my-app/dev/ and /my-app/prod/.
    Which API retrieves all parameters under /my-app/dev/ in one call?

    - 13. 
    A developer needs to store a 6 KB parameter value in SSM Parameter Store and receive an EventBridge notification before the parameter expires.
    What should they use?

    - 14. 
    A company needs to store an RDS database password and automatically rotate it every 30 days using a provided Lambda function.
    Which service is the BEST fit?

    - 15. 
    A CloudFormation template must use a SecureString stored in SSM Parameter Store without writing the value into the template.
    Which syntax should be used?

    - 16. 
    A developer wants to encrypt an existing CloudWatch Logs log group with a KMS key.
    How can this be done?

    - 17. 
    A CodeBuild project needs a database password during the build. The team does not want the password stored in plaintext in the buildspec or project settings.
    What should they do?

    - 18. 
    A company must process credit card data on EC2 in a fully isolated environment with no persistent storage, no interactive access, and no external networking, where only verified code can access KMS keys.
    Which feature should they use?


    ### Answers:
    - 1. 
    Client-side encryption
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=829)

    - 2. 
    GenerateDataKey (envelope encryption)
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=837)

    - 3. 
    4 KB
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=837)

    - 4. 
    GenerateDataKeyWithoutPlaintext
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=842)

    - 5. 
    An asymmetric KMS key, sharing the downloadable public key
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=831)

    - 6. 
    AWS managed KMS keys are automatically rotated every year
    Imported KMS keys can only be rotated manually by using an alias
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=832)

    - 7. 
    The snapshot is re-encrypted with a KMS key in the destination Region (KMS ReEncrypt)
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=833)

    - 8. 
    Attach a KMS key policy that authorizes cross-account access to the other account
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=835)

    - 9. 
    Retry with exponential backoff
    Use data key caching from the AWS Encryption SDK
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=843)

    - 10. 
    S3 Bucket Key
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=845)

    - 11. 
    AWS CloudHSM
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=849)

    - 12. 
    GetParametersByPath
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=856)

    - 13. 
    An advanced tier parameter with an ExpirationNotification parameter policy
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=858)

    - 14. 
    AWS Secrets Manager
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=861)

    - 15. 
    '{{resolve:ssm-secure:parameter-name:version}}'
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=864)

    - 16. 
    Use the CloudWatch Logs API associate-kms-key command
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=867)

    - 17. 
    Reference an SSM Parameter Store parameter or Secrets Manager secret in the CodeBuild environment variables
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=868)

    - 18. 
    AWS Nitro Enclaves
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=869)


    ### Wrong Answers:
    - 1. 
    Server-side encryption at rest
    Encryption in flight with TLS
    SSE-S3 encryption

    - 2. 
    Encrypt
    GenerateRandom
    ReEncrypt

    - 3. 
    64 KB
    1 MB
    16 KB

    - 4. 
    GenerateDataKey
    Encrypt
    GenerateRandom

    - 5. 
    A symmetric AES-256 KMS key, sharing the key material
    An AWS owned key
    An AWS managed key such as aws/s3

    - 6. 
    Customer managed KMS keys are rotated automatically every year by default without being enabled
    Imported KMS keys support automatic rotation every year
    AWS managed KMS keys can only be rotated manually

    - 7. 
    The snapshot keeps using the same KMS key, because KMS keys are global
    The snapshot is decrypted and stored unencrypted in the new Region
    The snapshot cannot be copied because encrypted snapshots cannot leave their Region

    - 8. 
    Nothing, because KMS keys can be used by any account by default
    Make the KMS key public
    Switch the snapshot to an AWS managed key such as aws/ebs

    - 9. 
    Switch from symmetric to asymmetric KMS keys
    Use a separate KMS key per request to avoid the shared quota
    Move the application to another AWS account

    - 10. 
    S3 Transfer Acceleration
    SSE-C encryption
    KMS automatic key rotation

    - 11. 
    AWS KMS with a customer managed key
    AWS Secrets Manager
    AWS KMS with an AWS managed key

    - 12. 
    GetParameter
    ListParameters
    GetSecretValue

    - 13. 
    A standard tier parameter with an ExpirationNotification parameter policy
    A standard tier SecureString parameter
    An advanced tier parameter with a NoChangeNotification policy only

    - 14. 
    SSM Parameter Store with a standard tier SecureString
    AWS KMS with a customer managed key
    AWS CloudHSM

    - 15. 
    '{{resolve:ssm:parameter-name:version}}'
    '{{resolve:secretsmanager:parameter-name}}'
    !GetAtt SSMParameter.Value

    - 16. 
    Select the KMS key in the CloudWatch console on the log group
    Enable encryption on the CloudWatch Logs service in the IAM console
    Delete and recreate the log group in the CloudWatch console with encryption enabled

    - 17. 
    Store the password as a plaintext environment variable in the project settings
    Store the password encrypted in the buildspec.yml file in the source repository
    Pass the password in the CodePipeline stage name

    - 18. 
    A Docker container on Amazon ECS with a task role
    AWS CloudHSM
    A dedicated EC2 host with an encrypted EBS volume
