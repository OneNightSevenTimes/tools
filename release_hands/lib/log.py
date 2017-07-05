# import os
# import logging
# from conf import settings
#
# class LoggerHelper(object):
#     _i = None
#     @classmethod
#     def instance(cls):
#         if cls._i:
#             return cls._i
#         else:
#             cls._i = LoggerHelper()
#             return cls._i
#     def __init__(self):
#         #错误日志文件对象
#         error_log = logging.FileHandler('error.log', 'a', encoding='utf-8')
#         fmt = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s")
#         error_log.setFormatter(fmt)
#
#         # 错误日志日志对象
#         error_logger = logging.Logger('s1', level=logging.ERROR)
#         error_logger.addHandler(error_log)
#         self.error_logger = error_logger
#
#         #执行日志文件对象
#         run_log = logging.FileHandler('run.log', 'a', encoding='utf-8')
#         fmt = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s")
#         run_log.setFormatter(fmt)
#
#         # 执行日志日志对象
#         run_logger = logging.Logger('s1', level=logging.ERROR)
#         run_logger.addHandler(error_log)
#         self.run_logger = run_logger




import os
import logging
from conf import settings


class Logger(object):
    __instance = None

    def __init__(self):
        self.run_log_file = settings.RUN_LOG_FILE
        self.error_log_file = settings.ERROR_LOG_FILE
        self.run_logger = None
        self.error_logger = None

        self.initialize_run_log()
        self.initialize_error_log()

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls, *args, **kwargs)
        return cls.__instance

    @staticmethod
    def check_path_exist(log_abs_file):
        log_path = os.path.split(log_abs_file)[0]
        if not os.path.exists(log_path):
            os.mkdir(log_path)

    def initialize_run_log(self):
        self.check_path_exist(self.run_log_file)
        file_1_1 = logging.FileHandler(self.run_log_file, 'a', encoding='utf-8')
        fmt = logging.Formatter(fmt="%(asctime)s - %(levelname)s :  %(message)s")
        file_1_1.setFormatter(fmt)
        logger1 = logging.Logger('run_log', level=logging.INFO)
        logger1.addHandler(file_1_1)
        self.run_logger = logger1

    def initialize_error_log(self):
        self.check_path_exist(self.error_log_file)
        file_1_1 = logging.FileHandler(self.error_log_file, 'a', encoding='utf-8')
        fmt = logging.Formatter(fmt="%(asctime)s  - %(levelname)s :  %(message)s")
        file_1_1.setFormatter(fmt)
        logger1 = logging.Logger('run_log', level=logging.ERROR)
        logger1.addHandler(file_1_1)
        self.error_logger = logger1

    def log(self, message, mode=True):
        """
        写入日志
        :param message: 日志信息
        :param mode: True表示运行信息，False表示错误信息
        :return:
        """
        if mode:
            self.run_logger.info(message)
        else:
            self.error_logger.error(message)
