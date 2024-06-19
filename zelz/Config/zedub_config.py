# config values will be loaded from here

import os

ENV = bool(os.environ.get("ENV", False))

if ENV:
    from sample_config import Config
elif os.path.exists("config.py"):
    from config import Development as Config
else:
    from sample_config import Config
