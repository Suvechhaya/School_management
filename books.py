class Books:
    def __init__(self, idd, name, author):
        self.idd = idd
        self.name = name
        self.author = author
        
    def getId(self):
        return self.idd
    
    def getName(self):
        return self.name
    making random edits
    def getAuthor(self):
        return self.author

book = []
n = int(input("how many book details? "))

for i in range(n):
    a = input("ENter id of book")
    b = input("Enter name of book: ")
    c = input("Enter author naame of the book: ")
    stud = Books(a, b, c)
    book.append(stud)

disp = map(lambda stud: stud.getId() + " " + stud.getName() + " " + stud.getAuthor(), Books)
print(list(disp))
