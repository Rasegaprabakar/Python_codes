# program to merge characters of 2 strings into a single string by  taking characters alternatively.   Input : S1= "ravi" S2="teja" output: rtaevjia


def merge_of_string():
    list_string =[]
    string1= input()
    string2 = input()
    length1 = len(string1)
    length2=len(string2)
    if(length1>length2):
        for i in range(0,length1):
            if(i<length2):
                list_string.append(string1[i])
                list_string.append(string2[i])
            else:
                list_string.append(string1[i])
    else:
        for i in range(0,length2):
            if(i<length1):
                list_string.append(string1[i])
                list_string.append(string2[i])
            else:
                list_string.append(string2[i])

    print(list_string)

if __name__ == '__main__':
    merge_of_string()