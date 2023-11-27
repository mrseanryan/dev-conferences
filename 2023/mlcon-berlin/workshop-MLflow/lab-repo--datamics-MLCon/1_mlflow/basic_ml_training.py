import mlflow
import pandas as pd
import numpy as np

from sklearn.linear_model import ElasticNet
from sklearn.model_selection import train_test_split
from sklearn import metrics

import matplotlib.pyplot as plt
import seaborn as sns

from PIL import Image

# load data

df = pd.read_csv("../data/winequality.csv")

print(df.head())
print(df.info())

# histogram of 'quality' field
sns.histplot(df['quality'])

# look for what influences quality - corellation metrics
corr = df.corr()

f, ax = plt.subplots(figsize=(6,5))

#snd heatmap
sns.heatmap(corr, center=0, square=True, linewidths=0.5)
plt.show()
plot_filename = 'quality_corr.png'
print(f"Saving plot to {plot_filename}")
plt.savefig(plot_filename)
print(" - Quality correlates with Alcohol and Volatile acidity ?")

# training set
X = df.drop('quality', axis = 1)
Y = df['quality']

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.25, random_state=43)

print(df.shape)

print(X_train.shape)

print(X_test.shape)

def fig2img(fig):
    """Convert a Matplotlib figure to a PIL Image and return it"""
    import io
    buf = io.BytesIO()
    fig.savefig(buf)
    buf.seek(0)
    img = Image.open(buf)
    return img

# mlflow loggin
with mlflow.start_run():

    # training
    alpha = 0.5
    l1 = 0.5

    # linear regression model
    lr = ElasticNet(alpha=alpha, l1_ratio=l1)

    lr.fit(X_train, y_train)

    def eval_metrics(ground_truth, pred):
        rmse = np.sqrt(metrics.mean_squared_error(ground_truth, pred))
        mae = metrics.mean_absolute_error(ground_truth, pred)
        r2 = metrics.r2_score(ground_truth, pred)

        return rmse, mae, r2

    # inference
    y_pred = lr.predict(X_train)
    print(y_pred.shape)

    rmse, mae, r2 = eval_metrics(y_train, y_pred)

    print(f"Out metrics: RMSE = {rmse}, MAE = {mae}, R2 = {r2}")
    # then you would adjust until you see good metrics

    # logged hyperparameters
    mlflow.log_param("alpha", alpha)
    mlflow.log_param("l1 ratio", l1)

    # logged metrics
    mlflow.log_metric("rmse", rmse)
    mlflow.log_metric("mae", mae)
    mlflow.log_metric("r2", r2)

    fig = plt.gcf()
    img = fig2img(fig)
    # TODO log image
    #mlflow.log_image(img, "quality_corr.png")

# create new experiment, custom run name, tags

experiment_name = "exp-1b"
run_name = "first mlflow custom run B"
tags = {
    "Demo": "True",
    "Created by": "Sean",
}
mlflow.set_experiment(experiment_name) # will create if needed, else re-use
# experiment changes the artifact store

# mlflow loggin
with mlflow.start_run(run_name = run_name):

    # training
    alpha = 0.5
    l1 = 0.5

    # linear regression model
    lr = ElasticNet(alpha=alpha, l1_ratio=l1)

    lr.fit(X_train, y_train)

    def eval_metrics(ground_truth, pred):
        rmse = np.sqrt(metrics.mean_squared_error(ground_truth, pred))
        mae = metrics.mean_absolute_error(ground_truth, pred)
        r2 = metrics.r2_score(ground_truth, pred)

        return rmse, mae, r2

    # inference
    y_pred = lr.predict(X_train)
    print(y_pred.shape)

    rmse, mae, r2 = eval_metrics(y_train, y_pred)

    print(f"Out metrics: RMSE = {rmse}, MAE = {mae}, R2 = {r2}")
    # then you would adjust until you see good metrics

    # logged hyperparameters
    mlflow.log_param("alpha", alpha)
    mlflow.log_param("l1 ratio", l1)

    # logged metrics
    mlflow.log_metric("rmse", rmse)
    mlflow.log_metric("mae", mae)
    mlflow.log_metric("r2", r2)

    fig = plt.gcf()
    img = fig2img(fig)
    # TODO log image
    #mlflow.log_image(img, "quality_corr.png")

    mlflow.set_tags(tags)

##### auto logging

# if pytorch, use mlflow.pytorch ...
mlflow.sklearn.autolog(log_models = True)

experiment_name = "exp-1c - auto logging"
run_name = "first mlflow custom run C - auto logging"
tags = {
    "Demo": "True",
    "Created by": "Sean",
}
mlflow.set_experiment(experiment_name) # will create if needed, else re-use
# experiment changes the artifact store

# mlflow loggin
with mlflow.start_run(run_name = run_name):    
    # training
    alpha = 0.5
    l1 = 0.5

    # linear regression model
    lr = ElasticNet(alpha=alpha, l1_ratio=l1)

    lr.fit(X_train, y_train)

    def eval_metrics(ground_truth, pred):
        rmse = np.sqrt(metrics.mean_squared_error(ground_truth, pred))
        mae = metrics.mean_absolute_error(ground_truth, pred)
        r2 = metrics.r2_score(ground_truth, pred)

        return rmse, mae, r2

    # inference
    y_pred = lr.predict(X_train)
    print(y_pred.shape)

    rmse, mae, r2 = eval_metrics(y_train, y_pred)

    print(f"Out metrics: RMSE = {rmse}, MAE = {mae}, R2 = {r2}")
    # then you would adjust until you see good metrics

    # logged hyperparameters
    # mlflow.log_param("alpha", alpha)
    # mlflow.log_param("l1 ratio", l1)

    # # logged metrics
    # mlflow.log_metric("rmse", rmse)
    # mlflow.log_metric("mae", mae)
    # mlflow.log_metric("r2", r2)

    fig = plt.gcf()
    img = fig2img(fig)
    # log image (as file)
    mlflow.log_artifact("quality_corr.png")

    mlflow.set_tags(tags)
