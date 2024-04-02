import os
import requests
from dotenv import load_dotenv
import pandas as pd
from datetime import datetime
import typer
from rich.progress import Progress
from rich import print
import time
from .path_utils import ensure_data_path

load_dotenv()

app = typer.Typer()



def fetch_data_with_progress(url: str, environment: str, progress: Progress, task_id: int, data_key: str):
    email = os.getenv(f"ZENDESK_{environment.upper()}_EMAIL")
    token = os.getenv(f"ZENDESK_{environment.upper()}_TOKEN")
    domain = os.getenv(f"ZENDESK_{environment.upper()}_DOMAIN")
    full_url = f"{domain}{url}"

    if not all([email, token, domain]):
        print(f"[bold red][{environment.upper()}] Missing credentials. Please ensure email, token, and domain are set.[/bold red]")
        return None

    results = []

    while full_url:
        response = requests.get(full_url, auth=(f"{email}/token", token))
        if response.status_code == 200:
            data = response.json()
            results.extend(data.get(data_key, []))
            full_url = data.get('next_page')
            progress.advance(task_id)
        else:
            print(f"[bold red]Error fetching data: {response.status_code}[/bold red]")
            return []

    return results



def merge_users_and_roles(users: list, roles: list) -> pd.DataFrame:
    roles_df = pd.DataFrame(roles).rename(columns={"id": "custom_role_id", "name": "role_name"})
    users_df = pd.DataFrame(users)

    merged_df = pd.merge(users_df, roles_df[['custom_role_id', 'role_name']], on='custom_role_id', how='left')

    cols = [col for col in merged_df.columns if col != 'role_name']

    cols.insert(1, 'role_name')
    merged_df = merged_df[cols]

    return merged_df




def reorder_columns(data_frame):

    columns = list(data_frame.columns)

    if 'role_name' in columns:
        columns.insert(1, columns.pop(columns.index('role_name')))
    data_frame = data_frame[columns]
    return data_frame



def prepare_and_save_data(data, data_type, environment):
    if isinstance(data, list) and not data:
        print(f"❌ - [bold red]Failed to fetch {data_type} from Zendesk for {environment} environment[/bold red]")
        return
    else:
        df = pd.DataFrame(data)

    if df.empty:
        print(f"❌ - [bold red]No {data_type} data found to save for {environment} environment[/bold red]")
        return

    dir_path = ensure_data_path(f'get_data/{data_type}', environment)
    file_path = os.path.join(dir_path, f"zd_{data_type}_{environment}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv")
    df.to_csv(file_path, index=False)

    base_path = os.getcwd()
    file_path_rel = os.path.relpath(file_path, base_path)

    print(f"[green][{environment.upper()}]--------------------------------------------------------------------- [/green]")
    print(f"✅ - [green]{data_type.capitalize()} data saved successfully to[/green] [bold green]{file_path_rel}[/bold green]")
    time.sleep(4)





@app.command()
def get_users(environment: str):

    with Progress() as progress:
        task_id = progress.add_task(f"[{environment.upper()}][cyan] Downloading users...", total=None)
        users = fetch_data_with_progress("/api/v2/users.json?role[]=admin&role[]=agent", environment, progress, task_id, 'users')

        if users is None:
            print(f"[bold red][{environment.upper()}] No users found in this environment[/bold red]")
            progress.remove_task(task_id)
            return

        roles = fetch_data_with_progress("/api/v2/custom_roles.json", environment, progress, task_id, 'custom_roles')

        if roles is None:
            print(f"[{environment.upper()}][bold red] No roles found in this environment[/bold red]")
            return

        progress.remove_task(task_id)

    merged_data = merge_users_and_roles(users, roles)
    prepare_and_save_data(merged_data, 'users', environment)



@app.command()
def get_macros(environment: str):

    with Progress() as progress:
        task_id = progress.add_task(f"[{environment.upper()}] [cyan] Downloading macros...", total=None)
        macros = fetch_data_with_progress("/api/v2/macros.json", environment, progress, task_id, 'macros')

        if macros is None:
            print(f"[bold red][{environment.upper()}] No macros found in this environment[/bold red]")
            progress.remove_task(task_id)
            return

        progress.remove_task(task_id)

    prepare_and_save_data(macros, 'macros', environment)





@app.command()
def get_articles(environment: str):

    with Progress() as progress:
        task_id = progress.add_task(f"[{environment.upper()}] [cyan] Downloading articles...", total=None)
        articles = fetch_data_with_progress("/api/v2/help_center/articles.json", environment, progress, task_id, 'articles')

        if articles is None:
            print(f"[bold red][{environment.upper()}] No articles found in this environment[/bold red]")
            progress.remove_task(task_id)
            return

        progress.remove_task(task_id)
    prepare_and_save_data(articles, 'articles', environment)


@app.command()
def get_organizations(environment: str):

    with Progress() as progress:
        task_id = progress.add_task(f"[{environment.upper()}] [cyan] Downloading organizations...", total=None)
        organizations = fetch_data_with_progress("/api/v2/organizations.json", environment, progress, task_id, 'organizations')

        if organizations is None:
            print(f"[bold red][{environment.upper()}] No organizations found in this environment[/bold red]")
            progress.remove_task(task_id)
            return

        progress.remove_task(task_id)
    prepare_and_save_data(organizations, 'organizations', environment)


@app.command()
def get_groups(environment: str):

    with Progress() as progress:
        task_id = progress.add_task(f"[{environment.upper()}] [cyan] Downloading groups...", total=None)
        groups = fetch_data_with_progress("/api/v2/groups.json", environment, progress, task_id, 'groups')

        if groups is None:
            print(f"[bold red][{environment.upper()}] No groups found in this environment[/bold red]")
            progress.remove_task(task_id)
            return

        progress.remove_task(task_id)
    prepare_and_save_data(groups, 'groups', environment)



@app.command()
def get_dynamic_content(environment: str):

    with Progress() as progress:
        task_id = progress.add_task(f"[{environment.upper()}] [cyan] Downloading dynamic content items...", total=None)
        items = fetch_data_with_progress("/api/v2/dynamic_content/items.json", environment, progress, task_id, 'items')

        if items is None:
            print(f"[bold red][{environment.upper()}] No dynamic content found in this environment[/bold red]")
            progress.remove_task(task_id)
            return

        progress.remove_task(task_id)
    prepare_and_save_data(items, 'dynamic_content', environment)



@app.command()
def get_views(environment: str):

    with Progress() as progress:
        task_id = progress.add_task(f"[{environment.upper()}] [cyan] Downloading views...", total=None)
        views = fetch_data_with_progress("/api/v2/views.json", environment, progress, task_id, 'views')

        if views is None:
            print(f"[bold red][{environment.upper()}] No views found in this environment[/bold red]")
            progress.remove_task(task_id)
            return

        progress.remove_task(task_id)
    prepare_and_save_data(views, 'views', environment)


@app.command()
def get_triggers(environment: str):

    with Progress() as progress:
        task_id = progress.add_task(f"[{environment.upper()}] [cyan] Downloading triggers...", total=None)
        triggers = fetch_data_with_progress("/api/v2/triggers.json", environment, progress, task_id, 'triggers')

        if triggers is None:
            print(f"[bold red][{environment.upper()}] No triggers found in this environment[/bold red]")
            progress.remove_task(task_id)
            return

        progress.remove_task(task_id)
    prepare_and_save_data(triggers, 'triggers', environment)


@app.command()
def get_automations(environment: str):

    with Progress() as progress:
        task_id = progress.add_task(f"[{environment.upper()}] [cyan] Downloading automations...", total=None)
        automations = fetch_data_with_progress("/api/v2/automations.json", environment, progress, task_id, 'automations')

        if automations is None:
            print(f"[bold red][{environment.upper()}] No automations found in this environment[/bold red]")
            progress.remove_task(task_id)
            return

        progress.remove_task(task_id)
    prepare_and_save_data(automations, 'automations', environment)



@app.command()
def get_brands(environment: str):

    with Progress() as progress:
        task_id = progress.add_task(f"[{environment.upper()}] [cyan] Downloading brands...", total=None)
        brands = fetch_data_with_progress("/api/v2/brands.json", environment, progress, task_id, 'brands')

        if brands is None:
            print(f"[bold red][{environment.upper()}] No brands found in this environment[/bold red]")
            progress.remove_task(task_id)
            return

        progress.remove_task(task_id)
    prepare_and_save_data(brands, 'brands', environment)



@app.command()
def get_user_fields(environment: str):

    with Progress() as progress:
        task_id = progress.add_task(f"[{environment.upper()}] [cyan] Downloading user fields...", total=None)
        user_fields = fetch_data_with_progress("/api/v2/user_fields.json", environment, progress, task_id, 'user_fields')

        if user_fields is None:
            print(f"[bold red][{environment.upper()}] No user fields found in this environment[/bold red]")
            progress.remove_task(task_id)
            return

        progress.remove_task(task_id)
    prepare_and_save_data(user_fields, 'user_fields', environment)



@app.command()
def get_ticket_fields(environment: str):

    with Progress() as progress:
        task_id = progress.add_task(f"[{environment.upper()}] [cyan] Downloading ticket fields...", total=None)
        ticket_fields = fetch_data_with_progress("/api/v2/ticket_fields.json", environment, progress, task_id, 'ticket_fields')

        if ticket_fields is None:
            print(f"[bold red][{environment.upper()}] No ticket fields found in this environment[/bold red]")
            progress.remove_task(task_id)
            return

        progress.remove_task(task_id)
    prepare_and_save_data(ticket_fields, 'ticket_fields', environment)



if __name__ == "__main__":
    app()
