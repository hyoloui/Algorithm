str = input()
result = []

upp = str.upper()
low = str.lower()

for idx, val in enumerate(str):
    uppStr = upp[idx]
    lowStr = low[idx]
    if uppStr == val : result.append(lowStr)
    else : result.append(uppStr)
    
print(''.join(result))