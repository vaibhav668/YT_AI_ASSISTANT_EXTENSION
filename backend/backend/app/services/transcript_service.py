from youtube_transcript_api import YouTubeTranscriptApi,TranscriptsDisabled

def get_video_transcript(video_id:str):

    try:
        api=YouTubeTranscriptApi()

        transcript_list = api.fetch(video_id)

        transcript = " ".join(chunks.text for chunks in transcript_list)
        return transcript 
    except TranscriptsDisabled:
        print("Transcripts are Disabled")