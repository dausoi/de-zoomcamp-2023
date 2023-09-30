## Week 2 Homework
Solution to [Data Engineering Zoomcamp Week 2](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2023/week_2_workflow_orchestration/homework.md), with commands and queries used. 

If you find any mistake in the document, feel free to point out.

### Question 2
- Answer : 447,770
- Code used : From `etl_web_to_gcs.py` with slight modifications, e.g. changing from `tpep-pickup-datetime` to `lpep-pickup-datetime`.

### Question 2
- Answer : `0 5 1 * *`

### Question 3
- Answer : 14,851,920

### Question 4
- Answer : 88,605
- Code used for local deployment ( :
```
from prefect.filesystems import GitHub
import prefect.deployments 

def main(dep_name, flow_name):
    github_storage = GitHub.load("my-github-cred")
    deployment = prefect.deployments.Deployment(
        name=dep_name,
        storage=github_storage,
        entrypoint=f"flows/web_to_gcs.py:{flow_name}",
        flow_name=flow_name,
        parameters={"color":"green", "year": 2020, "month": 11}
    )
    deployment.apply()
    prefect.deployments.run_deployment(f"{flow_name}/{dep_name}")


if __name__ == "__main__":
    main("github-deployment", "etl_web_to_gcs")
```
