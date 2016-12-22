import itertools
import operator


class Match:

    def __init__(self, first_picker):
        self.first_picker = first_picker
        self.bans = []
        self.enemy_picks = []
        self.ally_picks = []

    def ban(self, champion):
        self.bans.append(champion)

    def pick_enemy(self, champion):
        self.enemy_picks.append(champion)

    def pick_ally(self, champion):
        self.ally_picks.append(champion)

    def recommend_first_pick(self):
        enemy_bans = [self.bans[1],
                      self.bans[3],
                      self.bans[5]]
        list_of_counters = []
        for ban in enemy_bans:
            list_of_counters = list_of_counters + ban.get_what_it_counters()
        most_common_champ_list = self.most_common_champ(list_of_counters)
        return_index = -1
        banned = True
        while banned:
            return_index += 1
            banned = self.check_if_champ_banned(most_common_champ_list[return_index])
        return most_common_champ_list[return_index][0]

    def check_if_champ_banned(self, champ):
        for banned in self.bans:
            if banned.get_name() == champ[0]:
                return True
        return False

    def most_common(self, list_of_elements):
        # get an iterable of (item, iterable) pairs
        SL = sorted((x, i) for i, x in enumerate(list_of_elements))
        # print('SL:', SL)
        groups = itertools.groupby(SL, key=operator.itemgetter(0))

        # auxiliary function to get "quality" for an item
        def _auxfun(g):
            item, iterable = g
            count = 0
            min_index = len(list_of_elements)
            for _, where in iterable:
                count += 1
                min_index = min(min_index, where)
            # print 'item %r, count %r, minind %r' % (item, count, min_index)
            return count, -min_index

        # pick the highest-count/earliest item
        return max(groups, key=_auxfun)[0]

    def most_common_champ(self, list_of_elements):
        number_of_exists = {}
        champs = [champ.get_name() for champ in list_of_elements]
        for champ in champs:
            number_of_exists[champ] = champs.count(champ)
        sorted_dangerous_champs_list = sorted(number_of_exists.items(), key=operator.itemgetter(1), reverse=True)
        return sorted_dangerous_champs_list
