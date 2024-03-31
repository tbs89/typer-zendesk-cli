import os
import requests
from dotenv import load_dotenv
import pandas as pd
from datetime import datetime
import typer
from rich.progress import Progress
from rich import print
import time
app = typer.Typer()


def fetch_data_with_progress(url: str, environment: str, progress: Progress, task_id: int, data_key: str):
    """Fetch data from the given Zendesk API endpoint with pagination, specifying the environment and data key."""
    load_dotenv()
    email = os.getenv(f"ZENDESK_{environment.upper()}_EMAIL")
    token = os.getenv(f"ZENDESK_{environment.upper()}_TOKEN")
    domain = os.getenv(f"ZENDESK_{environment.upper()}_DOMAIN")
    full_url = f"{domain}{url}"

    results = []
    while full_url:
        response = requests.get(full_url, auth=(f"{email}/token", token))
        if response.status_code != 200:
            print(f"[bold red]Error fetching data: {response.status_code}[/bold red]")
            print(f"[bold yellow]Error details: {response.text}[/bold yellow]")
            return []

        data = response.json()
        results.extend(data.get(data_key, []))
        full_url = data.get('next_page')
    return results




def merge_users_and_roles(users: list, roles: list) -> pd.DataFrame:
    """Merge user data with their custom roles based on role_id."""
    roles_df = pd.DataFrame(roles).rename(columns={"id": "custom_role_id", "name": "role_name"})
    users_df = pd.DataFrame(users)
    merged_df = pd.merge(users_df, roles_df[['custom_role_id', 'role_name']], on='custom_role_id', how='left')
    return merged_df

def reorder_columns(data_frame):
    """Reorder DataFrame columns to ensure role_name is in the second position."""
    columns = list(data_frame.columns)

    if 'role_name' in columns:
        columns.insert(1, columns.pop(columns.index('role_name')))
    data_frame = data_frame[columns]
    return data_frame



def prepare_and_save_data(data, data_type, environment):

    if isinstance(data, list):
        if not data:
            print(f"❌ - [bold red]Failed to fetch {data_type} from Zendesk for {environment} environment[/bold red]")
            time.sleep(4)
            return
        else:
            df = pd.DataFrame(data)
    else:
        df = data

    if df.empty:
        print(f"❌ - [bold red]No {data_type} data found to save for {environment} environment[/bold red]")
        time.sleep(4)
        return

    dir_path = f'typer_data/get_data/{data_type}/{environment}/'
    os.makedirs(dir_path, exist_ok=True)

    file_path = os.path.join(dir_path,
                             f"zd_{data_type}_{environment}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv")
    df.to_csv(file_path, index=False)
    print(f"✅ - [green]{data_type.capitalize()} data saved successfully to[/green] [bold green]{file_path}[/bold green]")
    time.sleep(4)


@app.command()
def get_users(environment: str):
    """Fetches users and their roles from Zendesk and saves them to a CSV file, specifying the environment."""
    with Progress() as progress:
        task_id = progress.add_task("[cyan]Downloading users...", total=None)
        users = fetch_data_with_progress("/api/v2/users.json?role[]=admin&role[]=agent", environment, progress, task_id, 'users')
        roles = fetch_data_with_progress("/api/v2/custom_roles.json", environment, progress, task_id, 'custom_roles')
        progress.remove_task(task_id)

    merged_data = merge_users_and_roles(users, roles)
    prepare_and_save_data(merged_data, 'users', environment)

# Ejemplo para get_macros adaptado
@app.command()
def get_macros(environment: str):
    """Fetches macros from Zendesk and saves them to a CSV file."""
    with Progress() as progress:
        task_id = progress.add_task("[cyan]Downloading macros...", total=None)
        macros = fetch_data_with_progress("/api/v2/macros.json", environment, progress, task_id, 'macros')
        progress.remove_task(task_id)

    prepare_and_save_data(macros, 'macros', environment)



@app.command()
def get_articles(environment: str):
    """Fetches help center articles from Zendesk and saves them to a CSV file."""
    with Progress() as progress:
        task_id = progress.add_task("[cyan]Downloading articles...", total=None)
        articles = fetch_data_with_progress("/api/v2/help_center/articles.json", environment, progress, task_id, 'articles')
        progress.remove_task(task_id)
    prepare_and_save_data(articles, 'articles', environment)

@app.command()
def get_organizations(environment: str):
    """Fetches organizations from Zendesk and saves them to a CSV file."""
    with Progress() as progress:
        task_id = progress.add_task("[cyan]Downloading organizations...", total=None)
        organizations = fetch_data_with_progress("/api/v2/organizations.json", environment, progress, task_id, 'organizations')
        progress.remove_task(task_id)
    prepare_and_save_data(organizations, 'organizations', environment)

@app.command()
def get_groups(environment: str):
    """Fetches groups from Zendesk and saves them to a CSV file."""
    with Progress() as progress:
        task_id = progress.add_task("[cyan]Downloading groups...", total=None)
        groups = fetch_data_with_progress("/api/v2/groups.json", environment, progress, task_id, 'groups')
        progress.remove_task(task_id)
    prepare_and_save_data(groups, 'groups', environment)

@app.command()
def get_dynamic_content(environment: str):
    """Fetches dynamic content items from Zendesk and saves them to a CSV file."""
    with Progress() as progress:
        task_id = progress.add_task("[cyan]Downloading dynamic content items...", total=None)
        items = fetch_data_with_progress("/api/v2/dynamic_content/items.json", environment, progress, task_id, 'items')
        progress.remove_task(task_id)
    prepare_and_save_data(items, 'dynamic_content', environment)

@app.command()
def get_views(environment: str):
    """Fetches views from Zendesk and saves them to a CSV file."""
    with Progress() as progress:
        task_id = progress.add_task("[cyan]Downloading views...", total=None)
        views = fetch_data_with_progress("/api/v2/views.json", environment, progress, task_id, 'views')
        progress.remove_task(task_id)
    prepare_and_save_data(views, 'views', environment)

@app.command()
def get_triggers(environment: str):
    """Fetches triggers from Zendesk and saves them to a CSV file."""
    with Progress() as progress:
        task_id = progress.add_task("[cyan]Downloading triggers...", total=None)
        triggers = fetch_data_with_progress("/api/v2/triggers.json", environment, progress, task_id, 'triggers')
        progress.remove_task(task_id)
    prepare_and_save_data(triggers, 'triggers', environment)

@app.command()
def get_automations(environment: str):
    """Fetches automations from Zendesk and saves them to a CSV file."""
    with Progress() as progress:
        task_id = progress.add_task("[cyan]Downloading automations...", total=None)
        automations = fetch_data_with_progress("/api/v2/automations.json", environment, progress, task_id, 'automations')
        progress.remove_task(task_id)
    prepare_and_save_data(automations, 'automations', environment)

@app.command()
def get_brands(environment: str):
    """Fetches brands from Zendesk and saves them to a CSV file."""
    with Progress() as progress:
        task_id = progress.add_task("[cyan]Downloading brands...", total=None)
        brands = fetch_data_with_progress("/api/v2/brands.json", environment, progress, task_id, 'brands')
        progress.remove_task(task_id)
    prepare_and_save_data(brands, 'brands', environment)

@app.command()
def get_user_fields(environment: str):
    """Fetches user fields from Zendesk and saves them to a CSV file."""
    with Progress() as progress:
        task_id = progress.add_task("[cyan]Downloading user fields...", total=None)
        user_fields = fetch_data_with_progress("/api/v2/user_fields.json", environment, progress, task_id, 'user_fields')
        progress.remove_task(task_id)
    prepare_and_save_data(user_fields, 'user_fields', environment)

@app.command()
def get_ticket_fields(environment: str):
    """Fetches ticket fields from Zendesk and saves them to a CSV file."""
    with Progress() as progress:
        task_id = progress.add_task("[cyan]Downloading ticket fields...", total=None)
        ticket_fields = fetch_data_with_progress("/api/v2/ticket_fields.json", environment, progress, task_id, 'ticket_fields')
        progress.remove_task(task_id)
    prepare_and_save_data(ticket_fields, 'ticket_fields', environment)



if __name__ == "__main__":
    app()
