def cmpfunction (element1, element2):
    if element1["id"] == element2["id"]:
        return 0
    elif element1["id"] < element2["id"]:
        return -1
    else:
        return 1

class Comparation:
    def __init__(self, tag='id'):
        self.tag = tag

    def upVal(self, element1, element2):
        if float(element1[self.tag]) > float(element2[self.tag]):
            return True
        return False

    def downVal(self, element1, element2):
        if float(element1[self.tag]) < float(element2[self.tag]):
            return True
        return False