# Section 27: Cognito: Cognito User Pools, Cognito Identity Pools & Cognito Sync ---> [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=757)
    ============================================================================================================================================================
- ### Questions:
    - 1. 
    A company is creating an application that will require users to access AWS services and allow them to reset their own passwords. Which of the following would allow the company to manage users and authorization while allowing users to reset their own passwords?

    - 2. 
    A Developer has created an Amazon Cognito user pool and configured a domain for it. The Developer wants to add sign-up and sign-in pages to an app with a company logo.
    What should the Developer do to meet these requirements?

    - 3. 
    An application developer is crafting a new software product. To streamline the registration process, they want new users to be able to set up their accounts using their existing social media profiles.
    Which AWS service or feature would be the most appropriate for achieving this goal?

    - 4. 
    A development team are creating a mobile application that customers will use to receive notifications and special offers. Users will not be required to log in.
    What is the MOST efficient method to grant users access to AWS resources?

    - 5. 
    A mobile application has hundreds of users. Each user may use multiple devices to access the application. The Developer wants to assign unique identifiers to these users regardless of the device they use.
    Which of the following methods should be used to obtain unique identifiers?

    - 6. 
    A Developer is writing a web application that allows users to view images from an Amazon S3 bucket. The users will log in with their Amazon login, as well as Facebook and/or Google accounts.
    How can the Developer provide this authentication capability?

    - 7. 
    A Developer is creating a banking application that will be used to view financial transactions and statistics. The application requires multi-factor authentication to be added to the login protocol.
    Which service should be used to meet this requirement?
     
    - 8. 
    A Developer is creating a web application that will be used by employees working from home. The company uses a SAML directory on-premises for storing user information. The Developer must integrate with the SAML directory and authorize each employee to access only their own data when using the application.
    Which approach should the Developer take?

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
    Amazon Cognito user pools and identity pools
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=757)

    - 2. 
    Customize the Amazon Cognito hosted web UI and add the company logo.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=779)

    - 3. 
    Amazon Cognito User Pools
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=759)

    - 4. 
    Use Amazon Cognito to associate unauthenticated users with an IAM role that has limited access to resources
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=775)

    - 5. 
    Implement developer-authenticated identities by using Amazon Cognito, and get credentials for these identities
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=775)

    - 6. 
    Use Amazon Cognito with web identity federation
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=772)

    - 7. 
    Amazon Cognito User Pool with MFA
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=759)
    
    - 8. 
    Use an Amazon Cognito identity pool, federate with the SAML provider, and use a trust policy with an IAM condition key to limit employee access.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=)

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
    AWS IAM users and IAM groups
    AWS Directory Service Simple AD
    AWS STS with SAML 2.0 federation

    - 2. 
    Create a custom Amazon S3 static website with the company logo and link it to the IAM console sign-in page.
    Customize the Amazon Cognito identity pool authentication flow and add the company logo.
    Use AWS Amplify to replace the Cognito user pool domain with an AWS IAM Identity Center portal and add the company logo.

    - 3. 
    AWS IAM Identity Center
    AWS Directory Service
    AWS STS GetFederationToken

    - 4. 
    Create an IAM user for each customer and embed the access keys in the application
    Use Amazon Cognito user pools to require users to sign up before accessing resources
    Use a single set of root account access keys stored in the application code

    - 5. 
    Create an IAM user for each device and use the IAM user ID as the identifier
    Use the device's hardware serial number as the identifier and store it in Amazon DynamoDB
    Generate a random UUID on each device at install time and use it as the identifier

    - 6. 
    Use AWS IAM Identity Center with SAML 2.0 federation
    Create IAM users for each person and map them to their social accounts
    Use Amazon S3 bucket policies that reference the social account IDs

    - 7. 
    AWS IAM with virtual MFA for each application user
    Amazon Cognito identity pool with unauthenticated access
    AWS Directory Service Simple AD

    - 8. 
    Create an IAM user for each employee and attach a policy that limits access to their own data.
    Use an Amazon Cognito identity pool with unauthenticated access enabled and a single shared IAM role for all employees.
    Use AWS STS GetSessionToken with the on-premises SAML credentials and attach a resource-based policy to each object.
