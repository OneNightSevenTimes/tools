import paramiko
class SSH(object):
    def __init__(self,host,port,user,pwd):
        self.host = host
        self.port = port
        self.user = user
        self.pwd = pwd
        self.transport = None

    def connect(self):
        self.transport = paramiko.Transport(self.host,self.port)
        self.transport.connect(username=self.user,password=self.pwd)

    def cmd(self,command):
        ssh = paramiko.SSHClient()
        ssh._transport = self.transport
        stdin,stdout,stderr = ssh.exec_command(command)
        return stdout.read()

    def download(self,server_path,local_path):
        sftp = paramiko.SFTPClient.from_transport(self.transport)
        sftp.get(server_path,local_path)

    def upload(self,server_path,local_path):
        sftp = paramiko.SFTPClient.from_transport(self.transport)
        sftp.put(local_path, server_path)

    def close(self):
        self.transport.close()

obj = SSH('172.28.35.37',22,'root','3xEnDfZ*^ilSP0qk')
obj.connect()
command = 'rsync -ar /export/Packages/searcher/20170629175327_1498707566068 root@172.22.193.65:/tmp'
obj.cmd(command)
