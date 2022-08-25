"""
                                      '||
... ...  .... ... ... ... ...  ....    ||
 ||'  ||  '|.  |   ||  ||  |  '' .||   ||
 ||    |   '|.|     ||| |||   .|' ||   ||
 ||...'     '|       |   |    '|..'|' .||.
 ||      .. |
''''      ''
Created by Dylan Araps.
"""

import os
import platform


__version__ = "3.3.1"
__cache_version__ = "1.1.0"


HOME = os.getenv("HOME", os.getenv("USERPROFILE"))
XDG_CACHE_DIR = os.getenv("XDG_CACHE_HOME", os.path.join(HOME, ".cache")) #second arg is default value, in this case ~/.cache/
XDG_CONF_DIR = os.getenv("XDG_CONFIG_HOME", os.path.join(HOME, ".config"))

CACHE_DIR = os.getenv("PYWAL_CACHE_DIR", os.path.join(XDG_CACHE_DIR, "wal")) # ~/.cache/wal
CONF_DIR = os.path.join(XDG_CONF_DIR, "wal") # ~/.config/wal
MODULE_DIR = os.path.dirname(__file__)

OS = platform.uname()[0] # Linux
