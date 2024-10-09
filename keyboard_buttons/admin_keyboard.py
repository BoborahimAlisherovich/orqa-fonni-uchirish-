from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


admin_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Foydalanuvchilar soni"),
            KeyboardButton(text="Reklama yuborish"),
        ]
        
    ],
   resize_keyboard=True,
   input_field_placeholder="Menudan birini tanlang"
)

admin_button_xabar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="ADMIN UCHUN XABAR"),
           
        ]
        
    ],
   resize_keyboard=True,
)
orqa_button_xabar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="ORQAGA"),
           
        ]
        
    ],
   resize_keyboard=True,
)
