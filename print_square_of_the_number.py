"""
2) Read an integer N . For all non-negative integers i<N , print i². See the sample for details.
            Input Format :The first and only line contains the integer,N .
            Constraints : 1≤N≤20
            Output Format : Print N lines, one corresponding to each i .
                                                                                                               Sample Input  : 5
                                                                                                               Sample Output : 0  
1
4
9
16


"""

def printsquare():
    n = int(input())
    for i in range(0,n):
        print(i*i)
    


if __name__ == '__main__':
    printsquare()
