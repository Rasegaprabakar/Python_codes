# program to print characters at the odd positions first followed by even position characters    Input: SOFTWARE   Output:OTAESFWR  (with and without slice operator)

def with_out_slice():
    list_string =[]
    data= input()
    length = len(data)
    for i in range(1,length,2):
        list_string.append(data[i])
    for i in range(0,length,2):
        list_string.append(data[i])
    
    for i in range(0,length):
        print(list_string[i],end="")

if __name__ == '__main__':
    with_out_slice()