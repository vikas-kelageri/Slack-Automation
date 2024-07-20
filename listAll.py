def list_channels():
    try:
        response = client.conversations_list()
        channels = response['channels']
        return channels
    except SlackApiError as e:
        print(f"Error listing channels: {e.response['error']}")
        return []

