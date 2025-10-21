import os
from youtube_transcript_api import YouTubeTranscriptApi

video_id = "jJFdkDoDyDc" # use video id, not url

ytt_api = YouTubeTranscriptApi()
transcription = ytt_api.fetch(video_id)
with open('transcript.txt', "w", encoding="UTF-8") as f:
    for entry in transcription:
        f.write(f'{entry.start} | {entry.text} | {entry.duration}\n')
    print('text saved in transcript.txt!')