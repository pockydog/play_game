import random


class Pocky:
    POKER_TYPE = ['♠', '♥', '♣', '♦']
    POKER_KING = ['J', 'Q', 'K']
    POKER_NUM = 11
    POKER_TOTALLY = 52
    PEOPLE_MAX_LIMIT = 4
    PEOPLE_MIN_LIMIT = 1
    DIFFERENT_CASE = 3
    DEFAULT = '♣3'

    @classmethod
    def create_poker(cls):
        types = Pocky.POKER_TYPE
        numbers = Pocky.POKER_NUM
        king = Pocky.POKER_KING
        poker_list = list()
        for n in range(1, numbers):
            for t in types:
                num = t + str(n)
                poker_list.append(num)
        for t in types:
            for k in king:
                king_type = t + k
                poker_list.append(king_type)
        return poker_list

    @classmethod
    def verify_pocker(cls, my_poker):
        check_poker = set(my_poker)
        if len(check_poker) != Pocky.POKER_TOTALLY:
            raise Exception('Missing card')
        else:
            return True

    @classmethod
    def start_shuffle(cls, player):
        Pokers = Pocky.create_poker()
        if player > Pocky.PEOPLE_MAX_LIMIT or player <= Pocky.PEOPLE_MIN_LIMIT:
            raise Exception('cannot over four players or less two players')
        check = Pocky.verify_pocker(Pokers)
        random.shuffle(Pokers)
        num = len(Pokers) // player
        play = [Pokers[pocker:pocker + num] for pocker in range(0, len(Pokers), num)]
        print(f' {player} player.')
        if player == Pocky.DIFFERENT_CASE:
            for p in play:
                if Pocky.DEFAULT in p:
                    p.extend(play[-1])
                if len(p) < player:
                    play.pop()
                    return play
        return play

    # @classmethod
    # def play_rule(cls):




if __name__ == '__main__':
    print(Pocky.start_shuffle(player=3))



