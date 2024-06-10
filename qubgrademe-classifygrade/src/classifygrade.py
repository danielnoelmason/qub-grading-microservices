def classifygrade(score):    
    if score > 100 or score < 0:
        return 'Invalid Grade'
    elif score >= 80:
        return 'Distinction'
    elif score >= 70:
        return 'Commendation'
    elif score >= 60:
        return 'Pass'
    elif score >= 50:
        return 'Fail'
    elif score >= 40:
        return 'Marginal Fail'
    else:
        return 'Low Fail'

def averagemark(*marks):
    totalScore = 0
    for mark in marks:
        print(mark)
        totalScore+= mark
    score = totalScore/len(marks)
    return score

def checkValidMark(*marks):
    for mark in marks:
        if mark >100 or mark <0:
            return False
    return True