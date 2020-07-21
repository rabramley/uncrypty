class Subject():
    def __init__(self, name) -> None:
        self.name = name
        self.observers = set()

    def attach(self, func):
        self.observers.add(func)
    
    def detatch(self, func):
        self.observers.remove(func)
    
    async def notify(self):
        for o in self.observers:
            await o(self.name, self.state())
    
    def state(self):
        return {}


class Users(Subject):
    def __init__(self, domian_objects):
        self.users = set()
        self.domian_objects = domian_objects
        super().__init__('users')

    async def register(self, websocket):
        self.users.add(websocket)
        await self.notify()

        # When a new user is registered we need
        # to send the domain to them.  This also sends
        # it to all other users (does it need to?)
        for d in self.domian_objects:
            await d.notify()

    async def unregister(self, websocket):
        self.users.remove(websocket)
        await self.notify()

    def state(self):
        return {'count': len(self.users)}


class Counter(Subject):
    def __init__(self):
        self.value = 0
        super().__init__('state')

    async def plus(self):
        self.value += 1
        await self.notify()

    async def minus(self):
        self.value -= 1
        await self.notify()

    def state(self):
        return {'value': self.value}
