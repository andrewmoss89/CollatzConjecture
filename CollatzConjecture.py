import numpy as np
import datetime

#Request & Print Input
maxNumInput = input("\nPlease enter a maximum number of iterations for the calculation: ")
maxNum = int(maxNumInput)
if maxNum <= 0: 
    maxNum = 100 #default
print("The maximum number selected (N.B. default is 100 if 0 or less is entered) = ", maxNum)

#Start Timer
start_time = datetime.datetime.now()

#Pre-set array sizes
maxArraySize = 2000 #assumed sequence will never exceed 2000 steps in sequence 

answerArray = np.ones((maxArraySize, maxNum))
initialArray = (list(range(1,maxNum+1)))
lengthArray = np.ones((1,maxNum))
answerArray[0,0:maxNum] = answerArray[0,0:maxNum] * initialArray

#The Collatz Conjecture Calculation
# 1) Choose a whole number greater than 0
# 2) If the number is even divide by 2
# 3) If the number is odd then multiply by 3 and add 1
# 4) Repeat from Step 2 until end point reached (i.e. where output = 1 and sequence enters '4, 2, 1' loop).

evenCalc = lambda a, b : (a / b)
oddCalc = lambda c, d, e : (c * d) + e
for id in range(maxNum):
    i=answerArray[0,id]
    n=1;
    while i != 1:
        temp = answerArray[n-1,id]
        if (temp % 2) == 0:
            answerArray[n,id] = evenCalc(temp, 2)
            i=answerArray[n,id]
            n=n+1
        else:
            answerArray[n,id] = oddCalc(temp, 3, 1)  
            i=answerArray[n,id]
            n=n+1
    lengthArray[0,id] = n
    answerArray[n:maxArraySize,id] = np.NaN

#Calculate Length and values in longest sequence
longestArray = np.where(lengthArray[0,:] == np.amax(lengthArray))
a = ~np.isnan(answerArray[0:(maxArraySize),:])
a = a[:,longestArray[0]]
b = answerArray[:,longestArray[0]]

#Stop Timer
end_time = datetime.datetime.now()

#Print Output
print("\n\nFor", maxNum, "iterations,",int(longestArray[0]+1),"is the number that creates the longest sequence.")
print("\n\nThe Array is shown here: ",  list(b[a[:,0],0]))
print("\n\nThis array has", len(b[a[:,0],0]) , "numbers in the sequence.")
print("\n\nThe time taken for this calculation was:",end_time - start_time, "\n\n")

