from typing import Union
import mindsdb_sdk
from pydantic import BaseModel
import os


class DBCredentials(BaseModel):
    db_rename: str = None
    engine: str
    user: str
    password: str
    host: str
    port: Union[int, str]
    db_name: str


class MindsDBCredentials(BaseModel):
    subscription: str
    url: str = os.getenv('MINDSDB_URL', None)
    email_id: str = None
    password: str = None


class TrainDetails(BaseModel):
    name_of_model: str
    db_credentials: DBCredentials
    mindsdb_credentials: MindsDBCredentials
    training_set_schema: str = None
    training_set_tableName: str
    optional_filter_condition: str = None
    input_columns_names: str
    output_column_names: str
    project_name: str = None


class ModelDetails(BaseModel):
    project_name: str = None
    mindsdb_credentials: MindsDBCredentials


def get_connection(mindsdb_credentials: MindsDBCredentials):
    subscription = mindsdb_credentials.subscription
    url = mindsdb_credentials.url
    email_id = mindsdb_credentials.email_id
    password = mindsdb_credentials.password
    if subscription == "local":
        if url is None:
            server = mindsdb_sdk.connect()
        else:
            server = mindsdb_sdk.connect(url)
    elif subscription == "cloud":
        if email_id is None or password is None:
            raise ValueError(f'Email id or password is missing')
        if url is None:
            server = mindsdb_sdk.connect(login=email_id, password=password)
        else:
            server = mindsdb_sdk.connect(url, login=email_id, password=password)
    elif subscription == "pro":
        if email_id is None or password is None:
            raise ValueError(f'Email id or password is missing')
        if url is None:
            raise ValueError('URL is missing')
        else:
            server = mindsdb_sdk.connect(url, login=email_id, password=password, is_managed=True)
    else:
        raise ValueError(f'Invalid subscription: {subscription}')
    return server
