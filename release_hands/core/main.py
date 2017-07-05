#from lib import get_host_info
from lib import pre
#from lib import get_host_info
from lib import ssh_connect
from concurrent.futures import ThreadPoolExecutor
from lib import pre
#获取主机集群信息
def run():
    #get_host_info.get_result()
    obj = pre.pre_work()
    print('正常实例化')
    print(type(obj))
    obj.optimize()


# passwd_list = settings.passwd
# for passwd  in passwd_list:
#     try:
#         obj = SSH('192.168.206.130',22,'root',passwd)
#         obj.connect()
#     except Exception as e:
#         print(Exception)
#
# a = obj.cmd('ls')
# print(a.decode())
# obj.close()

#比较单行机器是否有变化，hashlib验证md5



