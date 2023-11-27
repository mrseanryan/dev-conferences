import mlflow
from random import random, randint

run_description = """
### Header
This is a test **Bold**, *italic*, ~~strikethrough~~ text.
[And this is an example hayperlink](http://example.com/).
"""

with mlflow.start_run(description=run_description):
    
    mlflow.log_param("Loss", randint(0,100))
    mlflow.log_metric("Accuracy", randint(0,100))
    mlflow.log_metric("F1 score", randint(0,100))
    
    experiment_id = mlflow.create_experiment("New Experiment 3")
    # mlflow.delete_experiment(experiment_id)

    # Examine the deleted experiment details.
    experiment = mlflow.get_experiment(experiment_id)
    print(f"Name: {experiment.name}")
    mlflow.log_param("experiment_name", experiment.name)
    mlflow.log_param("artifact_location", experiment.artifact_location)

    print(f"Artifact Location: {experiment.artifact_location}")
    print(f"Lifecycle_stage: {experiment.lifecycle_stage}")
    print(f"Last Updated timestamp: {experiment.last_update_time}")
