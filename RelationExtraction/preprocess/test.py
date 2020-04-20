line = '谷类'
line = line.strip().replace('「','').replace('」','').split()
print(len(line))
if line == '':
    print("True")
print(line)
