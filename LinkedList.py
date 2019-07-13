class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Node:
    def __init__(self,data,tail=None,head=None):
        self.data = data
        self.tail = tail
        self.head = head
class List:
    def __init__(self):
        self.node = None
        self.EndP = None
    def AddToLastForcefully(self,data):
        if self.node == None:
            self.node = Node(data)
            self.EndP = self.node
        else:
            self.EndP.tail = Node(data)
            temp = self.EndP.tail
            self.EndP = temp
    def AddToLast(self,data):
        if self.EndP != None:
            self.EndP.tail = Node(data)
            temp = self.EndP.tail
            self.EndP = temp
        else:
            print(bcolors.WARNING+"Warning: "+bcolors.ENDC+"Woah! Your List is Empty There's Nothing to Add With \nPlease Try To add Something First Using: "+bcolors.BOLD+bcolors.OKBLUE+"AddToStart(<YourData>)"+bcolors.ENDC+" or "+bcolors.BOLD+bcolors.OKBLUE+"AddToLastForcefully(<YourData>)"+bcolors.ENDC)
    def AddToStart(self,data):
        temp = self.node
        self.node = Node(data)
        self.node.tail = temp
    def Show(self):
        temp = self.node
        while(temp != None):
            print(temp.data)
            temp = temp.tail

obj = List()
obj.AddToLastForcefully(10)
obj.Show()