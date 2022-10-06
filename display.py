class Display():

    def __init__(self):
        self.__visual = [' ___ ','/   \\','\   /',' \ / ','  o  ',' /|\ ',' / \ ','','^^^^^']

    def print_visual(self):
        if len(self.__visual) < 6:
            self.__visual[0] = '  x  '
            self.__visual.pop(len(self.__visual)-2)
        for item in self.__visual:
            print(item)

    def update_visual(self):
        self.__visual.pop(0)

    