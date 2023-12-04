import random 
import time 

NUMBER_OF_ELEMENTS = 10000

lst = list(range(NUMBER_OF_ELEMENTS))
random.shuffle(lst)


s = set(lst)


startTime = time.time()
for i in range(NUMBER_OF_ELEMENTS):
  i in s
endTime = time.time()
runTime = int((endTime - startTime) * 1000)
print("To test if", NUMBER_OF_ELEMENTS, 
"elements are in the set\n", "The runtime is", runTime, "milliseconds"
)

startTime = time.time()
for i in range(NUMBER_OF_ELEMENTS): 
  i in lst
endTime = time.time()
runTime