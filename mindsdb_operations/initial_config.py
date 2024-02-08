import mindsdb_sdk
from pydantic import BaseModel


class TrainDetails(BaseModel):
    name_of_model: str
    db_credentials: dict
    training_set_schema: str = None
    training_set_tableName: str
    optional_filter_condition: str = None
    input_columns_names: str
    output_column_names: str


def get_connection(db_credentials: dict):
    subscription = db_credentials.get("subscription", "cloud")
    url = db_credentials.get("url", None)
    email_id = db_credentials.get("email_id", None)
    password = db_credentials.get("password", None)
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
