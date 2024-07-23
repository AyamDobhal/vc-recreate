import os

import discord
from discord.ext import commands

client = commands.Bot(command_prefix=")", intents=discord.Intents.all())


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


@client.event
async def on_guild_channel_delete(channel: discord.abc.GuildChannel):
    if not isinstance(channel, discord.VoiceChannel):
        return
    await channel.guild.create_voice_channel(
        name=channel.name,
        category=channel.category,
        user_limit=channel.user_limit,
        bitrate=channel.bitrate,
        position=channel.position,
        overwrites=channel.overwrites,
        reason="Voice channel was deleted",
    )
    print(f"Recreated voice channel {channel.name}")


client.run(os.getenv("TOKEN"))
