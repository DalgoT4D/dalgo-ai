from mindsdb_operations.initial_config import get_connection, TrainDetails


def generate_train_query(item: TrainDetails):
    db_name = item.db_credentials.get("db_name", None)
    project_name = item.project_name if item.project_name is not None else "mindsdb"
    schema = f"{item.training_set_schema}." if item.training_set_schema is not None else ""
    filter_condition = f" WHERE {item.optional_filter_condition}" if item.optional_filter_condition is not None else ""
    query = (f"CREATE MODEL {project_name}.{item.name_of_model} FROM {db_name} "
             f"(SELECT {item.input_columns_names} FROM {schema}{item.training_set_tableName}{filter_condition}) "
             f"PREDICT {item.output_column_names};")
    return query


def train_fn(item: TrainDetails):
    server = get_connection(item.db_credentials)
    mindsdb = server.get_project('mindsdb')
    if item.project_name is not None:
        mindsdb.query(f"CREATE PROJECT IF NOT EXISTS {item.project_name};").fetch()
    result = mindsdb.query(generate_train_query(item)).fetch().to_dict(orient='records')
    return result
