"""Save the provider data in the actual DB"""

import os
import sys

import environ

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from web.config.settings.base import ENV_DIR

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(env_file=os.path.join(ENV_DIR, ".env.local"))

DEBUG = True
import MySQLdb

conn = MySQLdb.connect(
    user=env("DB_USER"),
    passwd=env("DB_PASSWORD"),
    host=env("DB_HOST"),
    port=int(env("DB_PORT")),
    db=env("DB_NAME"),
)
cursor = conn.cursor()

watch_providers = {"8": "NF", "337": "WV", "356": "WC", "97": "DP", "119": "AP"}
logo_key = {
    "8": "https://image.tmdb.org/t/p/original/9A1JSVmSxsyaBK4SUFsYVqbAYfW.jpg",
    "337": "https://image.tmdb.org/t/p/original/8N0DNa4BO3lH24KWv1EjJh4TxoD.jpg",
    "356": "https://image.tmdb.org/t/p/original/cNi4Nv5EPsnvf5WmgwhfWDsdMUd.jpg",
    "97": "https://image.tmdb.org/t/p/original/dgPueyEdOwpQ10fjuhL2WYFQwQs.jpg",
    "119": "https://image.tmdb.org/t/p/original/68MNrwlkpF7WnmNPXLah69CR5cb.jpg",
}

for key in watch_providers:
    sql = "INSERT INTO provider (tmdb_id, name, logo_key ) VALUES (%s, %s, %s)"
    values = (key, watch_providers[key], logo_key[key])
    cursor.execute(sql, values)
    conn.commit()

conn.close()
