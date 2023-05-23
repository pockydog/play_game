import random


class Mahjong:
    DEFAULT_CH = {5: '中', 6: '發', 7: '白板', 8: '東', 9: '南', 10: '西', 11: '北'}
    DEFAULT_EN = ['條','筒', '萬']
    DEFAULT_FLOWERS = {137: '春🌹', 138: '2夏🌹', 139: '3秋🌹', 140: '4冬🌹', 141: '1梅🌹', 142: '2蘭🌹', 143: '3竹🌹',
                       144: '4菊🌹'}
    MIDDLE_LINE = 64
    LAST_LINE = 80
    CH_NUM = 28
    EN_NUM = 108
    Player = 4

    @classmethod
    def creat_card(cls):
        default_en = Mahjong.DEFAULT_EN
        default_ch = Mahjong.DEFAULT_CH
        default_flower = Mahjong.DEFAULT_FLOWERS

        EN_NUM = 4
        EN_NUMM = 109
        dict_ = dict()
        # 基本牌

        # for num in range(1, EN_NUMM):
        #     for n in range(1, 10):
        #         for four in EN_NUM:

        for n in range(1, 10):
            for i in range(0, 4):
                EN_NUM += 1
                a = {int(f'{EN_NUM}'): str(f'{n}{default_en[i]}')}
                print(a)
                        # default_flower.update(a)

        # 中發白
        # for i in DEFAULT_CH:
        #     for ii in range(0, 4):
        #         EN_NUMM += 1
        #         a = {int(f'{EN_NUMM}'): str(f'{DEFAULT_CH[i]}')}
        #         DEFAULT_FLOWERS.update(a)

        # print(default_flower)

        # return DEFAULT_FLOWERS

    @classmethod
    def random_dic(cls, dicts):
        dict_key_ls = list(dicts.keys())
        random.shuffle(dict_key_ls)
        new_dic = dict()
        for key in dict_key_ls:
            new_dic[key] = dicts.get(key)
        return new_dic

    @classmethod
    def verify_card(cls, card):
        if len(card) != 144:
            raise Exception('Card missing')
        else:
            return True

    @classmethod
    def start_shuffle(cls):
        first_cards = 16
        card_list = list()
        middle = Mahjong.MIDDLE_LINE
        last = Mahjong.LAST_LINE
        cards = Mahjong.creat_card()
        card = Mahjong.random_dic(cards)
        cards = list(card.items())
        card = cards[:Mahjong.MIDDLE_LINE]
        new_card = cards[Mahjong.MIDDLE_LINE:]  # 尚未處理
        player = len(card) // Mahjong.Player
        plays = [card[c:c + player] for c in range(0, len(card), player)]
        # for play in plays:
        #     for play_card in play:
        #         # print(play_card)
        #         print('----------')
                # print(Mahjong.DEFAULT_FLOWERS.keys())
                # if play_card in Mahjong.DEFAULT_FLOWERS.keys():
                #     print(new_card[:1])
                #     play.extend(new_card[:1])
                #     new_card.pop()
        print(Mahjong.DEFAULT_FLOWERS)


if __name__ == '__main__':
    # print(Mahjong.parse_flower())
    # print(Mahjong.start_shuffle())
    print(Mahjong.creat_card())
