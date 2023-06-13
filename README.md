# recruiterbot


- **How to setup codespaces** 
    - In the repo on GitHub while on the code tab select Code button and switch to the Codespaces option. Click `Create codespace on main1
    - Launch the desktop VS Code from browser-based vs code that codespaces opened for you
    - Create a Python Virtual Environment `python3 -m venv ~/.venv`
    - Source the virtual env created every time a new terminal session is started by adding source command to .bashrc for quick start
    - Edit my .bashrc `vim ~/.bashrc`
    - and add `source ~/.venv/bin/activate`
    - While you are here might as well add your API Key in the .bashrc file. so you do not have to enter the key anywhere in the code
    - add `export OPENAI_API_KEY="paste your key here"`
    - Save .bashrcusing  `ESC :wq`
    - Start a new terminal session so that the recently edited .bashrc is in effect. Notice (.venv) in the prompt. Also, check for your OpenAI API key using the command `echo $OPENAI_API_KEY`
    - Issue command `make install`

- **How to run?**
    - Add your OpenAI key in "bot_files/config.py"
    - Add resumes to the folder "files" or through the UI. (Note: Currently the embeddings are created and loaded on the existing database. 
    - If you want to recreate the embeddings, Run update_database.py
    - Run index.py and open localhost to see the UI.
 
- **Setting Up SQL Database and Server on Azure.**
    - Please run the ARM template azureSQLDeploy. Detailed instrutcions have been provided in the Wiki of this repository [here](https://github.com/radlakha/recruiterbot/wiki/Set-Up-Instructions-For-Azure-SQL-Database-and-Server-and-Azure-Function).
