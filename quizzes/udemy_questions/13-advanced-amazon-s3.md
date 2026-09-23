# Section 13: Advanced Amazon S3 ---> [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=248)
    ============================================================================================================================================================
- ### Questions:
    - 1. 
    An application reads data from Amazon S3 and makes 55,000 read requests per second. A Developer must design the storage solution to ensure the performance requirements are met cost-effectively.
    How can the storage be optimized to meet these requirements?

    - 2. 
    Data must be loaded into an application each week for analysis. The data is uploaded to an Amazon S3 bucket from several offices around the world. Latency is slowing the uploads and delaying the analytics job. What is the SIMPLEST way to improve upload times?

    - 3. 
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
    Create at least 10 prefixes and split the files across the prefixes.
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=257)

    - 2. 
    Upload using Amazon S3 Transfer Acceleration
    [AWS Developer Slides](AWS_Certified_Developer_Slides_v45.pdf#page=258)

    - 3. 
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
    Store all the files under a single prefix to maximize request throughput.
    Enable Amazon S3 Transfer Acceleration on the bucket.
    Move the files to the S3 Glacier Flexible Retrieval storage class.

    - 2. 
    Upload using Amazon S3 Cross-Region Replication
    Upload using Amazon S3 Byte-Range Fetches
    Upload using Amazon S3 Select
