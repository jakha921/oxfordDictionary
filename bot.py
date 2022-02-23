import logging
from aiogram import Bot, Dispatcher, executor, types

from config import TOKEN
from oxfordDefinition import getDefinition
from googletrans import Translator


translator = Translator()

API_TOKEN = TOKEN

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nYou press start button")


@dp.message_handler(commands=['help'])
async def help_me(message: types.Message):
    await message.reply("Hi!\nHow may I help you?")


@dp.message_handler()
async def translate_text(message: types.Message):
    lang = translator.detect(message.text).lang # detect language
    if len(message.text.split()) > 2:
        dest = 'ru' or 'uz' if lang == 'en' else 'en'
        await message.answer(translator.translate(message.text, dest=dest).text)
    else: 
        if lang == 'en':
            word_id = message.text
        else:
            word_id = translator.translate(message.text, dest='en').text
    
    lookup = getDefinition(word_id)
    if lookup:
        await message.reply(f"Word: {word_id}\nDefinition:\n {lookup['definitions']}")
        if lookup.get('audio'):
            await message.reply_voice(lookup['audio'])
    else:
        await message.reply('Sorry, I don\'t know this word')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

