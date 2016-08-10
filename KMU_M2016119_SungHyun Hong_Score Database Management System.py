from tkinter import *

## Data Base Module ##
class Score:
    def __init__(self):
        self.List = []
        self.numbering = len(self.List)

    def isNum(self, number):
        try:
            int(number)
            return True
        except ValueError:
            return False

    def searchname(self, named):
        for tupl in self.List:
            if(tupl[1] == named):
                return False
        return True

    def searchnum(self, numbered):
        for tupl in self.List:
            if(int(tupl[0]) == int(numbered)):
                return self.List.index(tupl)
        return -1
        
    def add(self, naming, scoring):
        if(self.searchname(naming)):
            self.numbering += 1
            T = (self.numbering, naming, scoring)
            self.List.insert(len(self.List), T)
            return True
        else:
            return False
        
    def remove(self, numbering):
        if(not(self.isNum(numbering))):
            return -2
  
        isThere = self.searchnum(numbering)
        if(isThere > -1):
            self.List.pop(isThere)
            return 1
        else:
            return -1

    def store(self):
        string = ""
        for tupl in self.List:
            string += str(tupl[0]) + "   " + str(tupl[1]) + "   " + str(tupl[2]) + "\n"
        return string[0:len(string) - 1]

    def load(self, string):
        self.numbering = 0
        del self.List[:]
        text = string.split("\n")
        for i in range(0, len(text)):
            token = text[i].split("   ")
            T = (token[0], token[1], token[2])
            self.List.insert(len(self.List), T)
            self.numbering += 1

    def numorder(self):
        self.List.sort(key = lambda x : int(x[0]))

    def nameorder(self):
        self.List.sort(key = lambda x : x[1].lower())
        
    def downorder(self):
        self.List.sort(key = lambda x : float(x[2]), reverse = True)

    def uporder(self):
        self.List.sort(key = lambda x : float(x[2]))
        

## Interface Module ##
s = Score()

def adding():
    naming = name.get()
    scoring = score.get()
    possible = s.add(naming, scoring)
    
    if(possible):
        data.delete(0.0, END)
        data.insert(END, s.store())
        status.delete(0.0, END)
        status.insert(END, "추가 성공!!!")
    else:
        status.delete(0.0, END)
        status.insert(END, "추가 실패... 동일한 이름 존재.")
        
def removing():
    numbering = number.get()
    success = s.remove(numbering)

    if(success >= 0):
        data.delete(0.0, END)
        data.insert(END, s.store())
        status.delete(0.0, END)
        status.insert(END, "삭제 성공!!!")
    elif(success == -1):
        status.delete(0.0, END)
        status.insert(END, "삭제 실패... 데이터가 존재하지 않음.")
    elif(success == -2):
        status.delete(0.0, END)
        status.insert(END, "삭제 실패... 잘못된 번호 입력.")

def storing():
    filename = file1.get()
    try:
        f = open(filename + ".txt", 'w')
    except ValueError:
        status.delete(0.0, END)
        status.insert(END, "저장 실패...")
        file1.delete(0, len(filename))
    else:
        string = s.store()
        f.write(string)
        f.close()
        status.delete(0.0, END)
        status.insert(END, "저장 성공!!!. <파일이름 : " + filename + ".txt>")
        file1.delete(0, len(filename))

def loading():
    filename = file2.get()
    try:
        f = open(filename + ".txt")
    except FileNotFoundError:
        status.delete(0.0, END)
        status.insert(END, "로드 실패... 파일이 존재하지 않음.")
        file2.delete(0, len(filename))
    else:
        string = f.read()
        s.load(string)
        f.close()
        status.delete(0.0, END)
        status.insert(END, "로드 성공!!!. <파일이름 : " + filename + ".txt>")
        file2.delete(0, len(filename))
        data.delete(0.0, END)
        data.insert(END, s.store())
    
    
def numordering():
    status.delete(0.0, END)
    s.numorder()
    data.delete(0.0, END)
    data.insert(END, s.show())
    
def nameordering():
    status.delete(0.0, END)
    s.nameorder()
    data.delete(0.0, END)
    data.insert(END, s.show())
    
def downordering():
    status.delete(0.0, END)
    s.downorder()
    data.delete(0.0, END)
    data.insert(END, s.show())

def upordering():
    status.delete(0.0, END)
    s.uporder()
    data.delete(0.0, END)
    data.insert(END, s.show())

## Visual Interface ##
window = Tk()
window.title("Score Database Management")

Label(window, text = "이름: ").grid(row = 0, column = 0, sticky = W)
name = Entry(window, width = 20, bg = "light green")
name.grid(row = 0, column = 1, columnspan = 6, sticky = W)
type(name)

Label(window, text = "점수:  ").grid(row = 0, column = 7, sticky = E)
score = Entry(window, width = 7, bg = "light green")
score.grid(row = 0, column = 8, sticky = W)
type(score)

Label(window, text = "번호:  ").grid(row = 1, column = 7, sticky = E)
number = Entry(window, width = 5, bg = "light green")
number.grid(row = 1, column = 8, sticky = W)
type(number)

Label(window, text = "파일이름:  ").grid(row = 2, column = 7, sticky = E)
file1 = Entry(window, width = 20, bg = "light blue")
file1.grid(row = 2, column = 8, columnspan = 6, sticky = W)
type(file1)

Label(window, text = "파일이름:  ").grid(row = 3, column = 7, sticky = E)
file2 = Entry(window, width = 20, bg = "light blue")
file2.grid(row = 3, column = 8, columnspan = 6, sticky = W)
type(file2)

Button(window, text = "추가", width = 5, command = adding).grid(row = 0, column = 14, sticky = E)
Button(window, text = "삭제", width = 5, command = removing).grid(row = 1, column = 14, sticky = E)
Button(window, text = "저장", width = 5, command = storing).grid(row = 2, column = 14, sticky = E)
Button(window, text = "열기", width = 5, command = loading).grid(row = 3, column = 14, sticky = E)

Button(window, text = "번호순", width = 5, command = numordering).grid(row = 4, column = 1, sticky = W)
Button(window, text = "이름순", width = 5, command = nameordering).grid(row = 4, column = 2, sticky = W)
Button(window, text = "점수내림차순", width = 15, command = downordering).grid(row = 4, column = 3, columnspan = 3, sticky = W)
Button(window, text = "점수오름차순", width = 15, command = upordering).grid(row = 4, column = 6, columnspan = 3, sticky = W)

data = Text(window, width = 75, height = 10, wrap = WORD, background = "#FFFFBB")
data.grid(row = 5, column = 0, columnspan = 15, sticky = W)

status = Text(window, width = 75, height = 1, wrap = WORD, background = "#FFBBBB")
status.grid(row = 6, column = 0, columnspan = 15, sticky = W)


