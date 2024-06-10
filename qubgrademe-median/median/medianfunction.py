def getMedianMark(*marks):
    n = len(marks)
    s = sorted(marks)
    return (s[n//2-1]/2.0+s[n//2]/2.0, s[n//2])[n % 2] if n else None