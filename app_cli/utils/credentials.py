import os
import time

import typer
from zenpy import Zenpy
from rich import print

from .helpers import validate_email, verify_connection

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

    print(f"[bold green][{environment.upper()}] Credentials saved in .env file[/bold green]")







@app.command()
def set_credentials(
    email: str = typer.Option(..., prompt="Enter your user email", callback=validate_email),
    domain_input: str = typer.Option(..., prompt="Enter your company name for the Zendesk domain (example: 'your_company', for 'your_company.zendesk.com')"),
    token: str = typer.Option(..., prompt="Enter your Zendesk API token (it will not appear here)", hide_input=True, confirmation_prompt=True),
):

    while True:
        environment = typer.prompt("Is this for production or sandbox? [Type '0' to exit]")
        if environment == "0":
            typer.echo("Exiting the application...")
            raise typer.Exit()
        elif environment.lower() in ['production', 'sandbox']:
            break
        else:
            typer.echo("Invalid input. Please type 'production', 'sandbox', or '0' to exit.")

    domain = f"https://{domain_input}.zendesk.com/"
    if verify_connection(domain, email, token):
        print(f"[bold green][{environment.upper()}] Connection verified successfully![/bold green]")
        save_credentials(email, domain, token, environment)
        print(f"--------------------------------------------------------------------------------")
        print(f"[bold green][{environment.upper()}] CONFIGURATION:[/bold green]")
        print(f"[bold green] USER EMAIL: {email} - DOMAIN: {domain}[/bold green]")
        print(f"[bold green] Token: {token[:10]}******************************** [/bold green]")
        print(
            f"[bold green][{environment.upper()}] App is correctly configured to be used in {environment.capitalize()}[/bold green]")
        print(f"--------------------------------------------------------------------------------")
        print(f"[bold green]Run the app again![/bold green]")
    else:
        print("[bold red]Failed to verify connection with the provided credentials. Run the app and try again[/bold red]")





@app.command()
def update_credentials():
    while True:
        environment = typer.prompt("Which environment do you want to update? (production/sandbox) [0 to exit]",
                                   type=str)
        if environment == "0":
            print("[bold yellow]Closing app... [/bold yellow]")
            time.sleep(2)
            print("[bold yellow]Run the app again to update the credentials[/bold yellow]")
            raise typer.Exit()
        if environment in ["production", "sandbox"]:
            break
        print("Invalid environment. Choose 'production' or 'sandbox' or '0' to exit.")

    email = typer.prompt("Enter your user email")
    domain_input = typer.prompt("Enter your company name for the Zendesk domain (example: 'your_company')")
    domain = f"https://{domain_input}.zendesk.com/"
    token = typer.prompt("Enter your Zendesk API token", hide_input=True)

    if verify_connection(domain, email, token):
        print(f"[bold green][{environment.upper()}] Connection verified successfully![/bold green]")
        save_credentials(email, domain, token, environment)
        print(f"--------------------------------------------------------------------------------")
        print(f"[bold green][{environment.upper()}] CONFIGURATION:[/bold green]")
        print(f"[bold green] USER EMAIL: {email} - DOMAIN: {domain}[/bold green]")
        print(f"[bold green] Token: {token[:10]}******************************** [/bold green]")
        print(
            f"[bold green][{environment.upper()}] Credentials updated correctly in {environment.capitalize()}[/bold green]")
        print(f"--------------------------------------------------------------------------------")
        print(f"[bold green]Run the app again![/bold green]")
    else:
        print("❌ - [bold red]Failed to verify connection with the provided credentials. Please check and try again[/bold red]")




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







if __name__ == "__main__":
    app()

