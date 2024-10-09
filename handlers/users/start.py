from aiogram.types import Message, FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp, db, bot
from aiogram.filters import CommandStart
import time
from rembg import remove
from aiogram import F,types
import aiofiles
import os
from .aloqa import process_reply_callback
from PIL import Image
from keyboard_buttons import removebutton, admin_keyboard
from aiogram.fsm.context import FSMContext


@dp.message(CommandStart())
async def start_command(message: Message):
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id
    try:
        db.add_user(full_name=full_name, telegram_id=telegram_id)  # User added to database
        await message.answer(text="Assalomu alaykum, Botdan foydalanish uchun rasm yuboring", reply_markup=admin_keyboard.admin_button_xabar)
    except:
        await message.answer(text="Assalomu alaykum, Botdan foydalanish uchun rasm yuboring", reply_markup=admin_keyboard.admin_button_xabar)


@dp.message(lambda message: not message.photo and not message.document and not message.text.startswith('/'))
async def photo_del(message: types.Message):
    await message.answer(text="Faqat rasm yoki fayl yuboring ❗️")
    await message.delete()


# Handling both photos and image files (e.g., .jpg, .png)
@dp.message(F.photo | F.document.mime_type.in_(["image/jpeg", "image/png"]))
async def handle_photo(message: types.Message, state: FSMContext):
    await message.answer("Rasmni qayta ishlayapman, kuting...")
    await state.clear()

    user_id = message.from_user.id
    input_path = f"input_{user_id}.jpg"
    output_path = f"output_{user_id}.png"  

    # Check and delete previous files if they exist
    if os.path.exists(output_path):
        os.remove(output_path)
    if os.path.exists(input_path):
        os.remove(input_path)

    try:
        # Download the image (photo or file)
        if message.photo:
            photo = message.photo[-1]  # Get the highest resolution
            file = await bot.get_file(photo.file_id)
        else:
            file = await bot.get_file(message.document.file_id)

        await bot.download_file(file.file_path, input_path)

        # Remove background
        start_time = time.time()
        async with aiofiles.open(input_path, "rb") as input_file:
            input_data = await input_file.read()
        output_data = remove(input_data)

        # Save the processed image (PNG with transparency)
        async with aiofiles.open(output_path, "wb") as output_file:
            await output_file.write(output_data)

        end_time = time.time()
        await message.answer(f"Rasm orqa foni {str(end_time - start_time)[:4]} sekundda o'chirildi.")
        
        # Send the processed PNG image
        await message.answer_document(FSInputFile(output_path), caption="PNG format")

        # Send buttons for color selection
        await message.answer("Orqa fon rangini tanlang yoki asliga qaytaring:", reply_markup=removebutton.colors_button)

    except Exception as e:
        await message.answer(f"Xatolik yuz berdi: {str(e)}")

    finally:
        # Clean up the input file after processing
        if os.path.exists(input_path):
            os.remove(input_path)


# Handling color selection from inline buttons
@dp.callback_query()
async def handle_color_choice(callback_query: types.CallbackQuery):
    choice = callback_query.data
    user_id = callback_query.from_user.id
    output_path = f"output_{user_id}.png"
    colorized_path = f"colorized_{user_id}.png"

    # Check and delete the previous colorized image if it exists
    if os.path.exists(colorized_path):
        os.remove(colorized_path)

    # Deleting previous message (to avoid clutter)
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)

    # Handle reply callbacks separately
    if choice.startswith("reply:"):
        await process_reply_callback(callback_query, None)
        return

    if choice == "restore":
        # Send the original PNG file without any background changes
        await callback_query.message.answer_document(FSInputFile(output_path), caption="Asliga qaytarilgan PNG format")
        await callback_query.message.answer("Orqa fon rangini yana o'zgartirish uchun rang tanlang:", reply_markup=removebutton.colors_button)
        return

    try:
        if not os.path.exists(output_path):
            await callback_query.answer("Rasm topilmadi. Iltimos, qayta urinib ko'ring.")
            return

        # Open the image and apply the selected background color
        image = Image.open(output_path).convert("RGBA")
        background = Image.new("RGBA", image.size, choice)
        final_image = Image.alpha_composite(background, image)

        # Save the colorized image as PNG
        final_image.save(colorized_path, "PNG")

        # Send the updated PNG image
        await callback_query.message.answer_document(FSInputFile(colorized_path), caption="Yangi orqa fon bilan PNG format")

    except Exception as e:
        await callback_query.message.answer(f"Xatolik yuz berdi: {str(e)}")

    finally:
        if os.path.exists(colorized_path):
            os.remove(colorized_path)  # Remove the processed image after sending

        # Send buttons again for further changes
        await callback_query.message.answer("Orqa fon rangini yana o'zgartirish uchun rang tanlang:", reply_markup=removebutton.colors_button)
