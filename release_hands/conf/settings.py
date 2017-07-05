import os
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# channel = [
#     ('app','lf'),
#     ('app','mjq'),
#     ('pc','lf'),
#     ('pc','mjq'),
# ]

env = ['production']#本次需要发布的环境
all_env = ['production','ab']#所有环境

del_env = [item for item in all_env if item not in env]




all_terminal = ['pc','app','weixin','qq','jos','coupon']#所有渠道
terminal = ['weixin','qq']#本次发布渠道
del_terminal = [item for item in all_terminal if item not in terminal]
del_env.extend(del_terminal)


passwd = [
    '3xEnDfZ*^ilSP0qk',
    'nFslTb67oRHsioidIZXwqGk!NO8W6FtW#*Tz*dwrhFNRVDXtqBRt&KZWh*8lC8Zz',
]

ERROR_LOG_FILE = os.path.join(BASEDIR,'log','error.log')
RUN_LOG_FILE = os.path.join(BASEDIR, "log", 'run.log')


LINK = '/export/Packages/searcher/latest'
