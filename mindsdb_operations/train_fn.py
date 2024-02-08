from mindsdb_operations.initial_config import get_connection, TrainDetails


def generate_train_query(item: TrainDetails):
    db_name = item.db_credentials.get("db_name", None)
    if item.optional_filter_condition is None:
        if item.project_name is None:
            query = str(
                f"CREATE MODEL mindsdb.{item.name_of_model} FROM {db_name}.{item.training_set_schema} "
                f"(SELECT {item.input_columns_names} FROM {item.training_set_tableName}) "
                f"PREDICT {item.output_column_names};")
        else:
            query = str(
                f"CREATE MODEL {item.project_name}.{item.name_of_model} FROM {db_name}.{item.training_set_schema} "
                f"(SELECT {item.input_columns_names} FROM {item.training_set_tableName}) "
                f"PREDICT {item.output_column_names};")
    else:
        if item.project_name is None:
            query = str(
                f"CREATE MODEL mindsdb.{item.name_of_model} FROM {db_name}.{item.training_set_schema} "
                f"(SELECT {item.input_columns_names} FROM {item.training_set_tableName} "
                f"WHERE {item.optional_filter_condition}) "
                f"PREDICT {item.output_column_names};")
        else:
            query = str(
                f"CREATE MODEL {item.project_name}.{item.name_of_model} FROM {db_name}.{item.training_set_schema} "
                f"(SELECT {item.input_columns_names} FROM {item.training_set_tableName} "
                f"WHERE {item.optional_filter_condition}) "
                f"PREDICT {item.output_column_names};")
    return query


def train_fn(item: TrainDetails):
    server = get_connection(item.db_credentials)
    print(1)
    mindsdb = server.get_project('mindsdb')
    if item.project_name is not None:
        mindsdb.query(f"CREATE DATABASE [IF NOT EXISTS] {item.project_name};")
        mindsdb = server.get_project(item.project_name)
    print(3)
    result = mindsdb.query(generate_train_query(item)).fetch()
    print(4)
    return result.to_dict(orient='records')
