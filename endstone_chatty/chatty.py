from endstone.plugin import Plugin
from endstone.event import event_handler, BroadcastMessageEvent


class Chatty(Plugin):
    api_version = "0.6"
    authors = ["Kupujljl-samu", "Kopatel"]
    prefix = "Chatty"

    commands = {}
    log_top = "╔" + "═"*28 + "╗"
    log_bottom = "╚" + "═"*28 + "╝"
    end_violators = set()
    def on_load(self):
        self.save_default_config()
        self.reload_config()

    def on_enable(self):
        self.logger.info(self.log_top)
        self.logger.info(f"║__EndStone-Chatty загружен__║")
        self.logger.info(f"║__________by Kupujljl-samu__║")
        self.logger.info(self.log_bottom)
        self.register_events(self)

    @event_handler
    def message(self, event: BroadcastMessageEvent):
        self.logger.info(f"Вызван ивент с текстом: {event.message} от игрока {event.event_name}")