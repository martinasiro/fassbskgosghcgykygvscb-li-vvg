from typing import Optional
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import aiohttp  # إضافة هذه السطر لاستيراد مكتبة aiohttp

# Replace with your actual Telegram Bot Token
TOKEN = "7841773846:AAF82Ny90PFpGKbTPCI2gzkn4XWPAc5POh0"

async def get_avatar_banner(uid: str, region: str) -> Optional[str]:
    """Fetch avatar banner image URL asynchronously."""
    url = f"https://wlx-avatar-banner-api.vercel.app/wlx_demon?uid={uid}&region={region}&key=wlx_demon"
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return url
            return None

async def avatar_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /avatar command."""
    if len(context.args) != 2:
        await update.message.reply_text("❌ Usage: /avatar <UID> <Region>")
        return

    uid, region = context.args
    banner_url = await get_avatar_banner(uid, region)

    if banner_url:
        await update.message.reply_photo(photo=banner_url, caption=f"🎭 Avatar Banner for UID: {uid}\n🌍 Region: {region}")
    else:
        await update.message.reply_text("❌ Error fetching avatar banner!")

def main():
    """Start the bot."""
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("avatar", avatar_command))

    print("🤖 Bot is running...")
    app.run_polling()  

if __name__ == "__main__":
    main()
