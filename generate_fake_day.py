import numpy as np
from numpy import random

def generate_fake_day():
    people_number=10
    result = np.zeros(2*people_number)
    ya_entraron = 0
    for i in range(2*people_number):
        parcial = np.sum(result)
        assert parcial >=0
        new_value = 0

        if (parcial <=0): #Si ya salieron todos los que entraron
            result[i] = 1
            ya_entraron+=1
            continue

        if (ya_entraron >= people_number): #Si ya entraron todos los que queria
            result[i] = -1
            continue
        
        new_value = random.choice([-1,1])
        if (new_value == 1):
            ya_entraron+=1
        result[i] = new_value

    assert np.sum(result) == 0
    assert result[0] == 1
    assert result[(2*people_number)-1] == -1
    print(result)
    return result