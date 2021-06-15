"""
4)Given the participants' score sheet for your University Sports Day. you are required to find the runner-up score.
             You are given n scores. Store them in a list and find the score of the runner-up.
            Input Format: The first line contains n . The second line contains an array A[] of n integers each separated by a space.
            Constraints : 2≤n≤5
                                     -100≤A[i]≤100
            Output Format : Print the runner-up score.
            Sample Input : 5
                                          2 3 6 6 5
             Sample Output : 5

"""

def findingrunnerup():
    score_list =[]
    score_set = {}
    final_list = []
    number_of_participants=int(input())
    for i in range(0,number_of_participants):
        list_value=input()
        score_list.append(list_value)
    score_set=set(score_list)
    final_list = list(score_set)
    #print(final_list)
    final_list.sort()
    #print(final_list)
    print(final_list[-2])
        



if __name__ == '__main__':
    findingrunnerup()
