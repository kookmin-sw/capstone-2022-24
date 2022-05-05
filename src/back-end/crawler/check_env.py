"""Checking envrionment and Reading Env file for DB"""

import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import environ
from web.config.settings.base import ENV_DIR


def setting_env():
    """Checking envrionment and Reading Env file"""
    if "prod" in sys.argv:
        environ.Env.read_env(env_file=os.path.join(ENV_DIR, ".env.prod"))
        sys.argv.remove("prod")
    elif "dev" in sys.argv:
        environ.Env.read_env(env_file=os.path.join(ENV_DIR, ".env.dev"))
        sys.argv.remove("dev")
    else:
        environ.Env.read_env(env_file=os.path.join(ENV_DIR, ".env.local"))
