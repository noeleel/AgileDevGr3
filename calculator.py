# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 08:41:53 2018

@author: lucas
"""


#==============================================================================
# INPUT
#==============================================================================

user_mass = 70  #kg
fat_per = 6/100  #percentage of fat of the user

activity_factor = 1 #detailed in the lines below
# A : for daily activities and 30 min walk / day : <1.40    
# B : A + ~60 min of small activities (ex. walk at 5-7 km/h) : 1.40-1.60  
# C : A + >60 min of small activities, or 30-60 min intensive activities : 1.60-1.90 
# D : A + >60min of intensive activities : 1.90-2.50

user_mass_objective = 77 #in kg. the mass that the user want to have



#==============================================================================
# FUNCTION
#==============================================================================


def calculator(user_mass, fat_per, activity_factor, user_mass_objective):
    """calcul the energy, glucide, proteine and lipide needed.
    
    INPUT : user's mass (kg), user's percentage of fat, user's activity factor, user's mass objective (kg)
    OUTPUT : Energy (cal), glucide (g), proteine (g), lipide (g) needed by the user
    """
    ### nutritional basis ###     -> percentage of each types of element to be healthy 
    glu_basis = 50/100  #glucides
    pro_basis = 30/100 #proteines
    lip_basis = 20/100  #lipides
    
    ### calculus ###
    user_mass_without_fat = user_mass*(1-fat_per)   #in kg
    TMB = 370+21.6*user_mass_without_fat  # cal.  Obscurus quantity used for metabolism calculus
    daily_E_spent = TMB*activity_factor
    mass_ratio = (user_mass_objective-user_mass)/user_mass*100  #percentage of gain or loss of mass
    E_needed = 50*mass_ratio+daily_E_spent    #in cal, the energy the user needs to eat
    glu_objective = glu_basis*E_needed/4   #quantity of glucide needed in g
    pro_objective = pro_basis*E_needed/4   #quantity of proteine needed in g
    lip_objective = lip_basis*E_needed/9   #quantity of lipide needed in g
    
    return E_needed, glu_objective, pro_objective, lip_objective



#==============================================================================
# TEST OF THE FUNCTION
#==============================================================================


goal = calculator(user_mass,fat_per,activity_factor,user_mass_objective)
E_goal = goal[0]
glu_goal = goal[1]
pro_goal = goal[2]
lip_goal = goal[3]

print("Quantity of calorie to absorb : ", E_goal, "\n")
print("Quantity of glucide to absorb : ", glu_goal, "\n")
print("Quantity of proteine to absorb : ", pro_goal, "\n")
print("Quantity of lipide to absorb : ", lip_goal, "\n")




