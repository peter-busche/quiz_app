# Section 24: AWS CICD: CodeCommit, CodePipeline, CodeBuild, CodeDeploy ---> [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=700)
    ============================================================================================================================================================
- ### Questions:
    - 1. 
    A team of Developers are building a continuous integration and delivery pipeline using AWS Developer Tools. Which services should they use for running tests against source code and installing compiled code on their AWS resources? (Select TWO.)

    - 2. 
    An engineer wishes to share a software project they've developed with their team members for review. The shared application code needs to be preserved over time, with multiple versions and batch modifications being tracked. What is the most appropriate AWS service for this purpose?

    - 3. 
    A developer must deploy an update to Amazon ECS using AWS CodeDeploy. The deployment should expose 10% of live traffic to the new version. Then after a period of time, route all remaining traffic to the new version.
    Which ECS deployment should the company use to meet these requirements?

    - 4. 
    A company needs a version control system for collaborative software development. The solution must include support for batches of changes across multiple files and parallel branching.
    Which AWS service will meet these requirements?

    - 5. 
    A developer is creating a microservices application that includes and AWS Lambda function. The function generates a unique file for each execution and must commit the file to an AWS CodeCommit repository.
    How should the developer accomplish this?

    - 6. 
    A company uses continuous integration and continuous delivery (CI/CD) systems. A Developer needs to automate the deployment of a software package to Amazon EC2 instances as well as to on-premises virtual servers.
    Which AWS service can be used for the software deployment?

    - 7. 
    A firm intends to utilize AWS CodeDeploy to deploy an application to Amazon Elastic Container Service (Amazon ECS). While deploying an updated version of the application, the company's initial requirement is to direct 10% of active traffic to the updated application version. Following a 15-minute interval, all remaining active traffic must be rerouted to the updated application.
    Which predefined CodeDeploy configuration aligns with these needs?

    - 8. 
    A Development team is creating a microservices application running on Amazon ECS. The release process workflow of the application requires a manual approval step before the code is deployed into the production environment.
    What is the BEST way to achieve this using AWS CodePipeline?

    - 9. 
    A team of Developers have been assigned to a new project. The team will be collaborating on the development and delivery of a new application and need a centralized private repository for managing source code. The repository should support updates from multiple sources. Which AWS service should the development team use?

    - 10. 
    A Developer is deploying an update to a serverless application that includes AWS Lambda using the AWS Serverless Application Model (SAM). The traffic needs to move from the old Lambda version to the new Lambda version gradually, within the shortest period of time.
    Which deployment configuration is MOST suitable for these requirements?

    - 11. 
    A Developer has joined a team and needs to connect to the AWS CodeCommit repository using SSH. What should the Developer do to configure access using Git?

    - 12. 
    A company needs a fully-managed source control service that will work in AWS. The service must ensure that revision control synchronizes multiple distributed repositories by exchanging sets of changes peer-to-peer. All users need to work productively even when not connected to a network.
    Which source control service should be used?

    - 13. 
    A development team require a fully-managed source control service that is compatible with Git.
    Which service should they use?

    - 14. 
    A Developer needs to access AWS CodeCommit over SSH. The SSH keys configured to access AWS CodeCommit are tied to a user with the following permissions:
        {
        "version": "2012-10-17"
        "Statement": [
        {
        "Effect": "Allow",
        "Action": [
        "codecommit:BatchGetRepositories",
        "codecommit:Get*"
        "codecommit:List*",
        "codecommit:GitPull"
        ],
        "Resource": "*"
        }
        ]
        }
        The Developer needs to create/delete branches.
    Which specific IAM permissions need to be added based on the principle of least privilege?

    - 15. 
    A Development team have moved their continuous integration and delivery (CI/CD) pipeline into the AWS Cloud. The team is leveraging AWS CodeCommit for management of source code. The team need to compile their source code, run tests, and produce software packages that are ready for deployment.
    Which AWS service can deliver these outcomes?

    - 16. 
    A Developer is deploying an Amazon ECS update using AWS CodeDeploy. In the appspec.yaml file, which of the following is a valid structure for the order of hooks that should be specified?

    - 17. 
    A Developer is deploying an AWS Lambda update using AWS CodeDeploy. In the appspec.yaml file, which of the following is a valid structure for the order of hooks that should be specified?

    - 18. 
    A company has implemented AWS CodePipeline to automate its release pipelines. The Development team is writing an AWS Lambda function that will send notifications for state changes of each of the actions in the stages.
    Which steps must be taken to associate the Lambda function with the event source?

    - 19. 
    A developer is using AWS CodeBuild to build an application into a Docker image. The buildspec file is used to run the application build. The developer needs to push the Docker image to an Amazon ECR repository only upon the successful completion of each build.

    - 20. 
    A Development team would use a GitHub repository and would like to migrate their application code to AWS CodeCommit.
    What needs to be created before they can migrate a cloned repository to CodeCommit over HTTPS?

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
    AWS CodeBuild for running tests against source code
    AWS CodeDeploy for installing compiled code on their AWS resources
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=709)

    - 2. 
    AWS CodeCommit
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=706)

    - 3. 
    Blue/green with canary
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=724)

    - 4. 
    AWS CodeCommit
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=706)

    - 5. 
    Use an AWS SDK to instantiate a CodeCommit client. Invoke the PutFile method to add the file to the repository and execute a commit with CreateCommit.
    https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/codecommit/AWSCodeCommitClient.html

    - 6. 
    AWS CodeDeploy
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=718)

    - 7. 
    CodeDeployDefault.ECSCanary10Percent15Minutes
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=724)

    - 8. 
    Use an approval action in a stage before deployment
    https://docs.aws.amazon.com/codepipeline/latest/userguide/approvals.html

    - 9. 
    AWS CodeCommit
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=706)

    - 10. 
    CodeDeployDefault.LambdaCanary10Percent5Minutes
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=)

    - 11. 
    Generate an SSH public and private key. Upload the public key to the Developer’s IAM account
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=707)

    - 12. 
    AWS CodeCommit
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=705)

    - 13. 
    AWS CodeCommit
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=705)

    - 14. 
    “codecommit:CreateBranch” and “codecommit:DeleteBranch”
    https://docs.aws.amazon.com/cli/latest/reference/codecommit/index.html#cli-aws-codecommit

    - 15. 
    AWS CodeBuild
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=713)

    - 16. 
    BeforeInstall > AfterInstall > AfterAllowTestTraffic > BeforeAllowTraffic > AfterAllowTraffic
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=718)
    https://docs.aws.amazon.com/codedeploy/latest/userguide/reference-appspec-file-structure-hooks.html

    - 17. 
    BeforeAllowTraffic > AfterAllowTraffic
    https://docs.aws.amazon.com/codedeploy/latest/userguide/reference-appspec-file-structure-hooks.html

    - 18. 
    Create an Amazon CloudWatch Events rule that uses CodePipeline as an event source
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=712)

    - 19. 
    Add a post_build phase to the buildspec file that uses the commands block to push the Docker image.
    https://docs.aws.amazon.com/codebuild/latest/userguide/sample-docker.html
    https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html

    - 20. 
    A set of Git credentials generated with IAM
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=707)

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
    AWS CodeCommit for running tests against source code
    AWS CodePipeline for installing compiled code on their AWS resources
    AWS CodeArtifact for installing compiled code on their AWS resources

    - 2. 
    AWS CodeBuild
    AWS CodeDeploy
    AWS CodePipeline

    - 3. 
    Blue/green with all-at-once
    Blue/green with linear
    Rolling update with a minimum healthy percent of 10

    - 4. 
    AWS CodeBuild
    AWS CodePipeline
    AWS CodeArtifact

    - 5. 
    Use an AWS SDK to instantiate a CodeCommit client. Invoke the CreateRepository method to add the file and execute a commit with MergeBranchesByFastForward.
    Use the AWS CLI inside the function to run the git push command directly against the repository without any Git credentials.
    Upload the file to an Amazon S3 bucket and configure an S3 event notification to commit the file to CodeCommit automatically.

    - 6. 
    AWS CodeBuild
    AWS Elastic Beanstalk
    AWS CodeCommit

    - 7. 
    CodeDeployDefault.ECSLinear10PercentEvery3Minutes
    CodeDeployDefault.ECSCanary10Percent5Minutes
    CodeDeployDefault.ECSAllAtOnce

    - 8. 
    Use a test action in a stage before deployment
    Use an invoke action to pause the pipeline for a fixed period before deployment
    Use a source action that polls for a manual commit before deployment

    - 9. 
    AWS CodeBuild
    AWS CodeDeploy
    Amazon S3

    - 10. 
    CodeDeployDefault.LambdaLinear10PercentEvery10Minutes
    CodeDeployDefault.LambdaAllAtOnce
    CodeDeployDefault.LambdaCanary10Percent30Minutes

    - 11. 
    Generate an SSH public and private key. Upload the private key to the Developer's IAM account
    Generate an IAM access key ID and secret access key. Add them to the Developer's SSH config file
    Generate Git credentials in IAM. Upload them to the CodeCommit repository settings

    - 12. 
    AWS CodePipeline
    AWS CodeBuild
    Amazon S3 with versioning enabled

    - 13. 
    AWS CodeBuild
    AWS CodeArtifact
    AWS CodePipeline

    - 14. 
    “codecommit:Put*” and “codecommit:Update*”
    “codecommit:GitPush” and “codecommit:Update*”
    “codecommit:*”

    - 15. 
    AWS CodeDeploy
    AWS CodePipeline
    AWS CodeArtifact

    - 16. 
    ApplicationStop > BeforeInstall > AfterInstall > ApplicationStart > ValidateService
    BeforeAllowTraffic > AfterAllowTraffic
    BeforeInstall > AfterAllowTestTraffic > AfterInstall > AfterAllowTraffic > BeforeAllowTraffic

    - 17. 
    BeforeInstall > AfterInstall > AfterAllowTestTraffic > BeforeAllowTraffic > AfterAllowTraffic
    ApplicationStop > BeforeInstall > AfterInstall > ApplicationStart > ValidateService
    AfterAllowTraffic > BeforeAllowTraffic

    - 18. 
    Create an Amazon SNS topic subscription that uses CodePipeline as an event source
    Create a Lambda event source mapping that uses CodePipeline as an event source
    Create an AWS CloudTrail trail that invokes the Lambda function directly

    - 19. 
    Add a pre_build phase to the buildspec file that uses the commands block to push the Docker image.
    Add an install phase to the buildspec file that uses the commands block to push the Docker image.
    Add an artifacts section to the buildspec file that specifies the ECR repository as the destination.

    - 20. 
    An SSH key pair uploaded to the GitHub account
    An IAM access key ID and secret access key for the root user
    A personal access token generated in GitHub
