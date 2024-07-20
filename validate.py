def validate_archived_channel(channel_id):
    channels = list_channels()
    for channel in channels:
        if channel['id'] == channel_id:
            return not channel['is_archived']
    return True

