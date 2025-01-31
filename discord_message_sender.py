import random
import time
from logging import Logger
from threading import Thread
from pathlib import Path

import requests

from models.config import DiscordData


class DiscordMessageSender(Thread):

    def __init__(self, cfg: DiscordData, logger: Logger):
        Thread.__init__(self)
        self._cfg = cfg
        self._logger = logger
        self._init_data()
        self._discord_api_url = 'https://discord.com/api/v9'
        self._messages_count = 0
        self._proxies = {
            'http': self._cfg.proxy,
            'https': self._cfg.proxy
        }

    def run(self):
        while True:
            self._send_message()
            time.sleep(self._timeout)

    def _init_messages_files(self, filename: str):
        file_path = Path(__file__).parent.resolve() / 'assets' / filename
        with open(file_path, 'r') as file:
            lines = file.readlines()
        lines = [line.strip() for line in lines]
        self._logger.info(f'[DiscordMessageSender:_init_messages_files] - Successfully initialized list of messages. Total: {len(lines)}')
        return lines

    def _init_data(self):
        self._username = self._cfg.name
        self._channel_id = self._cfg.channel_id
        self._messages = self._init_messages_files(filename=self._cfg.messages)
        self._timeout = self._cfg.timeout
        self._headers = {
            'authorization': self._cfg.token
        }
        self._logger.info(f'[DiscordMessageSender:_init_data] - Successfully initialized DiscordMessageSender')

    def _send_message(self):
        url = f'{self._discord_api_url}/channels/{self._channel_id}/messages'
        payload = {
            'content': random.choice(self._messages)
        }
        try:
            response = requests.post(url=url, data=payload, headers=self._headers, proxies=self._proxies)
            if response.status_code == 200:
                self._messages_count += 1
                self._logger.info(f'[DiscordMessageSender:_send_message] - Successfully sent message. Total: {self._messages_count}')
                # self._delete_message(message_id=response.json().get('id'))
            else:
                self._logger.error(f'[DiscordMessageSender:_send_message] - Error sending message: {response.text}')
        except Exception as e:
            self._logger.error(f'[DiscordMessageSender:_send_message] - Error sending message. Exception: {e}')


    def _delete_message(self, message_id: str):
        url = f'{self._discord_api_url}/channels/{self._channel_id}/messages/{message_id}'
        requests.delete(url=url, headers=self._headers)

