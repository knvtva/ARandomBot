"""
"ARandomBot" Discord Bot source code. This is public and can be changed by anyone.
Contributions are welcome and can be PR'd to the main repository or run the bot 
yourself for your own purposes!

@knvtva
"""

from Utils.Config import ReadConfigFile


Config = ReadConfigFile.ReadJSONFile()

def info(data):
    print(f"[ARandomBot] <INFO> {data}")

def warning(data):
    print(f"[ARandomBot] <WARNING> {data}")

def error(data):
    print(f"[ARandomBot] <ERROR> {data}")

def debug(data):
    if [Config['Debug']] == True:
        print(f"[ARandomBot] <DEBUG> {data}")