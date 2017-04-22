def timedifference(time_str):
    time_str=str(time_str)
    h, m,s = time_str.split(':')
    return int(h) * 60 + int(m)