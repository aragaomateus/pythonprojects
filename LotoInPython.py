import random

''' function that gets the data from a file and turns it into a dictinarie with the 
key as the number and the values as the frequnecy that it appears in the file. 
'''
def getDataNumbers():
    numbers = []
    #Open the file
    
    with open("winner.txt") as fp:
        #Iterate through each line
        for line in fp:
            numbers.extend( #Append the list of numbers to the result array
                [int(item) #Convert each number to an integer
                for item in line.split() #Split each line of whitespace
                ])
    print(numbers)
    # initializing dict to store frequency of each element
    elements_count = {}
    # iterating over the elements for frequency
    for element in numbers:
    # checking whether it is in the dict or not
        if element in elements_count:
            # incerementing the count by 1
            elements_count[element] += 1
        else:
            # setting the count to 1
            elements_count[element] = 1
    # printing the elements frequencies
    return elements_count

def frequencyPrinter(numbers_n_frequency, desired_frequency,amoun_of_lines):
    count = 0
    best_in_frequency = []
    for i in sorted (numbers_n_frequency) : 
        lista = list(numbers_n_frequency.values())
        lista2 = [ float(x) for x in lista ]
        if lista[i] > desired_frequency:
            best_in_frequency.append(i)
            print (i , lista[i] , "percentage : {:.2f}".format((lista2[i] / amoun_of_lines) * 100.0))
            count+=1
    print(".....................")
    print(count)
    print(".....................")
    return best_in_frequency

def printTwentyRandom(best_in_frequency):
    chosen = []
    while len(chosen) < 20:
        num = random.choice(best_in_frequency)
        if num not in chosen:
            chosen.append(num)
    chosen.sort()
    print(' '.join(map (str,chosen)))
    print(best_in_frequency)


def main():
    logic = True
    while logic:
        amoun_of_lines = int (input("Type the amount of lines: "))
        numbers_n_frequency = getDataNumbers()
        desired_frequency = int (input("Frequency: "))
        best_in_frequency = frequencyPrinter(numbers_n_frequency, desired_frequency,amoun_of_lines)
        printTwentyRandom(best_in_frequency)
        option = input("type -1 to leave or any key to continue:")
        int (option)
        if option == -1:
            logic = False
        else:
            logic = True
 


main()
