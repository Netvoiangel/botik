from typing import AsyncIterable
from aiogram import types, Bot, Dispatcher, executor
from config import token_for_tele
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import os


bot = Bot(token=token_for_tele)
dp = Dispatcher(bot)


#Articles


russian_lang = "Русский 🇷🇺"
english_lang = "English 🇬🇧"
back_interlang = "Назад / back"
back_rus = "Назад"
back_eng = "Back"
a = 1

#international part


@dp.message_handler(commands="start")
async def on_starting(message: types.Message):

    buttons_language = [russian_lang, english_lang]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons_language)

    await message.answer("Выберите язык / Choose language", reply_markup=keyboard)


#Русская версия


@dp.message_handler(Text(equals=russian_lang))
async def russian_main_page(message: types.Message):
    buttons = ['Группы 👥', 'Новости 📰', back_rus]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)

    await message.answer("Выберите категорию 🔠", reply_markup=keyboard)


@dp.message_handler(Text(equals="Группы 👥"))
async def russian_groups_all(message: types.Message):
    buttons = ['4931101/20001', '4931101/20002', '4931101/20003', '4931102/20001', '4931102/20002',
    '4931102/20003', '4931104/20001', '4931104/20002', '4931104/20003', '4931601/20001',
    '4931601/20002', '4931601/20003', back_rus]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)

    await message.answer("Выберите группу", reply_markup=keyboard)


#English version


@dp.message_handler(Text(equals=english_lang))
async def english_main_page(message: types.Message):
    buttons = ['Groups 👥', 'News 📰', back_eng]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)

    await message.answer("Choose category 🔠", reply_markup=keyboard)


@dp.message_handler(Text(equals="Groups 👥"))
async def english_groups_all(message: types.Message):
    buttons = ['4931101/20001', '4931101/20002', '4931101/20003', '4931102/20001', '4931102/20002',
    '4931102/20003', '4931104/20001', '4931104/20002', '4931104/20003', '4931601/20001',
    '4931601/20002', '4931601/20003', back_eng]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)

    await message.answer("Choose group", reply_markup=keyboard)


#Launch


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
