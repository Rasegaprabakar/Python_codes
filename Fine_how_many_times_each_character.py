#program how many times  each character present in string

def countthecharacters():
    value=input()
    d = {}
    for i in value:
        key1 = i
        data1 = value.count(i)
        d[key1]=data1
    print(d)
        
    

if __name__ =='__main__':
    countthecharacters()