import configparser
import os
import sys


class PARSER_CONFIG:

    def __init__(self, path_file_param):

        sys.path.insert(0, os.path.realpath(path_file_param))

        self.config = configparser.ConfigParser()
        self.config.read(path_file_param)

        # EMAIL
        self.email_server         = self.config['EMAIL']['server']
        self.email_port           = self.config['EMAIL']['port']
        self.email_da             = self.config['EMAIL']['da']
        self.email_da             = self.config['EMAIL']['da']
        self.email_a              = self.config['EMAIL']['a']
        self.email_cc             = self.config['EMAIL']['cc']
        self.email_oggetto        = self.config['EMAIL']['oggetto']
        self.email_dir_allegato   = self.config['EMAIL']['dir_allegato']
        self.email_fname_allegato = self.config['EMAIL']['fname_allegato']


class PARSER_CONNECT_DB:

    def __init__(self):

        self.path_home = os.path.dirname(os.path.abspath(__file__))

        self.config = configparser.ConfigParser()
        self.config.read(self.path_home + r'/string_connection.ini')

        self.db_string_tln = self.config['CONNECTIONS']['db_string_tln']
        self.db_string_sg_fn = self.config['CONNECTIONS']['db_string_sg_fn']

        self.db_string_OutsourcingSmartcard_Service = self.config['CONNECTIONS']['db_string_OutsourcingSmartcard_Service']


if __name__ == '__main__':

    test = PARSER_CONNECT_DB()
    print(test.db_string_sg_fn)











