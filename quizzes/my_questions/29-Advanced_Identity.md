# Section 29: My Questions: Advanced Identity ---> [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=804)
    ============================================================================================================================================================
- ### Questions:
    - 1. 
    A developer in Account A needs temporary access to an S3 bucket in Account B. An IAM role in Account B trusts Account A.
    Which STS API should the developer call to get temporary credentials for that role?

    - 2. 
    A developer receives an "encoded authorization failure message" after an AWS API call is denied, and wants to read the details of why it failed.
    Which STS API should they use?

    - 3. 
    A script needs to confirm which IAM user or role it is currently using to make AWS API calls.
    Which STS API returns this information?

    - 4. 
    A company wants users to be able to call sensitive APIs only after they authenticate with MFA. Users will get temporary credentials after entering an MFA code. (Select TWO.)

    - 5. 
    A mobile app lets users sign in with Google or Facebook and then needs temporary AWS credentials. AWS STS offers AssumeRoleWithWebIdentity for this.
    What does AWS recommend using instead?

    - 6. 
    What is the valid duration range for temporary credentials returned by the STS AssumeRole API (per the course)?

    - 7. 
    An on-premises server needs to call AWS APIs. What is the recommended best practice for its credentials?

    - 8. 
    An EC2 instance role allows read/write access to my_bucket. The bucket policy on my_bucket explicitly denies that role.
    What is the result?

    - 9. 
    An EC2 instance role has NO S3 permissions. The bucket policy on my_bucket explicitly allows read/write to that role.
    What is the result?

    - 10. 
    In simplified IAM policy evaluation, which order is followed?

    - 11. 
    A company wants every IAM user to have access only to their own /home/<username>/ folder in an S3 bucket, using a single IAM policy.
    What should they use in the policy?

    - 12. 
    A team wants a permissions policy that can be reused by many IAM roles, supports versioning and rollback, and is centrally managed.
    Which type of policy is the best practice?

    - 13. 
    What happens to an inline policy when the IAM user it is attached to is deleted?

    - 14. 
    A developer tries to create a Lambda function and assign it an existing IAM execution role, but gets an AccessDenied error.
    Which IAM permission is the developer MOST likely missing?

    - 15. 
    A developer has iam:PassRole permission but still cannot pass a role to an AWS service. What else must be true for the role to be passed to that service?

    - 16. 
    A company wants users managed in its on-premises Microsoft Active Directory to sign in to AWS applications, without storing or syncing any users in AWS.
    Which AWS Directory Service option should they use?

    - 17. 
    A company needs a managed Active Directory in AWS where users are managed locally, with MFA support and a trust relationship with its on-premises AD.
    Which option should they use?


    ### Answers:
    - 1. 
    AssumeRole
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=806)

    - 2. 
    DecodeAuthorizationMessage
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=805)

    - 3. 
    GetCallerIdentity
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=805)

    - 4. 
    Call the STS GetSessionToken API with the MFA code
    Use an IAM policy condition of aws:MultiFactorAuthPresent: true
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=808)

    - 5. 
    Amazon Cognito Identity Pools
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=805)

    - 6. 
    15 minutes to 1 hour
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=806)

    - 7. 
    Call STS to obtain temporary security credentials
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=809)

    - 8. 
    The EC2 instance cannot read or write to my_bucket
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=815)

    - 9. 
    The EC2 instance can read and write to my_bucket
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=816)

    - 10. 
    If any explicit DENY, deny; otherwise if any ALLOW, allow; otherwise deny
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=812)

    - 11. 
    The ${aws:username} policy variable
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=818)

    - 12. 
    Customer managed policy
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=820)

    - 13. 
    The inline policy is deleted along with the user
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=820)

    - 14. 
    iam:PassRole
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=821)

    - 15. 
    The role's trust policy must allow that service to assume the role
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=823)

    - 16. 
    AD Connector
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=825)

    - 17. 
    AWS Managed Microsoft AD
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=825)


    ### Wrong Answers:
    - 1. 
    GetSessionToken
    GetFederationToken
    AssumeRoleWithSAML

    - 2. 
    GetCallerIdentity
    GetSessionToken
    kms:Decrypt

    - 3. 
    DecodeAuthorizationMessage
    GetSessionToken
    iam:GetRole

    - 4. 
    Call the STS AssumeRoleWithWebIdentity API with the MFA code
    Use an IAM policy condition of aws:SecureTransport: true
    Store the MFA code in the user's access key

    - 5. 
    Amazon Cognito User Pools with STS GetFederationToken
    IAM users created for each mobile user
    AWS Directory Service AD Connector

    - 6. 
    1 minute to 15 minutes
    1 hour to 12 hours
    Credentials never expire until revoked

    - 7. 
    Store an IAM user's access keys in a config file on the server
    Hard-code the root account access keys in the application
    Attach an EC2 instance profile to the on-premises server

    - 8. 
    The EC2 instance can read and write to my_bucket because the IAM role allows it
    The EC2 instance can read but not write to my_bucket
    The result depends on which policy was created first

    - 9. 
    The EC2 instance cannot access my_bucket because the IAM role has no S3 permissions
    The EC2 instance can only read from my_bucket
    The request is denied unless the role also has an explicit allow

    - 10. 
    If any ALLOW, allow; otherwise if any explicit DENY, deny; otherwise allow
    The most recently attached policy always wins
    Resource policies are evaluated first and override IAM policies

    - 11. 
    One IAM policy per user, each hard-coding the user's folder
    The ${aws:PrincipalTag} variable with an S3 access point per user
    An S3 bucket ACL granting each user their own prefix

    - 12. 
    AWS managed policy
    Inline policy
    S3 bucket policy

    - 13. 
    The inline policy is moved to the user's group
    The inline policy is kept and can be reattached to another user
    The inline policy becomes a customer managed policy

    - 14. 
    iam:GetRole
    lambda:InvokeFunction
    sts:GetSessionToken

    - 15. 
    The developer must be the root user of the account
    The role must have an inline policy attached
    The service must be in the same Region as the IAM role

    - 16. 
    Simple AD
    AWS Managed Microsoft AD with users synced to AWS
    Amazon Cognito User Pools

    - 17. 
    Simple AD
    AD Connector
    Amazon Cognito Identity Pools
