def archive_channel(channel_id):
    try:
        response = client.conversations_archive(channel=channel_id)
        print(f"Channel archived: {channel_id}")
    except SlackApiError as e:
        print(f"Error archiving channel: {e.response['error']}")

