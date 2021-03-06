import os
from telegram.ext import ConversationHandler
from ravager.config import STATE_SECRET_KEY

SECRET_SALT = STATE_SECRET_KEY.encode("utf-8")
PROJECT_PATH = os.environ.get("PROJECT_PATH")

# Conversation States
DRIVE_HANDLER, SHARED_DRIVE_SELECTION = range(2)
DOWNLOAD_HANDLER, DDL_HANDLER, TORRENT_HANDLER, MAGNET_HANDLER = range(4)
FILES_HANDLER, DOWNLOAD_FILE = range(2)
GET_ALLOWLIST_PASSWD, SEND_AUTH_URL = range(2)
FILTER_USER = range(1)

HANDLE_ADMIN_PANEL, LIMITS_PANEL, FILTERS_PANEL, ADMIN_OPTIONS_PANEL, HANDLE_FILTERS_PANEL, SYS_INFO_PANEL, LOGS_HANDLER = range(7)

END = ConversationHandler.END
