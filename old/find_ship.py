class Battleship(object):

    def __init__(self, battleground):
        self.battleground = battleground

    def find_ship(self):
        # search vertically first
        _list = self.battleground

        skipped = False
        for index, value in enumerate(list):
            if not skipped:
                print(index)
                for index_2, value_2 in enumerate(list[index]):
                    if value_2 == 1:
                        a = [(index, index_2)]
                        if _list[index+1][index_2] == 1:
                            a.append((index+1, index_2))
                            a.append((index+2, index_2))
                            return a


list = [[0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 1],
        [0, 1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 0]]

instance = Battleship(list)
print(instance.find_ship())
