# twitch-chat-logger
Logs Twitch chatrooms.

This is useful for twitch streams that don't save their videos.

Combining this with software for stream backups gives all the necessary info to replicate the experience.

Note: This is pretty heavily inspired from other projects. Nothing novel here.

# Setup

Create an OAuth token to authenticate with Twitch IRC by visiting here: https://twitchapps.com/tmi/

Create a `.env` file and add the OAuth Token and associated Twitch handle into it:

    twitch_token = 'oauth:TheTokenValueShouldGoRightHere'
    twitch_user  = 'SomeUserGoesHere'

# Usage
    usage: twitch-chat-logger.py [-h] [-o OUTPUT] [-q] -c CHANNEL
    
    optional arguments:
      -h, --help            show this help message and exit
      -o OUTPUT, --output OUTPUT
                            File to write to, if not provided, it will default to a timestamp
      -v, --verbose         Show chat output
      -c CHANNEL, --channel CHANNEL
                            Channel to log
