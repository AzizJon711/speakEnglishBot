import logging
from googletrans import Translator
from oxfordDictionary import getAudiofile, getDefinitions
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6077506863:AAH8flqISkuvLKx9wMeWrNfzsXa-OQ25zCM'
tarjimon = Translator()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):

    await message.reply("Salom!\nMen SpeakEnglishBotman!")


@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.reply("Salom!\nMen sizga qanday yordam berishim kerak! Marhamat yozing!")

@dp.message_handler()
async def echo(message: types.Message):
    word_id=message.text
    lang = tarjimon.detect(word_id).lang
    if len(word_id.split())>2:
        if lang == "uz":
            dest="en"
        else:
            dest="uz"
        await message.answer(tarjimon.translate(word_id, dest).text)
    else:
        try:
            word_id=tarjimon.translate(word_id, "en").text
            definitions = getDefinitions(word_id)
            definitions_text = "English:\n"
            uz_def=""
            for i in definitions:
                definitions_text += f"👉 {i}\n"
            for j in definitions:
                uz_def += f"👉 {tarjimon.translate(j, 'uz').text}\n"
            definitions_text=definitions_text+"O'zbekcha:\n"+uz_def
            if lang=="uz":
                await message.reply(tarjimon.translate(word_id, "en").text)
            elif lang=="en":
                await message.reply(tarjimon.translate(word_id, "uz").text)
            await message.answer(definitions_text)
            await message.reply_voice(getAudiofile(word_id))
        except:
            return 0

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)