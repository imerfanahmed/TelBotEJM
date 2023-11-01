from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
from datetime import datetime
import locale


def dateParse(date_string):
    # Create datetime object from string in the format 'yyyy-mm-dd'
    datetime_object = datetime.strptime(date_string, "%Y-%m-%d")

    # Convert datetime object to string in the format 'd mmm yyyy'
    formatted_date = datetime_object.strftime("%d %b %Y")

    return formatted_date

def timeParse(time_string):
    # Create datetime object from string in the format 'hh:mm:ss'
    datetime_object = datetime.strptime(time_string, "%H:%M:%S")

    # Convert datetime object to string in the format 'hh:mm' with am or pm
    formatted_time = datetime_object.strftime("%I:%M %p")

    return formatted_time

#get prayer time from my api using requests
def get_prayer_time():
    x= requests.get('https://essexmasjid.com/wp-json/dpt/v1/prayertime?filter=today')
    x = x.json()
    return "Today : " +dateParse(x[0]['d_date']) + '\n'+ "________________________"+ '\n' "Fajr Jamah : "+ timeParse(x[0]['fajr_jamah']) + '\n' + "Sunrise : "+ x[0]['sunrise'] + '\n' + "Zuhr Jamah : "+ x[0]['zuhr_jamah'] + '\n' +"Asr Jamah : "+ x[0]['asr_jamah'] + '\n' + "Magrib Jamah : "+ x[0]['maghrib_jamah'] + '\n' + "Isha Jamah : "+ timeParse( x[0]['isha_jamah'])


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(get_prayer_time())



token = '6794319131:AAFzA76AEKXrtesZ5oKSRYHApMoU6CwKTnY'

#create  a telegram notification that will fire every day at 12 am
app = ApplicationBuilder().token(token).build()

app.add_handler(CommandHandler("today", hello))

app.run_polling()




