#!/usr/bin/env python

import asyncio
import json


class Server():

    def __init__(self, users, actions):
        self.users = users
        self.actions = actions

        self.users.attach(self.send_message)

    async def send_message(self, message_type, data):
        if self.users.users:
            message = json.dumps({
                'type': message_type,
                **data,
            })
            await asyncio.wait([u.send(message) for u in self.users.users])

    async def manage_user_connection(self, websocket, path):
        await self.users.register(websocket)

        try:
            await self.process_messages(websocket)
        finally:
            await self.users.unregister(websocket)

    async def process_messages(self, websocket):
        async for message in websocket:
            data = json.loads(message)

            for a in self.actions:
                await a.process(data)
