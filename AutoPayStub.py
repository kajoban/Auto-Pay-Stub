#Kajoban Kuhaparan
#AutoPayStub Version 1.1
#2017-07-25

from graphics import * #Allows use of GUI

def main(): #Houses both major functions which process the file and create the GUI
    n = raw_input("Please enter the name of the input file: ")
    wage = input("Please enter your hourly wage: ") 
    TBT,TAT,WW,diff = processFile(n)
    minutes,hours = time(wage,TBT)
    outputGUI(TBT,TAT,WW,diff,minutes,hours)
    

def processFile(n): #This function processes the file 
    infile = open(n,'r') 

    w = [] #array for weeks
    bt = [] #array for weekly pay before tax
    at = [] #array for weekly pay after tax

    for line in infile: #This loop reads the file line by line and sorts the info in each line to their respected array
        currentline = line.split("\t") 
        w.append(currentline[0].strip()) 
        bt.append(float(currentline[1])) 
        at.append(float(currentline[2]))

    

    infile.close() #the file reader is closed 

    TBT = beforetax(bt) #total before tax is obtained using the before tax array
    TAT = aftertax(at) #total after tax is obtained using the after tax array
    WW = weeksworked(w) #total weeks worked is obtained using the weeks array
    diff = difference(TAT,TBT) #difference is calculated using both totals 

    return TBT,TAT,WW,diff

def beforetax(bt): #calculates the total pay before taxes
    TBT = 0
    for i in range(len(bt)):
        TBT += bt[i]
    return TBT

def aftertax(at): #calculates the total pay after taxes
    TAT = 0
    for i in range(len(at)):
        TAT += at[i]
    return TAT

def weeksworked(w): #calculated the total weeks worked 
    WW = len(w)
    return WW

def difference(TAT,TBT): #calculates the amount of tax paid
    diff = TBT - TAT
    return diff

def outputGUI(TBT,TAT,WW,diff,minutes,hours): #creates the GUI which displays all relavent information 
    W = GraphWin("Automatic Paystub Checker",1000,400)
    W.setBackground("lightgreen")
    sentence1 = Text(Point(500,130),("Before Tax = $"+str(TBT)))
    sentence2 = Text(Point(500,200),("After Tax = $"+str(TAT)))
    sentence3 = Text(Point(500,60),("Weeks Worked = "+str(WW)))
    sentence4 = Text(Point(500,270),("Lost by Tax = $"+str(diff)))
    sentence5 = Text(Point(500,340),("Time Worked = "+str(hours)+" hours & "+str(minutes)+" minutes"))
    sentence1.setSize(25)
    sentence2.setSize(25)
    sentence3.setSize(25)
    sentence4.setSize(25)
    sentence5.setSize(25)
    sentence1.setTextColor("white")
    sentence2.setTextColor("white")
    sentence3.setTextColor("white")
    sentence4.setTextColor("white")
    sentence5.setTextColor("white")
    sentence1.draw(W)
    sentence2.draw(W)
    sentence3.draw(W)
    sentence4.draw(W)
    sentence5.draw(W)   
    W.getMouse()
    W.close()

def time(wage,TBT):#calculates hours worked based on wage
    hoursworked = float("{0:.2f}".format((TBT/wage)))
    minutes = int(((hoursworked * 60)%60))
    hours = int(hoursworked)
    return minutes,hours 
                
        
main() #runs program

'''
VERSIONS:

1.0: intial release, includes total before tax, total after tax, weeks worked and tax deduction.
1.1: added time worked

'''
