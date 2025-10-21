from youtube_transcript_api import YouTubeTranscriptApi
import yt_dlp

video_id = "SkGW-Wcn9Vs" # use video id, not url
video_url = f"https://www.youtube.com/watch?v={video_id}"
ytt_api = YouTubeTranscriptApi()
ydl_opts = {}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:  # fetch video metadata by yt_dlp
    info = ydl.extract_info(video_url, download=False)
    title = info['title']
    author = info['uploader']
    duration_sec = info['duration']

transcription = ytt_api.fetch(video_id, languages=['en', 'ru']) # change to your languages
with open('transcript.txt', "w", encoding="UTF-8") as f:
    f.write(f'Video name: {title}\nAuthor: {author}\nDuration: {duration_sec}s\n')
    f.write('------------------------------\n')
    for entry in transcription:
        start = entry.start
        end = entry.start + entry.duration

        def fmt_time(t):
            m, s = divmod(t, 60) # split total seconds t into minutes and seconds
            return f"{int(m):02}:{s:04.1f}" # format like MM:SS.s with leading zeros

        time_str = f"{fmt_time(start)} - {fmt_time(end)}"
        f.write(f'[{time_str}] | {entry.text}\n')
    print(f'------------\nTranscript saved, check transcript.txt!\nVideo name: {title}\nAuthor: {author}\nDuration: {duration_sec}s')