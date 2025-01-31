from pathlib import Path

from models.config import Config
from utils.target_logger import get_logger
from discord_message_sender import DiscordMessageSender


cfg = Config.parse_file(Path(__file__).parent.resolve() / 'Config.yaml')


def main():
    for profile in cfg.discord.profiles:
        lg = get_logger(name='DiscordMessageSender', session_id=profile.name)
        DiscordMessageSender(cfg=profile, logger=lg).start()


if __name__ == '__main__':
    main()
