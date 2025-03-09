from SelxMusic.core.bot import Selx
from SelxMusic.core.dir import dirr
from SelxMusic.core.git import git
from SelxMusic.core.userbot import Userbot
from SelxMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Selx()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
