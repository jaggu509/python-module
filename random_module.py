import random


c=random.choice([ 2, "jo", 3.45, [2,3,4], (3,4,5), {4,5,3,3,}, {3:2} ])         #chosses a random element form list given input of any datatype

c=random.randint(1,100)                                                         #returns a random integer including the boundaries 

c=random.random()                                                               #returns a float between 0 and 1

c=random.sample(['red', 'red', 'red', 'green', 'blue', 'blue'], k=5)            #returns list of k elements randomely choosed from given sample 

random.shuffle(list_input)                                                      #shuffles the list in-place taking a list of elements as inputs and returns NONE 

c=random.uniform(1.00,2.5)                                                      #returns a random float in the range [a, b) or [a, b] depending on rounding.
