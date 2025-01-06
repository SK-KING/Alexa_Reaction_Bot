from os import environ as env

class Config:
    API_ID = int(env.get("API_ID", "")) #TG API ID
    API_HASH = env.get("API_HASH", "") #TG API HASH
    BOT_TOKEN = env.get("BOT_TOKEN", "") #Add Bot Token, get from botfather
    FSUB_ID = int(env.get("FSUB_ID", "-1002218982582"))  #Add Your FSub Channel Id -100xxxxxxxxx
    FSUB = bool(env.get("FSUB", True)) #Keep True If U Want Force Subscribe         
    SB_PIC = env.get("SB_PIC", "https://i.ibb.co/c6vkVBP/photo-2024-11-15-12-13-41-7437478159336865812.jpg") # Add Link For Start Cmd Picture 
    BOT_USERNAME = env.get("BOT_USERNAME", "Alexa_testingbot") # Add Bot Username Without @
    EMOJIS = [
        "👍", "👎", "❤", "🔥", 
        "🥰", "👏", "😁", "🤔",
        "🤯", "😱", "🤬", "😢",
        "🥶", "🤩", "🤮", "💩",
        "🙏", "👌", "🤣", "🤡",
        "🥱", "🥴", "😍", "🤓",
        "❤‍🔥", "🌚", "😐", "💯",
        "🤣", "⚡", "🍌", "🏆",
        "💔", "🤨", "😐", "😡",
        "👅", "🆒", "🖕", "😈",
        "😴", "😭", "👻", "⚡",
        "👨‍💻", "👀", "🎃", "🙄",
        "😇", "😨", "🤝", "🤐",
        "🤗", "🫡", "🎅", "🥸",
        "🤫", "😶‍🌫", "🤪", "😏",
        "😘", "👾", "🤷‍♂", "😎"
    ]
