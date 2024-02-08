from mindsdb_operations.initial_config import get_connection, ModelDetails
import pandas as pd


def models_fn(item: ModelDetails):
    server = get_connection(item.db_credentials)
    project = server.get_project('mindsdb')
    if item.project_name is None:
        final_result = project.query("SHOW MODELS").fetch()

    else:
        project_name = item.project_name
        final_result = project.query(f"SELECT * FROM {project_name}.models").fetch()
    return final_result.to_dict(orient='records')
