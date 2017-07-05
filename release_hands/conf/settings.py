import os
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

channel = [
    ('app','lf'),
    ('app','mjq'),
    ('pc','lf'),
    ('pc','mjq'),
]

env = 'production'
terminal = ['pc','app']

passwd = [
    '3xEnDfZ*^ilSP0qk',
    'nFslTb67oRHsioidIZXwqGk!NO8W6FtW#*Tz*dwrhFNRVDXtqBRt&KZWh*8lC8Zz',
]

ERROR_LOG_FILE = os.path.join(BASEDIR,'log','error.log')
RUN_LOG_FILE = os.path.join(BASEDIR, "log", 'run.log')


LINK = '/export/Packages/searcher/latest'
