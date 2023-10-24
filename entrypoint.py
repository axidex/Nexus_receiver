import argparse
import logging
import os

from nexuscli.nexus_client import NexusClient
from nexuscli.nexus_client import NexusConfig

from src.misc.timetz import timetz
from src.misc.yml_to_dict import yml_to_dict

logging.Formatter.converter = timetz

path_to_logs = "logs/CodeQL_client.log"
dir_path = os.path.dirname(path_to_logs)
os.makedirs(dir_path, exist_ok=True)

logging.basicConfig(filename=path_to_logs,
                    format="[%(asctime)s.%(msecs)03d] %(levelname)s - %(name)s: %(message)s",
                    level=logging.INFO)

logger = logging.getLogger("CodeQL_client")

parser = argparse.ArgumentParser(prog='CodeQL client',
                                 description='SAST analyse with CodeQL')
# parser.add_argument("--scan_id", 
#                     help="Scan_id from orch", 
#                     required=True)
args = parser.parse_args()

scan_id = args.scan_id

path_to_config = "config.yml"
config_yml = yml_to_dict(path_to_yml=path_to_config)

path_to_secret = config_yml["path_to_secret"]
path_to_bin = config_yml["path_to_bin"]

secret_yml = yml_to_dict(path_to_yml=path_to_secret)

nexus_config = NexusConfig(username=secret_yml["username"],
                           password=secret_yml["password"],
                           url=config_yml["url"])

client = NexusClient(config=nexus_config)
client.tasks

# TODO: Добавить Wait flag

