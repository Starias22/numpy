import numpy as np
#nd array of 50 items from 1 to 15 with 15 inside
arr=np.linspace(start=1,stop=20)
print(arr)

#nd array of 15 items from 1 to 20 with 20 inside
arr=np.linspace(1,stop=20,num=15)
print(arr)

#nd array of 15 items from 1 to 20 with 20 outside
arr=np.linspace(start=1,stop=20,num=5,endpoint=False)
print(arr)