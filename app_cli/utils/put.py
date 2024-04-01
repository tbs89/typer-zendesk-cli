import pandas as pd
import os
import typer
import requests
from dotenv import load_dotenv
from .credentials import get_auth
import json
from rich import print

app = typer.Typer()

load_dotenv()


def update_macro_permissions(file_name: str, environment: str):
    
    auth, domain = get_auth(environment)

    dir_path = '../typer_data/put_data/update_permissions_macros/'
    os.makedirs(dir_path, exist_ok=True)
    file_path = os.path.join(dir_path, file_name)

    try:
        df = pd.read_csv(file_path)
        if 'macro_id' not in df.columns or 'group_1' not in df.columns:
            print("[bold yellow]The file must have at least 'macro_id' and 'group_1' columns.[/bold yellow]")
            return

        if not typer.confirm("\nAre you sure you want to proceed?", default=False):
            print("[bold red]Operation cancelled.[/bold red]")
            return

        for index, row in df.iterrows():
            macro_id = row['macro_id']
            open_to_all = any(str(row[column]).strip().lower() == 'open' for column in df.columns if column.startswith('group_'))

            if open_to_all:
                payload = json.dumps({"macro": {"restriction": None}})
            else:
                group_ids = [row[column] for column in df.columns if column.startswith('group_') and pd.notna(row[column]) and str(row[column]).strip().lower() != 'null']
                restriction_payload = {"type": "Group", "ids": [int(gid) for gid in group_ids]}
                payload = json.dumps({"macro": {"restriction": restriction_payload}})

            headers = {'Content-Type': 'application/json'}
            response = requests.put(f"{domain}/api/v2/macros/{macro_id}.json", data=payload, auth=auth, headers=headers)

            if response.status_code in [200, 201]:
                action = "opened to all groups" if open_to_all else "restricted to specific groups"
                print(f"[bold green]Macro ID {macro_id} successfully {action}.[/bold green]")
            else:
                error_message = response.json().get('error', 'Unknown error')
                print(f"[bold red]Failed to update Macro ID {macro_id}: {error_message}[/bold red]")

    except FileNotFoundError:
        print(f"[bold yellow]File '{file_name}' not found.[/bold yellow]")
    except ValueError as e:
        print(f"[bold red][{environment.upper()}] Error processing file: {e}. Please ensure your 'group_id' values are valid group ID#s or 'open' to open access.[/bold red]")





if __name__ == "__main__":
    app()
