## Week 4 Homework
Solution to [Data Engineering Zoomcamp Week 4](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2023/week_4_analytics_engineering/homework.md), with commands and queries used. 

If you find any mistake in the document, feel free to point out.

### Question 1
- Answer : 61,648,442
- Note: My dataset gives 61xxxxxx.

### Question 2
- Answer : 89.9/10.1
- See my Looker Studio Report (my beautiful report)

### Question 3
- Answer : 43,244,696 (exact number)
- Code used:
```
SELECT COUNT(1) 
  FROM `de-zoomcamp-400010.dbt_zoomcamp_cloud.stg_fhv_tripdata` 
  WHERE EXTRACT(YEAR FROM pickup_datetime) = 2019;
```

### Question 4
- Answer : 22,998,722 (exact number)
- Code used:
```
SELECT COUNT(1)
  FROM `de-zoomcamp-400010.dbt_zoomcamp_cloud.fact_fhv_trips`
  WHERE EXTRACT(YEAR FROM pickup_datetime) = 2019;
```

### Question 5
- Answer : January
- Note: See my Looker Studio Report, although you can see that number of trips is heavily skewed to January, which is to be investigated.
