# Section 18: AWS CloudFormation ---> [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=379)
    ============================================================================================================================================================
- ### Questions:
    - 1. 
    To include objects defined by the AWS Serverless Application Model (SAM) in an AWS CloudFormation template, in addition to Resources, what section MUST be included in the document root?

    - 2. 
    The source code for an application is stored in a file named index.js that is in a folder along with a template file that includes the following code:
        AWSTemplateFormatVersion: '2010-09-09'
        Transform: 'AWS::Serverless-2016-10-31'
        Resources:
        LambdaFunctionWithAPI:
        Type: AWS::Serverless::Function
        Properties:
        Handler: index.handler
        Runtime: nodejs12.x
    What does a Developer need to do to prepare the template so it can be deployed using an AWS CLI command?

    - 3. 
    How can a Developer view a summary of proposed changes to an AWS CloudFormation stack without implementing the changes in production?

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
    Transform
    https://digitalcloud.training/aws-sam/

    - 2. 


    - 3. 
    Create a Change Set
    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.html

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
    Parameters
    Mappings
    Metadata

    - 3. 
    Create a StackSet
    Run drift detection
    Create a stack policy
