from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import model


class Images_processing(StatesGroup):
    waiting_for_style = State()
    waiting_for_content = State()
    waiting_for_result = State()


async def style(message: types.Message):
    await message.answer("Загрузите стиль:")
    await Images_processing.waiting_for_style.set()


async def style_chosen(message: types.Message, state: FSMContext):
    #document_id = message['photo'][-1].file_id
    await message['photo'][-1].download("style.jpg")
    with open('style.jpg', 'rb') as img:
        await message.answer_photo(img)
    #await message.answer_photo(document_id)
    await message.answer("Теперь выберете изображение на которое будет накладываться стиль:")
    await Images_processing.waiting_for_content.set()


async def content_chosen(message: types.Message, state: FSMContext):
    await message['photo'][-1].download("content.jpg")
    await message.answer("Вы выбрали контент ожидайте результат обработки")
    final_image = model.magic_function()
    final_image.save('result.jpg', format='JPEG')
    with open('result.jpg', 'rb') as img:
        await message.answer_photo(img)
    await state.finish()


def register_handlers_photo(dp: Dispatcher):
    dp.register_message_handler(style, commands="style", state="*")
    dp.register_message_handler(style_chosen, content_types=["photo"], state=Images_processing.waiting_for_style)
    dp.register_message_handler(content_chosen, content_types=["photo"], state=Images_processing.waiting_for_content)