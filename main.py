from telethon import client
from kantex.md import *
from telethon import events
from telethon.tl import custom
from telethon.tl.custom import Message
from telethon.tl.types import (Channel, User)

from telethon import TelegramClient

# Remember to use your own values from my.telegram.org!
api_id = 653921
api_hash = 'ff362f2e52c7ddafac3e88aec6a80db8'
client: client = TelegramClient('session', api_id, api_hash)


@client.on(events.NewMessage(pattern='\\?\\?gban'))
async def bban(event):
    """Globally ban a user.

    This will call the joinprotectbot function to gban a user in the Bolverwatch Network



    """

    await event.delete()
    msg: Message = event.message
    chat: Channel = event.chat
    if msg.is_reply:

        reply_msg: Message = await msg.get_reply_message()

        uid = reply_msg.from_id

        offender: User = await client.get_entity(uid)

        # Make an inline query to @like
        results: custom.inlineresults = await client.inline_query('JoinProtectionBot',
                                                                  f'gban {uid} {offender.username if offender.username else offender.first_name}')
        haftbefehl: custom.InlineResult = results[0]

        message = await haftbefehl.click(chat, reply_to=reply_msg)

    else:
        await client.send_message(chat, str(KanTeXDocument(Section('Error', SubSection(Code('Not an reply'))))))


@client.on(events.NewMessage(pattern='\\?\\?token'))
async def btoken(event):
    """Globally token a user.

    This will call the joinprotectbot function to tokenize a user in the Bolverwatch Network



    """
    await event.delete()
    msg: Message = event.message
    chat: Channel = event.chat

    if msg.is_reply:

        reply_msg: Message = await msg.get_reply_message()

        uid = reply_msg.from_id

        offender: User = await client.get_entity(uid)

        # Make an inline query to @like
        results: custom.inlineresults = await client.inline_query('JoinProtectionBot', f'token {uid} {offender.username if offender.username else offender.first_name}')
        haftbefehl: custom.InlineResult = results[0]

        message = await haftbefehl.click(chat, reply_to=reply_msg)

    else:
        await client.send_message(chat, str(KanTeXDocument(Section('Error', SubSection(Code('Not an reply'))))))


with client:
    client.run_until_disconnected()
