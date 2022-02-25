""""
    █▀▄▀█ █▀█ █▀█ █ █▀ █ █ █▀▄▀█ █▀▄▀█ █▀▀ █▀█
    █ ▀ █ █▄█ █▀▄ █ ▄█ █▄█ █ ▀ █ █ ▀ █ ██▄ █▀▄
    Copyright 2022 t.me/morisummerzxc
    Licensed under the Apache License, Version 2.0
"""
from .. import loader, utils
from telethon.tl.types import *
import logging
from asyncio import sleep
import io
from telethon.utils import get_display_name

logger = logging.getLogger(__name__)
letters = {
    " ": """✨✨✨✨✨✨✨✨✨✨✨
✨✨✨✨✨✨✨✨✨✨✨
✨✨✨✨✨✨✨✨✨✨✨
✨✨✨✨✨✨✨✨✨✨✨
✨✨✨✨✨✨✨✨✨✨✨
✨✨✨✨✨✨✨✨✨✨✨
✨✨✨✨✨✨✨✨✨✨✨
✨✨✨✨✨✨✨✨✨✨✨
✨✨✨✨✨✨✨✨✨✨✨
✨✨✨✨✨✨✨✨✨✨✨
✨✨✨✨✨✨✨✨✨✨✨""",
    "a": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨✨✨✨💖💖✨✨✨✨✨
✨✨✨✨💖💖💖💖✨✨✨✨
✨✨✨💖💖💖💖💖💖✨✨✨
✨✨💖💖💖✨✨💖💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "b": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨💖💖💖💖💖💖💖✨✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖💖💖💖💖💖✨✨✨
✨✨💖💖💖💖💖💖💖✨✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖💖💖💖💖💖✨✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "c": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨✨💖💖💖💖💖💖✨✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨✨💖💖💖💖💖💖✨✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "d": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨💖💖💖💖💖💖💖✨✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨✨💖💖✨✨✨💖💖✨✨
✨✨✨💖💖✨✨✨💖💖✨✨
✨✨✨💖💖✨✨✨💖💖✨✨
✨✨✨💖💖✨✨✨💖💖✨✨
✨✨✨💖💖✨✨✨💖💖✨✨
✨✨✨💖💖✨✨✨💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖💖💖💖💖💖✨✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "e": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨💖💖💖💖💖💖💖✨✨✨
✨✨💖💖💖💖💖💖💖✨✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨💖💖💖💖💖💖✨✨✨✨
✨✨💖💖💖💖💖💖✨✨✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨💖💖💖💖💖💖💖✨✨✨
✨✨💖💖💖💖💖💖💖✨✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "f": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨✨💖💖💖💖💖💖✨✨✨
✨✨💖💖💖💖💖💖💖✨✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨💖💖💖💖💖💖✨✨✨✨
✨✨💖💖💖💖💖💖✨✨✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "g": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨✨💖💖💖💖💖💖✨✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨💖💖✨✨💖💖💖💖✨✨
✨✨💖💖✨✨💖💖💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨✨💖💖💖💖💖💖✨✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "h": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "i": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨✨✨✨💖💖✨✨✨✨✨
✨✨✨✨✨💖💖✨✨✨✨✨
✨✨✨✨✨💖💖✨✨✨✨✨
✨✨✨✨✨💖💖✨✨✨✨✨
✨✨✨✨✨💖💖✨✨✨✨✨
✨✨✨✨✨💖💖✨✨✨✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "j": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨✨💖💖💖💖💖💖💖✨✨
✨✨✨💖💖💖💖💖💖💖✨✨
✨✨✨✨✨✨✨💖💖✨✨✨
✨✨✨✨✨✨✨💖💖✨✨✨
✨✨✨✨✨✨✨💖💖✨✨✨
✨✨✨✨✨✨✨💖💖✨✨✨
✨✨💖💖✨✨✨💖💖✨✨✨
✨✨💖💖✨✨✨💖💖✨✨✨
✨✨💖💖💖💖💖💖💖✨✨✨
✨✨✨💖💖💖💖💖✨✨✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "k": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨💖💖💖✨✨
✨✨💖💖✨✨💖💖💖✨✨✨
✨✨💖💖✨💖💖💖✨✨✨✨
✨✨💖💖💖💖💖✨✨✨✨✨
✨✨💖💖💖💖💖✨✨✨✨✨
✨✨💖💖✨💖💖💖✨✨✨✨
✨✨💖💖✨✨💖💖💖✨✨✨
✨✨💖💖✨✨✨💖💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "l": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "m": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖💖✨✨💖💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖✨💖💖✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "n": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖💖✨✨✨💖💖✨✨
✨✨💖💖💖💖✨✨💖💖✨✨
✨✨💖💖💖💖💖✨💖💖✨✨
✨✨💖💖✨💖💖💖💖💖✨✨
✨✨💖💖✨✨💖💖💖💖✨✨
✨✨💖💖✨✨✨💖💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "o": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨✨💖💖💖💖💖💖✨✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨✨💖💖💖💖💖💖✨✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "p": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨💖💖💖💖💖💖💖✨✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖💖💖💖💖💖✨✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "q": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨✨💖💖💖💖💖💖✨✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨💖💖✨💖💖✨✨
✨✨💖💖✨💖💖💖💖💖✨✨
✨✨💖💖✨✨💖💖💖✨✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨✨💖💖💖💖✨💖💖✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "r": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨💖💖💖💖💖💖💖✨✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖💖💖💖💖💖✨✨✨
✨✨💖💖✨✨✨💖💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "s": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨✨💖💖💖💖💖💖✨✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨💖💖💖💖💖💖💖✨✨✨
✨✨✨💖💖💖💖💖💖💖✨✨
✨✨✨✨✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨✨💖💖💖💖💖💖✨✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "t": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨✨✨✨💖💖✨✨✨✨✨
✨✨✨✨✨💖💖✨✨✨✨✨
✨✨✨✨✨💖💖✨✨✨✨✨
✨✨✨✨✨💖💖✨✨✨✨✨
✨✨✨✨✨💖💖✨✨✨✨✨
✨✨✨✨✨💖💖✨✨✨✨✨
✨✨✨✨✨💖💖✨✨✨✨✨
✨✨✨✨✨💖💖✨✨✨✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "u": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨✨💖💖💖💖💖💖✨✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "v": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖💖✨✨💖💖💖✨✨
✨✨✨💖💖💖💖💖💖✨✨✨
✨✨✨✨💖💖💖💖✨✨✨✨
✨✨✨✨✨💖💖✨✨✨✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "w": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨💖💖✨💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖💖✨✨💖💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "x": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖💖✨✨💖💖💖✨✨
✨✨✨💖💖💖✨💖💖✨✨✨
✨✨✨✨💖💖💖💖✨✨✨✨
✨✨✨✨💖💖💖💖✨✨✨✨
✨✨✨💖💖✨💖💖💖✨✨✨
✨✨💖💖💖✨✨💖💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "y": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨✨💖💖💖💖💖💖💖✨✨
✨✨✨✨✨✨✨✨💖💖✨✨
✨✨✨✨✨✨✨✨💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖💖💖💖💖💖✨✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "z": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨✨✨✨✨✨💖💖💖✨✨
✨✨✨✨✨✨💖💖💖✨✨✨
✨✨✨✨✨💖💖💖✨✨✨✨
✨✨✨✨💖💖💖✨✨✨✨✨
✨✨✨💖💖💖✨✨✨✨✨✨
✨✨💖💖💖✨✨✨✨✨✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "а": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨✨✨✨💖💖✨✨✨✨✨
✨✨✨✨💖💖💖💖✨✨✨✨
✨✨✨💖💖💖💖💖💖✨✨✨
✨✨💖💖💖✨✨💖💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "б": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨💖💖💖💖💖💖💖✨✨✨
✨✨💖💖💖💖💖💖💖✨✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨💖💖💖💖💖💖💖✨✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖💖💖💖💖💖✨✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "в": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨💖💖💖💖💖💖💖✨✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖💖💖💖💖💖✨✨✨
✨✨💖💖💖💖💖💖💖✨✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖💖💖💖💖💖✨✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "г": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨✨✨💖💖💖💖💖💖✨✨
✨✨✨💖💖💖💖💖💖💖✨✨
✨✨✨💖💖✨✨✨✨✨✨✨
✨✨✨💖💖✨✨✨✨✨✨✨
✨✨✨💖💖✨✨✨✨✨✨✨
✨✨✨💖💖✨✨✨✨✨✨✨
✨✨✨💖💖✨✨✨✨✨✨✨
✨✨✨💖💖✨✨✨✨✨✨✨
✨✨✨💖💖✨✨✨✨✨✨✨
✨✨✨💖💖✨✨✨✨✨✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "д": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨✨✨✨💖💖💖💖✨✨✨
✨✨✨✨💖💖💖💖💖💖✨✨
✨✨✨💖💖💖✨✨💖💖✨✨
✨✨💖💖💖✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨💖💖💖💖💖💖💖💖💖💖✨
✨💖💖💖✨✨✨✨💖💖💖✨
✨💖💖✨✨✨✨✨✨💖💖✨
✨💖💖✨✨✨✨✨✨💖💖✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "е": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨💖💖💖💖💖💖💖✨✨✨
✨✨💖💖💖💖💖💖💖✨✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨💖💖💖💖💖💖✨✨✨✨
✨✨💖💖💖💖💖💖✨✨✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨💖💖💖💖💖💖💖✨✨✨
✨✨💖💖💖💖💖💖💖✨✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "ё": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨💖💖💖💖💖💖💖✨✨✨
✨✨💖💖💖💖💖💖💖✨✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨💖💖💖💖💖💖✨✨✨✨
✨✨💖💖💖💖💖💖✨✨✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨💖💖💖💖💖💖💖✨✨✨
✨✨💖💖💖💖💖💖💖✨✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "ж": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨💖💖✨💖💖✨💖💖✨✨
✨✨💖💖✨💖💖✨💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨✨💖💖💖💖💖💖✨✨✨
✨✨✨✨💖💖💖💖✨✨✨✨
✨✨✨✨💖💖💖💖✨✨✨✨
✨✨✨💖💖💖💖💖💖✨✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖✨💖💖✨💖💖✨✨
✨✨💖💖✨💖💖✨💖💖✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "з": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨✨💖💖💖💖💖💖✨✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨✨✨✨✨✨✨💖💖✨✨
✨✨✨✨✨💖💖💖💖✨✨✨
✨✨✨✨✨💖💖💖💖✨✨✨
✨✨✨✨✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨✨💖💖💖💖💖💖✨✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "и": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨💖💖💖✨✨
✨✨💖💖✨✨💖💖💖💖✨✨
✨✨💖💖✨💖💖💖💖💖✨✨
✨✨💖💖💖💖💖✨💖💖✨✨
✨✨💖💖💖💖✨✨💖💖✨✨
✨✨💖💖💖✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "й": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨💖💖✨💖💖✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨💖💖💖✨✨
✨✨💖💖✨✨💖💖💖💖✨✨
✨✨💖💖✨💖💖💖💖💖✨✨
✨✨💖💖💖💖💖✨💖💖✨✨
✨✨💖💖💖💖✨✨💖💖✨✨
✨✨💖💖💖✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "к": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨💖💖💖✨✨
✨✨💖💖✨✨💖💖💖✨✨✨
✨✨💖💖✨💖💖💖✨✨✨✨
✨✨💖💖💖💖💖✨✨✨✨✨
✨✨💖💖💖💖💖✨✨✨✨✨
✨✨💖💖✨💖💖💖✨✨✨✨
✨✨💖💖✨✨💖💖💖✨✨✨
✨✨💖💖✨✨✨💖💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "л": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨✨✨✨💖💖✨✨✨✨✨
✨✨✨✨💖💖💖💖✨✨✨✨
✨✨✨💖💖💖💖💖💖✨✨✨
✨✨💖💖💖✨✨💖💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "м": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖💖✨✨💖💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖✨💖💖✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "н": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "о": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨✨💖💖💖💖💖💖✨✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨✨💖💖💖💖💖💖✨✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "п": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "р": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨💖💖💖💖💖💖💖✨✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖💖💖💖💖💖✨✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "с": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨✨💖💖💖💖💖💖✨✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨✨💖💖💖💖💖💖✨✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "т": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨✨✨✨💖💖✨✨✨✨✨
✨✨✨✨✨💖💖✨✨✨✨✨
✨✨✨✨✨💖💖✨✨✨✨✨
✨✨✨✨✨💖💖✨✨✨✨✨
✨✨✨✨✨💖💖✨✨✨✨✨
✨✨✨✨✨💖💖✨✨✨✨✨
✨✨✨✨✨💖💖✨✨✨✨✨
✨✨✨✨✨💖💖✨✨✨✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "у": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨✨💖💖💖💖💖💖💖✨✨
✨✨✨✨✨✨✨✨💖💖✨✨
✨✨✨✨✨✨✨✨💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖💖💖💖💖💖✨✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "ф": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨✨💖💖💖💖💖💖✨✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨💖💖✨✨💖💖✨✨💖💖✨
✨💖💖✨✨💖💖✨✨💖💖✨
✨💖💖✨✨💖💖✨✨💖💖✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨✨💖💖💖💖💖💖✨✨✨
✨✨✨✨✨💖💖✨✨✨✨✨
✨✨✨✨✨💖💖✨✨✨✨✨
✨✨✨✨✨💖💖✨✨✨✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "х": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖💖✨✨💖💖💖✨✨
✨✨✨💖💖💖✨💖💖✨✨✨
✨✨✨✨💖💖💖💖✨✨✨✨
✨✨✨✨💖💖💖💖✨✨✨✨
✨✨✨💖💖✨💖💖💖✨✨✨
✨✨💖💖💖✨✨💖💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "ц": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖💖💖💖💖💖💖💖✨
✨✨✨💖💖💖💖💖💖💖💖✨
✨✨✨✨✨✨✨✨✨💖💖✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "ч": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨✨💖💖💖💖💖💖💖✨✨
✨✨✨✨✨✨✨✨💖💖✨✨
✨✨✨✨✨✨✨✨💖💖✨✨
✨✨✨✨✨✨✨✨💖💖✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "ш": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨💖💖✨💖💖✨✨
✨✨💖💖✨💖💖✨💖💖✨✨
✨✨💖💖✨💖💖✨💖💖✨✨
✨✨💖💖✨💖💖✨💖💖✨✨
✨✨💖💖✨💖💖✨💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "щ": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨💖💖✨💖💖✨✨
✨✨💖💖✨💖💖✨💖💖✨✨
✨✨💖💖✨💖💖✨💖💖✨✨
✨✨💖💖✨💖💖✨💖💖✨✨
✨✨💖💖💖💖💖💖💖💖💖✨
✨✨💖💖💖💖💖💖💖💖💖✨
✨✨✨✨✨✨✨✨✨💖💖✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "ь": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨💖💖💖💖💖💖💖✨✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖💖💖💖💖💖✨✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "ъ": """✨✨✨✨✨✨✨✨✨✨✨✨
✨💖💖💖✨✨✨✨✨✨✨✨
✨💖💖💖✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨✨✨✨✨
✨✨💖💖💖💖💖💖💖✨✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖💖💖💖💖💖✨✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "ы": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖💖💖💖✨💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖✨✨✨💖💖💖✨✨
✨✨💖💖✨✨✨💖💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖💖💖💖✨💖💖✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "э": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨✨💖💖💖💖💖💖✨✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨✨✨✨✨✨✨💖💖✨✨
✨✨✨✨💖💖💖💖💖💖✨✨
✨✨✨✨💖💖💖💖💖💖✨✨
✨✨✨✨✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨✨💖💖💖💖💖💖✨✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "ю": """✨✨✨✨✨✨✨✨✨✨✨✨
✨💖💖✨✨💖💖💖💖💖✨✨
✨💖💖✨💖💖💖💖💖💖💖✨
✨💖💖✨💖💖✨✨✨💖💖✨
✨💖💖✨💖💖✨✨✨💖💖✨
✨💖💖💖💖💖✨✨✨💖💖✨
✨💖💖💖💖💖✨✨✨💖💖✨
✨💖💖✨💖💖✨✨✨💖💖✨
✨💖💖✨💖💖✨✨✨💖💖✨
✨💖💖✨💖💖💖💖💖💖💖✨
✨💖💖✨✨💖💖💖💖💖✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "я": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨✨💖💖💖💖💖💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖✨✨✨✨💖💖✨✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨✨💖💖💖💖💖💖💖✨✨
✨✨✨✨✨✨💖💖💖💖✨✨
✨✨✨✨✨💖💖💖💖💖✨✨
✨✨✨✨💖💖💖✨💖💖✨✨
✨✨✨💖💖💖✨✨💖💖✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    ".": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨✨✨✨✨✨✨✨✨✨✨
✨✨✨✨✨✨✨✨✨✨✨✨
✨✨✨✨✨✨✨✨✨✨✨✨
✨✨✨✨✨✨✨✨✨✨✨✨
✨✨✨✨✨✨✨✨✨✨✨✨
✨✨✨✨✨✨✨✨✨✨✨✨
✨✨✨✨✨✨✨✨✨✨✨✨
✨✨✨✨✨✨✨✨✨✨✨✨
✨✨✨✨✨💖💖✨✨✨✨✨
✨✨✨✨✨💖💖✨✨✨✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "!": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨✨✨✨💖💖✨✨✨✨✨
✨✨✨✨✨💖💖✨✨✨✨✨
✨✨✨✨✨💖💖✨✨✨✨✨
✨✨✨✨✨💖💖✨✨✨✨✨
✨✨✨✨✨💖💖✨✨✨✨✨
✨✨✨✨✨💖💖✨✨✨✨✨
✨✨✨✨✨✨✨✨✨✨✨✨
✨✨✨✨✨✨✨✨✨✨✨✨
✨✨✨✨✨💖💖✨✨✨✨✨
✨✨✨✨✨💖💖✨✨✨✨✨
✨✨✨✨✨✨✨✨✨✨✨✨""",
    "💖": """✨✨✨✨✨✨✨✨✨✨✨✨
✨✨💖💖💖✨✨💖💖💖✨✨
✨💖💖🤍💖💖💖💖💖💖💖✨
✨💖🤍💖💖💖💖💖💖💖💖✨
✨💖💖💖💖💖💖💖💖💖💖✨
✨💖💖💖💖💖💖💖💖💖💖✨
✨💖💖💖💖💖💖💖💖💖💖✨
✨✨💖💖💖💖💖💖💖💖✨✨
✨✨✨💖💖💖💖💖💖✨✨✨
✨✨✨✨💖💖💖💖✨✨✨✨
✨✨✨✨✨💖💖✨✨✨✨✨
✨✨✨✨✨✨✨✨✨✨✨✨"""
}


class PicsaverMod(loader.Module):
    """"Magic Text generator"""
    strings = {"name": "MagicText"}

    async def client_ready(self, client, db) -> None:
        self.db = db
        self.client = client

    async def magictextcmd(self, message: Message):
        """Send message with animating text"""
        text = utils.get_args_raw(message)
        text = text.replace("<3", "💖")
        await message.edit(letters[' '])
        _last = ""
        for letter in text:
            if _last and _last == letter:
                await sleep(.7)
                continue
            if letter not in letters and _last not in letters:
                await sleep(.7)
                continue
            await message.edit(letters.get(letter.lower(), '<b>🚫 Not supported symbol</b>'))
            _last = letter
            await sleep(.7)
        await message.edit("✨💖<b>" + text + "</b>💖✨")
