[![Medium](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@tbs89berlin)
[![image](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/tomas-b-s)
![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Typer Zendesk CLI Tool

<body>
    <p>Typer Zendesk CLI Tool is a powerful command-line interface application designed to facilitate the management of Zendesk Admin tasks. The app allows interaction with the Zendesk API to carry out actions such as data download, ticket updates, users, bulk actions, and more.</p>

<p>Typer Zendesk CLI has been developed using <a href="https://typer.tiangolo.com" target="_blank">Typer</a>, a powerful library for building CLI applications with Python. Typer was created by <a href="https://github.com/tiangolo" target="_blank">Sebastián Ramírez</a>, the same developer behind the popular FastAPI framework. 

<hr>


## Table of Contents
1. [Introduction](#introduction)
2. [As a Zendesk Administrator, What You Can Do with Typer Zendesk CLI](#as-a-zendesk-administrator-what-you-can-do-with-typer-zendesk-cli)
3. [Download](#download)
4. [Creation](#creation)
5. [Update](#update)
6. [Advanced - Bulk Actions](#advanced---bulk-actions)
7. [Production or Sandbox](#production-or-sandbox)
8. [Easy Navigation](#easy-navigation)
9. [Installation](#installation)
10. [Setting Up](#setting-up)
11. [Usage](#usage)
12. [Getting Started](#getting-started)
13. [Contribution and Contact](#contribution-and-contact)
14. [License](#license)
15. [Acknowledgements](#acknowledgements)

<hr>


## As a Zendesk Administrator, What You Can Do with Typer Zendesk CLI
  <p>Zendesk administrators typically carry out daily tasks from the Zendesk UI itself. However, there are certain actions where the Zendesk UI is limited and must be carried out using the API.

Actions such as obtaining the list of agents with their information (email, role name, etc.), downloading Help Center articles, applying a macro given a list of ticket IDs, assigning a group to a long list of agents, changing macro permissions, etc.

Getting the list of agents or macros in CSV format can only be obtained through the API, as well as obtaining Help Center articles. On the other hand, Zendesk allows applying macros to tickets, but only up to 100 tickets per action and all must be in a view. Also, changing macro permissions or assigning a group to a long list of agents can be tedious and time-consuming, as well as creating a long list of Zendesk agents with their corresponding role.
<br><br>

<p>Typer Zendesk CLI allows Admins to perform all these actions in a matter of seconds:</p>
<br>

## DOWNLOAD
<br>

- Download lists of agents, groups, macros, triggers, articles, etc.
<br><br>

```console
[PRODUCTION] Select the data you want to download:
---------------------------------------
[1] Users [2] Macros [3] Articles [4] Organizations
[5] Groups [6] Dynamic Content [7] Views [8] Triggers
[9] Automations [10] Brands [11] User Fields [12] Ticket Fields
[13] Go Back
Enter your choice: 

```

By selecting the data we want to download, the app will do so in a matter of seconds in CSV format:

```console
[PRODUCTION] Select the data you want to download:
---------------------------------------
[1] Users [2] Macros [3] Articles [4] Organizations
[5] Groups [6] Dynamic Content [7] Views [8] Triggers
[9] Automations [10] Brands [11] User Fields [12] Ticket Fields
[13] Go Back
Enter your choice: 1

✅ - Users data saved successfully to typer_data/get_data/users/production/zd_users_production_2024-04-01_11-58-14.csv

```

The CSV file will be ready for use in spreadsheets or excel.
<br><br>
<hr>

## CREATION
<br>

- Bulk create groups or agents with their corresponding role, as well as assign them to groups.


```console
[PRODUCTION] Select the bulk action you want to perform:
---------------------------------------
[1] Groups - Create Groups
[2] Groups - Assign Agents to a Group
[3] Users - Create Agents
[0] Go Back
Enter your choice:
```
<br><br>
<hr>

## UPDATE
<br>

- Bulk update macros permissions, such as restricting the use of macros to certain groups, or conversely, allowing all macros to be visible.
<br><br>

```console
[PRODUCTION] Select the PUT action you want to perform:
---------------------------------------
[1] Macros - Update Permissions
[0] Go Back
Enter your choice:
```
<br><br>
<hr>

## ADVANCED - BULK ACTIONS
<br>

- Apply a macro to a large list of tickets or simply add a tag to them by providing a CSV file.

```console
[PRODUCTION] Select the ADVANCED action you want to perform:
---------------------------------------
[1] Tickets - Apply Macro to Tickets
[2] Tickets - Apply Tags to Tickets
[0] Go Back
Enter your choice:
```
<br><br>
<hr>

## PRODUCTION OR SANDBOX
<br>

- The app allows interaction both in production and in the sandbox, enabling switching between both environments to test bulk actions or updates on tickets, groups, or users before going to production.

```console
Is this for 'production' or 'sandbox'? (Enter '0' to go back):
```
<br><br>
<hr>



## Easy Navigation
<p>The Typer Zendesk CLI is designed with user experience in mind, offering an intuitive navigation system that guides the user through each step without the constant need to resort to <code>--help</code> for guidance.</p>


```console
Main Menu:
[1] Set up Zendesk credentials
[2] Update Zendesk credentials
[3] Admin Actions
-------------------------------------------------
[4] Documentation
[0] Exit App >>
Enter your choice:
```

<hr>

## Installation
<p>To use the Typer Zendesk CLI Tool, first clone or download the repository from GitHub:</p>
<pre><code>git clone https://github.com/tbs89/typer-zendesk-cli.git</code></pre>
<p>Alternatively, you can download the repository as a ZIP file and extract it.</p>

## Setting Up
<p>Navigate to the project directory:</p>
<pre><code>cd typer-zendesk-cli</code></pre>
<p>It's recommended to use a virtual environment. Create and activate one with:</p>
<pre><code>python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`</code></pre>
<p>Install the required dependencies:</p>
<pre><code>pip install -r requirements.txt</code></pre>

## Usage
<p>To start using the CLI tool, invoke the main script:</p>

```console
(venv) (base) tomasbaidal@MBP-de-Tomas app-cli % python main.py

Main Menu:
[1] Set up Zendesk credentials
[2] Update Zendesk credentials
[3] Admin Actions
-------------------------------------------------
[4] Documentation
[0] Exit App >>
Enter your choice:
```
<p>This command will display the Main Menu, guiding you through the available commands and options.</p>


<br><br>

## Getting Started
<p>Before using the commands and functionalities, you need to set up your credentials. Navigate to <strong>'Set up Zendesk credentials'</strong> from the Main Menu and provide your Zendesk email, domain, and API token. 
    
```console
Main Menu:
[1] Set up Zendesk credentials
[2] Update Zendesk credentials
[3] Admin Actions
-------------------------------------------------
[4] Documentation
[0] Exit App >>
Enter your choice: 1
Let's set the credentials
Enter your user email: 
```

<p>The application will prompt you to enter your user email, domain, API Token, and environment</p>


```console
Enter your choice: 1
Let's set the credentials
Enter your user email: name.surname@me.com
Enter your company name for the Zendesk domain (example: 'your_company', for 'your_company.zendesk.com'): mycompany
Enter your Zendesk API token (it will not appear here):
Repeat for confirmation:
Is this for production or sandbox?: production
```

<p>Upon entering the credentials (email, API token, and domain), the app initiates an API call to this endpoint: {domain}api/v2/users/me.json. The app verifies the correctness of the credentials by making an API call to check them. If the verification is successful, the app creates a <code>.env</code> file where it stores the credentials from that point forward and uses them for any action:</p>

```console
[PRODUCTION] Connection verified successfully!
[PRODUCTION] Credentials saved in .env file
[PRODUCTION] App is correctly configured
--------------------------------------------------------------------------------
Run the app again!
```

<p>Credentials can also be modified in option <b>[2] Update Zendesk Credentials</b> or you can simply delete them by removing the <code>.env</code> file</p>

<hr>


## Contribution and Contact
<p>Contributions to the Typer Zendesk CLI Tool are welcome! Feel free to fork the repository, make your changes, and submit a pull request. The app includes functionalities that I use in my day-to-day activities, but if you have any suggestions or additional features you'd like to see, just open an issue, and I will consider expanding the app's capabilities.</p>
<p>If you are Zendesk Admin and you have questions, suggestions, or issues, please open an issue on the GitHub repository.</p>


## License
<p>The <strong>Typer Zendesk CLI Tool</strong> is released under the MIT License. See the LICENSE file for more details.</p>

<br>

## Acknowledgements
<p>I would also like to extend a heartfelt thank you to <a href="https://github.com/tiangolo" target="_blank">Sebastián Ramírez</a>, the creator of Typer, for developing such a cool tool. Thank you for your contribution to the open-source community!</p>


