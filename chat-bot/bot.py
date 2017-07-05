from mee6 import Mee6
import os
import logging

from plugins.commands import Commands
from plugins.help import Help
from plugins.levels import Levels
from plugins.welcome import Welcome
from plugins.moderator import Moderator
from plugins.messages import Messages
#from plugins.early_backers import EarlyBackers
from plugins.music import Music
#from plugins.reddit import Reddit
from plugins.search import Search

# Global plugins
from plugins.basiclogs import BasicLogs
#from plugins.changelog import ChangeLog
from plugins.asciiwelcome import AsciiWelcome
from plugins.mee6game import Mee6Game

token = '***'
redis_url = 'redis://localhost'
mongo_url = os.getenv('MONGO_URL')
mee6_debug = 'sa'
sentry_dsn = os.getenv('SENTRY_DSN')
shard = os.getenv('SHARD') or 0
shard_count = os.getenv('SHARD_COUNT') or 1
dd_agent_url = os.getenv('DD_AGENT_URL')
if mee6_debug:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

bot = Mee6(shard_id=int(shard), shard_count=int(shard_count), redis_url=redis_url,
           mongo_url=mongo_url, dd_agent_url=dd_agent_url,
           sentry_dsn=sentry_dsn)
bot.run(token)
