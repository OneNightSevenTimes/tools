#根据今天发布的环境生成对应的目录和主机名
import os
import sys
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)


import configparser
from conf import settings
import subprocess
import datetime
from lib import ssh_connect
from concurrent.futures import ThreadPoolExecutor
from lib import log
import traceback
from lib import single_to_local

config = configparser.ConfigParser(allow_no_value=True)
config.read('hosts.txt')

class pre_work(object):
    def __init__(self):
        self.single_ip = []
        self.config = configparser.ConfigParser(allow_no_value=True)
        self.config.read('hosts.txt')


    def optimize(self):
        pool = ThreadPoolExecutor(10)
        print(settings.del_env)
        for section in self.config.sections():
            if 'searcher' in section and settings.del_env[0] not in section and settings.del_env[1] not in section and settings.del_env[2] not in section and settings.del_env[3] not in section and settings.del_env[4] not in section:
                print(section)
                dir_name = section
                host_list = config.items(section)
                pool.submit(self.mkdir,dir_name,host_list)

    def mkdir(self,dir_name,host_list):
        cur = datetime.datetime.now()
        date = str(cur.month) + '-'+str(cur.day)
        path = '%s/%s/%s' % (settings.PATH,date,dir_name)
        subprocess.Popen('mkdir -p %s' %path, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        self.attend_host(host_list,path)

# production-mjq_qq-searcher_p4 [('172.28.139.85', ''), ('172.28.139.104', ''), ('172.28.139.109', ''), ('172.28.139.135', ''), ('172.28.148.137', ''), ('172.28.148.143', '')]
    def attend_host(self,host_list,path):
        host_path = path+'/hosts'
        path_dir = path
        subprocess.Popen('touch %s' % host_path, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        with open(host_path,'a') as f:
            for i in host_list:
                f.writelines((i[0],'\n'))
        self.get_single(path_dir,host_path)
#单行机器列表，去机器上拉取包


    def get_single(self,path,host_path):
        '''
        path:各环境位置
        :return:
        '''
        with open(host_path,encoding='utf-8')as f2:
            for index,single_ip in enumerate(f2):
                if index == 1:
                    ip = single_ip
                    print('single_ip-------------------',ip)
                    break
        passwd_list = settings.passwd
        msg = {'host': single_ip, 'status': 'ssh connected'}
        for passwd in passwd_list:
            log_obj = log.Logger()  # 实例化，创建文件对象，日志对象
            try:
                ssh_obj = ssh_connect.SSH(single_ip, 22, 'root', passwd)
                ssh_obj.connect()
                log_obj.log(msg)#记录是否ssh成功
                print('connected %s'%single_ip)
                break
            except Exception as e:
                err = traceback.format_exc()
                log_obj.log(err, False)
        package_obj  = single_to_local.Distribute(path,single_ip,settings.LINK,log_obj,ssh_obj)
        #package_obj.check()
  
        package_obj.get_package_name()
        print('开始打包啦')
        package_obj.get_package()
        ssh_obj.close()



if __name__ == '__main__':
    obj = pre_work()
    obj.optimize()
