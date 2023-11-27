# README 

lab overview - see photo on iPhone (Dropbox)

tinyurl.com/mlcon-berlin

seans copy:
- https://docs.google.com/document/d/1po1VZQL3SuHdoDp1_m2yk8R7CAw20OGXRlR6IDbHXT4/edit#heading=h.w2b92xvdlc28

original:
- https://docs.google.com/document/d/1-9k_avvLNItteqQ1_nVhO30CfgHDgRNxtHCF3-noAS8/edit

https://github.com/datamics/MLCon

presented by datamics company

# MLflow

- OSS platform to manage ML

## Why MLflow:

- track experiments: can search by hyperparameters, arch, artifacts ...
-- MLflow tracking server

- reproducible runs
-- MLflow project (dependencies, config, code, data)

- complexity - handling tools and libraries
-- MLflow model - standard model format (equiv of ONNX?)

ONNX interop
- mlflow.onnx
- The mlflow.onnx module provides APIs for logging and loading ONNX models in the MLflow Model format
- https://mlflow.org/docs/latest/python_api/mlflow.onnx.html#:~:text=onnx%20module%20provides%20APIs%20for%20logging,MLflow%20Models%20with%20the%20following%20flavors%3A&text=onnx%20module%20provides%20APIs,with%20the%20following%20flavors%3A&text=provides%20APIs%20for%20logging,MLflow%20Models%20with%20the

- deployment manage
-- tracking server
-- model registry
--- lifecycle stages: exper, staging, prod, archived

# model monitoring (if need retraining)

https://docs.aporia.com/

- monitor model, to see if it needs re-training

- calculates the model drift (data drift)
- compares training vs inference (prod) to tell you if inference no longer agrees with training
-- e.g. a feature has a much different range that what was trained for
