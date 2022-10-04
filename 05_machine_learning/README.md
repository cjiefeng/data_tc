# Machine Learning

Added a convenience docker-compose.yml to test locally
```
$ docker compose run predict_buying
```

Using the dataset from https://archive.ics.uci.edu/ml/datasets/Car+Evaluation,
create a machine learning model to predict the buying price given the following
parameters:
- `maint`=`high`
- `doors`=`4`
- `lug_boot`=`big`
- `safety`=`high`
- `class`=`good`

Model predicts `buying`: `low`
