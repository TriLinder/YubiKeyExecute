# YubiKeyExecute

A python script to execute a command when a YubiKey / YubiKeys are disconnected.

‏‏‎ ‎

**How to use:**

    1. [Download](https://github.com/TriLinder/YubiKeyExecute/releases/download/v1.1/YubiKeyExecute.zip) the latest release and decompress the `.zip` file

    2. Run `pip install -r requirements.txt` inside the folder

    3. Run `generateConfig.py` to create your config file

    4. Run `main.py`

    5. Done!

‏‏‎ ‎

**Options:**

    `Require All` - Require all YubiKeys (if multiple) to be inserted at the same time

    `Command` - The command to execute when the conditions are met

    `Invert` - Invert conditions, insert YubiKey(s) to execute command

    `Require Once` - Require the YubiKey(s) at least once on start, before the command execution starts

    `Wait for Insert` - Should we wait for the condtions to be met again, before we execute the command

‎

**TIP:**

On Windows you can set the command to:

`Rundll32.exe user32.dll,LockWorkStation`

To lock your computer when the YubiKey / YubiKeys are disconnected.
