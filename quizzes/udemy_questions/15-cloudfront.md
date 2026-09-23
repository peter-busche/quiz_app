# Section 15: CloudFront ---> [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=281)
    ============================================================================================================================================================
- ### Questions:
    - 1. 
    An application uses an Auto Scaling group of Amazon EC2 instances, an Application Load Balancer (ALB), and an Amazon Simple Queue Service (SQS) queue. An Amazon CloudFront distribution caches content for global users. A Developer needs to add in-transit encryption to the data by configuring end-to-end SSL between the CloudFront Origin and the end users.
    How can the Developer meet this requirement? (Select TWO.)

    - 2. 
    A company is using Amazon CloudFront to provide low-latency access to a web application to its global users. The organization must encrypt all traffic between users and CloudFront, and all traffic between CloudFront and the web application.
    How can these requirements be met? (Select TWO.)

    - 3. 
    A website is being delivered using Amazon CloudFront and a Developer recently modified some images that are displayed on website pages. Upon testing the changes, the Developer noticed that the new versions of the images are not displaying.
    What should the Developer do to force the new images to be displayed?

    - 4. 
    An online retail platform uses the AWS SDK for Python (Boto3) on the frontend to handle user authentication through AWS Security Token Service (AWS STS). The platform stores its digital assets in an Amazon S3 bucket and delivers them using an Amazon CloudFront distribution, which uses the S3 bucket as its origin.
    Currently, the application holds its role credentials in plaintext within a Python file in the application code. The platform developers are looking to improve security by creating a mechanism that enables the application to retrieve user credentials without embedding any credentials in the application code.
    What solution would meet these requirements?

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
    Configure the Origin Protocol Policy
    Configure the Viewer Protocol Policy
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=283)
    https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html

    - 2. 
    Set the Origin Protocol Policy to “HTTPS Only”
    Set the Viewer Protocol Policy to “HTTPS Only” or “Redirect HTTP to HTTPS”
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=283)
    https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html

    - 3. 
    Invalidate the old versions of the images on the edge caches
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=294)

    - 4. 
    Integrate a Lambda@Edge function with the CloudFront distribution. Trigger the function upon each viewer request. Give the execution role of the function the required permissions to interact with AWS STS. Shift all SDK calls from the frontend to this function.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=567)

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
    Configure the Cache Behavior TTL settings
    Configure the Price Class of the distribution
    Configure Origin Access Control on the SQS queue

    - 2. 
    Set the Origin Protocol Policy to “Match Viewer” with viewers allowed to use HTTP
    Set the Viewer Protocol Policy to “HTTP and HTTPS”
    Set the Origin Protocol Policy to “HTTP Only”

    - 3. 
    Enable versioning on the CloudFront distribution
    Increase the TTL of the cached images on the edge caches
    Disable and re-enable the Amazon S3 origin bucket

    - 4. 
    Move the role credentials from the Python file into environment variables in the frontend application code. Continue to call AWS STS from the frontend using the SDK.
    Store the role credentials in a public object in the S3 origin bucket. Configure the frontend to download the credentials through the CloudFront distribution before each SDK call.
    Add the role credentials as custom headers on the CloudFront distribution origin. Configure the frontend to read the headers and pass them to AWS STS on each request.
