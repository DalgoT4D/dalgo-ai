# Input format of body for train API
## 1. Headers
```python
{
    "Content-Type": "application/json"
}
```
## 2. Body
```python
body_in_train_request = {
    "name_of_model": "<model name>",
    "db_credentials": "db_credentials (read below for db_credentials)",
    "training_set_schema": "<optional: if schema present enter schema>",
    "training_set_tableName": "<enter table_name>",
    "input_columns_names": "<enter '*' for all otherwise enter 'col1,col2,col3,..'>",
    "output_column_names": "<enter '*' for all otherwise enter 'col1,col2,col3,..'>",
    "project_name": "<optional: if you want to create a model in a particular project, then enter this field, otherwise default project is 'mindsdb'>",
}
```
## db_credentials format
1. For training the model on your local device
```python
db_credentials = {
    "db_name": "<enter mindsdb database name>",
    "subscription": "local",
    "url":"<required if mindsdb is created on EC2 instance or other cloud services, otherwire for local device, it is not required>"
}
```
2. For training the model on cloud
```python
db_credentials = {
    "db_name": "<enter mindsdb database name>",
    "subscription": "<optional: default value is 'cloud'>",
    "url":"<optional if using default cloud mindsdb, otherwise required>",
    "email_id": "<email_id>",
    "password": "<password>"
}
```
3. For training the model mindsdb pro
```python
db_credentials = {
    "db_name": "<enter mindsdb database name>",
    "subscription": "pro",
    "url":"<url for pro>",
    "email_id": "<email_id>",
    "password": "<password>"
}
```

## For models api
```python
{
    "project_name": "<optional: if you want list of models from a particular project, then enter this filed, else it will return all models>",
    "db_credentials": "db_credentials (same format as above)"
}
```