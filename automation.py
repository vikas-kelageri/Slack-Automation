channel_name = "test-channel"
new_channel_name = "renamed-channel"

channel_id = create_channel(channel_name)
if channel_id:
    join_channel(channel_id)
    rename_channel(channel_id, new_channel_name)
    channels = list_channels()
    channel_names = [channel['name'] for channel in channels]
    if new_channel_name in channel_names:
        print(f"Channel name successfully changed to: {new_channel_name}")
    archive_channel(channel_id)
    if not validate_archived_channel(channel_id):
        print(f"Channel archived successfully: {channel_id}")
    else:
        print(f"Channel archiving failed: {channel_id}")

