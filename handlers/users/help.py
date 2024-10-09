from aiogram.types import Message
from loader import dp
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext


#help commands
@dp.message(Command("help"))
async def help_commands(message:Message,state:FSMContext):
    await message.answer("""  
🤖 **Yordam - Botdan qanday foydalanish:**
Assalomu alaykum! Mening yordamimga xush kelibsiz! Bu bot orqali rasm yuborib, orqa fonni o'chirib, uni turli ranglarga o'zgartirishingiz mumkin. Mana qanday ishlaydi:
1️⃣ **Rasm yuborish**: Botga rasm yuboring. Eng yaxshi natija uchun yuqori sifatli rasm tanlang.
2️⃣ **Orqa fonni o'chirish**: Rasm yuborilgandan so'ng, bot orqa fonni o'chirib beradi va sizga PNG va JPG formatida qayta ishlangan rasmlarni yuboradi.
3️⃣ **Rang tanlash**: Qayta ishlangan rasmni olganingizdan so'ng, orqa fon rangini tanlashingiz mumkin. Rangni tanlash uchun tugmalar orqali tanlov qiling.
4️⃣ **Asliga qaytarish**: Agar siz orqa fonni o'zgartirmoqchi bo'lsangiz, "Asliga qaytarish" tugmasini bosib, dastlabki rasmni qaytarib olishingiz mumkin.
❓ **Savollaringiz bormi?** Menga har qanday savol bilan murojaat qilishingiz mumkin!   
""")
    await state.clear()
