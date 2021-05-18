import subprocess, os, argparse, sys
# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# WebClient insantiates a client that can call API methods
# When using Bolt, you can use either `app.client` or the `client` passed to listeners.

# Load token from environment or paste your token here
#client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])
client = WebClient(token="xoxb-XXXX")

# Use custom icon
icon = "https://cdn.shopify.com/s/files/1/1061/1924/products/Ghost_Emoji_large.png"

def main(args):

    try:
        # Call the chat.postMessage method using the WebClient
        result = client.chat_postMessage(
            channel=args.channel,
            text=args.text,
            username=args.username,
            icon_url=icon,
            mrkdwn="true"
        )

    except SlackApiError as e:
        print(f"Error posting message: {e}")

if __name__ == "__main__":

    # parse argument
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--text", action="store", help="Text to send", required=True)
    parser.add_argument("-c", "--channel", action="store", help="Channel to send", default="general")
    parser.add_argument("-u", "--username", action="store", help="Username to send", default="Bot")
    args = parser.parse_args()

    # execute main
    main(args)
