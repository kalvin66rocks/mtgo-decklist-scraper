# -*- coding: utf-8 -*-

from pathlib import Path


class MtgoDecklistScraperPipeline(object):
    def open_spider(self, spider):
        output_path = Path.cwd().joinpath('outputs', spider.identifier + '.tsv')
        if output_path.exists():
            output_path.unlink()

        self.__f = output_path.open('w')
        # self.__write_row(['event                    ', 'deck_id', 'player', 'is_sideboard', 'number', 'card_name', 'card_type'])

    def process_item(self, item, spider):
        row = [
                str(item['deck_id']), item['player']
        ]
        self.__write_row(row)
        row = [
                'Main Deck'
        ]
        self.__write_row(row)
        for c in item['mainboard'].card_list:
            row = [
                str(c.number), c.name
            ]
            self.__write_row(row)

        row = [
                'Sideboard'
        ]
        self.__write_row(row)

        for c in item['sideboard'].card_list:
            row = [
                str(c.number), c.name
            ]
            self.__write_row(row)

        row = [
                ' '
        ]
        self.__write_row(row)

        return item

    def close_spider(self, spider):
        self.__f.close()

    def __write_row(self, row: list):
        self.__f.write('\t'.join(row) + '\n')
