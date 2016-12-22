from source_parsers.lolcounter import LoLCounterParser
from models.match import Match
from models.champion import Champion

if __name__ == "__main__":
    print('Who ban first?')
    print('1. My Team')
    print('2. Enemy Team')
    first_picker = int(input())
    match = Match(first_picker)
    lolcounter = LoLCounterParser()
    for i in range(1, 7):
        text = 'Ban ' + str(i) + ': '
        to_ban_name = input(text)
        champ_to_ban = Champion(to_ban_name)
        match.ban(champ_to_ban)

    if first_picker == 1:
        who = 'ally'
    else:
        who = 'enemy'

    for i in range(1, 7):
        if first_picker == 1:
            if i in [1, 4, 5]:
                if i == 1:
                    print('Recommended first pick:', match.recommend_first_pick())
                who = 'ally'
            else:
                who = 'enemy'
        else:
            if i in [1, 4, 5]:
                who = 'enemy'
            else:
                who = 'ally'
        text = 'Pick ' + who + ': '
        to_pick = input(text)
        champ_to_pick = Champion(to_pick)
        if first_picker == 1:
            if i in [1, 4, 5]:
                match.pick_ally(champ_to_pick)
            else:
                match.pick_enemy(champ_to_pick)
        else:
            if i in [1, 4, 5]:
                match.pick_enemy(champ_to_pick)
            else:
                match.pick_ally(champ_to_pick)
