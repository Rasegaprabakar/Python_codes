"""Given an integer,n, perform the following conditional actions:
            If n is odd, print Weird
            If n is even and in the inclusive range of  2 to 5, print Not Weird
            If n is even and in the inclusive range of 6 to 10 , print Weird
            If n is even and greater than 20 , print Not Weird
                Input Format : A single line containing a positive integer,n .
                Constraints : 1≤n≤100
                Output Format : Print Weird if the number is weird; otherwise, print Not Weird.
"""


def numbercheck():
    n = int(input())
    if(n%2!=0):
        print("Weird")
    elif(n%2 ==0 and n in range(2,6)):
        print("Not weird")
    elif(n%2 ==0 and n in range(6,11)):
        print("Not Weird")
    else:
        print("Not Weird")


if __name__ =="__main__":
    numbercheck()
