# Fibonacci seguence in 8 lines. 
numbers = []
for i in range(99):
    if i < 2:
        numbers.insert(0,0)
        numbers.insert(1,1)
    else:
        numbers.insert(i, numbers[i-1] + numbers[i-2])
print (numbers)
