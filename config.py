"""
Music Player, Telegram Voice Chat Bot
Copyright (c) 2021-present Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    def __init__(self) -> None:
        self.API_ID: str = os.environ.get("7880210")
        self.API_HASH: str = os.environ.get("1bb4b2ff1489cc06af37cba448c8cce9")
        self.SESSION: str = os.environ.get("BQASzhFZda-a0v2rd97WS1fPAy_Lz0cHmYVYo5Gi9k27va2zWat2GJhF3Yt81T_LOqsLRK5_8PPcbh1w0Iaq1u1TkFToYph2LZhXErIyRvda-ElkmkhlHphbnZO226nWQBSFS5xpTrFZ38axOrbSJqso2UmaYPv9VCvvX8mlWJRmg--m45GXZSuPcWM1Raj3IMHvJiUN0HID0t5SLUzjMbnSsWQQB98LdWQmVLR6PI6R1jMtSZzRmzQUXsmtbx8YWi7xgOi7Chd8HXbtMHUuU-cFBW3xLcbHTg0G_aiX2MfRQsAkjYPmT03X2SGv7C79VFYJPWUgij_BhaLIy9CWSv_SYbzVEgA")
        self.BOT_TOKEN: str = os.environ.get("5393472170:AAHOAilipKeK80pfgdf4oCn3ZbXSTys8h5k")
        self.SUDOERS: list = [
            int(id) for id in os.environ.get("1639765266").split() if id.isnumeric()
        ]
        if not self.SESSION or not self.API_ID or not self.API_HASH:
            print("ERROR: SESSION, API_ID and API_HASH is required!")
            quit(0)
        self.SPOTIFY: bool = False
        self.QUALITY: str = os.environ.get("QUALITY", "high").lower()
        self.PREFIXES: list = os.environ.get("PREFIX", "!").split()
        self.LANGUAGE: str = os.environ.get("LANGUAGE", "en").lower()
        self.STREAM_MODE: str = (
            "audio"
            if (os.environ.get("STREAM_MODE", "audio").lower() == "audio")
            else "video"
        )
        self.ADMINS_ONLY: bool = os.environ.get("ADMINS_ONLY", False)
        self.SPOTIFY_CLIENT_ID: str = os.environ.get("SPOTIFY_CLIENT_ID", None)
        self.SPOTIFY_CLIENT_SECRET: str = os.environ.get("SPOTIFY_CLIENT_SECRET", None)


config = Config()
