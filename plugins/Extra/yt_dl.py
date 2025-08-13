# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from __future__ import unicode_literals

import os, requests, asyncio, math, time, wget
from pyrogram import filters, Client
from pyrogram.types import Message
from info import CHNL_LNK
from youtube_search import YoutubeSearch
from youtubesearchpython import SearchVideos
from yt_dlp import YoutubeDL


@Client.on_message(filters.command(["video", "mp4"]))
async def vsong(client, message: Message):
    try:
        urlissed = get_text(message)
        if not urlissed:
            return await message.reply_text("Example: /video Baby Shark or youtube link")

        pablo = await message.reply_text("**Finding your video...**")
        
        # Search for the video
        search = YoutubeSearch(urlissed, max_results=1).to_dict()
        if not search:
            return await pablo.edit("No results found")
            
        mo = f"https://youtube.com{search[0]['url_suffix']}"
        thum = search[0]["title"]
        fridayz = search[0]["id"]
        kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
        
        # Download thumbnail
        sedlyf = wget.download(kekme)
        
        # Download options
        opts = {
            "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]",
            "addmetadata": True,
            "key": "FFmpegMetadata",
            "prefer_ffmpeg": True,
            "geo_bypass": True,
            "nocheckcertificate": True,
            "postprocessors": [{"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}],
            "outtmpl": "%(id)s.mp4",
            "logtostderr": False,
            "quiet": True,
        }

        try:
            with YoutubeDL(opts) as ytdl:
                ytdl_data = ytdl.extract_info(mo, download=True)
        except Exception as e:
            return await pablo.edit_text(f"**Download Failed**\nError: `{str(e)}`")

        file_stark = f"{ytdl_data['id']}.mp4"
        capy = f"""**TITLE:** [{thum}]({mo})
**REQUESTED BY:** {message.from_user.mention}"""

        await client.send_video(
            message.chat.id,
            video=open(file_stark, "rb"),
            duration=int(ytdl_data["duration"]),
            file_name=str(ytdl_data["title"]),
            thumb=sedlyf,
            caption=capy,
            supports_streaming=True,
            reply_to_message_id=message.id
        )
        
    except Exception as e:
        await pablo.edit_text(f"An error occurred: `{str(e)}`")
    finally:
        await pablo.delete()
        for files in (sedlyf, file_stark):
            if files and os.path.exists(files):
                os.remove(files)
