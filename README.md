# Server Manager
A VERY Simple Python Script to mass execute commands in multiple servers using ssh.
This script can be used for mass restarting or mass package installing in multiple servers!


# How it works:
It's really simple, the script reads the server credentials from the config file and opens ssh connections target to all the servers, laters asks you to input a command and press Enter. The command you entered is executed to all servers.



# Installation Steps:
1. Install latest version of Python
2. Open cmd and type ```pip install parakimo``` and then ```pip install setproctitle```
3. Configure servers.ini with your server credentials
4. Open cmd (same dir) and type ```py server_manager.py```




⚠️Warning: This script is created for educational purposes and only, Im am not responsible for any wrong/illegal use of the code!


## Credits
- [@DimisSSH](https://github.com/DimisSSH)
