import os
from _Modules.parser_config import PARSER_CONFIG, PARSER_CONNECT_DB
from tr_package.tr_db_connect import CONNECT_DB
from tr_package.tr_email import SENDMAIL
import logging
import pyodbc


class FLOW_SSO_CLEAN_GUEST:

    def __init__(self):

        # self.path_home = os.path.realpath('.')
        self.path_home = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
        
        self.path_config_param = self.path_home + r'/config/config_param.ini'
        self.param = PARSER_CONFIG(self.path_config_param)

        self.path_query = self.path_home + r'/query/q_sso_clean_guest.sql'
        self.path_msg = self.path_home + r'/config/email_msg.txt'  # messaggio corpo email

        string_conn = PARSER_CONNECT_DB()

        self.db = CONNECT_DB()
        self.cur, self.conn, self.status_db = self.db.run_connect('SQL_MS', string_conn.db_string_tln)

    def query_report(self):

        query = open(self.path_query).read()

        return query

    def run_store_procedure(self, cur):
        """ """

        print("\n>> run_store_procedure"), logging.info(">> run_store_procedure")

        print("Attendi fine processo..")

        # EXEC dbo.sp_CleanGuest @pNUM_DAYSTOKEEP = 30 , @pCHECK_ONLY = 0
        # output = cur.callproc('TN_CUSTOMER.dbo.sp_CleanGuest', args)

        # output = cur.execute('{CALL [TN_CUSTOMER.dbo.sp_CleanGuest](@pNUM_DAYSTOKEEP =?, @pCHECK_ONLY=?)}', (30, 1))

        sql = """\
        EXEC TN_CUSTOMER.dbo.sp_CleanGuest @pNUM_DAYSTOKEEP=?, @pCHECK_ONLY=?
        """
        params = (20, False)
        output = cur.execute(sql, params)

        msg = output
        print(msg), logging.info(msg)

        return output

    def send_mail_no_dati(self):

        send = SENDMAIL(self.param.email_server, self.param.email_port)

        email_msg = open(self.path_msg, 'r').read()

        send.email(self.param.email_da, self.param.email_a, self.param.email_cc, self.param.email_oggetto,
                   email_msg)

    def flow_sso_clean_guest(self):

        # CONNECT DB TLN

        # ESEGUI QUERY N° RECORD

        # ESEGUI STORE PROCEDURE

        # ESEGUI QUERY N° RECORD

        # INVIA MAIL REPORT

        if self.status_db:

            logging.info("db_connect: " + str(self.status_db))

            query = self.query_report()
            records, status_query = self.db.run_query(self.cur, query)

            if status_query:

                conteggio = list()

                for row in records:
                    conteggio.append(row)
                print(conteggio[0])

                # ESEGUI STORE PROCEDURE
                # EXEC TN_CUSTOMER.dbo.sp_CleanGuest @pNUM_DAYSTOKEEP = 30 , @pCHECK_ONLY = 0
                self.run_store_procedure(self.cur)

            else:

                msg = 'error esecutive query'
                print(msg), logging.warning(msg)

        else:

            logging.warning("db_connect: " + str(self.status_db))

        self.db.conn_stop(self.cur, self.conn)