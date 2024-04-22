class GameContext:
    def __init__(self, tick_event=None, on_event=None):
        self.tick_event = tick_event
        self.on_event = on_event
        
    def get_tick_event(self):
        return self.tick_event

    def get_on_event(self):
        return self.on_event