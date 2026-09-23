# Section 23: AWS Serverless: API Gateway ---> [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=656)
- ### Questions:
    - 1. 
    A company is releasing an updated version of its APIs for its new mobile application, which uses Amazon API Gateway. The developers aim to gradually and seamlessly roll out the new version of APIs.
    What is the MOST straightforward method for them to introduce the new API version to a subset of users through API Gateway?

    - 2. 
    A customer requires a schema-less, key/value database that can be used for storing customer orders. Which type of AWS database is BEST suited to this requirement?

    - 3. 
    An Amazon API Gateway API developer aims to integrate request validation in a production setting but wants to test it before deployment. Which of the following methods offers the least operational overhead for testing via a tool by sending test requests?

    - 4. 
    A Development team are creating a new REST API that uses Amazon API Gateway and AWS Lambda. To support testing there need to be different versions of the service. What is the BEST way to provide multiple versions of the REST API?

    - 5. 
    A legacy service has an XML-based SOAP interface. The Developer wants to expose the functionality of the service to external clients with the Amazon API Gateway. Which technique will accomplish this?

    - 6. 
    A company wants to implement authentication for its new REST service using Amazon API Gateway. To authenticate the calls, each request must include HTTP headers with a client ID and user ID. These credentials must be compared to authentication data in an Amazon DynamoDB table.
    What MUST the company do to implement this authentication in API Gateway?

    - 7. 
    A company is creating a REST service using an Amazon API Gateway with AWS Lambda integration. The service must run different versions for testing purposes.
    What would be the BEST way to accomplish this?

    - 8. 
    A set of APIs are exposed to customers using Amazon API Gateway. These APIs have caching enabled on the API Gateway. Customers have asked for an option to invalidate this cache for each of the APIs.
    What action can be taken to allow API customers to invalidate the API Cache?

    - 9. 
    A company is providing APIs as a web-based service to allow anonymous access to daily updated statistical data, using Amazon API Gateway and AWS Lambda for API development. The service's popularity has grown, and the company aims to improve the API responsiveness.
    What measure should the company undertake to fulfill this objective?

    - 10. 
    A Developer has deployed an AWS Lambda function and an Amazon DynamoDB table. The function code returns data from the DynamoDB table when it receives a request. The Developer needs to implement a front end that can receive HTTP GET requests and proxy the request information to the Lambda function.
    What is the SIMPLEST and most COST-EFFECTIVE solution?

    - 11. 
    A software organization has developed a new feature in its serverless application hosted on AWS. This feature involves an AWS Lambda function that gets invoked by an Amazon API Gateway API. Currently, the API uses a specific Lambda alias to invoke the Lambda function. The organization wants to roll out this new feature to a select group of users for beta testing without affecting the application's existing users.
    What would be the most efficient approach to meet these requirements?

    - 12. 
    An online multiplayer game employs Amazon API Gateway WebSocket APIs with an HTTP backend. The game developer needs to add a feature that identifies players with unstable connections who repeatedly join and leave the game. The developer also wants the ability to disconnect such players from the game.
    What two modifications should the developer implement in the game to fulfill these requirements? (Select TWO.)

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
    - 1. Utilize the canary release deployment feature in API Gateway. Configure the canarySettings to redirect a portion of the API traffic.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=667)

    - 2. Amazon DynamoDB
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=607)

    - 3. 
    Modify the existing API to include request validation, deploy this to a new API Gateway stage, test it, then deploy it to the production stage.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=666)

    - 4. 
    Deploy the API versions as unique stages with unique endpoints and use stage variables to provide further context
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=666)

    - 5. 
    Create a RESTful API with the API Gateway; transform the incoming JSON into a valid XML message for the SOAP interface using mapping templates
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=672)

    - 6. 
    Implement an AWS Lambda authorizer that references the DynamoDB authentication table
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=690)

    - 7. 
    Deploy the API version as unique stages with unique endpoints and use stage variables to provide further context
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=663)

    - 8. 
    Ask customers to pass an HTTP header called Cache-Control:max-age=0
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=678)

    - 9. 
    Activate caching in API Gateway.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=667)

    - 10. 
    Implement an API Gateway API with Lambda proxy integration
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=669)

    - 11. 
    Create a new version of the Lambda function. Build a new stage on API Gateway integrated with this new Lambda version. Utilize this new API Gateway stage for beta testing.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=666)

    - 12. 
    Implement $connect and $disconnect routes in the backend service.
    Add logic to track the player's connection status using Amazon DynamoDB in the backend service.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=698)
    https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-route-keys-connect-disconnect.html

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
    Use stage variables in API Gateway to route all API traffic to the new version immediately.
    Create a usage plan in API Gateway and associate a subset of API keys with the new API version.
    Enable API caching in API Gateway and configure a cache TTL to redirect a portion of the API traffic.

    - 2. 
    Amazon RDS
    Amazon Redshift
    Amazon Aurora

    - 3. 
    Deploy the API with request validation directly to the production stage and monitor Amazon CloudWatch Logs for validation errors.
    Create a new AWS account, rebuild the entire API with request validation, and test it using AWS X-Ray traces before migrating.
    Export the API as an OpenAPI file, import it into a local API emulator on an EC2 instance, and test request validation there.

    - 4. 
    Create a separate AWS account for each API version and use cross-account IAM roles to provide further context
    Deploy each API version to the same stage and use Lambda environment variables to switch between versions
    Create a usage plan for each API version and use API keys to route requests to the correct version

    - 5. 
    Create a WebSocket API with the API Gateway; forward the incoming JSON directly to the SOAP interface using a Lambda authorizer
    Create a RESTful API with the API Gateway; pass the incoming JSON to the SOAP interface unchanged using an HTTP proxy integration
    Create an HTTP API with the API Gateway; convert the incoming JSON into XML for the SOAP interface using request validators

    - 6. 
    Configure an Amazon Cognito user pool authorizer that references the DynamoDB authentication table
    Use IAM authorization and add the client ID and user ID to an IAM policy for each caller
    Enable API keys on the method and store the client ID and user ID in a usage plan

    - 7. 
    Deploy each API version to a separate AWS Region and use Amazon Route 53 weighted records to provide further context
    Deploy a single stage and use Lambda environment variables to switch between versions for testing
    Create separate usage plans for each version and use API keys to provide further context

    - 8. 
    Ask customers to pass a query string parameter called cache=invalidate
    Ask customers to call the CloudFront CreateInvalidation API for the API endpoint
    Ask customers to pass an HTTP header called X-Amz-Cache-Invalidate:true

    - 9. 
    Enable request validation in API Gateway.
    Activate usage plans with API keys in API Gateway.
    Increase the Lambda function timeout setting.

    - 10. 
    Implement an Application Load Balancer in front of EC2 instances that call the Lambda function
    Implement an Amazon CloudFront distribution with an Amazon S3 origin that stores the DynamoDB data
    Implement an Amazon EC2 instance running NGINX as a reverse proxy to the Lambda function

    - 11. 
    Update the existing Lambda alias to point to the new function version. Keep using the existing API Gateway stage for beta testing.
    Publish the new code to the $LATEST version of the Lambda function. Point the production API Gateway stage at $LATEST for beta testing.
    Create a new Lambda function in a different Region. Update the production API Gateway stage to invoke it directly for beta testing.

    - 12. 
    Implement a $default route only and let API Gateway track connection status automatically.
    Configure an API Gateway usage plan to throttle players with unstable connections.
    Enable API Gateway caching on the WebSocket API to store each player's connection status.
