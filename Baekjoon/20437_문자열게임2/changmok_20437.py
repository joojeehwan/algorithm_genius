for t in range(int(input())):
    w = input().rstrip()
    k = int(input())

    chars = [0] * 26

    for c in w:
        chars[ord(c)-97] += 1

    pcs = []
    for i in range(26):
        if chars[i] >= k:
            pcs.append(chr(i+97))
    
    if not pcs:
        print(-1)
    else:
        coords = {}
        for pc in pcs:
            coords[pc] = []
        
        shr = -1
        lng = -1
        for i in range(len(w)):
            if w[i] in coords:
                coords[w[i]].append(i)
        
        for coordList in coords.values():
            l = 0
            r = k - 1
            lnth = coordList[r] - coordList[l] + 1
            if shr == -1:
                shr = lnth
            else:
                shr = min(shr, lnth)
            if lng == -1:
                lng = lnth
            else:
                lng = max(lng, lnth)
            while r < len(coordList)-1:
                r += 1
                l += 1
                lnth = coordList[r] - coordList[l] + 1
                shr = min(shr, lnth)
                lng = max(lng, lnth)

        print(shr, lng)