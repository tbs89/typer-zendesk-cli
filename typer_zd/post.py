import pandas as pd
import os
import typer
import requests
from dotenv import load_dotenv

app = typer.Typer()
load_dotenv()


def create_groups(file_name: str, environment: str):

    email = os.getenv(f"ZENDESK_{environment.upper()}_EMAIL")
    token = os.getenv(f"ZENDESK_{environment.upper()}_TOKEN")
    domain = os.getenv(f"ZENDESK_{environment.upper()}_DOMAIN")
    auth = (f"{email}/token", token)

    dir_path = 'typer_data/post_data/create_groups/'
    os.makedirs(dir_path, exist_ok=True)
    file_path = os.path.join(dir_path, file_name)

    try:
        df = pd.read_csv(file_path)
        if 'group_name' not in df.columns or df.empty:
            typer.echo("The file must have a header with 'group_name' as the first column name and at least one group name.")
            return

        df['group_id'] = None

        for index, row in df.iterrows():
            group_name = row['group_name']
            response = requests.post(
                f"{domain}api/v2/groups.json",
                json={"group": {"name": group_name}},
                auth=auth
            )
            if response.status_code == 201:
                group_id = response.json()['group']['id']
                df.at[index, 'group_id'] = group_id
                typer.echo(f"Group '{group_name}' created with ID {group_id}.")
            else:
                typer.echo(f"Failed to create group '{group_name}': {response.text}")

        df.to_csv(f'{file_path}', index=False)
        typer.echo(f"File updated with group IDs at {file_path}")
    except FileNotFoundError:
        typer.echo(f"File {file_name} not found.")


if __name__ == "__main__":
    app()

