"""
All configurations for pycontacts
"""
import os

from pytconf.config import Config, ParamCreator


class ConfigAuthFiles(Config):
    """
    Parameters for authentication files
    """
    client_secret = ParamCreator.create_existing_file(
        help_string="Where are the credentials?",
        default=os.path.expanduser("~/.config/pycontacts/client_secret.json")
    )
    token = ParamCreator.create_str(
        help_string="Where will we store the user access token?",
        default=os.path.expanduser("~/.config/pycontacts/token.pickle")
    )
