#Read 3 numbers and print max value using ternary operator . (don’t use pre defined functions)
def maxofthreenumber():
    a,b,c = input().split()
    maxnumber = a if a > b and a > c else ( b if b > c else c)
    print("The maximum among the three number is" ,maxnumber)
    

if __name__ == '__main__':
    maxofthreenumber()
