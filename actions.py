class Action():
    def __init__(self, name):
        self.name = name

    async def process(self, message):
        if message['action'] == self.name:
            await self._do_process()
            return True
        else:
            return False

    async def _do_process(self):
        pass


class Plus(Action):
    def __init__(self, counter):
        self.counter = counter
        super().__init__(name='plus')

    async def _do_process(self):
        await self.counter.plus()


class Minus(Action):
    def __init__(self, counter):
        self.counter = counter
        super().__init__(name='minus')

    async def _do_process(self):
        await self.counter.minus()


def all_actions(counter):
    return [
        Plus(counter=counter),
        Minus(counter=counter),
    ]

