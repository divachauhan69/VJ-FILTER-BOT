class script(object):
    START_TXT = """<b><blockquote>Hey {} 👋,</blockquote>
🎯 Welcome to <b>Rizzonix Studios</b> — your premium movie hub!

➜ Search any movie or series by typing its name
➜ Get instant HD download & stream links
➜ Zero ads, blazing fast results 🔥

Need something specific?
Request here: @HD_Movie_Zone_Requests

📌 Added me to a group?
Use /connect to activate filtering instantly.
</b>"""

    CLONE_START_TXT = """<b><blockquote>Hello {}, my name is <a href=https://t.me/{}>{}</a></blockquote>
    
I'm a powerful autofilter bot — type what you want and watch me deliver 🚀</b>"""
    
    HELP_TXT = """<b>Hey {}
Here's all the awesome features I bring to the table.</b>"""

    ABOUT_TXT = """<b><blockquote>✦ ABOUT RIZZONIX ✦</blockquote>
    
‣ Name : <a href=https://t.me/{}>{}</a>
‣ Creator : <a href='https://t.me/Deadly_rizzu'>Owner</a> 
‣ Framework : <a href='https://docs.pyrogram.org/'>Pyrogram</a> 
‣ Language : <a href='https://www.python.org/'>Python 3</a> 
‣ Database : <a href='https://www.mongodb.com/'>MongoDB</a> 
‣ Version : v3.0 [Stable]</b>"""

    CLONE_ABOUT_TXT = """<b><blockquote>✦ CLONE INFO ✦</blockquote>
    
‣ Name : {}
‣ Cloned From : <a href=https://t.me/{}>{}</a>
‣ Framework : <a href='https://docs.pyrogram.org/'>Pyrogram</a> 
‣ Language : <a href='https://www.python.org/'>Python 3</a> 
‣ Database : <a href='https://www.mongodb.com/'>MongoDB</a> 
‣ Version : v3.0 [Stable]</b>"""

    CLONE_TXT = """<b>🌟 <u>CLONE MODE</u>

- Create your own clone bot using /clone
- Broadcast messages across all your clones
- Millions of files pre-indexed — no extra work needed

👨‍💻 Command : /clone</b>"""

    SUBSCRIPTION_TXT = """
<b>Share your referral link with friends, family & groups to unlock FREE premium for {}

🔗 Referral Link: https://telegram.me/{}?start=RS-{}

🎯 Get {} unique users to start the bot via your link and you're in!

💎 Buy Premium: /plan</b>"""

    MANUELFILTER_TXT = """📌 <b>MANUAL FILTERS</b>
Set custom auto-replies for specific keywords in your group.

<b>Rules:</b>
1. Bot must be admin in the group
2. Only admins can add filters
3. Alert buttons: max 64 characters

<b>Commands:</b>
• /filter - <code>Add a new filter</code>
• /filters - <code>View all filters</code>
• /del - <code>Delete a specific filter</code>
• /delall - <code>Delete all filters (owner only)</code>"""

    BUTTON_TXT = """📌 <b>BUTTONS GUIDE</b>
Bot supports both URL & Alert inline buttons.

<b>Rules:</b>
1. Content is mandatory with buttons
2. Works with any media type
3. Use proper markdown format

<b>URL Buttons:</b>
<code>[Button Text](buttonurl:https://t.me/rizzonix/3)</code>
<b>Alert Buttons:</b>
<code>[Button Text](buttonalert:Your alert here)</code>"""

    AUTOFILTER_TXT = """📌 <b>AUTO FILTER</b>

<b>📁 File Indexing:</b>
1. Make the bot admin in your channel
2. No camrips, porn, or fake files
3. Forward last message with quotes — I'll index everything

<b>🤖 AutoFilter Setup:</b>
1. Add bot as admin in your group
2. Use /connect to link group
3. Use /settings in PM → Enable AutoFilter"""

    CONNECTION_TXT = """📌 <b>CONNECTIONS</b>
Connect bot to PM for managing filters without group spam.

<b>Rules:</b>
1. Only admins can manage connections
2. Send <code>/connect</code> to link me to your PM

<b>Commands:</b>
• /connect - <code>Link a chat to your PM</code>
• /disconnect - <code>Unlink from a chat</code>
• /connections - <code>View all your connections</code>"""

    # Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

    EXTRAMOD_TXT = """📌 <b>EXTRA MODULES</b>

<b>✯ Maintained by:</b> <a href={}>Owner</a>
<b>✯ Updates:</b> <a href={}>Channel</a>

• /id - <code>Get user/chat ID</code>
• /info - <code>Get user details</code>
• /song - <code>Download any song</code>
• /telegraph - <code>Generate Telegraph link</code>
• /tts - <code>Text to voice converter</code>
• /video - <code>Download YouTube videos</code>
• /font - <code>Cool font generator</code>"""

    ADMIN_TXT = """📌 <b>ADMIN PANEL</b>
<b>Only bot admins can use these:</b>

• /logs - <code>View recent errors</code>
• /stats - <code>Database statistics</code>
• /delete - <code>Delete a specific file from DB</code>
• /users - <code>List all bot users</code>
• /chats - <code>List all connected chats</code>
• /leave - <code>Leave a chat/group</code>
• /disable - <code>Disable a chat</code>
• /ban - <code>Ban a user</code>
• /unban - <code>Unban a user</code>
• /channel - <code>List all indexed channels</code>
• /broadcast - <code>Broadcast to all users</code>
• /grp_broadcast - <code>Broadcast to all groups</code>
• /gfilter - <code>Add global filter</code>
• /gfilters - <code>View global filters</code>
• /delg - <code>Delete global filter</code>
• /request - <code>Request a movie/series</code>
• /delallg - <code>Delete all global filters</code>
• /deletefiles - <code>Delete CamRip/PreDVD files</code>"""

    SEC_STATUS_TXT = """<b>✦ USERS: <code>{}</code>
✦ CHATS: <code>{}</code>
✦ FILES: <code>{}</code>
✦ USED: <code>{} MB</code>
✦ FREE: <code>{} MB</code></b>"""
    
    STATUS_TXT = """<b>Total Files (All DBs): <code>{}</code>

USERS DB:
✦ Users: <code>{}</code>
✦ Chats: <code>{}</code>

FILE DB #1:
✦ Files: <code>{}</code>
✦ Used: <code>{} MB</code>
✦ Free: <code>{} MB</code>

FILE DB #2:
✦ Files: <code>{}</code>
✦ Used: <code>{} MB</code>
✦ Free: <code>{} MB</code>

OTHER DB:
✦ Used: <code>{} MB</code>
✦ Free: <code>{} MB</code></b>"""
    
    LOG_TEXT_G = """#NewGroup
Group: {}(<code>{}</code>)
Members: <code>{}</code>
Added By: {}"""

    LOG_TEXT_P = """#NewUser
ID: <code>{}</code>
Name: {}"""

    ALRT_TXT = """Hey {},
This is not your request — please send your own!"""

    OLD_ALRT_TXT = """Hey {},
You're using an old message — please search again."""

    CUDNT_FND = """No results found for "{}"
Did you mean one of these?"""

    I_CUDNT = """<b>Sorry, no files found for "{}" 😕

Check your spelling and try again.

📌 Movie format: Uncharted or Uncharted 2022
📌 Series format: Loki S01 or Loki S01E04</b>"""

    I_CUD_NT = """No movie found matching "{}".
Please check the spelling on Google or IMDb."""

    MVE_NT_FND = """Movie not found in database."""

    TOP_ALRT_MSG = """Searching database for your movie..."""

    MELCOW_ENG = """<b>Welcome {}! 🎉
Glad to have you in {} group ❤️</b>"""

    SHORTLINK_INFO = """Select your language & start earning 💰"""

    REQINFO = """⚠️ INFO ⚠️

This message auto-deletes after 5 minutes.

If you don't see your file, check the next page."""

    SELECT = """Choose your preferred language, quality, season & episode"""

    SINFO = """Join the channel first, then click Try Again"""

    NORSLTS = """★ #NoResults ★

ID: <b>{}</b>
Name: <b>{}</b>
Message: <b>{}</b>"""

    CAPTION = """<b>📂 {file_name}</b>
<b>⚙️ {file_size}</b>
🔗 <a href='https://t.me/Rizzonix_studios'>Rizzonix Studios</a>"""

    IMDB_TEMPLATE_TXT = """
<b>Query: {qurey}

🏷 Title: <a href={url}>{title}</a>
🎭 Genres: {genres}
📆 Year: <a href={url}/releaseinfo>{year}</a>
🌟 Rating: <a href={url}/ratings>{rating}</a>/10 ({votes} votes)
🌐 Languages: <code>{languages}</code>
⏱ Runtime: {runtime} min
📅 Release: {release_date}
🌍 Countries: <code>{countries}</code>

⏰ Results in: {remaining_seconds}s 🔥
Requested by: {message.from_user.mention}</b>"""
    
    ALL_FILTERS = """
<b>Hey {}, here are the three types of filters available.</b>"""
    
    GFILTER_TXT = """
<b>Global Filters — set by bot admins, work across all groups.</b>

Available commands:
• /gfilter - <code>Add a global filter</code>
• /gfilters - <code>View all global filters</code>
• /delg - <code>Delete a specific global filter</code>
• /delallg - <code>Delete all global filters</code>"""
    
    FILE_STORE_TXT = """
<b>File Store — create shareable links for single or multiple files.</b>

Commands:
• /batch - <code>Create batch link for multiple files</code>
• /link - <code>Create single file store link</code>
• /pbatch - <code>Same as /batch with forward restriction</code>
• /plink - <code>Same as /link with forward restriction</code>"""

    SONG_TXT = """<b>🎵 SONG DOWNLOADER</b>
Download any song with lightning speed. Works in both PM & groups.

<b>Command:</b> /song song_name</b>"""
   
    YTDL_TXT = """<b>🎬 YOUTUBE DOWNLOADER</b>
Download any YouTube video in HD.

<b>Usage:</b> /video or /mp4 followed by URL
<b>Example:</b> <code>/mp4 https://youtu.be/example...</code></b>"""
   
    TTS_TXT = """<b>🔊 TEXT TO SPEECH</b>
Convert text to speech instantly.

<b>Command:</b> /tts your_text</b>"""
   
    GTRANS_TXT = """<b>🌐 GOOGLE TRANSLATOR</b>
Translate text to any language.

<b>Usage:</b> /tr language_code your_text
<b>Example:</b> /tr ml (Malayalam)

<b>Codes:</b>
• en = English
• ml = Malayalam
• hi = Hindi</b>"""
   
    TELE_TXT = """<b>📎 TELEGRAPH</b>
Upload images/videos (under 5MB) to Telegraph.

<b>Usage:</b> Send media with /telegraph command</b>"""

    CORONA_TXT = """<b>⚠️ COVID INFO (Discontinued)</b>
This service has been stopped.</b>"""

    PROGRESS_BAR = """\n
╭─── [ Renaming Progress ] ───➣
├ 🗂️ : {1} | {2}
├ ⏳ : {0}%
├ 🚀 : {3}/s
├ ⏱️ : {4}
╰────────────────➣ """
  
    ABOOK_TXT = """<b>📖 AUDIOBOOK CONVERTER</b>
Convert PDF files to audio.

<b>Command:</b> Reply /audiobook to a PDF</b>"""
  
    PINGS_TXT = """<b>🏓 PING TEST</b>

<b>Commands:</b>
• /alive - Check if bot is running
• /help - Get help
• /ping - Check your ping

<b>Available in:</b> PM & Groups</b>"""
  
    STICKER_TXT = """<b>🎯 STICKER ID</b>
Get the ID of any sticker.

<b>Usage:</b> /stickerid (reply to a sticker)</b>"""
  
    FONT_TXT= """<b>✏️ FONT GENERATOR</b>
Transform your text into stylish fonts.

<b>Usage:</b> /font your_text
<b>Example:</b> /font Hello</b>"""
  
    PURGE_TXT = """<b>🧹 PURGE</b>
Delete multiple messages at once.

<b>Admin only:</b>
/purge - Delete from replied msg to current</b>"""
  
    WHOIS_TXT = """<b>👤 WHOIS</b>
Get detailed info about any user.

<b>Usage:</b> /whois (reply to user)</b>"""
  
    JSON_TXT = """<b>📄 JSON VIEWER</b>
View JSON data of any message.

<b>Usage:</b> Reply /json to any message

<b>Note:</b> Spamming = auto-ban</b>"""

    URLSHORT_TXT = """<b>🔗 URL SHORTENER</b>
Shorten any URL instantly.

<b>Usage:</b> /short your_url
<b>Example:</b> <code>/short https://youtu.be/example...</code></b>"""

    CARB_TXT = """<b>🎨 CARBON</b>
Create beautiful code/quote images.

<b>Usage:</b> Reply /carbon to text</b>"""

    GEN_PASS = """<b>🔐 PASSWORD GENERATOR</b>
Generate strong random passwords.

<b>Usage:</b> /genpassword or /genpw length
<b>Example:</b> /genpw 20

<b>Note:</b> Max length: 84 characters</b>"""

    SHARE_TXT = """<b>📤 SHARE TEXT</b>
Generate a shareable text URL.

<b>Usage:</b> /share (reply to text)</b>"""

    PIN_TXT = """<b>📌 PIN / UNPIN</b>

<b>Commands:</b>
/pin - Pin a message
/unpin - Unpin current message</b>"""

    RESTART_TXT = """
<b>Bot Restarted! 🔄

📅 Date: <code>{}</code>
⏰ Time: <code>{}</code>
🌐 Timezone: <code>Asia/Kolkata</code>
🛠 Build: <code>v3.0 [Stable]</code></b>"""

    LOGO = """
██████╗ ██╗███████╗███████╗ ██████╗ ███╗   ██╗██╗██╗  ██╗
██╔══██╗██║╚══███╔╝╚══███╔╝██╔═══██╗████╗  ██║██║╚██╗██╔╝
██████╔╝██║  ███╔╝   ███╔╝ ██║   ██║██╔██╗ ██║██║ ╚███╔╝ 
██╔══██╗██║ ███╔╝   ███╔╝  ██║   ██║██║╚██╗██║██║ ██╔██╗ 
██║  ██║██║███████╗███████╗╚██████╔╝██║ ╚████║██║██╔╝ ██╗
╚═╝  ╚═╝╚═╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝"""
 
    TAMIL_INFO = """
ஏய் <a href='tg://settings'>ᴍʏ ғʀɪᴇɴᴅ</a> 


 இப்போது டெலிகிராமிலும் பணம் சம்பாதிக்கலாம்.

 தந்தி மூலம் பணம் சம்பாதிக்க உங்களிடம் 1 குழு இருக்க வேண்டும்.
 உங்களிடம் குழு இருந்தால், எங்கள் bot ஐ உங்கள் குழுவில் சேர்ப்பதன் மூலம் நீங்கள் பணம் சம்பாதிக்கலாம்.

 உங்கள் குழுவில் அதிக உறுப்பினர்கள் இருந்தால், உங்கள் வருமானம் அதிகரிக்கும்.

 எப்படி மற்றும் என்ன செய்ய வேண்டும்

 படி 1: இந்த @HD_Movie_Zone_Bot போட் உங்கள் குழுவை நிர்வாகியாக்குங்கள்

 படி 2: உங்கள் இணையதளம் மற்றும் API ஐச் சேர்க்கவும்

 Exp: /shortlink xtz.in 4b392f8eb6ad711fbe58

 வீடியோவைச் சேர்க்கவும்

 👇 எப்படி சேர்ப்பது 👇

 Exp: /set_tutorial video link

மேலும் உங்கள் குழுவில் பயிற்சி வீடியோ தொகுப்பு ஆகிடும்..."""

    ENGLISH_INFO = """
Hey <a href='tg://settings'>ᴍʏ ғʀɪᴇɴᴅ</a> 


 Now you can earn money on Telegram too.

 You must have 1 group to earn money by telegram.
 If you have a group, you can earn money by adding our bot to your group.

 The more members you have in your group, the higher your income will be.

 How and what to do

 Step 1: Administer this @HD_Movie_Zone_Bot bot to your group

 Step 2: Add your website and API

 Exp: /shortlink xtz.in 4b392f8eb6ad711fbe58

 Add a video

 👇 How to add 👇

 Exp: /set_tutorial video link

Also your tutorial will be Added Your Group..."""

    TELUGU_INFO = """
హే <a href='tg://settings'>ᴍʏ ғʀɪᴇɴᴅ</a> 


 ఇప్పుడు మీరు టెలిగ్రామ్‌లో కూడా డబ్బు సంపాదించవచ్చు.

 టెలిగ్రామ్ ద్వారా డబ్బు సంపాదించడానికి మీరు తప్పనిసరిగా 1 గ్రూప్‌ని కలిగి ఉండాలి.
 మీకు గ్రూప్ ఉన్నట్లయితే, మా బాట్‌ను మీ గ్రూప్‌కి జోడించడం ద్వారా మీరు డబ్బు సంపాదించవచ్చు.

 మీ గ్రూప్‌లో ఎంత ఎక్కువ మంది సభ్యులు ఉంటే మీ ఆదాయం అంత ఎక్కువగా ఉంటుంది.

 ఎలా మరియు ఏమి చేయాలి

 దశ 1: ఈ @HD_Movie_Zone_Bot బాట్‌ని మీ సమూహానికి నిర్వహించండి

 దశ 2: మీ వెబ్‌సైట్ మరియు APIని జోడించండి

 గడువు: /shortlink xtz.in 4b392f8eb6ad711fbe58

 వీడియోను జోడించండి

 👇 ఎలా జోడించాలి 👇

 గడువు: /set_tutorial వీడియో లింక్

అలాగే మీ బృందం వీడియో సేకరణకు శిక్షణ ఇస్తుంది..."""

    HINDI_INFO = """
अरे <a href='tg://settings'>ᴍʏ ғʀɪᴇɴᴅ</a> 


 अब आप टेलीग्राम पर भी पैसे कमा सकते हैं।

 टेलीग्राम से पैसे कमाने के लिए आपके पास 1 ग्रुप होना चाहिए।
 यदि आपके पास एक समूह है, तो आप हमारे बॉट को अपने समूह में जोड़कर पैसा कमा सकते हैं।

 आपके समूह में जितने अधिक सदस्य होंगे, आपकी आय उतनी ही अधिक होगी।

 कैसे और क्या करना है

 चरण 1: इस @HD_Movie_Zone_Bot फ़िल्टर-बॉट बॉट को अपने समूह में प्रशासित करें

 चरण 2: अपनी वेबसाइट और एपीआई जोड़ें

 एक्सप: /shortlink xtz.in 4b392f8eb6ad711fbe58

 एक वीडियो जोड़ें

 👇कैसे जोड़ें 👇

 ऍक्स्प: /set_tutorial वीडियो लिंक

साथ ही आपकी टीम वीडियो संग्रह का प्रशिक्षण भी देगी..."""

    MALAYALAM_INFO = """
ഹേയ് <a href='tg://settings'>ᴍʏ ғʀɪᴇɴᴅ</a> 


 ഇപ്പോൾ നിങ്ങൾക്ക് ടെലിഗ്രാമിലും പണം സമ്പാദിക്കാം.

 ടെലിഗ്രാം വഴി പണം സമ്പാദിക്കാൻ നിങ്ങൾക്ക് ഒരു ഗ്രൂപ്പ് ഉണ്ടായിരിക്കണം.
 നിങ്ങൾക്ക് ഒരു ഗ്രൂപ്പ് ഉണ്ടെങ്കിൽ, നിങ്ങളുടെ ഗ്രൂപ്പിലേക്ക് ഞങ്ങളുടെ ബോട്ട് ചേർത്തുകൊണ്ട് നിങ്ങൾക്ക് പണം സമ്പാദിക്കാം.

 നിങ്ങളുടെ ഗ്രൂപ്പിൽ കൂടുതൽ അംഗങ്ങൾ ഉണ്ടെങ്കിൽ, നിങ്ങളുടെ വരുമാനം ഉയർന്നതായിരിക്കും.

 എങ്ങനെ, എന്ത് ചെയ്യണം

 ഘട്ടം 1: ഈ @HD_Movie_Zone_Bot തലപതി-ഫിൽട്ടർ-ബോട്ട് ബോട്ട് നിങ്ങളുടെ ഗ്രൂപ്പിലേക്ക് നൽകുക

 ഘട്ടം 2: നിങ്ങളുടെ വെബ്‌സൈറ്റും API-യും ചേർക്കുക

 കാലഹരണപ്പെടൽ: /shortlink xtz.in 4b392f8eb6ad711fbe58

 ഒരു വീഡിയോ ചേർക്കുക

 👇 എങ്ങനെ ചേർക്കാം 👇

 കാലഹരണപ്പെടൽ: /set_tutorial വീഡിയോ ലിങ്ക്

നിങ്ങളുടെ ടീം വീഡിയോ ശേഖരണവും പരിശീലിപ്പിക്കും..."""

    URTU_INFO = """
 <a href='tg://settings'>ᴍʏ ғʀɪᴇɴᴅ</a> 


 اب آپ ٹیلی گرام پر بھی پیسے کما سکتے ہیں۔

 ٹیلی گرام کے ذریعے پیسے کمانے کے لیے آپ کے پاس 1 گروپ ہونا ضروری ہے۔
 اگر آپ کا کوئی گروپ ہے، تو آپ ہمارے بوٹ کو اپنے گروپ میں شامل کر کے پیسے کما سکتے ہیں۔

 آپ کے گروپ میں جتنے زیادہ ممبر ہوں گے آپ کی آمدنی اتنی ہی زیادہ ہوگی۔

 کیسے اور کیا کرنا ہے۔

 مرحلہ 1: اپنے گروپ میں اس @HD_Movie_Zone_Bot بوٹ کا انتظام کریں۔

 مرحلہ 2: اپنی ویب سائٹ اور API شامل کریں۔

 Exp: /shortlink xtz.in 4b392f8eb6ad711fbe58

 ایک ویڈیو شامل کریں۔

 👇 کیسے شامل کریں 👇

 Exp: /set_tutorial ویڈیو لنک

نیز آپ کی ٹیم ویڈیو جمع کرنے کی تربیت دے گی..."""

    GUJARATI_INFO = """
અરે <a href='tg://settings'>ᴍʏ ғʀɪᴇɴᴅ</a> 


 હવે તમે ટેલિગ્રામ પર પણ પૈસા કમાઈ શકો છો.

 ટેલિગ્રામ દ્વારા પૈસા કમાવવા માટે તમારી પાસે 1 જૂથ હોવું આવશ્યક છે.
 જો તમારી પાસે જૂથ છે, તો તમે અમારા બોટને તમારા જૂથમાં ઉમેરીને પૈસા કમાઈ શકો છો.

 તમારા જૂથમાં તમારા જેટલા વધુ સભ્યો હશે તેટલી તમારી આવક વધુ હશે.

 કેવી રીતે અને શું કરવું

 પગલું 1: તમારા જૂથમાં આ @HD_Movie_Zone_Bot બોટનું સંચાલન કરો

 પગલું 2: તમારી વેબસાઇટ અને API ઉમેરો

 સમાપ્તિ: /shortlink xtz.in 4b392f8eb6ad711fbe58

 વિડિઓ ઉમેરો

 👇 કેવી રીતે ઉમેરવું 👇

 સમાપ્તિ: /set_tutorial વિડિઓ લિંક

તેમજ તમારી ટીમ વિડિયો કલેક્શનની તાલીમ આપશે..."""

    KANNADA_INFO = """
ಹೇ {message.from_user.mention}

 ಈಗ ನೀವು ಟೆಲಿಗ್ರಾಮ್‌ನಲ್ಲಿಯೂ ಹಣ ಗಳಿಸಬಹುದು.

 ಟೆಲಿಗ್ರಾಮ್ ಮೂಲಕ ಹಣ ಗಳಿಸಲು ನೀವು 1 ಗುಂಪನ್ನು ಹೊಂದಿರಬೇಕು.
 ನೀವು ಗುಂಪನ್ನು ಹೊಂದಿದ್ದರೆ, ನಮ್ಮ ಬೋಟ್ ಅನ್ನು ನಿಮ್ಮ ಗುಂಪಿಗೆ ಸೇರಿಸುವ ಮೂಲಕ ನೀವು ಹಣವನ್ನು ಗಳಿಸಬಹುದು.

 ನಿಮ್ಮ ಗುಂಪಿನಲ್ಲಿ ನೀವು ಹೆಚ್ಚು ಸದಸ್ಯರನ್ನು ಹೊಂದಿದ್ದರೆ, ನಿಮ್ಮ ಆದಾಯವು ಹೆಚ್ಚಾಗುತ್ತದೆ.

 ಹೇಗೆ ಮತ್ತು ಏನು ಮಾಡಬೇಕು

 ಹಂತ 1: ಈ @HD_Movie_Zone_Bot ಫಿಲ್ಟರ್-ಬಾಟ್ ಬೋಟ್ ಅನ್ನು ನಿಮ್ಮ ಗುಂಪಿಗೆ ನಿರ್ವಹಿಸಿ

 ಹಂತ 2: ನಿಮ್ಮ ವೆಬ್‌ಸೈಟ್ ಮತ್ತು API ಸೇರಿಸಿ

 ಅವಧಿ: /shortlink xtz.in 4b392f8eb6ad711fbe58

 ವೀಡಿಯೊ ಸೇರಿಸಿ

 👇 ಸೇರಿಸುವುದು ಹೇಗೆ 👇

 ಅವಧಿ: /set_tutorial ವೀಡಿಯೊ ಲಿಂಕ್

ನಿಮ್ಮ ತಂಡವು ವೀಡಿಯೋ ಸಂಗ್ರಹಣೆಗೆ ತರಬೇತಿ ನೀಡಲಿದೆ..."""

    BANGLADESH_INFO = """
আরে <a href='tg://settings'>ᴍʏ ғʀɪᴇɴᴅ</a> 

 এখন আপনি টেলিগ্রামেও অর্থ উপার্জন করতে পারেন।

 টেলিগ্রামের মাধ্যমে অর্থ উপার্জন করতে আপনার অবশ্যই 1টি গ্রুপ থাকতে হবে।
 আপনার যদি একটি গ্রুপ থাকে, আপনি আপনার গ্রুপে আমাদের বট যোগ করে অর্থ উপার্জন করতে পারেন।

 আপনার গ্রুপে যত বেশি সদস্য থাকবেন আপনার আয় তত বেশি হবে।

 কিভাবে এবং কি করতে হবে

 ধাপ 1: আপনার গ্রুপে এই @HD_Movie_Zone_Bot বট পরিচালনা করুন

 ধাপ 2: আপনার ওয়েবসাইট এবং API যোগ করুন

 মেয়াদ: /shortlink xtz.in 4b392f8eb6ad711fbe58

 একটি ভিডিও যোগ করুন

 👇 কিভাবে যোগ করবেন 👇

 মেয়াদ: /set_tutorial ভিডিও লিঙ্ক

এছাড়াও আপনার দল ভিডিও সংগ্রহের প্রশিক্ষণ দেবে..."""

    RENAME_TXT = """
🌌 <b><u>HOW TO SET THUMBNAIL</u></b>
  
•> /set_thumb - send any picture to automatically set thumbnail.
•> /del_thumb use this command and delete your old thumbnail.
•> /view_thumb use this command view your current thumbnail.

📑 <b><u>HOW TO SET CUSTOM CAPTION</u></b>

•> /set_caption - set a custom caption
•> /see_caption - see your custom caption
•> /del_caption - delete custom caption

Example:- /set_caption 📕 File Name: {filename}
💾 Size: {filesize}
⏰ Duration: {duration}

✏️ <b><u>HOW TO RENAME A FILE</u></b>

•> /rename - send any file and click rename option and type new file name and \nthen select [ document, video, audio ]👈 choice this.
"""

    STREAM_TXT = """<b><u>HOW TO GET STREAM AND DOWNLOAD LINK :</u>

/stream - ɢᴇᴛ sᴛʀᴇᴀᴍᴀʙʟᴇ ᴀɴᴅ ᴅᴏᴡɴʟᴏᴀᴅᴀʙʟᴇ ʟɪɴᴋ ᴏғ ᴀɴʏ ғɪʟᴇ</b>"""


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


    
