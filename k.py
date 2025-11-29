from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8436188294:AAE1By3nZeth0pUHraqzc-yZ18UUrUzwa4E"

# ---------------------------
# MAIN MENU
# ---------------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📚 منصّات التعليم", callback_data="learning")],
        [InlineKeyboardButton("🛠️ أدوات Cybersecurity", callback_data="tools")],
        [InlineKeyboardButton("🎥 فيديوهات تعليمية", callback_data="videos")],
        [InlineKeyboardButton("📌 Roadmap", callback_data="roadmap")],
        [InlineKeyboardButton("📢 قناتنا على Telegram", url="https://t.me/cybergroupe")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    text = (
        "🔥 مرحبا! هذا البوت يساعدك تتعلم CyberSecurity بطريقة قانونية وآمنة.\n"
        "اختر أحد الأقسام 👇"
    )

    # إذا جابها في Callback
    if update.callback_query:
        await update.callback_query.edit_message_text(text, reply_markup=reply_markup)
    else:
        await update.message.reply_text(text, reply_markup=reply_markup)

# ---------------------------
# CALLBACK HANDLER
# ---------------------------
async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # زر الرجوع
    back_button = InlineKeyboardMarkup(
        [[InlineKeyboardButton("⬅️ الرجوع للرئيسية", callback_data="start")]]
    )

    # 📚 منصات التعليم
    if query.data == "learning":
        text = (
            "📚 **أفضل مواقع التعليم الآمنة:**\n\n"
            "• TryHackMe\nhttps://tryhackme.com\n\n"
            "• HackTheBox Academy\nhttps://academy.hackthebox.com\n\n"
            "• PortSwigger Web Academy\nhttps://portswigger.net/web-security\n\n"
            "• OverTheWire\nhttps://overthewire.org\n"
        )
        await query.edit_message_text(text, reply_markup=back_button)

    # 🛠️ أدوات Cybersecurity
    elif query.data == "tools":
        text = (
            "🛠️ **روابط تنزيل أدوات Cybersecurity الآمنة:**\n\n"
            "• Wireshark\nhttps://www.wireshark.org/download.html\n\n"
            "• Burp Suite Community\nhttps://portswigger.net/burp/communitydownload\n\n"
            "• VirtualBox\nhttps://www.virtualbox.org/wiki/Downloads\n\n"
            "• Kali Linux (للـ VM)\nhttps://www.kali.org/get-kali/\n"
        )
        await query.edit_message_text(text, reply_markup=back_button)

    # 🎥 فيديوهات
    elif query.data == "videos":
        text = (
            "🎥 **أفضل الفيديوهات لتعلم CyberSecurity:**\n\n"
            "1️⃣ أساسيات الشبكات:\nhttps://youtu.be/qiQR5rTSshw\n\n"
            "2️⃣ تعلم Linux:\nhttps://youtu.be/yz7nYlnXLfE\n\n"
            "3️⃣ OWASP Top 10:\nhttps://youtu.be/-HHHcSz7p6A\n\n"
            "4️⃣ دورة كاملة:\nhttps://youtu.be/Jt0qS6m7FPc\n"
        )
        await query.edit_message_text(text, reply_markup=back_button)

    # 📌 Roadmap
    elif query.data == "roadmap":
        text = (
            "📌 **Roadmap CyberSecurity (مبتدئ → محترف):**\n\n"
            "1) IT + Linux\n"
            "2) Networking (TCP/IP – DNS – HTTP)\n"
            "3) Web Security + OWASP\n"
            "4) Tools (Nmap – Burp – Wireshark)\n"
            "5) TryHackMe\n"
            "6) HackTheBox Academy\n"
            "7) Blue Team Basics\n"
            "8) Incident Response\n"
            "9) Red Team (قانونياً)\n"
        )
        await query.edit_message_text(text, reply_markup=back_button)

    # زر الرجوع للرئيسية
    elif query.data == "start":
        await start(update, context)

# ---------------------------
# RUN BOT
# ---------------------------
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(menu))
app.run_polling()
