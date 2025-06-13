# 🔐 Importlar
import random
import asyncio
import time
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram.client.default import DefaultBotProperties

# 🔑 Bot token
BOT_TOKEN = "7272427921:AAFFj7wvnlU1AouIJUJ7RSlGnGkBl8OAJOA"

# 📚 So'zlar ro'yxati
WORDS = [
    "telegram", "python", "dasturchi", "kompyuter", "aiogram", "kitob", "robot", "oyin",
    "suniyintellekt", "internet", "telegrambot", "mobililova", "server", "client",
    "frontend", "backend", "bazama'lumot", "dastur", "kod", "debug", "terminal",
    "loop", "funksiya", "operator", "ifoda", "tuzilma", "websayt", "telegramapi",
    "asyncio", "github", "versiya", "shart", "oyinbot", "proyekt", "komanda", "parol",
    "chatgpt", "suniyidrok", "login", "ramka", "html", "css", "javascript",
    "pythonbot", "sozlash", "dasturiy", "mobil", "oyinsoz", "openai", "kreativ",
    "ilmfan", "alifbo", "matematika", "fizika", "kimyo", "biologiya", "maktab",
    "oquvchi", "darslik", "axborot", "televizor", "telefon", "kamera", "fayl",
    "papka", "zip", "rar", "tasvir", "rasm", "videorolik", "audiofayl", "taqdimot",
    "slayd", "prezentatsiya", "mikrofon", "ma'lumot", "kuzatuvchi", "operatsion",
    "interfeys", "drayver", "konsol", "muloqot", "sozlashmalar", "kompilyator",
    "tuzuvchi", "yangilash", "chegaralash", "muhit", "sistema", "faylsistemasi",
    "jarayon", "modul", "poytaxt", "xalq", "dunyoqarash", "axloq", "davlat",
    "vazifa", "yutuq", "imkoniyat", "qobiliyat", "xotira", "tashabbus", "ilhom",
    "tushuncha", "fikr", "goya", "strategiya", "taktika", "natija", "xulosa",
    "qadam", "loyiha", "namuna", "kreativlik", "izlanish", "aniqlik", "tejamkorlik",
    "samaradorlik", "internetlashtirish", "raqamlashtirish", "chip", "sensor",
    "yordamchi", "hisobot", "robototexnika", "texnologiya", "kuzatuv", "algoritm",
    "arxitektura", "kodlashtirish", "parolingiz", "blok", "yuklash", "saqlash",
    "ko‘chirish", "ishga", "tushirish", "tanlash", "tasdiqlash", "bekor", "qidiruv",
    "aloqa", "sifat", "foydali", "resurs", "hamkorlik", "yangilik", "maqola",
    "xabar", "suniyintellekt", "kompyuterlashtirish", "ma'lumotnoma", "raqamli",
    "chiplar", "sensorlar", "kodlar", "kompilyatsiya", "avtomatlashtirish",
    "o‘rganish", "algoritmlar", "blokcheyn", "kriptografiya", "neyrontarmoq",
    "o‘yinlar", "vebsaytlar", "mobililovalar", "backendkod", "frontendilova",
    "dasturchilik", "fullstack", "vebinterfeys", "vazifalar", "boshqaruv",
    "funksional", "modullar", "interaktiv", "ma'lumotlar", "tizimlar",
    "startap", "suniyonglik", "boshqarish", "monitor", "klaviatura",
    "interaktivlik", "uskunalar", "xavfsizlik", "parollar", "foydalanuvchi",
    "profil", "sozlamalar", "xizmatlar", "loyihalar", "qiziqarli", "fikrlar",
    "tashkilot", "platforma", "asosiy", "muammo", "echim", "tajriba",
    "innovatsiya", "muvaffaqiyat", "xarakat", "tashqi", "ichki", "rivojlanish",
    "tayyorgarlik", "natijadorlik", "boshqaruvchanlik", "ijodiy", "fikrlash",
    "muloqotli", "bashorat", "nazorat", "hamkor", "ijrochi", "kodi", "loyiha",
    "kompaniya", "ishlabchiqarish", "sifatnazorat", "hisobotlar", "yangilanish",
    "mobilplatforma", "televizion", "audio", "video", "vebyig‘in", "robotlar",
    "dron", "raqamliiqtisod", "ma'lumotlarbazasi", "yuznianglash", "tovushnianglash",
    "tilnianglash", "qidiruvmexanizmi", "chatbot", "intellektualtizim",
    "vebportallar", "onlineservis", "raqamlikutubxona", "onlinedars", "interaktivtaqdimot",
    "kodplatforma", "aiogramexample", "telegramintegratsiya", "pythonmodul",
    "innovatsion", "vebmonitoring", "suniyongliksensor", "sensorbazasi",
    "mobilavlod", "kompyuterilova", "vebtexnologiya", "fullstackdeveloper",
    "tizimi", "markazi", "uzeli", "moduli", "dasturi", "platformasi", "bazas", "kontroller", "monitoring", "sensor",
    "tex", "soft", "baz", "kod", "monitor", "robot", "aloqa", "algoritm", "interfeys", "tarmoq",
    "suniy", "veb", "dastur", "kompyuter", "mobil", "innovatsion", "ma'lumot", "aql", "sensor", "internet", "raqamli",
    "internetinterfeysmoduli", "internettarmoquzeli", "sensortarmoqmonitoring", "innovatsionbazdasturi",
    "kompyutersoftdasturi", "innovatsionsoftplatformasi", "aqlsoftmonitoring", "suniysoftbazas",
    "mobiltarmoquzeli", "aqlrobotdasturi",
]
# 🧠 Sessiyalar va ballar
user_sessions = {}
user_scores = {}

# 🤖 Bot va dispatcher
bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()

# 🎲 Shuffle
def shuffle_word(word: str) -> str:
    letters = list(word)
    random.shuffle(letters)
    return ''.join(letters)

# ⌨️ Oddiy klaviatura

def get_main_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🛑 Stop"), KeyboardButton(text="📊 Reyting")],
            [KeyboardButton(text="📋 Foydalanuvchilar"), KeyboardButton(text="👨‍💼 Admin")]
        ], resize_keyboard=True
    )

# 🧾 Inline tugmalar

def get_inline_profile(user_id):
    return InlineKeyboardMarkup(
        inline_keyboard=[[
            InlineKeyboardButton(text="📄 Profilni ko'rish", callback_data=f"profile:{user_id}")
        ]]
    )

# 🔰 /start
@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "🧠 <b>🧩 Shifrlangan So‘z</b> o‘yiniga xush kelibsiz!\n\n🎯 Maqsad: Berilgan aralashtirilgan so‘zni topish.\n🎮 Boshlash uchun <b>/game</b> ni yozing.",
        reply_markup=get_main_keyboard()
    )

# 🎮 /game
@dp.message(Command("game"))
async def cmd_game(message: Message):
    user_id = message.from_user.id
    user_sessions[user_id] = {
        "score": 0,
        "start_time": time.time(),
        "current_word": None,
        "playing": True,
        "name": message.from_user.full_name,
        "username": message.from_user.username or "Noma'lum"
    }
    await message.answer(f"🎮 <b>O'yin boshlandi!</b>", reply_markup=get_main_keyboard())
    await send_next_word(message)

# 🔁 So'z yuborish
async def send_next_word(message: Message):
    user_id = message.from_user.id
    word = random.choice(WORDS)
    shuffled = shuffle_word(word)
    user_sessions[user_id]["current_word"] = word
    await message.answer(f"🔐 So'zni toping: <b>{shuffled}</b>")

# 📩 Har qanday xabar
@dp.message()
async def handle_message(message: Message):
    user_id = message.from_user.id
    text = message.text.strip()

    # Maxsus admin menyusi uchun parol
    if text == "👨‍💼 Admin":
        user_sessions[user_id] = user_sessions.get(user_id, {})
        user_sessions[user_id]["awaiting_admin_password"] = True
        await message.answer("🔐 Maxsus parolni kiriting:")
        return

    if user_sessions.get(user_id, {}).get("awaiting_admin_password"):
        if text == "12345":
            user_sessions[user_id]["awaiting_admin_password"] = False
            admin_kb = ReplyKeyboardMarkup(
                keyboard=[
                    [KeyboardButton(text="👥 Foydalanuvchilarni ko‘rish")],
                    [KeyboardButton(text="📣 Reklama tarqatish")],
                    [KeyboardButton(text="🔙 Ortga")]
                ], resize_keyboard=True
            )
            await message.answer("🔧 Admin menyusi:", reply_markup=admin_kb)
        else:
            await message.answer("❌ Parol noto‘g‘ri.")
        return

    if text == "👥 Foydalanuvchilarni ko‘rish":
        if not user_scores:
            await message.answer("⛔ Foydalanuvchilar yo‘q.")
            return
        msg = "📋 <b>Foydalanuvchilar:</b>\n"
        for uid, data in user_scores.items():
            label = f"@{data['username']}" if data['username'] != "Noma'lum" else f"ID: {uid}"
            msg += f"👤 <b>{data['name']}</b> — {data['score']} ball ({label})\n"
        await message.answer(msg)
        return

    if text == "📣 Reklama tarqatish":
        await message.answer("✍️ Iltimos, reklama matnini yuboring:")
        user_sessions[user_id] = {"awaiting_ad": True}
        return

    if user_id in user_sessions and user_sessions[user_id].get("awaiting_ad"):
        ad_text = text
        for uid in user_scores:
            try:
                await bot.send_message(uid, f"📢 <b>Reklama</b>:\n{ad_text}")
            except:
                continue
        await message.answer("✅ Reklama yuborildi.", reply_markup=get_main_keyboard())
        del user_sessions[user_id]
        return

    if text == "🔙 Ortga":
        await message.answer("🔙 Asosiy menyuga qaytdingiz.", reply_markup=get_main_keyboard())
        return

    if user_id not in user_sessions or not user_sessions[user_id].get("playing"):
        await message.answer("ℹ️ Avval /game deb yozing.")
        return

    if text == "🛑 Stop":
        session = user_sessions[user_id]
        session["playing"] = False
        duration = int(time.time() - session["start_time"])
        minutes = duration // 60
        seconds = duration % 60
        score = session["score"]

        user_scores[user_id] = {
            "name": session["name"],
            "score": score,
            "username": session["username"]
        }

        await message.answer(
            f"🏁 <b>O'yin tugadi!</b>\n"
            f"👤 Ism: <b>{session['name']}</b>\n"
            f"💯 Ball: <b>{score}</b>\n"
            f"⏱ Davomiylik: <b>{minutes} daqiqa {seconds} soniya</b>",
            reply_markup=get_main_keyboard()
        )
        return

    correct = user_sessions[user_id]["current_word"]
    if text.lower() == correct.lower():
        user_sessions[user_id]["score"] += 5
        await message.answer("✅ To'g'ri! +5 ball")
    else:
        user_sessions[user_id]["score"] -= 2
        await message.answer(f"❌ Noto'g'ri! -2 ball\nTo'g'ri javob: <b>{correct}</b>")

    await send_next_word(message)

# 📊 Reyting ko'rsatish
@dp.message(lambda msg: msg.text == "📊 Reyting")
async def show_scores(message: Message):
    if not user_scores:
        await message.answer("📉 Hozircha hech kimda natija yo'q.")
        return

    sorted_scores = sorted(user_scores.items(), key=lambda x: x[1]['score'], reverse=True)
    top_user = sorted_scores[0][1]

    text = "🏆 <b>Eng yaxshi o'yinchilar</b>:\n"
    for i, (uid, data) in enumerate(sorted_scores[:10], 1):
        text += f"{i}. <b>{data['name']}</b> — {data['score']} ball\n"

    text += f"\n👑 <b>#1:</b> @{top_user['username']} — <b>{top_user['score']} ball</b> (eng yuqori natija)"

    await message.answer(text)

# 📋 Foydalanuvchilar tugmasi
@dp.message(lambda msg: msg.text == "📋 Foydalanuvchilar")
async def list_users(message: Message):
    if not user_scores:
        await message.answer("⛔ Hozircha hech kim o‘ynamagan.")
        return

    text = "👥 <b>O‘ynagan foydalanuvchilar:</b>\n"
    for i, (uid, data) in enumerate(user_scores.items(), 1):
        label = f"@{data['username']}" if data['username'] != "Noma'lum" else f"<a href=\"tg://user?id={uid}\">Profil</a>"
        text += f"{i}. <b>{data['name']}</b> (Ball: {data['score']}) — {label}\n"
    text += f"\n📊 Jami foydalanuvchilar: <b>{len(user_scores)}</b> ta"
    await message.answer(text)

# 🔍 Inline tugma orqali profil
@dp.callback_query(lambda c: c.data.startswith("profile:"))
async def show_profile(call: CallbackQuery):
    user_id = int(call.data.split(":")[1])
    data = user_scores.get(user_id)
    if not data:
        await call.message.answer("⛔ Foydalanuvchi topilmadi.")
        return
    await call.message.answer(f"👤 <b>{data['name']}</b> profili:\n💯 Ball: <b>{data['score']}</b>")
    await call.answer()

# 🔁 Start
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
