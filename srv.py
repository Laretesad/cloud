import paramiko
def sing(commands):
    password='12qwasZX'
    command='sudo singularity run'+commands
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(hostname='127.0.0.1', username='svyatoslav',password='12qwasZX', port=22)
    except:
        return (-1)
    stdin,stdout,stderr=client.exec_command(command, timeout=300)
    print(stdin,stdout,stderr)
    return(stdin)
