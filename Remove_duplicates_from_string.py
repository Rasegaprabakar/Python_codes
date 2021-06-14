#program to remove duplicate characters of the string      Input : mississippi   Output:misp

def removeduplicates():
    string=input()
    t=[]
    for i in string:
        if i in t:
            pass 
        else:
            t.append(i)
    for i in t:
        print(i,end="")



if __name__ =='__main__':
    removeduplicates()