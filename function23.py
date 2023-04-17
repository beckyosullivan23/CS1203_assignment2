import random
#Q2: return a list of the town names

def list_towns():
    t=open('assignment_2.txt','r')

    town_names = t.readlines()

    for i in range(len(town_names)):
        town_names[i] = town_names[i].strip('\n')
    return(town_names)

#Q3:
def random_names(n):
    rt_towns= (random.sample(list_towns(), k=n))
    return(rt_towns)

