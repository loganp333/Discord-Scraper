#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
query.py - Collection module.
"""

__author__ = "Logan"

# Standard Python Library
import sqlite3
conn = sqlite3.connect('../db/discord.db')
c = conn.cursor()

# Pay attention to argument data types (All IDs should be passed as strings)
def updateUserTable(id, profilePicture, userName, userDiscrim):
    c.execute(f"INSERT INTO users VALUES ({int(id)}, '{profilePicture}', '{userName}', '{userDiscrim}')")
    conn.commit()

def checkForUserRecord(id, profilePicture, userName, userDiscrim):
    c.execute(f"SELECT EXISTS (SELECT user_id FROM users WHERE user_id = {int(id)})")
    if (c.fetchone()[0] == 0):
        updateUserTable(id, profilePicture, userName, userDiscrim)

def updateUserServersTable(id, serverID, lastSeen, serverName, userName):
      c.execute(f"INSERT INTO user_servers VALUES ({int(id)}, {int(serverID)}, '{lastSeen}', '{serverName}', '{userName}')")
      conn.commit()

def checkForUserServersRecord(id, serverID, lastSeen, serverName, userName):
    c.execute(f"SELECT EXISTS (SELECT server_id FROM user_servers WHERE server_id = {int(serverID)} AND user_id = {int(id)})")
    if (c.fetchone()[0] == 0):
        updateUserServersTable(id, serverID, lastSeen, serverName, userName)

def updateServersTable(serverID, serverName, memberCount, serverIcon, serverOwner, creationDate):
    c.execute(f"INSERT INTO servers VALUES ({int(serverID)}, '{serverName}', {memberCount}, '{serverIcon}', {int(serverOwner)}, '{creationDate}')")
    conn.commit()

def checkForServersRecord(serverID, serverName, memberCount, serverIcon, serverOwner, creationDate):
    c.execute(f"SELECT EXISTS (SELECT server_id FROM servers WHERE server_id = {int(serverID)})")
    if (c.fetchone()[0] == 0):
     updateServersTable(serverID, serverName, memberCount, serverIcon, serverOwner, creationDate)

def updateUserMessages(id, messageContent, serverID, timeStamp, channelID, userName, userDiscrim):
    c.execute(f"INSERT INTO user_messages VALUES ({int(id)}, '{messageContent}', {int(serverID)}, '{timeStamp}', {int(channelID)}, '{userName}', {userDiscrim})")
    conn.commit()
