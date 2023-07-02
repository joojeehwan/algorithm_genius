
def solution(cards1, cards2, goal):

    n1 = len(cards1)
    n2 = len(cards2)

    i, j = 0, 0

    for target in goal:

        #if target == cards1[i] and i < n1  :
        if i < n1 and target == cards1[i] :
            i += 1

        #elif target == cards2[j] and j < n2:
        elif j < n2 and target == cards2[j] :
            j += 1

        else:
            return "No"

    return "Yes"




def solution(cards1, cards2, goal):
    for target in goal:
        if len(cards1) > 0 and target == cards1[0]:
            cards1.pop(0)
        elif len(cards2) > 0 and target == cards2[0]:
            cards2.pop(0)
        else:
            return "No"
    return "Yes"


from collections import deque

def solution(cards1, cards2, goal):
    card1_q = deque(list(cards1))
    card2_q = deque(list(cards2))

    for target in goal:
        if card1_q and card1_q[0] == target:
            card1_q.popleft()
        elif card2_q and card2_q[0] == target:
            card2_q.popleft()
        else:
            return "No"

    return "Yes"