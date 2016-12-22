from source_parsers.lolcounter import LoLCounterParser


class Champion:

    def __init__(self, name):
        self.name = name
        self.lolcounter_parser = LoLCounterParser()
        self.counters = self.lolcounter_parser.get_counters_for_champ(self.name)
        self.counter_for = self.lolcounter_parser.get_what_it_counters(self.name)

    def get_name(self):
        return self.name

    def get_counters(self):
        return self.counters

    def get_what_it_counters(self):
        return self.counter_for

    def __repr__(self):
        return self.get_name()
