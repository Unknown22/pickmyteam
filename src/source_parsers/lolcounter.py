import requests
from lxml import html
from models.counter_champion import CounterChamp


class LoLCounterParser:

    def __init__(self):
        pass

    def get_counters_for_champ(self, champion: str) -> dict:
        path = self._create_path_weak_against(champion)
        page = requests.get(path)
        tree = html.fromstring(page.content)
        counters = []

        names = tree.xpath('//div[@class="name"]/text()')[1:]
        up_votes = tree.xpath('//div[@class="uvote tag_green"]/text()')
        down_votes = tree.xpath('//div[@class="dvote tag_red"]/text()')

        for counter_id in range(len(names)):
            counters.append(CounterChamp(names[counter_id],
                                         float(up_votes[counter_id].replace(',', '.')),
                                         float(down_votes[counter_id].replace(',', '.'))))
        return counters

    def get_what_it_counters(self, champion: str) -> dict:
        path = self._create_path_strong_against(champion)
        page = requests.get(path)
        tree = html.fromstring(page.content)
        counter_for = []

        names = tree.xpath('//div[@class="name"]/text()')[1:]
        up_votes = tree.xpath('//div[@class="uvote tag_green"]/text()')
        down_votes = tree.xpath('//div[@class="dvote tag_red"]/text()')

        for countered_id in range(len(names)):
            counter_for.append(CounterChamp(names[countered_id],
                                            float(up_votes[countered_id].replace(',', '')),
                                            float(down_votes[countered_id].replace(',', ''))))
        return counter_for

    def _create_path_weak_against(self, champion: str) -> str:
        return 'http://lolcounter.com/champions/' + champion + '/weak'

    def _create_path_strong_against(self, champion: str) -> str:
        return 'http://lolcounter.com/champions/' + champion + '/strong'
