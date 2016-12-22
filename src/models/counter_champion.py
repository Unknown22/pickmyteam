
class CounterChamp:

    def __init__(self, name, up, down):
        self.name = name
        self.up_votes = up
        self.down_votes = down
        self.ratio = self.up_votes/self.down_votes

    def get_up_votes(self):
        return self.up_votes

    def get_down_votes(self):
        return self.down_votes

    def get_ratio(self):
        return self.ratio

    def get_name(self):
        return self.name

    def __repr__(self):
        return "{}:{}".format(self.get_name(), self.get_ratio())

    def __lt__(self, other):
        return self.get_ratio() > other.get_ratio()