import os

def ensure_data_path(relative_path, environment):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    data_path = os.path.join(base_dir, 'typer_data', environment, relative_path)
    os.makedirs(data_path, exist_ok=True)
    return data_path