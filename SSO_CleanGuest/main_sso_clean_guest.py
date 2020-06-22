import sys
import os

root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
# root = os.path.abspath(os.path.join(root, os.path.pardir))
sys.path.append(root)

from SSO_CleanGuest.modules.flow_sso_clean_guest import FLOW_SSO_CLEAN_GUEST
from tr_package.tr_log_template import LOG_FILE


if __name__ == '__main__':

    path_log = root + '/_Logs/'
    crea_log = LOG_FILE()
    crea_log.logging(path_log, 'sso_clean_guest')  # LOG FILE NAME

    run = FLOW_SSO_CLEAN_GUEST()
    run.flow_sso_clean_guest()

