from mindsdb_operations.initial_config import get_connection, TrainDetails


def generate_train_query(item: TrainDetails):
    db_name = item.db_credentials.get("db_name", None)
    if item.optional_filter_condition is None:
        query = str(
            f"CREATE MODEL mindsdb.{item.name_of_model} FROM {db_name}.{item.training_set_schema} "
            f"(SELECT {item.input_columns_names} FROM {item.training_set_tableName}) "
            f"PREDICT {item.output_column_names};")
    else:
        query = str(
            f"CREATE MODEL mindsdb.{item.name_of_model} FROM {db_name}.{item.training_set_schema} "
            f"(SELECT {item.input_columns_names} FROM {item.training_set_tableName} "
            f"WHERE {item.optional_filter_condition}) "
            f"PREDICT {item.output_column_names};")
    return query


def train_fn(item: TrainDetails):
    server = get_connection(item.db_credentials)
    mindsdb = server.get_project('mindsdb')
    output = mindsdb.query(generate_train_query(item))
    result = output.fetch().to_dict(orient='records')
    return result
