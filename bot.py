import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.tl.types import ChannelParticipantAdmin
from telethon.tl.types import ChannelParticipantCreator
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.errors import UserNotParticipantError

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)
spam_chats = []

@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply(
    "__**────────────────────────ㅤ ㅤ𝐈'𝐌 𝐓𝐄𝐀𝐌 𝐓𝐉 𝐌𝐄𝐍𝐓𝐈𝐎𝐍 𝐁𝐎𝐓 ────────────────────────**  ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱   ㅤㅤ𝐓𝐄𝐀𝐌 𝐓𝐉 𝐂𝐀𝐍 𝐌𝐄𝐍𝐓𝐈𝐎𝐍 𝐀𝐋𝐋 𝐌𝐄𝐌𝐁𝐄𝐑𝐒 𝐈𝐍 𝐆𝐑𝐎𝐔𝐏 𝐎𝐑 𝐂𝐇𝐀𝐍𝐍𝐄𝐋  ▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱ㅤ  **/help** 𝐅𝐎𝐑 𝐌𝐎𝐑𝐄 𝐈𝐍𝐅𝐖𝐑𝐌𝐀𝐓𝐈𝐎𝐍__\n\n'🔺 ᴅ ᴇ ᴠ ᴇ ʟ ᴏ ᴘ ᴇ ʀ 🔻 [@king_of_izzy]",
    link_preview=False,
    buttons=(
      [
        Button.url('🔺 ᴄ ʜ ᴀ ᴛ 🔻', 'https://t.me/tamil_junctions'),
        Button.url('🔺 ᴅ ᴇ ᴠ ᴇ ʟ ᴏ ᴘ ᴇ ʀ 🔻', 'https://t.me/king_of_izzy')
      ]
    )
  )

@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
  helptext = "**Help Menu of MentionAllBot**\n\nCommand: /all \n__𝐘𝐎𝐔 𝐂𝐀𝐍 𝐔𝐒𝐄 𝐓𝐇𝐈𝐒 𝐂𝐎𝐌𝐌𝐀𝐍𝐃 𝐖𝐈𝐓𝐇 𝐓𝐄𝐗𝐓 𝐖𝐇𝐀𝐓 𝐘𝐎𝐔 𝐖𝐄𝐍𝐓 𝐓𝐎 𝐌𝐄𝐍𝐓𝐈𝐎𝐍 𝐎𝐓𝐇𝐄𝐑𝐒.__\n`𝐄𝐗𝐀𝐌𝐏𝐋𝐄 : /all 𝐆𝐎𝐎𝐃 𝐌𝐎𝐑𝐍𝐈𝐍𝐆 𝐓𝐄𝐀𝐌 𝐓𝐉!`\n__𝐘𝐎𝐔 𝐂𝐀𝐍 𝐘𝐎𝐔 𝐓𝐇𝐈𝐀 𝐂𝐎𝐌𝐌𝐄𝐍𝐃 𝐀𝐒 𝐀 𝐑𝐄𝐏𝐋𝐀𝐘 𝐓𝐎 𝐀𝐍𝐘 𝐌𝐀𝐒𝐒𝐀𝐆𝐄. 𝐁𝐎𝐓 𝐖𝐈𝐋𝐋 𝐓𝐀𝐆 𝐔𝐒𝐄𝐑𝐀 𝐓𝐎 𝐓𝐇𝐀𝐓 𝐑𝐄𝐏𝐋𝐈𝐄𝐃 𝐌𝐀𝐒𝐒𝐀𝐆𝐄__.\n\n'🔺 ᴅ ᴇ ᴠ ᴇ ʟ ᴏ ᴘ ᴇ ʀ 🔻 [@king_of_izzy]"
  await event.reply(
    helptext,
    link_preview=False,
    buttons=(
      [
        Button.url('🔺 ᴄ ʜ ᴀ ᴛ 🔻', 'https://t.me/tamil_junctions'),
        Button.url('🔺 ᴅ ᴇ ᴠ ᴇ ʟ ᴏ ᴘ ᴇ ʀ 🔻', 'https://t.me/king_of_izzy')
      ]
    )
  )
  
@client.on(events.NewMessage(pattern="^/all ?(.*)"))
async def mentionall(event):
  chat_id = event.chat_id
  if event.is_private:
    return await event.respond("__𝐓𝐇𝐈𝐒 𝐂𝐎𝐌𝐌𝐀𝐍𝐃 𝐂𝐀𝐍 𝐁𝐄 𝐔𝐒𝐄 𝐈𝐍 𝐆𝐑𝐎𝐔𝐏 𝐀𝐍𝐃 𝐂𝐇𝐄𝐍𝐍𝐄𝐋𝐒!__")
  
  is_admin = False
  try:
    partici_ = await client(GetParticipantRequest(
      event.chat_id,
      event.sender_id
    ))
  except UserNotParticipantError:
    is_admin = False
  else:
    if (
      isinstance(
        partici_.participant,
        (
          ChannelParticipantAdmin,
          ChannelParticipantCreator
        )
      )
    ):
      is_admin = True
  if not is_admin:
    return await event.respond("__Only admins can mention all!__")
  
  if event.pattern_match.group(1) and event.is_reply:
    return await event.respond("__Give me one argument!__")
  elif event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.is_reply:
    mode = "text_on_reply"
    msg = await event.get_reply_message()
    if msg == None:
        return await event.respond("__𝐈 𝐂𝐀𝐍'𝐓 𝐌𝐄𝐍𝐓𝐈𝐎𝐍 𝐌𝐄𝐌𝐁𝐄𝐑𝐒 𝐅𝐎𝐄 𝐎𝐋𝐃𝐄𝐑 𝐌𝐄𝐒𝐒𝐀𝐆𝐄! (𝐌𝐄𝐒𝐒𝐀𝐆𝐄𝐒 𝐖𝐇𝐈𝐓𝐂𝐇 𝐀𝐑𝐄 𝐒𝐄𝐍𝐃 𝐁𝐄𝐅𝐎𝐑𝐄 𝐈'𝐦 𝐀𝐃𝐃𝐄𝐃 𝐓𝐎 𝐆𝐑𝐎𝐔𝐏)__")
  else:
    return await event.respond("__𝐑𝐄𝐏𝐋𝐀𝐘 𝐓𝐎 𝐀 𝐌𝐄𝐒𝐒𝐀𝐆𝐄 𝐎𝐑 𝐆𝐈𝐕𝐄 𝐌𝐄 𝐒𝐎𝐌𝐄 𝐓𝐄𝐗𝐓 𝐓𝐎 𝐌𝐄𝐍𝐓𝐈𝐎𝐍 𝐎𝐓𝐇𝐄𝐑𝐒!__")
  
  spam_chats.append(chat_id)
  usrnum = 0
  usrtxt = ''
  async for usr in client.iter_participants(chat_id):
    if not chat_id in spam_chats:
      break
    usrnum += 1
    usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
    if usrnum == 1:
      if mode == "text_on_cmd":
        txt = f"{usrtxt}\n\n{msg}"
        await client.send_message(chat_id, txt)
      elif mode == "text_on_reply":
        await msg.reply(usrtxt)
      await asyncio.sleep(2)
      usrnum = 0
      usrtxt = ''
  try:
    spam_chats.remove(chat_id)
  except:
    pass

@client.on(events.NewMessage(pattern="^/cancel$"))
async def cancel_spam(event):
  if not event.chat_id in spam_chats:
    return await event.respond('__𝐓𝐇𝐄𝐑𝐄 𝐈𝐒 𝐍𝐎 𝐏𝐑𝐎𝐂𝐂𝐄𝐒𝐒 𝐎𝐍 𝐆𝐎𝐈𝐍𝐆...__')
  else:
    try:
      spam_chats.remove(event.chat_id)
    except:
      pass
    return await event.respond('__Stopped.__')

print(">> BOT STARTED <<")
client.run_until_disconnected()
