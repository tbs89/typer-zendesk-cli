<body>
    <h1>Typer Zendesk CLI Tool</h1>
    <p>Typer Zendesk CLI Tool is a powerful command-line interface application designed to facilitate the management of Zendesk tasks. It leverages the flexibility of Typer and the comprehensive API provided by Zendesk to offer a seamless user experience for managing tickets, users, groups, and more directly from your terminal.</p>
    
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

<br>
<img src="https://github.com/tbs89/typer-zendesk-cli/blob/main/docs/screenshots/main_menu.png" alt="Main Menu" width="400">

  <h2>Easy Navigation</h2>
    <p>The Typer Zendesk CLI is designed with user experience in mind, offering an intuitive navigation system that guides you through each step. This approach ensures that you can access all functionalities easily, without the constant need to resort to <code>--help</code> for guidance.</p>

<h2>Getting Started</h2>
<p>Before diving into the commands and functionalities, you need to set up your credentials. Navigate to 'Set up Zendesk credentials' from the Main Menu and provide your Zendesk email, domain, and API token. 

<img src="https://github.com/tbs89/typer-zendesk-cli/blob/main/docs/screenshots/setup_api.png" alt="Set Up" width="800">

The application supports both production and sandbox environments, with the sandbox being optional for a safer testing ground.</p>

<img src="https://github.com/tbs89/typer-zendesk-cli/blob/main/docs/screenshots/setup_api2.png" alt="Set Up" width="800">



<img src="https://github.com/tbs89/typer-zendesk-cli/blob/main/docs/screenshots/api_success.png" alt="Set Up" width="600">


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



<img src="https://github.com/tbs89/typer-zendesk-cli/blob/main/docs/screenshots/get_data.png" alt="Set Up" width="600">

The data is downloaded in CSV in a folder created by the app:

<img src="https://github.com/tbs89/typer-zendesk-cli/blob/main/docs/screenshots/get_data2.png" alt="Set Up" width="800">






<ul> 
    <li><strong>Put Actions</strong>: Update existing Zendesk configurations and permissions.</li>
    <li><strong>Post Actions</strong>: Create new users, groups, and other entities in bulk.</li>
    <li><strong>ADVANCED</strong>: Perform advanced actions using Zenpy, such as applying macros to tickets and adding tags.</li>
</ul>
<p>This structured approach ensures that you can easily navigate and utilize the tool's features without the need to rely on <code>--help</code> commands at every step.</p>

<h2>Key Commands and Features</h2>
<p>The Typer Zendesk CLI Tool offers a wide range of commands to streamline your Zendesk management tasks:</p>
<ul>
    <li><code>get-users</code>: Retrieves and displays a list of Zendesk users.</li>
    <li><code>create-group</code>: Creates a new group within Zendesk.</li>
    <li><code>apply-macro</code>: Applies a specified macro to a list of tickets, allowing for efficient bulk updates.</li>
    <li><code>add-tags</code>: Adds tags to a specified ticket, enhancing ticket organization and filtering.</li>
</ul>
<p>These commands represent just the beginning of what the Typer Zendesk CLI Tool can do. Dive into each section within the <strong>Admin Actions</strong> menu to discover more capabilities designed to enhance your Zendesk experience.</p>

<p>The 'Admin Actions' menu is designed for easy navigation, enabling you to execute powerful Zendesk operations without ever needing to use the <code>--help</code> command.</p>

<img src="https://github.com/tbs89/typer-zendesk-cli/blob/main/docs/screenshots/admin_actions.png" alt="Set Up" width="400">



<h2>Advanced Usage</h2>
<p>For those looking to leverage the full power of <a href="http://docs.facetoe.com.au/zenpy.html">Zenpy</a>, the 'ADVANCED' section offers more functionalities:</p>

<ul>
    <li><strong>Apply Macros to Tickets</strong> - Automate ticket responses and actions by applying predefined macros in bulk, saving time and ensuring consistency in your communications.</li>
    <li><strong>Apply Tags to Tickets</strong> - Enhance ticket categorization and searchability by adding tags in bulk, allowing for more effective ticket management and reporting.</li>
</ul>

<p>These advanced features make it possible to handle complex Zendesk tasks directly from your terminal, offering a level of control and efficiency that can significantly boost your support operations.</p>











    

  

  <h2>Contribution</h2>
    <p>Contributions to the Typer Zendesk CLI Tool are welcome! Feel free to fork the repository, make your changes, and submit a pull request.</p>

  <h2>License</h2>
    <p>The Typer Zendesk CLI Tool is released under the MIT License. See the LICENSE file for more details.</p>

  <h2>Contact</h2>
    <p>For questions, suggestions, or issues, please open an issue on the GitHub repository.</p>
</body>


