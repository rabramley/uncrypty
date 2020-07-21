#!/usr/bin/env python

from server import Server
from actions import all_actions
import asyncio
from domain import Counter, Users
import logging
import websockets

logging.basicConfig()


counter = Counter()
domain_objects=[counter]

users = Users(domian_objects=domain_objects)
conn = Server(users=users, actions=all_actions(counter))

for d in domain_objects:
    d.attach(conn.send_message)

start_server = websockets.serve(conn.manage_user_connection, "localhost", 6789)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
