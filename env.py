import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "").strip()
API_HASH = os.getenv("API_HASH", "").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
DATABASE_URL = os.getenv("DATABASE_URL", "").strip()
MUST_JOIN = os.getenv("MUST_JOIN", "")

if not API_ID:
    raise SystemExit("ɴᴏ ᴀᴘɪ_ɪᴅ ꜰᴏᴜɴᴅ. ᴇxɪᴛɪɴɢ...")
elif not API_HASH:
    raise SystemExit("ɴᴏ ᴀᴘɪ_ʜᴀꜱʜ ꜰᴏᴜɴᴅ. ᴇxɪᴛɪɴɢ...")
elif not BOT_TOKEN:
    raise SystemExit("ɴᴏ ʙᴏᴛ_ᴛᴏᴋᴇɴ ꜰᴏᴜɴᴅ. ᴇxɪᴛɪɴɢ...")

try:
    API_ID = int(API_ID)
except ValueError:
    raise SystemExit("ᴀᴘɪ_ɪᴅ ɪꜱ ɴᴏᴛ ᴀ ᴠᴀʟɪᴅ ɪɴᴛᴇɢᴇʀ. ᴇxɪᴛɪɴɢ...")

if 'postgres' in DATABASE_URL and 'postgresql' not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
