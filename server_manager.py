import paramiko
import configparser
import setproctitle

setproctitle.setproctitle('Multi-Server Manager')
config = configparser.ConfigParser()
config.read('servers.ini')
ssh_servers = config.sections()
for ssh_server in ssh_servers:
    host = config[ssh_server]['Host']
    port = int(config[ssh_server]['Port'])
    username = config[ssh_server]['Username']
    password = config[ssh_server]['Password']
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, port=port, username=username, password=password)
    command = input('Command to mass-execute: ')
    stdin, stdout, stderr = ssh.exec_command({command})
    output = stdout.read().decode('utf-8')
    print(f'Server Outputs: \n{ssh_server}:\n{output}')
    ssh.close()
    