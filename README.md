<body>
    <h1>Typer Zendesk CLI Tool</h1>
    <p>The Typer Zendesk CLI Tool is a powerful command-line interface application designed to facilitate the management of Zendesk tasks. It leverages the flexibility of Typer and the comprehensive API provided by Zendesk to offer a seamless user experience for managing tickets, users, groups, and more directly from your terminal.</p>
    
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
<p>This command will display the Main Menu, guiding you through the available commands and options.</p>
<p>For a visual guide, see the screenshots available in the <a href="https://github.com/tbs89/typer-zendesk-cli/blob/main/docs/screenshots">docs/screenshots</a> directory.</p>

  <h2>Easy Navigation</h2>
    <p>The Typer Zendesk CLI is designed with user experience in mind, offering an intuitive navigation system that guides you through each step. This approach ensures that you can access all functionalities easily, without the constant need to resort to <code>--help</code> for guidance.</p>

  <h2>Commands</h2>
    <p>Here are some of the commands you can use with the Typer Zendesk CLI Tool:</p>
    <ul>
        <li><code>get-users</code> - Fetch and display Zendesk users.</li>
        <li><code>create-group</code> - Create a new group in Zendesk.</li>
        <li><code>apply-macro</code> - Apply a macro to a list of tickets.</li>
        <li><code>add-tags</code> - Add tags to a ticket.</li>
    </ul>

  <h2>Contribution</h2>
    <p>Contributions to the Typer Zendesk CLI Tool are welcome! Feel free to fork the repository, make your changes, and submit a pull request.</p>

  <h2>License</h2>
    <p>The Typer Zendesk CLI Tool is released under the MIT License. See the LICENSE file for more details.</p>

  <h2>Contact</h2>
    <p>For questions, suggestions, or issues, please open an issue on the GitHub repository.</p>
</body>


