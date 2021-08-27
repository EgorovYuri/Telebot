from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text, IDFilter


async def cmd_start(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Привет! Это тестовый бот предназначенный для стилизации изображений.")
    await message.answer("Для начала добавьте стиль с помощью команды: /style.")

async def cmd_cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Все отмененно")

def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start", state="*")
    dp.register_message_handler(cmd_cancel, commands="cancel", state="*")