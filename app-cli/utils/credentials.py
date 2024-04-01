import os
import typer
import requests
from zenpy import Zenpy
from rich import print


app = typer.Typer()

def save_credentials(email: str, domain: str, token: str, environment: str = "production"):

    env_file = "../.env"
    credentials = {
        f"ZENDESK_{environment.upper()}_EMAIL": email,
        f"ZENDESK_{environment.upper()}_DOMAIN": domain,
        f"ZENDESK_{environment.upper()}_TOKEN": token,
    }

    if os.path.exists(env_file):
        with open(env_file, "r") as file:
            lines = file.readlines()

        with open(env_file, "w") as file:
            updated = False
            for line in lines:
                key = line.split("=")[0]
                if key in credentials:
                    file.write(f"{key}={credentials[key]}\n")
                    del credentials[key]
                    updated = True
                else:
                    file.write(line)
            if not updated:
                for key, value in credentials.items():
                    file.write(f"{key}={value}\n")
    else:
        with open(env_file, "w") as file:
            for key, value in credentials.items():
                file.write(f"{key}={value}\n")

    print(f"[bold green]Credentials for {environment} environment saved successfully![/bold green]")






def verify_connection(domain: str, email: str, token: str) -> bool:

    test_url = f"{domain}api/v2/users/me.json"
    response = requests.get(test_url, auth=(f"{email}/token", token))
    return response.status_code in range(200, 299)






@app.command()
def set_credentials(
    email: str = typer.Option(..., prompt="Enter your user email"),
    domain_input: str = typer.Option(..., prompt="Enter your company name for the Zendesk domain (example: 'your_company', for 'your_company.zendesk.com')"),
    token: str = typer.Option(..., prompt="Enter your Zendesk API token (it will not appear here)", hide_input=True, confirmation_prompt=True),
    environment: str = typer.Option("production", prompt="Is this for production or sandbox?")
):

    domain = f"https://{domain_input}.zendesk.com/"
    if verify_connection(domain, email, token):
        print("[bold green]Connection verified successfully![/bold green]")
        save_credentials(email, domain, token, environment)
        print(f"[bold green]{environment.capitalize()} credentials saved successfully[/bold green]")
    else:
        print("[bold red]Failed to verify connection with the provided credentials. Please check and try again[/bold red]")






@app.command()
def update_credentials():

    environment = typer.prompt("Which environment do you want to update? (production/sandbox)", type=str)
    assert environment in ["production", "sandbox"], "Invalid environment. Choose 'production' or 'sandbox'."

    email = typer.prompt("Enter your user email")
    domain_input = typer.prompt("Enter your company name for the Zendesk domain (example: 'your_company')")
    domain = f"https://{domain_input}.zendesk.com/"
    token = typer.prompt("Enter your Zendesk API token", hide_input=True)

    if verify_connection(domain, email, token):
        print("✅ - [bold green]Connection verified successfully[/bold green] - ✅")
        save_credentials(email, domain, token, environment)
        print(f"[bold green]{environment.capitalize()} credentials updated successfully![/bold green]")
    else:
        print("❌ - [bold red]Failed to verify connection with the provided credentials. Please check and try again[/bold red]")






def get_auth(environment: str):

    email = os.getenv(f"ZENDESK_{environment.upper()}_EMAIL")
    token = os.getenv(f"ZENDESK_{environment.upper()}_TOKEN")
    domain = os.getenv(f"ZENDESK_{environment.upper()}_DOMAIN")
    auth = (f"{email}/token", token)
    return auth, domain





def get_zenpy_client(environment: str):

    email = os.getenv(f'ZENDESK_{environment.upper()}_EMAIL')
    token = os.getenv(f'ZENDESK_{environment.upper()}_TOKEN')
    domain_url = os.getenv(f'ZENDESK_{environment.upper()}_DOMAIN')

    subdomain = domain_url.split("//")[1].split(".")[0]

    creds = {
        'email': email,
        'token': token,
        'subdomain': subdomain
    }
    return Zenpy(**creds)






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






if __name__ == "__main__":
    app()

