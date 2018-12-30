try:
    y = 2+1
except EnvironmentError:
    print(1)
else:
    print(2)


scores = {'Dha': [10,20], 'koh': [100,200],'roh':[]}

try:
    scores['roh'].append([50, 0])
except KeyError:
    scores['roh'] = [50, 0]
else:
    print("completed gracefully")

print(scores)


