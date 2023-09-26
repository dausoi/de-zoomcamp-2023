## Week 1 Homework
Solution to [Data Engineering Zoomcamp Week 1](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2023/week_1_docker_sql/homework.md), with commands and queries used. 

If you find any mistake in the document, feel free to point out.

### Question 1
- Answer : `--iidfile string`
- Command used : `docker build --help`

### Question 2
- Answer : 3
- Command used in host machine : `docker run -it python:3.9 bash`
- Command used inside container : `pip list`

### Question 3
- Answer : 20530
- SQL query used :
```
SELECT COUNT(1) FROM taxi_trip
WHERE lpep_pickup_datetime::date = '2019-01-15'
AND lpep_dropoff_datetime::date = '2019-01-15';
```

### Question 4
- Answer : 2019-01-15
- SQL query used :
```
SELECT 	lpep_pickup_datetime::date AS trip_date, MAX(trip_distance) AS max_trip_distance 
FROM taxi_trip
GROUP BY lpep_pickup_datetime::date
ORDER BY 2 DESC;
```

### Question 5
- Answer : 2 is 1282 and 3 is 254
- SQL query used :
```
SELECT passenger_count, COUNT(1) as trip_count
FROM taxi_trip
WHERE lpep_pickup_datetime::date = '2019-01-01'
GROUP BY passenger_count
HAVING passenger_count IN (2, 3);
```

### Question 6
- Answer : Long Island City/Queens Plaza
- SQL query used :
```
SELECT tzp."Zone", tzd."Zone", MAX(tip_amount) AS max_tip
FROM taxi_trip tr
JOIN taxi_zone tzp ON tzp."LocationID" = tr."PULocationID"
JOIN taxi_zone tzd ON tzd."LocationID" = tr."DOLocationID"
GROUP BY tzp."Zone", tzd."Zone"
HAVING tzp."Zone" = 'Astoria'
ORDER BY 3 DESC;
```
