# Telegram Video Downloader Bot

بوت تلغرام بسيط لتحميل الفيديوهات باستخدام yt-dlp.

## التشغيل المحلي
1. فعل بيئة افتراضية:
```bash
python -m venv env
source env/bin/activate  # أو .\env\Scripts\activate على ويندوز
```

2. ثبّت الحزم:
```bash
pip install -r requirements.txt
```

3. شغّل البوت:
```bash
export BOT_TOKEN=توكن_البوت  # أو set BOT_TOKEN=... على ويندوز
python bot.py
```

## النشر على Render
- Build command: `pip install -r requirements.txt`
- Start command: `python bot.py`
- Environment variable: `BOT_TOKEN`