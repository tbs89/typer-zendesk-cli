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


<h2>Exploring Admin Actions</h2>
<p>Once your credentials are set, the 'Admin Actions' menu becomes your central hub for managing Zendesk tasks. Here's an overview into what you can do:</p>

<ul>
    <li><strong>Get Actions</strong> - Retrieve and display various data from Zendesk, including users, tickets, groups, and more. This is crucial for understanding your current Zendesk setup and making informed decisions.</li>
    <li><strong>Put Actions</strong> - Modify existing Zendesk configurations, like updating macro permissions. This allows you to refine your workflow and ensure your team has the necessary access.</li>
    <li><strong>Post Actions</strong> - Create new entities within Zendesk, such as users and groups. This feature is essential for expanding your team and organizing your workspace efficiently.</li>
    <li><strong>ADVANCED</strong> - Leverage Zenpy-powered actions to apply macros to tickets and tags, streamlining repetitive tasks and enhancing your ticket management process.</li>
</ul>

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


