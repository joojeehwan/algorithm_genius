from collections import defaultdict


# def isSkip(targetIndex) :

#     print(chr(targetIndex + 97), alphas[chr(targetIndex + 97)])
#     if not alphas[chr(targetIndex + 97)]:
#         return True
#     return False

def solution(s, skip, index):
    alphas = {'a': False, 'b': False, 'c': False, 'd': False, 'e': False,
              'f': False, 'g': False, 'h': False, 'i': False, 'j': False, 'k': False, 'l': False, 'm': False,
              'n': False, 'o': False,
              'p': False, 'q': False, 'r': False, 's': False, 't': False, 'u': False, 'v': False, 'w': False,
              'x': False, 'y': False,
              'z': False}

    targetIndex = 0

    # skip 처리
    for skiptarget in skip:
        alphas[skiptarget] = True

    # mainProcess
    for target in s:

        count = 1
        while (count <= index):

            targetIndex = ord(target) + count

            # skip 처리
            # print(chr(targetIndex + 97))
            if alphas[chr(targetIndex)]:
                continue

            # #z 넘어가는 경우 처리
            # if targetIndex > ord('z') - 97:
            #     targetIndex = ord(target) - 97 + count -26

            count += 1
            # print(chr(targetIndex))

    #         if targetIndex > ord('z'):
    #             targetIndex = ord(target) + 5 - ord('z') + 96
    #         print(chr(targetIndex))

    answer = ''
    return answer


from collections import defaultdict


def solution(s, skip, index):
    alphas = {'a': False, 'b': False, 'c': False, 'd': False, 'e': False,
              'f': False, 'g': False, 'h': False, 'i': False, 'j': False, 'k': False, 'l': False, 'm': False,
              'n': False, 'o': False,
              'p': False, 'q': False, 'r': False, 's': False, 't': False, 'u': False, 'v': False, 'w': False,
              'x': False, 'y': False,
              'z': False}

    targetIndex = 0

    # skip 처리
    for skiptarget in skip:
        alphas[skiptarget] = True

    # mainProcess
    for target in s:

        count = 1
        test = 1
        while (test <= index):
            targetIndex = ord(target) + count

            # skip 처리
            if alphas[chr(targetIndex)]:
                count += 1
                continue

            count += 1
            test += 1

    answer = ''
    return answer