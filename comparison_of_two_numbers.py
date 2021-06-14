#Read 2 no's and compare the numbers whether 1st number is equal/greater/smaller  to 2nd number using Ternary operator

def compare():
    a,b = input().split()
    print("A is greater than B") if a > b else ( print("A is smaller than B") if a <b  else print("A and B are equal"))

if __name__ =='__main__':
    compare()
