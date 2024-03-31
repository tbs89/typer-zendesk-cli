import typer
import os
from rich import print
import time

from utils.credentials import app as credentials_app
from utils.get import (
    get_users,
    get_macros,
    get_articles,
    get_organizations,
    get_groups,
    get_dynamic_content,
    get_views,
    get_triggers,
    get_automations,
    get_brands,
    get_user_fields,
    get_ticket_fields
)
from utils.post import (
    create_groups,
    assign_agents_to_group,
    create_agents_in_bulk
)
from utils.put import update_macro_permissions
from utils.advanced import (
    run_macro_on_tickets,
    apply_tags_to_tickets
)



app = typer.Typer(add_completion=False,
                  help="Welcome to Typer Zendesk CLI. This is a command line tool for managing Zendesk tasks.")


def prompt_for_environment() -> str:

    while True:
        environment = typer.prompt("Is this for production or sandbox? (Enter '0' to go back)",
                                   default="", show_choices=False)
        if environment == '0':
            return 'back'
        if environment.lower() in ['production', 'sandbox']:
            return environment.lower()
        else:
            print("[bold red]Please enter 'production', 'sandbox', or '0' to go back.[/bold red]")

def get_data_actions(environment: str):
    while True:
        print(f"\n[bold blue][{environment.upper()}]Select the data you want to download:[/bold blue]")
        typer.echo("---------------------------------------")
        typer.echo("[1] Users [2] Macros [3] Articles [4] Organizations")
        typer.echo("[5] Groups [6] Dynamic Content [7] Views [8] Triggers")
        typer.echo("[9] Automations [10] Brands [11] User Fields [12] Ticket Fields")
        print("[bold magenta][13] Go Back[/bold magenta]")
        choice = typer.prompt("Enter your choice", type=int)


        if choice == 1:
            get_users(environment)
        elif choice == 2:
            get_macros(environment)
        elif choice == 3:
            get_articles(environment)
        elif choice == 4:
            get_organizations(environment)
        elif choice == 5:
            get_groups(environment)
        elif choice == 6:
            get_dynamic_content(environment)
        elif choice == 7:
            get_views(environment)
        elif choice == 8:
            get_triggers(environment)
        elif choice == 9:
            get_automations(environment)
        elif choice == 10:
            get_brands(environment)
        elif choice == 11:
            get_user_fields(environment)
        elif choice == 12:
            get_ticket_fields(environment)
        elif choice == 13:
            return
        else:
            print(f"[bold yellow]Invalid choice: {choice}, please try again[/bold yellow]")


def post_data_actions(environment: str):
    while True:
        print("\n[bold blue]Select the bulk action you want to perform:[/bold blue]")
        typer.echo("---------------------------------------")
        typer.echo("[1] Groups - Create Groups")
        typer.echo("[2] Groups - Assign Agents to a Group")
        typer.echo("[3] Users - Create Agents")
        print("[bold magenta][0] Go Back[/bold magenta]")
        choice = typer.prompt("Enter your choice", type=int)

        if choice == 0:
            return

        if choice == 1:
            dir_path = 'typer_data/post_data/create_groups/'
            os.makedirs(dir_path, exist_ok=True)
            typer.echo("----------------------------------------------")
            print("[bold blue]INSTRUCTIONS TO CREATE GROUPS IN BULK[/bold blue]")
            typer.echo("\n1 - First, ensure you've uploaded a CSV file to the following directory:")
            typer.echo(f"{dir_path} (folder has been created automatically already)")
            typer.echo("2 - The CSV file should have a header with 'group_name' as the first column.")
            typer.echo("This column should contain the names of the groups you wish to create.")
            print(
                "[Download CSV Template: https://github.com/tbs89/typer-zendesk-cli/blob/main/docs/templates/create_groups_template.csv]")
            file_name = typer.prompt("3 - Enter the name of the CSV file you've uploaded (including .csv)")
            create_groups(file_name, environment)
        elif choice == 2:
            dir_path = 'typer_data/post_data/assign_groups/'
            os.makedirs(dir_path, exist_ok=True)
            typer.echo("----------------------------------------------")
            print("[bold blue]INSTRUCTIONS TO ASSIGN AGENTS TO A GROUP IN BULK[/bold blue]")
            typer.echo("\n1 - First, ensure you've uploaded a CSV file to the following directory:")
            typer.echo(f"{dir_path} (folder has been created automatically already)")
            typer.echo("2 - The CSV file should have a header with 'email' as the first column.")
            typer.echo("This column should contain the email addresses of the agents you wish to assign to a group.")
            print(
                "[Download CSV Template: https://github.com/tbs89typer-zendesk-cli/blob/main/docs/templates/assign_agents_template.csv]")
            file_name = typer.prompt("3 - Enter the name of the CSV file you've uploaded (including .csv)")
            group_id = typer.prompt("4 - Enter the ID of the group you wish to assign the agents to", type=int)
            assign_agents_to_group(file_name, group_id, environment)

        elif choice == 3:
            dir_path = 'typer_data/post_data/create_agents/'
            os.makedirs(dir_path, exist_ok=True)
            typer.echo("----------------------------------------------")
            typer.echo("INSTRUCTIONS TO CREATE AGENTS IN BULK")
            typer.echo("\n1 - First, ensure you've uploaded a CSV file to the following directory:")
            typer.echo(f"{dir_path} (folder has been created automatically already)")
            typer.echo("2 - The CSV file should have 3 columns: 'name' as the first column, 'email' as second column and 'custom_role_id'")
            typer.echo("'name' should contain agent's name, 'email' agent's email and 'custom_role_id' the id of the role")
            print(
                "[Download CSV Template: https://github.com/tbs89/typer-zendesk-cli/blob/main/docs/templates/create_agents_template.csv]")
            file_name = typer.prompt("3 - Enter the name of the CSV file you've uploaded (including .csv)")
            create_agents_in_bulk(file_name, environment)
        else:
            print(f"[bold yellow]Invalid choice: {choice}, please try again[/bold yellow]")


def admin_actions():
    while True:
        typer.echo("-------------------------------------------------")
        print("[bold blue]Admin Actions:[/bold blue]")
        typer.echo("[1] Get Actions")
        typer.echo("[2] Put Actions")
        typer.echo("[3] Post Actions")
        typer.echo("[4] ADVANCED")
        typer.echo("-------------------------------------------------")
        typer.echo("[5] Not sure, give me info")
        print("[magenta][9] Go Back[/magenta]")
        print("[bold magenta][0] Exit App >>[/bold magenta]")
        choice = typer.prompt("Enter your choice", type=int)

        if choice == 9:
            return
        elif choice == 0:
            raise typer.Exit()

        if choice == 5:
            info_actions()
            time.sleep(10)
            continue

        environment = prompt_for_environment()
        if environment == 'back':
            continue


        if choice == 1:
            get_data_actions(environment)
        elif choice == 2:
            put_data_actions(environment)
        elif choice == 3:
            post_data_actions(environment)
        elif choice == 4:
            advanced_data_actions(environment)
        elif choice == 9:
            return
        elif choice == 0:
            raise typer.Exit()
        else:
            print(f"[bold yellow]Invalid choice {choice}, please try again [/bold yellow]")


def info_actions():
    print("\n[bold blue]Information about Admin Actions:[/bold blue]")
    print("[1] Get Actions - Download various Zendesk data like Users, Macros, Articles, etc.")
    print("[2] Put Actions - Update certain aspects of your Zendesk data like Macro permissions.")
    print("[3] Post Actions - Perform bulk actions like creating users, groups, or setting agents to groups.")
    print("[4] ADVANCED - Advanced operations like applying macros or tags to multiple tickets.")
    typer.echo("-------------------------------------------------\n")

def put_data_actions(environment: str):
    while True:
        print("\n[bold blue]Select the PUT action you want to perform:[/bold blue]")
        typer.echo("---------------------------------------")
        typer.echo("[1] Macros - Update Permissions")
        print("[bold magenta][0] Go Back[/bold magenta]")
        choice = typer.prompt("Enter your choice", type=int)

        if choice == 0:
            return

        if choice == 1:
            dir_path = 'typer_data/put_data/update_permissions_macros/'
            os.makedirs(dir_path, exist_ok=True)
            typer.echo("----------------------------------------------")
            print("[bold blue]INSTRUCTIONS TO UPDATE MACRO PERMISSIONS[/bold blue]")
            typer.echo("\n1 - First, ensure you've uploaded a CSV file to the following directory:")
            typer.echo(f"{dir_path} (folder has been created automatically already)")
            typer.echo("2 - The CSV file must have a 'macro_id' column and optionally 'group_1', 'group_2', ... for group restrictions.")
            print(
                  "[Download CSV Template: https://github.com/tbs89/typer-zendesk-cli/blob/main/docs/templates/macro_update_template.csv]")
            typer.echo("If you want to open macros (no restrictions), include 'open' in 'group_1' column only.")
            file_name = typer.prompt("3 - Enter the name of the CSV file you've uploaded (including .csv)")
            update_macro_permissions(file_name, environment)
        else:
            print(f"[bold yellow]Invalid choice: {choice}, please try again[/bold yellow]")


def advanced_data_actions(environment: str):
    while True:
        print("\n[bold blue]Select the ADVANCED action you want to perform:[/bold blue]")
        typer.echo("---------------------------------------")
        typer.echo("[1] Tickets - Apply Macro to Tickets")
        typer.echo("[2] Tickets - Apply Tags to Tickets")
        print("[bold magenta][0] Go Back[/bold magenta]")
        choice = typer.prompt("Enter your choice", type=int)

        if choice == 0:
            return


        if choice == 1:
            dir_path = 'typer_data/advanced/apply_macro/'
            os.makedirs(dir_path, exist_ok=True)
            typer.echo("----------------------------------------------")
            print("[bold blue]INSTRUCTIONS TO APPLY MACROS IN BULK[/bold blue]")
            typer.echo("\n1 - First, ensure you've uploaded a CSV file to the following directory:")
            typer.echo(f"{dir_path} (folder has been created automatically already)")
            typer.echo("2 - The CSV file must have a 'ticket_id' column and 'macro_id' column.")
            print("[Download CSV Template: https://github.com/tbs89/typer-zendesk-cli/blob/main/docs/templates/apply_macro_template.csv4]")
            typer.echo(
                "If you want to apply the same macro to all tickets, 'macro_id' column values should be the same.")
            print(
                "[bold magenta]Do not worry, before bulk action, you will test if works by giving a ticket ID[/bold magenta]")
            file_name = typer.prompt("3 - Enter the name of the CSV file you've uploaded (including .csv)")
            try:
                run_macro_on_tickets(file_name, environment)
                return
            except typer.Abort:
                typer.echo("Returning to the previous menu.")
                continue

        elif choice == 2:
            dir_path = 'typer_data/advanced/apply_tags/'
            os.makedirs(dir_path, exist_ok=True)
            print("[bold blue]INSTRUCTIONS TO APPLY TAGS TO TICKETS IN BULK[/bold blue]")
            print("\n- Ensure you've uploaded a CSV file to the following directory:")
            print(f"{dir_path} (folder has been created automatically already)")
            print("- The CSV file must have a 'ticket_id' column and columns starting with 'tag_' for each tag.")
            print(
                "[Download CSV Template: https://github.com/tbs89/typer-zendesk-cli/blob/main/docs/templates/apply_tags_template.csv]")
            file_name = typer.prompt("Enter the name of the CSV file you've uploaded (including .csv)")
            apply_tags_to_tickets(file_name, environment)
        else:
            print(f"[bold yellow]Invalid choice: {choice}, please try again[/bold yellow]")



def main_menu():
    while True:
        print("\n[bold blue]Main Menu:[/bold blue]")
        typer.echo("[1] Set up Zendesk credentials")
        typer.echo("[2] Update Zendesk credentials")
        typer.echo("[3] Admin Actions")
        typer.echo("-------------------------------------------------")
        typer.echo("[4] Documentation")
        print("[bold magenta][0] Exit App >> [/bold magenta]")
        choice = typer.prompt("Enter your choice", type=int)

        if choice == 1:
            print(f"[bold green] Let's set the credentials [/bold green]")
            credentials_app(['set-credentials'])
        elif choice == 2:
            print(f"[bold green] Let's update the credentials [/bold green]")
            credentials_app(['update-credentials'])
        elif choice == 3:
            admin_actions()
        elif choice == 4:
            print(f"[bold green]Documentation is in progress... [/bold green]")
            time.sleep(3)
        elif choice == 0:
            raise typer.Exit()
        else:
            print(f"[bold yellow]Invalid choice: {choice}, please try again [/bold yellow]")


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """
    This callback is used to display the main menu.
    """
    if ctx.invoked_subcommand is None:
        main_menu()


if __name__ == "__main__":
    app()