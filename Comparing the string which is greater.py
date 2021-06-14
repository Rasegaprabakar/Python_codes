# program to check given two strings are equal or not  if not  which is smaller and bigger


def stringcompare():
    string1=input()
    string2=input()
    if(string1==string2):
        print("Both strings are equal")
    else:
        if(string1>string2):
            print("string1 is greater than string2")
        else:
            print("String2 is greater than string1")


if __name__ == '__main__':
    stringcompare()