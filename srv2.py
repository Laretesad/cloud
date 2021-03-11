import paramiko
def sing2(commands):
    password='12qwas'
    command='singularity run'+commands
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(hostname='196.68.6.8', username='sub',password='12qwas', port=2222)
    except:
        return (-1)
    stdin,stdout,stderr=client.exec_command(command, timeout=300)
    return(stdin)
