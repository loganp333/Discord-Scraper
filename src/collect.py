#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
collect.py - Collection module.
"""

__author__ = "Bart, Logan"

# Third party libraries
import discord

# Project related
from query import (checkForUserRecord, checkForUserServersRecord,
                   checkForServersRecord, updateUserMessages)

# Global variables
TOKEN = ''
client = discord.Client(fetch_offline_members=False)


@client.event
async def on_ready():
    print('Collecting data as {0.user} {0.user.id}'.format(client))
    await client.change_presence(activity=discord.Game(name="Online"))


@client.event
async def on_message(message: discord.Message):
    # Doesn't log DMs messages
    if isinstance(message.channel, discord.DMChannel):
        return

    checkForUserRecord(str(message.author.id), str(message.author.avatar_url),
                       message.author.name, message.author.discriminator)

    checkForUserServersRecord(str(message.author.id), str(message.guild.id),
                              message.created_at.timestamp(),
                              message.guild.name, message.author.name)

    # message.guild.owner returns None anyways
    server_owner = message.guild.owner or discord.Object(404)
    checkForServersRecord(str(message.guild.id), message.guild.name,
                          message.guild.member_count,
                          str(message.guild.icon_url),
                          str(server_owner.id),
                          message.guild.created_at.timestamp())

    updateUserMessages(str(message.author.id), message.content,
                       str(message.guild.id), message.created_at.timestamp(),
                       str(message.channel.id), message.author.name,
                       message.author.discriminator)
    
    print(f"Logging: M:{message.id} from {message.guild} by {message.author}")


client.run(TOKEN, bot=False)
