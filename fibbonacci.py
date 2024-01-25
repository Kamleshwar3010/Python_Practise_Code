first_term=0
last_term=1
for i in range(10):
    print(first_term,end=",")
    next=first_term+last_term
    first_term=last_term
    last_term=next
