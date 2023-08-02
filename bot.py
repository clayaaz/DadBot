import discord
import responses

intents = discord.Intents.default()
intents.message_content = True


async def send_message(message, user_message):
    try:
        response = responses.handle_responcse(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = "YOUR TOKEN"  # insert you own token
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} is now running!")

    @client.event
    async def on_message(message):
        user_message = str(message.content)
        username = str(message.author)
        channel = str(message.channel)

        # print(f"{username} said: '{user_message}' ({channel})")

        await send_message(message, user_message)

    client.run(TOKEN)
