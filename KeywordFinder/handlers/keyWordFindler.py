from aiogram import Router, F, types
from aiogram.types import Message
from keyboards import reply

knowledge_base_router = Router()

@knowledge_base_router.message(F.text.lower() == "ответ по базе знаний")
async def menu_cmd(message: types.Message):
    await message.answer("generation answer from knowledge base", reply_markup=reply.start_kb)