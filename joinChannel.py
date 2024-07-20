def join_channel(channel_id):
    try:
        response = client.conversations_join(channel=channel_id)
        print(f"Joined channel: {channel_id}")
    except SlackApiError as e:
        print(f"Error joining channel: {e.response['error']}")

