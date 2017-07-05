import os
import sys
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)

from conf import settings
import subprocess
import datetime
from core import main

# cur = datetime.datetime.now()
# date = str(cur.month)+str(cur.day)
# for i in settings.channel:
#     str = '/home/admin/hongpeng/export/sd_ops/%s/%s_%s_p{0..4}'%(date,i[0],i[1])
#     subprocess.Popen('mkdir -p %s'%str,stdin=subprocess.PIPE,stdout=subprocess.PIPE,shell=True)

if __name__ == '__main__':
    main.run()
