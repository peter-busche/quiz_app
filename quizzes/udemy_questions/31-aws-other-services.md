# Section 31: AWS Other Services ---> [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=871)
    ============================================================================================================================================================
- ### Questions:
    - 1. 
    An international research organization holds a wide range of data across several Amazon S3 buckets. They recently received an alert indicating potential exposure of sensitive financial data via a public-facing web portal. The developer's job is to trace all potential data leakage points across their AWS infrastructure.
    What is the most effective strategy for this task?

    - 2. 
    A developer is looking to verify that redirects are performing as expected. What is the most efficient way that the developer can access the web logs and perform an analysis on them?

    - 3. 
    A developer is partitioning data using Athena to improve performance when performing queries. What are two things the analyst can do that would counter any benefit of using partitions? (Select TWO.)

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
    Implement Amazon Macie and apply the SensitiveData:S3Object/financial finding type across all S3 buckets to automatically identify potential exposure of sensitive financial data.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=886)

    - 2. 
    Store the logs in a S3 bucket and use Athena to run SQL queries.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=877)

    - 3. 
    Segmenting data too finely.
    Skewing data heavily to one partition value.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=878)

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
    Implement Amazon GuardDuty and apply the Recon:IAMUser/UserPermissions finding type across all S3 buckets to automatically identify potential exposure of sensitive financial data.
    Implement Amazon Inspector and run a network reachability assessment across all S3 buckets to automatically identify potential exposure of sensitive financial data.
    Implement AWS Trusted Advisor and run the S3 bucket permissions check to automatically classify sensitive financial data within all S3 objects.

    - 2. 
    Store the logs in an Amazon RDS database and use Amazon Kinesis to run SQL queries.
    Store the logs on an EBS volume and use AWS Glue DataBrew to replay the redirects.
    Store the logs in Amazon ElastiCache and use AWS X-Ray to run SQL queries.

    - 3. 
    Filtering queries on the partition key column.
    Storing the data in a columnar format such as Apache Parquet.
    Choosing a partition key that is frequently used in WHERE clauses.
