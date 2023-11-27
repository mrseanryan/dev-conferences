# lab-notes

```
git clone https://github.com/datamics/MLCon.git

pip3 install -r requirements.txt

cd 1_mlflow
mlflow ui
```

If mlflow not in path:

```
python3 /home/seanius/.local/lib/python3.10/site-packages/mlflow
```

2nd terminal:

```
python3 test_mlflow.py
```

Then refresh the MLflow UI -> the script should show up, with some metrics.

# WSL files on Windows

\\wsl$

e.g. = \\wsl.localhost\Ubuntu-22.04\home\seanius\src\github\others\MLCon


# basic ML training

```
python3 basic_ml_training.py
```

# mlflow

- can config to write to s3
- enterprise version from Databricks (user management)
-- https://docs.databricks.com/en/mlflow/index.html

## CI/CD

- bamboo pipeline

- web hooks are available to automate things like when a model is deployed to a different stage

- custom artifact store
-- can be a local dir (absolute path) OR S3

# serve model

## try fix python install issues (pip)

```
sudo apt-get install python-is-python3

virtualenv mlflow-1
export PATH="$HOME/.local/bin:$PATH"
```

## serve the model

# use --no-conda to avoid problem with conda re-installing Python!
```
~/.local/bin/mlflow  models serve --no-conda -m "models:/model_B/Staging" --port 5002
```

```
~/.local/bin/mlflow  models serve  -m "models:/model_B/Staging" --port 5002
```

OR

```
./go_mlflow.sh   models serve  -m "models:/model_name/stage" --port 5002
```

## custom MLFlow server

```
mlflow server --default-artifact-store <S3> --backend-store-ui  <DB-URI> --host 127.0.0.1 --port <port>
# in docker, would be 0.0.0.0 not 127.0.0.1

mlflow ui ---localhost:5000
```

