''' Question No. 10 (Practise set-3)'''

# Method-1 (Using Pre-Define Method)
li=input("Enter Element in list followed by backspace-\t").split(",")

for i in range(len(li)):
        li[i]=int(li[i])
frequency = {}
for i in li:
    frequency.update({i: li.count(i)})
print(frequency)

# Method-2
count = 1
di = {}

for i in range(len(li)):
    for j in range(i+1, len(li)):
        if li[i] == li[j]:
            count = count+1
    if li[i] not in di:
        di.update({li[i]: count})
    count = 1

print(di)
