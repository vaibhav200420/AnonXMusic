import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "28178139"))
API_HASH = getenv("API_HASH", "85172511f45230b7f8bb304f5ed8e6d8")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "8056822116:AAG94Et7TN9A86Z3KeTsqAjPAk_8L8UZcJ4")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://vg766337:xksmuYTJEN6nT9j2@yukkimusic-moded-repo.ianrw.mongodb.net/?retryWrites=true&w=majority&appName=YukkiMusic-Moded-Repo")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 6000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002180138448"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 1750583099))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/vaibhav200420/AnonXMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Ps_Corporation_Com")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+sW_L1vwSZ1Y4NDQ9")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True ))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BQF4liQAVQMaF1fI_wM7qR8bKCpjJh7Q1QjSZ5VOdCqov8pej2goqRzol9mT4pApWfagYOn8mhCzzdMgX1HOr_LM1B9NTWdajIQrkQG3V5LUsX9RNd-XFkaJlCh9wliXa8-zKRVgKlg2pS0AAFVsfE21c3fS9qMG42Xcov8JC7Ma-vmqGnO67lgJALnFlW5y_EYIFd0WT2ZdoaT9lVslWb6JvIBLQ24yTVeuYU3Ac5-RF6v65mCL2hEp7rOCkLie-pgydytj28VUT-QuT346Lmbg7hg1ums5YukrWTdFOX6hJ_7ZkfH7QY6XKuyQ5-EM7uu17wGvv6tuC7W9713SSRk-rVt-DgAAAAGeHxvxAA")
STRING2 = getenv("STRING_SESSION2", "BQGCtzAASc2P-f76Dr6jkU1m3gA623aerSNXgwZ71LVWI0b2OZA9ztpRaKTFG9OubkQfFUZteqEGEmkYfgBiJBM2gO2oytP_EHRmDwDVELE87uHjmQxhCNuc5kYxMsJTS3zZFcecTC9UMcNtQXQHoaDQkUNrg1t5A8vcVYyKOSHgIWwsSW_I98iToRmWV-yDjfdCGZanvdI1MXg451tYE9PRpHXfnwdAVh1XplOfC6J64YxXPNqP4T0Sn0opkFTsa2r48b13wTsET7erqi53eWmfdx7bmSk6MQoCht6DH-eiBZNtD3oiBSO6XOFpqrAehQB6_C4zv21yqoeDb6YPyFog7JWAAAAAGR1wUkAA")
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/9e2e83ad4bcd814a538c5.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://te.legra.ph/file/b8a0c1a00db3e57522b53.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
