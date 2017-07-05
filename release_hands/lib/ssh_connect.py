from conf import settings
import paramiko
import traceback
from lib import log
import logging


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

    def upload(self,local_path,server_path):
        sftp = paramiko.SFTPClient.from_transport(self.transport)
        sftp.put(local_path, server_path)

    def close(self):
        self.transport.close()

