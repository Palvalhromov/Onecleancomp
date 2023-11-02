from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

from aiogram.types import  InlineKeyboardMarkup, InlineKeyboardButton




API_TOKEN = '1961303904:AAE5oqTra0qsAaMGibvPBxgI3VKjV4ePYvw'
 
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
 
@dp.message_handler(commands='start')
async def url_command(message: types.Message):
   await message.answer(' Привет!\nЯ бот-помощник от группы компаний КлинСтайл!\nОтправь мне сообщение, я тебе обязательно отвечу.\nИли смело нажимай на кнопки.   ', reply_markup=urlkb)

urlkb = InlineKeyboardMarkup(row_width=1)
urlButton1 = InlineKeyboardButton(text='Канал Клининговой Компании', url='https://t.me/OneCleanComp')
urlkb.add(urlButton1)
urlButton2 = InlineKeyboardButton(text='Бренд униформы Chistopitt', url='https://t.me/chistopitt_forma')
urlkb.add(urlButton2)
urlButton3 = InlineKeyboardButton(text='Микрофибра, Бренд Chistopitt', url='https://t.me/chistopitt')
urlkb.add(urlButton3)
urlButton4 = InlineKeyboardButton(text='Напишите нам', url='https://t.me/OneCleanComp_bot')
urlkb.add(urlButton4)
urlButton5 = InlineKeyboardButton(text='МАГАЗИН Chistopitt', url='https://chistopitt.ru/katalog')
urlkb.add(urlButton5)
urlButton6 = InlineKeyboardButton(text='МАГАЗИН tutuborka', url='https://tutuborka.ru/o-kompanii')
urlkb.add(urlButton6)

 

@dp.message_handler(commands=['помощь'])
async def send_welcome(message: types.Message):
   await message.reply("Привет!\nЯ бот-помощник от группы компаний КлинСтайл!\nОтправь мне сообщение, я тебе обязательно отвечу.\nИли смело пиши, и нажимай на кнопки.")  
   
   
@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
   await message.reply("Привет!\nЯ бот-помощник от группы компаний КлинСтайл!\nОтправь мне сообщение, я тебе обязательно отвечу.\nИли смело пиши, и нажимай на кнопки.")   
   
   
   
  
@dp.message_handler()
async def echo(message: types.Message):
   await message.answer(message.text)     
        
  

                             
            
 
if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)