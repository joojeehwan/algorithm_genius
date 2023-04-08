def solution(fees, records):
    answer = []
    baseTime = fees[0]
    baseFee = fees[1]
    chargeTime = fees[2]
    chargeFee = fees[3]
    jangbu = dict()
    timedict = dict()
    for record in records:
        timestamp, platenum, IO = record.split()
        if IO == 'IN':
            jangbu[platenum] = timestamp
        else:
            iH, iM = map(int, jangbu[platenum].split(':'))
            oH, oM = map(int, timestamp.split(':'))
            chargeMins = 60*(oH - iH) + (oM - iM)
            if platenum in timedict:
                timedict[platenum] += chargeMins
            else:
                timedict[platenum] = chargeMins
            del jangbu[platenum]
    if any(jangbu):
        for leftover in jangbu:
            iH, iM = map(int, jangbu[leftover].split(':'))
            oH = 23
            oM = 59
            chargeMins = 60*(oH - iH) + (oM - iM)
            if leftover in timedict:
                timedict[leftover] += chargeMins
            else:
                timedict[leftover] = chargeMins
    plateL = [keys for keys in timedict]
    plateL.sort()
    for plate in plateL:
        Time = timedict[plate]
        fee = baseFee
        Time -= baseTime
        if Time > 0:
            chargeTick = Time // chargeTime
            if Time % chargeTime:
                chargeTick += 1
            fee += chargeTick * chargeFee
        answer.append(fee)
    return answer