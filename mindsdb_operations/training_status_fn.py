from mindsdb_operations.initial_config import get_connection, TrainingStatusDetails


def training_status_fn(item: TrainingStatusDetails):
    server = get_connection(item.db_credentials)
    project = server.get_project('mindsdb')
    final_result = project.query(f"SHOW MODELS WHERE name = '{item.model_name}'").fetch()
    return final_result.to_dict(orient='records')
