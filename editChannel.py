def rename_channel(channel_id, new_name):
    try:
        response = client.conversations_rename(channel=channel_id, name=new_name)
        print(f"Channel renamed to: {new_name}")
    except SlackApiError as e:
        print(f"Error renaming channel: {e.response['error']}")

