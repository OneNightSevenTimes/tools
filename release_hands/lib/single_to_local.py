import os
import time
import subprocess
class Distribute(object):
    def __init__(self,path,single_ip,package_link,log_obj,ssh_obj):
        self.cluster_path = path
        self.single_ip = single_ip
        self.package_link = package_link
        self.msg = {'status':True,'message':'package exist'}
        self.log_obj = log_obj
        self.ssh_obj = ssh_obj
        self.package_name = None
    def check(self):
        print(self.package_link)
        link = os.path.islink(self.package_link)
        print(link)
        if link:
            print('link 存在啊')
        else:
            print('bucunzai')
            self.msg['message'] = 'package not exist on %s'%self.single_ip
            self.log_obj.log(self.msg['message'],False)

    def get_package_name(self):
        command = 'ls -l %s'%self.package_link
        result= self.ssh_obj.cmd(command)#result是byte类型
        result = result.decode()
        self.package_name = result.split('->')[1]#包的位置

    def get_package(self):
        print('cmd')
        package_time = time.strftime('%Y-%m-%d')
        command_cvf = 'tar cvf /tmp/package_%s %s'%(package_time,self.package_name)
        single_name = self.package_name.split('/')[-1]
        print(command_cvf) 
        self.ssh_obj.cmd(command_cvf)
        print(self.cluster_path)
        try:
            self.ssh_obj.download('/tmp/package_%s'%package_time,self.cluster_path+'/'+single_name)
        except Exception as e:
            print(e)
