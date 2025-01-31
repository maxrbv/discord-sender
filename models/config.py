from typing import List, Optional

from pydantic import BaseModel
from pydantic_yaml import YamlModel


class DiscordData(BaseModel):
    name: str
    token: str
    channel_id: str
    messages: str
    timeout: int
    proxy: Optional[str]


class Discord(BaseModel):
    profiles: List[DiscordData]


class Config(YamlModel):
    discord: Discord
