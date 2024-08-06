import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "22160237"))
API_HASH = getenv("API_HASH", "095b9df69b08c2dcffbdd2f8542e3280")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7303444879:AAFcjLyxPxx2CYSPF_T75FJBI2FyQdSu45c")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://kurt67143:nays@cluster0.vjg7bma.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 360))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "5400")
)
# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002222241971"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 6604501109))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/mamakli06/mamaklimusic1",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/kumsaldestekkanal")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/gecemavisisohbett")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 314572800))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 3221225472))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "AgFSI20ASxD6Sm1GllHf6t5kX4LNedWp1cazmqmUX3TNe66H3lOeSin4UL6XXM-NWBy-mXEYlyELIWI-IR0UDa3UgWae0joml4WOpQLV5NfhCki4iJYkVMnqTJlm6kU2sSSiM7F3wkvBdBVn-5fDoSbEiGUfBAzOzxgJVMgXu-AJiW5dd7WcJHqTOzpzOaAhluS3jb90tgHCnuKa4iJEoLSAiWZRQpQhro5AeboMJ0Hv7HCSyVyyIB1vnaMX_nBrPAV7Px-wq70ylfTBM3fynSA3blOkOlrEGwWYHO4iQrIZdslnqW0zAKAL0pY_lwPA30eFb0heHaP6cSbT7jg9HN1P7k5yMAAAAAG4T-CvAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/e5a809fe337adff6f4d4a.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/e5a809fe337adff6f4d4a.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/e5a809fe337adff6f4d4a.jpg"
STATS_IMG_URL = "https://graph.org/file/e5a809fe337adff6f4d4a.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/e5a809fe337adff6f4d4a.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/e5a809fe337adff6f4d4a.jpg"
STREAM_IMG_URL = "https://graph.org/file/e5a809fe337adff6f4d4a.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/e5a809fe337adff6f4d4a.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/e5a809fe337adff6f4d4a.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/e5a809fe337adff6f4d4a.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/e5a809fe337adff6f4d4a.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/e5a809fe337adff6f4d4a.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))



if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
)
