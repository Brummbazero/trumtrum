from aiogram import  Bot, Dispatcher, executor, types
import python_weather

bot = Bot(token="6104168112:AAEyTlj9USG8Kd7z_BV7OkGS7rxnawn8DKM")
dp = Dispatcher (bot)
client = python_weather.Client(format=python_weather.IMPERIAL)

@dp.message_handler()
async def echo(message: types.Message):
    weather = await client.get(message.text)
    celsius = round((weather.current.temperature -32) /1.8)

    resp_msg = f"weather.location_name \n"
    resp_msg = f"Погода в данном городе: {celsius}\n"

    await message.answer(resp_msg)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)