"""
"ARandomBot" Discord Bot source code. This is public and can be changed by anyone.
Contributions are welcome and can be PR'd to the main repository or run the bot 
yourself for your own purposes!

@knvtva
"""

import os
import sys
import json

"""
Read our JSON config file. Get our bot token from here including any other settings
that maybe needed for the bot to run.

"""

def ReadJSONFile():
    # { Probably better ways of doing this, but I just simply don't care }
    script_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
    config_path = os.path.join(script_dir, 'config.json')
    if not os.path.isfile(config_path):
        sys.exit("'config.json' not found! Please add it and try again.")
    else:
        with open(config_path) as file:
            config = json.load(file)
            return config