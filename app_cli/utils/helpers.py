import os
import re
import typer
import requests

def ensure_data_path(relative_path, environment):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    data_path = os.path.join(base_dir, 'typer_data', environment, relative_path)
    os.makedirs(data_path, exist_ok=True)
    return data_path


def validate_email(email: str) -> str:
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(pattern, email):
        raise typer.BadParameter("This is not a valid email. Please enter a valid email address or press 0 to exit.")
    return email


def verify_connection(domain: str, email: str, token: str) -> bool:

    test_url = f"{domain}api/v2/users/me.json"
    response = requests.get(test_url, auth=(f"{email}/token", token))
    return response.status_code in range(200, 299)


def get_auth(environment: str):

    email = os.getenv(f"ZENDESK_{environment.upper()}_EMAIL")
    token = os.getenv(f"ZENDESK_{environment.upper()}_TOKEN")
    domain = os.getenv(f"ZENDESK_{environment.upper()}_DOMAIN")
    auth = (f"{email}/token", token)
    return auth, domain


def prompt_for_environment() -> str:

    while True:
        environment = typer.prompt("Is this for 'production' or 'sandbox'? (Enter '0' to go back)",
                                   default="", show_choices=False)
        if environment == '0':
            return 'back'
        if environment.lower() in ['production', 'sandbox']:
            return environment.lower()
        else:
            print("[bold red]Please enter 'production', 'sandbox', or '0' to go back.[/bold red]")



