# Section 14: Amazon S3 Security ---> [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=261)
    ============================================================================================================================================================
- ### Questions:
    - 1. 
    A company uses an Amazon S3 bucket to store a large number of sensitive files relating to eCommerce transactions. The company has a policy that states that all data written to the S3 bucket must be encrypted.
    How can a Developer ensure compliance with this policy?

    - 2. 
    A company has transferred some of its confidential documents to a private Amazon S3 bucket that is not publicly accessible. Now, the company intends to build a serverless application that allows its staff to securely share these files with others.
    Which AWS service should the company utilize to ensure secure file sharing and access?

    - 3. 
    A static website is hosted on Amazon S3 using the bucket name of dctlabs.com. Some HTML pages on the site use JavaScript to download images that are located in the bucket https://dctlabsimages.s3.amazonaws.com/. Users have reported that the images are not being displayed.
    What is the MOST likely cause?

    - 4. 
    You run an ad-supported photo sharing website using Amazon S3 to serve photos to visitors of your site. At some point you find out that other sites have been linking to the photos on your site, causing loss to your business.
    What is an effective method to mitigate this?

    - 5. 
    An application is running on a fleet of EC2 instances running behind an Elastic Load Balancer (ELB). The EC2 instances session data in a shared Amazon S3 bucket. Security policy mandates that data must be encrypted in transit.
    How can the Developer ensure that all data that is sent to the S3 bucket is encrypted in transit?

    - 6. 
    The development team is experiencing issues with their application hosted on Amazon EC2 instances, as they are unable to connect to an Amazon S3 bucket during test runs.
    What should be the appropriate measures to resolve this issue? (Select TWO.)

    - 7. 
    A business is providing its clients read-only permissions to items within an Amazon S3 bucket, utilizing IAM permissions to limit access to this S3 bucket. Clients are only permitted to access their specific files. Regulatory compliance necessitates the enforcement of in-transit encryption during communication with Amazon S3.
    What solution will fulfill these criteria?

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
    Create an S3 bucket policy that denies any S3 Put request that does not include the x-amz-server-side-encryption
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=270)

    - 2. 
    S3 presigned URLs
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=277)

    - 3. 
    Cross Origin Resource Sharing is not enabled on the dctlabsimages bucket
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=271)

    - 4. 
    Remove public read access and use signed URLs with expiry dates
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=277)

    - 5. 
    Create an S3 bucket policy that denies traffic where SecureTransport is false
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=269)

    - 6. 
    Verify the IAM roles attached to the EC2 instances and ensure they have the necessary permissions to access the S3 bucket.
    Check the bucket policies for the Amazon S3 bucket and confirm that they permit access from the EC2 instances.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=270)

    - 7. 
    Update the S3 bucket policy to include a condition that requires aws:SecureTransport for all actions.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=269)

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
    Create an S3 bucket policy that denies any S3 Get request that does not include the x-amz-server-side-encryption
    Enable S3 Versioning and MFA Delete on the bucket to protect the data
    Create an S3 bucket policy that denies any request where aws:SecureTransport is false

    - 2. 
    S3 Transfer Acceleration
    S3 Cross-Region Replication
    S3 access logs

    - 3. 
    S3 Transfer Acceleration is not enabled on the dctlabsimages bucket
    Versioning is not enabled on the dctlabsimages bucket
    Static website hosting is not enabled on the dctlabs.com bucket

    - 4. 
    Enable Amazon S3 Transfer Acceleration on the bucket
    Use Amazon S3 Cross-Region Replication to copy the photos to another bucket
    Enable S3 Versioning and store the photos in S3 Glacier

    - 5. 
    Create an S3 bucket policy that denies traffic where x-amz-server-side-encryption is missing
    Enable default encryption with SSE-S3 on the S3 bucket
    Create an S3 bucket policy that allows traffic where SecureTransport is false

    - 6. 
    Enable S3 Transfer Acceleration on the bucket to improve connectivity from the EC2 instances.
    Enable S3 Versioning on the bucket so that the EC2 instances can access previous object versions.
    Configure Cross-Origin Resource Sharing (CORS) on the bucket to allow requests from the EC2 instances.

    - 7. 
    Update the S3 bucket policy to include a condition that requires s3:x-amz-server-side-encryption for all actions.
    Enable default encryption with SSE-KMS on the S3 bucket for all objects.
    Enable S3 Object Lock on the bucket in compliance mode for all objects.
