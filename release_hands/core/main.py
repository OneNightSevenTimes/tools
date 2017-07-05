from lib import get_opcenter_hosts
from lib import pre
from lib import ssh_connect
from concurrent.futures import ThreadPoolExecutor
#获取主机集群信息
get_opcenter_hosts.get_result()


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



