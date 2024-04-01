import pandas as pd
import os
import typer
import requests
from dotenv import load_dotenv
from .credentials import get_auth
from rich import print

app = typer.Typer()

load_dotenv()



def create_groups(file_name: str, environment: str):

    auth, domain = get_auth(environment)

    dir_path = '../typer_data/post_data/create_groups/'
    os.makedirs(dir_path, exist_ok=True)
    file_path = os.path.join(dir_path, file_name)

    try:
        df = pd.read_csv(file_path)
        if 'group_name' not in df.columns or df.empty:
            print(
                "[bold yellow]The file must have a header with 'group_name' as the first column name and at least one group name./[bold yellow]")
            print(
                "[Download CSV Template: https://github.com/tbs89/typer-zendesk-cli/blob/main/docs/templates/create_groups_template.csv]")
            return

        typer.echo(f"[{environment.upper()}] You are about to create the following groups:")
        for index, row in df.iterrows():
            typer.echo(f"- {row['group_name']}")
        if not typer.confirm(f"[{environment.upper()}] Are you sure you want to proceed?"):
            print("[bold yellow]Operation cancelled.[/bold yellow]")
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
                print(f"[bold red]Failed to create group '{group_name}': {response.text}[/bold red]")

        df.to_csv(file_path, index=False)
        print(f"[bold green][{environment.upper()}] File updated with group IDs at {file_path}[/bold green]")
    except FileNotFoundError:
        print(f"[bold yellow]File '{file_name}' not found.[/bold yellow]")





def assign_agents_to_group(file_name: str, group_id: int, environment: str):

    auth, domain = get_auth(environment)

    dir_path = '../typer_data/post_data/assign_groups/'
    os.makedirs(dir_path, exist_ok=True)
    file_path = os.path.join(dir_path, file_name)

    try:
        group_response = requests.get(f"{domain}api/v2/groups/{group_id}.json", auth=auth)
        if group_response.status_code == 200:
            group_name = group_response.json()['group']['name']
        else:
            print("[bold red]Failed to fetch group information.[/bold red]")
            return

        print(f"[bold blue][{environment.upper()}] You are about to assign agents to the group: {group_name}[/bold blue]")
        if not typer.confirm(f"[{environment.upper()}] Are you sure you want to proceed?"):
            print("[bold yellow]Operation cancelled.[/bold yellow]")
            return

        df = pd.read_csv(file_path)
        if 'email' not in df.columns or df.empty:
            print("[bold yellow]The file must have a header with 'email' as the first column name.[/bold yellow]")
            print(
                "[Download CSV Template: https://github.com/tbs89/typer_zd/blob/main/docs/templates/assign_agents_template.csv]")
            return

        df['group_membership_id'] = None

        for index, row in df.iterrows():
            email = row['email']
            user_id = get_user_id_by_email(email, domain, auth)
            if user_id:
                membership_response = requests.post(
                    f"{domain}api/v2/users/{user_id}/group_memberships.json",
                    json={"group_membership": {"user_id": user_id, "group_id": group_id}},
                    auth=auth
                )
                if membership_response.status_code in [200, 201]:
                    membership_id = membership_response.json()['group_membership']['id']
                    df.at[index, 'group_membership_id'] = membership_id
                    print(f"[bold green]Agent {email} assigned to {group_name} with membership ID {membership_id}[/bold green]")
                else:
                    print(f"[bold yellow]Failed to assign {email} to {group_name}: {membership_response.text}[/bold yellow]")
            else:
                print(f"[bold yellow]Failed to find user ID for email: {email}[/bold yellow]")

        df.to_csv(file_path, index=False)
        print(f"[bold green][{environment.upper()}] CSV file updated with group memberships at {file_path}[/bold green]")
    except FileNotFoundError:
        print(f"[bold red]File '{file_name}' not found [/bold red]")






def get_user_id_by_email(email: str, domain: str, auth) -> int:
    """Fetch the user ID from Zendesk API by email."""
    search_url = f"{domain}api/v2/users/search.json?query=email:{email}"
    response = requests.get(search_url, auth=auth)
    if response.status_code == 200 and 'users' in response.json() and len(response.json()['users']) > 0:
        return response.json()['users'][0]['id']
    else:
        print(f"[bold yellow]Failed to fetch user ID for email: {email}. Response: {response.text}[/bold yellow]")
        return None






def create_agents_in_bulk(file_name: str, environment: str):
    auth, domain = get_auth(environment)

    dir_path = '../typer_data/post_data/create_agents/'
    os.makedirs(dir_path, exist_ok=True)
    file_path = os.path.join(dir_path, file_name)

    try:
        df = pd.read_csv(file_path)
        if not all(column in df.columns for column in ['name', 'email', 'custom_role_id']):
            print("[bold yellow]The file must have 'name', 'email', and 'custom_role_id' columns.[/bold yellow]")
            print("[Download CSV Template: https://github.com/tbs89/typer_zd/blob/main/docs/templates/create_agents_template.csv]")

            return

        typer.echo(f"[{environment.upper()}] You are about to create the following agents:")
        for index, row in df.iterrows():
            typer.echo(f"- {row['name']} - {row['email']} - {row['custom_role_id']}")

        if not typer.confirm(f"[{environment.upper()}]Are you sure you want to proceed?", default=False):
            print("[bold red]Operation cancelled [/bold red]")
            return

        df['status'] = None

        for index, row in df.iterrows():
            user_data = {
                "user": {
                    "name": row['name'],
                    "email": row['email'],
                    "role": "agent",
                    "custom_role_id": row['custom_role_id']
                }
            }
            response = requests.post(f"{domain}api/v2/users.json", json=user_data, auth=auth)
            if response.status_code in [200, 201]:
                df.at[index, 'status'] = "created"
                typer.echo("-----------------------------------------------------------------")
                print(f"[bold green]Created {row['name']} - {row['email']} - {row['custom_role_id']}[/bold green]")
            else:
                df.at[index, 'status'] = "failed"
                error_details = response.json().get('details', {})
                error_message = error_details.get('email', [{}])[0].get('description', 'Unknown error') if error_details else 'Unknown error'
                typer.echo("-----------------------------------------------------------------", err=True)
                print(f"[bold yellow]Failed to create {row['name']}: {error_message}[/bold yellow]", err=True)

        df.to_csv(file_path, index=False)
        typer.echo("-----------------------------------------------------------------")
        print(f"[bold green][{environment.upper()}] CSV file updated with creation status at {file_path}[/bold green]")
    except FileNotFoundError:
        print(f"[bold yellow]File '{file_name}' not found [/bold yellow]")





if __name__ == "__main__":
    app()

