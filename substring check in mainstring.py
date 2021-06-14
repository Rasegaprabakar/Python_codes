# program to check whether given sub-string present in the main string

def substringfunction():
    main_string = input()
    sub_string = input()
    if sub_string in main_string:
        print("Substring is present in main string")
    else:
        print("Substring is not present in main string")


if __name__ =='__main__':
    substringfunction()