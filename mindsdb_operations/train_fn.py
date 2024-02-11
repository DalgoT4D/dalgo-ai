from mindsdb_operations.initial_config import get_connection, TrainDetails, DBCredentials


def generate_train_query(item: TrainDetails):
    db_rename = item.db_credentials.db_rename
    db_name = item.db_credentials.db_name if db_rename is None else db_rename
    project_name = item.project_name if item.project_name is not None else db_name
    schema = f"{item.training_set_schema}." if item.training_set_schema is not None else ""
    filter_condition = f" WHERE {item.optional_filter_condition}" if item.optional_filter_condition is not None else ""
    query = (f"CREATE MODEL {project_name}.{item.name_of_model} FROM {db_name} "
             f"(SELECT {item.input_columns_names} FROM {schema}{item.training_set_tableName}{filter_condition}) "
             f"PREDICT {item.output_column_names};")
    return query


def create_database_query(item: DBCredentials):
    db_name = item.db_rename if item.db_rename is not None else item.db_name
    query = (f""" CREATE DATABASE IF NOT EXISTS {db_name} 
    WITH ENGINE='{item.engine}', PARAMETERS={{
    "user": "{item.user}", 
    "port": "{item.port}", 
    "password": "{item.password}", 
    "host": "{item.host}", 
    "database": "{item.db_name}"}};
    """)
    return query


def train_fn(item: TrainDetails):
    server = get_connection(item.mindsdb_credentials)
    mindsdb = server.get_project('mindsdb')
    mindsdb.query(create_database_query(item.db_credentials)).fetch()
    db_rename = item.db_credentials.db_rename
    db_name = db_rename if db_rename is not None else item.db_credentials.db_name
    project_name = item.project_name if item.project_name is not None else f"{db_name}"
    mindsdb.query(f"CREATE PROJECT IF NOT EXISTS {project_name};").fetch()
    result = mindsdb.query(generate_train_query(item)).fetch()
    return result.to_dict(orient='records')
