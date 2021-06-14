# program Input: a4b3c2 Output:aaaabbbcc   (characters followed by digits print characters those many number of times)

def printing():
    count=0
    list_value = []
    value=input()
    for i in range(0,(len(value)-1)):
        if(value[i] >='a' and value[i]<='z'):
            key = value[i]
            
        i=i+1
        if(value[i]>='0' and value[i]<='9'):
            data = value[i]
        
        for j in range(0,int(data)):
            list_value.append(key)
       
    print(list_value)
if __name__ == '__main__':
    printing()