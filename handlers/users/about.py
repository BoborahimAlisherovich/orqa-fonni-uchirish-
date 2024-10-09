from aiogram.types import Message
from loader import dp
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

#about commands
@dp.message(Command("about"))
async def about_commands(message:Message,state:FSMContext):
    await message.answer(""" 
🛠️ **Bot haqida:**
Salom! Men [Bot Ismi]man, sizning rasm qayta ishlash bo'yicha yordamchingiz! 📸
Mening maqsadim - sizning suratlaringizdan orqa fonni olib tashlash va ularni yangi ranglar bilan yangilashdir. Buning uchun men **rembg** kutubxonasi yordamida rasmni qayta ishlayman va sizga qulay formatda yuboraman.
💡 **Asosiy funksiyalarim:**
- Orqa fonni o'chirish (PNG va JPG formatlarda).
- Orqa fon rangini o'zgartirish imkoniyati.
- Foydalanuvchilar uchun qulay interfeys va tugmalar.
🔧 **Texnologiyalar**: 
- Python
- Aiogram (Telegram botlar uchun)
- Rembg (orqa fonni o'chirish uchun)
Sizning fikrlaringiz va takliflaringiz men uchun muhim! Agar biron-bir taklif yoki xato topgan bo'lsangiz, iltimos, menga xabar bering. 
Rahmat va rasm uzatishda omad tilayman! ✨
""")
    await state.clear()
    

