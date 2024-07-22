import yt_dlp

links = [
    "https://www.youtube.com/watch?v=H__i5LKFVXg",
    "https://www.youtube.com/watch?v=OtJVufo3IrA",
    "https://www.youtube.com/watch?v=nwHY2mhtcuE"
    ]

for link in links:
    try:
        ydl_opts = {
            'format': 'best',
            'outtmpl': '%(title)s.%(ext)s',  
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        print(f"Download complete for: {link}")
    except Exception as e:
        print(f"An error occurred with {link}: {e}")
