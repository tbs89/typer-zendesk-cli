import typer
from .credentials import get_zenpy_client
from dotenv import load_dotenv
import pandas as pd
import os
from rich import print


app = typer.Typer()

load_dotenv()



def apply_macro_to_ticket(zenpy_client, ticket_id: int, macro_id: int):

    macro_result = zenpy_client.tickets.show_macro_effect(ticket_id, macro_id)
    zenpy_client.tickets.update(macro_result.ticket)
    return "Applied" if macro_result.ticket else "Failed"



@app.command()
def run_macro_on_tickets(file_name: str, environment: str):

    zenpy_client = get_zenpy_client(environment)
    domain_url = os.getenv(f'ZENDESK_{environment.upper()}_DOMAIN').rstrip('/')
    subdomain = domain_url.split('//')[-1].split('.')[0]

    dir_path = '../typer_data/advanced/apply_macro/'
    os.makedirs(dir_path, exist_ok=True)
    file_path = os.path.join(dir_path, file_name)

    test_ticket_id_input = typer.prompt(
        "Enter the Ticket ID to test the macro on (press 9 to skip the test and start bulk action, 0 to return to menu)", default="",
        show_default=False)
    if test_ticket_id_input == '0':
        typer.echo("Returning to the previous menu.")
        return
    elif test_ticket_id_input != '9':
        try:
            test_ticket_id = int(test_ticket_id_input)
            macro_id_input = typer.prompt("Enter Macro ID to test (0 to return to menu)")
            if macro_id_input == '0':
                typer.echo("Returning to the previous menu.")
                return
            macro_id = int(macro_id_input)
            result = apply_macro_to_ticket(zenpy_client, test_ticket_id, macro_id)
            ticket_link = f"https://{subdomain}.zendesk.com/agent/tickets/{test_ticket_id}"
            print(f"---------------------------------------------------------------------")
            print(f"[bold magenta]Test result: {result}[/bold magenta]")
            print(f"[bold magenta]Check the ticket at: {ticket_link}[/bold magenta]")
            print(f"---------------------------------------------------------------------")
            if not typer.confirm("Do you want to continue applying macros to the full list of tickets?"):
                typer.echo("Operation aborted.")
                return
        except ValueError:
            typer.echo("Please enter a valid number or choose an option. Returning to the previous menu.")
            return

    df = pd.read_csv(file_path)
    if 'result' not in df.columns:
        df['result'] = None

    for index, row in df.iterrows():
        ticket_id = int(row['ticket_id'])
        macro_id = int(row['macro_id'])
        try:
            result = apply_macro_to_ticket(zenpy_client, ticket_id, macro_id)
            df.at[index, 'result'] = result
            print(
                f"[green]Macro Applied to {row['ticket_id']} - Check >> https://{subdomain}.zendesk.com/agent/tickets/{ticket_id}[/green]")
        except Exception as e:
            df.at[index, 'result'] = f"Failed: {e}"
            print(f"[bold yellow]Failed: {row['ticket_id']} - {e}[/bold yellow]")

    df.to_csv(file_path, index=False)
    typer.echo("-----------------------------------------------------------------")
    print(f"[bold green]Bulk Action Done - File Updated {file_path}[/bold green]")
    typer.echo("-----------------------------------------------------------------")




@app.command()
def apply_tags_to_tickets(file_name: str, environment: str):

    zenpy_client = get_zenpy_client(environment)

    dir_path = '../typer_data/advanced/apply_tags/'
    os.makedirs(dir_path, exist_ok=True)
    file_path = os.path.join(dir_path, file_name)

    df = pd.read_csv(file_path)


    if not any(col for col in df.columns if col.startswith('tag_')):
        print(f"[bold red]No tags found in the CSV file. Each tag should be in its own column starting with 'tag_'.[/bold red]")
        print(f"[bold blue]Download the CSV template and try again: https://github.com/tbs89/typer-zendesk-cli/blob/main/docs/templates/apply_tags_template.csv[/bold blue]")
        return

    print(f"[bold blue]You are about to tags the tickets[/bold blue]")

    if not typer.confirm("Do you want to proceed?", default=False):
        print("[bold red]Operation cancelled.[/bold red]")
        return

    for index, row in df.iterrows():
        ticket_id = row['ticket_id']
        tags = [str(row[tag_column]) for tag_column in df.columns if
                         tag_column.startswith('tag_') and pd.notnull(row[tag_column])]

        try:
            ticket = zenpy_client.tickets(id=ticket_id)
            ticket.tags.extend(tags)
            zenpy_client.tickets.update(ticket)
            df.at[index, 'result'] = 'Tags applied'
            print(f"-----------------------------------------------------------------")
            print(f"[green]Tags {tags} applied to ticket {ticket_id}[/green]")
        except Exception as e:
            df.at[index, 'result'] = f"Failed: {e}"
            print(f"-----------------------------------------------------------------")
            print(f"[bold yellow]Failed to apply tags to ticket {ticket_id}: {e}[/bold yellow]")

    df.to_csv(file_path, index=False)
    print(f"-----------------------------------------------------------------")
    print(f"[bold green]Tags Applied - File Updated {file_path}[/bold green]")




if __name__ == "__main__":
    app()


