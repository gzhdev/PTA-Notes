sample_cm=eval(input())
foot=sample_cm // 30.48
inch=int(((sample_cm / 30.48) - foot) * 12)
print("%d %d"%(foot,inch))  