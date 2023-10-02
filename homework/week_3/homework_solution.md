## Week 2 Homework
Solution to [Data Engineering Zoomcamp Week 2](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2023/week_2_workflow_orchestration/homework.md), with commands and queries used. 

If you find any mistake in the document, feel free to point out.

### Question 1
- Answer : 43,244,696

### Question 2
- Answer : 0 MB for the External Table and 317.94MB for the BQ Table
- Code used :
```
-- Scans 317.94 MB
SELECT DISTINCT Affiliated_base_number FROM `de-zoomcamp-400010.trip_data_all.fhv_2019`;
-- Scans 0 B
SELECT DISTINCT Affiliated_base_number FROM `de-zoomcamp-400010.trip_data_all.external_fhv_2019`;
```

### Question 3
- Answer : 717,748

### Question 4
- Answer : Partition by pickup_datetime / Cluster on affiliated_base_number

### Question 5
- Answer : 647.87 MB for non-partitioned table and 23.06 MB for the partitioned table
- Code used :
```
-- Create new table with partitioning and clustering; Takes 1.92 GB
CREATE OR REPLACE TABLE `de-zoomcamp-400010.trip_data_all.partitioned_fhv_2019`
PARTITION BY DATE(pickup_datetime)
CLUSTER BY affiliated_base_number AS
  SELECT * FROM `de-zoomcamp-400010.trip_data_all.fhv_2019`;

-- Estimate 647.87 MB / Actual 647.87 MB
SELECT DISTINCT affiliated_base_number FROM `de-zoomcamp-400010.trip_data_all.fhv_2019` WHERE pickup_datetime BETWEEN '2019-03-01' AND '2019-03-31';
-- Estimate  23.05 MB/ Actual 23.05 MB
SELECT DISTINCT affiliated_base_number FROM `de-zoomcamp-400010.trip_data_all.partitioned_fhv_2019` WHERE pickup_datetime BETWEEN '2019-03-01' AND '2019-03-31';
```

### Question 6
- Answer : GCP Bucket

### Question 7
- Answer : False (You should cluster your table when the size of the table is above 1 GB)
