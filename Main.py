from telegram import Update, ChatPermissions
from telegram.ext import Updater, CommandHandler, CallbackContext
import os

# دریافت توکن از متغیر محیطی
TOKEN = os.getenv("BOT_TOKEN")

def lock(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    permissions = ChatPermissions(can_send_messages=False)
    context.bot.set_chat_permissions(chat_id, permissions)
    update.message.reply_text("🔒 گروه قفل شد!")

def unlock(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    permissions = ChatPermissions(can_send_messages=True)
    context.bot.set_chat_permissions(chat_id, permissions)
    update.message.reply_text("🔓 گروه باز شد!")

def start(update: Update, context: CallbackContext):
    update.message.reply_text("سلام! من یک ربات مدیریت گروه هستم. از دستورات /lock و /unlock استفاده کنید.")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("lock", lock))
dp.add_handler(CommandHandler("unlock", unlock))

updater.start_polling()
updater.idle()
