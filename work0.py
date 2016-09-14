#!/usr/bin/python
import random

# Nicole Cheng & Brandon Huang
# softdev pd9
# 091316
# work0

CLASSES =  {                                                                                                                                                                                                                                
    4: [ 'Ayman', 'Shaeq', 'Patrick', 'Yvonne', 'Wilson', 'Brian', 'Farhan', \
         'Janet', 'Harry', 'Kevin', 'Nicholas', 'Jason', 'Yikai', 'Emma', \
         'Kenneth', 'Nala', 'Karol', 'Elias', 'Ely', 'Reo', 'Dhiraj', 'Amy', \
         'Arvind', 'Nobel', 'Angela', 'Edward', 'Jonathan', 'Celine', 'Daniel',\
         'Lindsey', 'Ziyan', 'Elina'],                                                                                                                                                             
    8: ['Julian', 'Sebastian', 'Jordan', 'Alan', 'Yuki', 'Chloe', 'Noah', \
        'Edvic', 'Jia Qi', 'Shan', 'Rodda', 'Anya', 'Edmond', 'Asher', 'Kathy', \
        'Sharon', 'Vncent', 'Lawrence', 'Sachal', 'Gabriel', 'Jason', 'Daniel', \
        'Felix', 'Jacob', 'Bayle', 'Fortune', 'Gio', 'Kelly', 'William', 'Jordan',\
        'Haley', 'Henry'],                                                                                                                                                                
    9: ['James', 'Vanna', 'Zicheng', 'Quinn', 'Anthony C', 'Joel', 'Steph', \
        'Xinhui', 'Richard', 'Misha', 'Maddie', 'Winston', 'Shariar', 'Nancy', \
        'Jerry', 'Michael', 'Stiven', 'Will',  'Olivia', 'Constantine', 'Jessica',\
        'Kate', 'Shamaul', 'Max', 'Sarah', 'Anthony L', 'Brandon', 'Nicole', \
        'Brian', 'Issac', 'Seiji', 'Lorenz']                                                                                                                                                
} ## 32 per class

def printRandom(x):
    m = random.randint(0,31)
    if x == 4:
        print CLASSES[4][m]
    elif x == 8:
        print CLASSES[8][m]
    elif x == 9:
        print CLASSES[9][m]

'''
print "Period 4:"
printRandom(4)
print "\nPeriod 8:"
printRandom(8)
print "\nPeriod 9:"
printRandom(9)
print "\nPeriod 4:"
printRandom(4)
print "\nPeriod 8:"
printRandom(8)
print "\nPeriod 9:"
printRandom(9)
'''
