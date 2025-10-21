from youtube_transcript_api import YouTubeTranscriptApi
import yt_dlp

video_id = "SkGW-Wcn9Vs" # use video id, not url
video_url = f"https://www.youtube.com/watch?v={video_id}"

ydl_opts = {}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(video_url, download=False)
    title = info['title']
    author = info['uploader']
    duration_sec = info['duration']

ytt_api = YouTubeTranscriptApi()
transcription = ytt_api.fetch(video_id, languages=['en', 'ru']) # 
with open('transcript.txt', "w", encoding="UTF-8") as f:
    for entry in transcription:
        start = entry.start
        end = entry.start + entry.duration
        if start >= 60 and end >= 60:
            m_start = int(start // 60)
            s_start = int(start % 60)
            m_end = int(end // 60)
            s_end = int(end % 60)
            time_str = f'{m_start}m{s_start}s - {m_end}m{s_end}s'
        else:
            time_str = f'{start:.1f}s - {end:.1f}s'

        f.write(f'[{time_str}] | {entry.text}\n')
    print(f'------------\ntext saved in transcript.txt!\nVideo name: {title}\nAuthor: {author}\nDuration: {duration_sec}s')
# with open('transcript.txt', "w", encoding="UTF-8") as f:
#     for entry in transcription:
#         f.write(f'{entry.start} | {entry.text} | {entry.duration}\n')
#     print('text saved in transcript.txt!')