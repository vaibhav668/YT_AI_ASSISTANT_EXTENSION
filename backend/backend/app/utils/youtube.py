from urllib.parse import urlparse, parse_qs


def extract_video_id(url: str):
    parsed_url = urlparse(url)

    # Normal YouTube URL
    if parsed_url.hostname in ["www.youtube.com", "youtube.com"]:
        return parse_qs(parsed_url.query).get("v", [None])[0]

    # Short YouTube URL
    if parsed_url.hostname == "youtu.be":
        return parsed_url.path[1:]

    return None