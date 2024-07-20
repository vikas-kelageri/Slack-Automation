def create_channel(channel_name):
    try:
        response = client.conversations_create(name=channel_name)
        channel_id = response['channel']['id']
        print(f"Channel created: {channel_name} (ID: {channel_id})")
        return channel_id
    except SlackApiError as e:
        print(f"Error creating channel: {e.response['error']}")
        return None

