class Conver:

    def __init__(self, index):
        self.mdy = index.split("/")
        self.mm = int(self.mdy[0])
        self.dd = int(self.mdy[1])
        self.yy = int(self.mdy[2])
