
class Player(object):
    def __init__(self,name,mark,number):
        self.name = name
        self.gender= mark
        self.number = number
    

    def getname(self):
        return self.name
        
    def __str__(self):
        return 'name : {} , player number : {}'.format(self.name,self.number)
    