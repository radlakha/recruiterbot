# recruiterbot


- How to setup codespaces
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

- How to run the bot
    - Change your directory to /ChatBot `cd /workspaces/recruiterbot/ChatBot`
    - To run on available embedding database run index.py and open localhost to see the UI `python index.py`
 
- How to update the resume database
    - Change your directory to /ChatBot `cd /workspaces/recruiterbot/ChatBot`
    - If there is no "files" directory, create one `mkdir files`
    - Copy your resumes to this directory
    - Run update_database `python botfiles/update_database.py`
