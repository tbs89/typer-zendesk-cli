<body>
    <h1>Typer Zendesk CLI Tool</h1>
    <p>Typer Zendesk CLI Tool is a powerful command-line interface application designed to facilitate the management of Zendesk tasks. It leverages the flexibility of Typer and the comprehensive API provided by Zendesk to offer a seamless user experience for managing tickets, users, groups, and more directly from your terminal.</p>

<p>The Typer Zendesk CLI Tool was developed using <a href="https://typer.tiangolo.com" target="_blank">Typer</a>, a powerful library for building CLI applications with Python. Typer is created by <a href="https://github.com/tiangolo" target="_blank">Sebastián Ramírez</a>, the same developer behind the popular FastAPI framework. 

<hr>
  <h2>Features</h2>
    <ul>
        <li>Fetch and display Zendesk data such as users, tickets, and groups.</li>
        <li>Create and manage users and groups in bulk.</li>
        <li>Apply macros and tags to tickets efficiently.</li>
        <li>Update Zendesk configurations and permissions with ease.</li>
        <li>Support for both sandbox and production environments.</li>
    </ul>

<h2>Installation</h2>
<p>To use the Typer Zendesk CLI Tool, first clone or download the repository from GitHub:</p>
<pre><code>git clone https://github.com/tbs89/typer-zendesk-cli.git</code></pre>
<p>Alternatively, you can download the repository as a ZIP file and extract it.</p>

<h2>Setting Up</h2>
<p>Navigate to the project directory:</p>
<pre><code>cd typer-zendesk-cli</code></pre>
<p>It's recommended to use a virtual environment. Create and activate one with:</p>
<pre><code>python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`</code></pre>
<p>Install the required dependencies:</p>
<pre><code>pip install -r requirements.txt</code></pre>

<h2>Usage</h2>
<p>To start using the CLI tool, invoke the main script:</p>
<pre><code>python app-cli/main.py</code></pre>
<p>This command will display the Main Menu, guiding you through the available commands and options:</p>

<br><br>
<img src="https://github.com/tbs89/typer-zendesk-cli/blob/main/docs/screenshots/main_menu.png" alt="Main Menu" width="400">

  <h2>Easy Navigation</h2>
    <p>The Typer Zendesk CLI is designed with user experience in mind, offering an intuitive navigation system that guides you through each step. This approach ensures that you can access all functionalities easily, without the constant need to resort to <code>--help</code> for guidance.</p>

<h2>Getting Started</h2>
<p>Before diving into the commands and functionalities, you need to set up your credentials. Navigate to 'Set up Zendesk credentials' from the Main Menu and provide your Zendesk email, domain, and API token. 
<br><br><br>
<img src="https://github.com/tbs89/typer-zendesk-cli/blob/main/docs/screenshots/setup_api.png" alt="Set Up" width="800">
<br><br><br>
The application supports both production and sandbox environments, with the sandbox being optional for a safer testing ground.</p>

<img src="https://github.com/tbs89/typer-zendesk-cli/blob/main/docs/screenshots/setup_api2.png" alt="Set Up" width="800">
<br>


<img src="https://github.com/tbs89/typer-zendesk-cli/blob/main/docs/screenshots/api_success.png" alt="Set Up" width="600">
<br><br><br>
<hr>
<h2>Navigating the Application</h2>
<p>Once your credentials are set up, navigate to the <strong>Admin Actions</strong> section from the main menu to explore a variety of tasks you can perform:</p>
<ul>
    <li><strong>Get Actions</strong>: Fetch and download as CSV various Zendesk entities such as:</li>
</ul>
        <ul>
    <li><code>Users</code>: Download a list of all users including agents and administrators.</li>
    <li><code>Macros</code>: Fetch all the macros set up for ticket responses and actions.</li>
    <li><code>Articles</code>: Retrieve all articles from your Zendesk Help Center.</li>
    <li><code>Organizations</code>: Get a list of all organizations added to your Zendesk.</li>
    <li><code>Groups</code>: Download details of agent groups for managing tickets.</li>
    <li><code>Dynamic Content</code>: Fetch all dynamic content items for use in tickets and help center articles.</li>
    <li><code>Views</code>: Retrieve all views that define ticket lists based on certain criteria.</li>
    <li><code>Triggers</code>: Download all triggers that automatically perform actions on tickets.</li>
    <li><code>Automations</code>: Fetch automations that perform actions on tickets after certain conditions have been met over time.</li>
    <li><code>Brands</code>: Get a list of all brands managed within your Zendesk instance.</li>
    <li><code>User Fields</code>: Download custom fields added to user profiles.</li>
    <li><code>Ticket Fields</code>: Retrieve custom fields added to tickets for additional data collection.</li>
        </ul>


<br>
<img src="https://github.com/tbs89/typer-zendesk-cli/blob/main/docs/screenshots/get_data.png" alt="Set Up" width="600">
<br>

The data is downloaded in CSV in a folder created by the app:

<img src="https://github.com/tbs89/typer-zendesk-cli/blob/main/docs/screenshots/get_data2.png" alt="Set Up" width="800">
<br><br><br>



<ul>
    <li>
        <strong>Put Actions</strong>: This feature enables the modification of existing permissions for macros within your Zendesk environment. You can specifically define the access control for macros, determining which user groups can utilize them for automated responses. This section facilitates both the restriction of macros to selected groups for focused use and the opening of macros for access by all users.
    </li>
</ul>

<br><br>
<img src="https://github.com/tbs89/typer-zendesk-cli/blob/main/docs/screenshots/update_macros_put.png" alt="Set Up" width="800">
<br><br><br>

<ul>
    <li>
        <strong>Post Actions</strong>: Facilitate bulk creation of users, groups, and other Zendesk entities to streamline administrative tasks. This functionality is ideal for large-scale deployments or organizational changes, enabling you to efficiently onboard new users, establish groups for better collaboration, and add other necessary entities with minimal manual input.
    </li>
</ul>

<br><br>
<img src="https://github.com/tbs89/typer-zendesk-cli/blob/main/docs/screenshots/post_options.png" alt="Set Up" width="600">
<br><br><br>
 <ul>   
    <li>
        <strong>ADVANCED</strong>: Using <a href="http://docs.facetoe.com.au/zenpy.html">Zenpy</a> for more management of tickets, including the application of macros and the addition of tags to tickets by giving a list of tickets, the user can apply macros directly to tickets.
    </li>
</ul>

<br><br>
<img src="https://github.com/tbs89/typer-zendesk-cli/blob/main/docs/screenshots/advanced.png" alt="Set Up" width="600">

<br><br><br>


<img src="https://github.com/tbs89/typer-zendesk-cli/blob/main/docs/screenshots/admin_actions.png" alt="Set Up" width="400">
<br><br><br>
<hr>

  <h2>Contribution</h2>
    <p>Contributions to the Typer Zendesk CLI Tool are welcome! Feel free to fork the repository, make your changes, and submit a pull request.</p>

  <h2>License</h2>
    <p>The Typer Zendesk CLI Tool is released under the MIT License. See the LICENSE file for more details.</p>

  <h2>Contact</h2>
    <p>For questions, suggestions, or issues, please open an issue on the GitHub repository.</p>
</body>


