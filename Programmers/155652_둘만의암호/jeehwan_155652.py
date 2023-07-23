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
        count = 0
        while index > 0:
            targetIndex = ord(target) + count

            # skip 처리
            if alphas[chr(targetIndex)]:
                count += 1
                continue
            count += 1
            index -= 1
    answer = ''
    return

def solution(s, skip, index):
    atoz = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for i in skip:
        atoz.remove(i)

    ans = ''
    for i in s:
        # 인덱스로 해도 되는 건, 알파벳은 각각이 고유해, 중복될일이 없다.
        # 모듈러 연산을 통해서, 다시 돌아가는 것 구현 => 그 해당의 배열 만큼 돌려야 다시 돌아오겟지?!
        ans += atoz[(atoz.index(i)+index)%len(atoz)]

    return ans


#런타임 에러
def solution(s, skip, index):
    answer = ''

    alphas = {'a': False, 'b': False, 'c': False, 'd': False, 'e': False,
              'f': False, 'g': False, 'h': False, 'i': False, 'j': False,
              'k': False, 'l': False, 'm': False, 'n': False, 'o': False,
              'p': False, 'q': False, 'r': False, 's': False, 't': False,
              'u': False, 'v': False, 'w': False, 'x': False, 'y': False,
              'z': False}

    # skip 처리
    for skiptarget in skip:
        alphas[skiptarget] = True

    # mainProcess
    for target in s:

        count = 0
        targetIndex = 0
        cnt = 0

        while cnt < index:

            targetIndex = ord(target) + count

            # skip 처리
            if alphas[chr(targetIndex)]:
                count += 1
                continue

            # z 넘어가는 경우 처리
            if targetIndex >= ord('z'):
                targetIndex = ord(target) + count - 26

            cnt += 1
            count += 1

        answer += (chr(targetIndex + 1))

    return answer