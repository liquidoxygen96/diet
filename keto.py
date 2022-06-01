# simple keto information guide and meal prep helper 
#top keto friendly food and their caloric information: 

import math
import numpy as np

#format 	[calories, fat(gram), carb (g), protein (g)
egg =       [78, 5, 1, 6] # 1 egg
butter =    [102, 12, 0, 0] # 1 teaspoon 
beef =      [291, 22, 0, 24] # 100 grams
chicken =   [239, 14, 0, 27]	# 100 grams 
cheese =    [105, 9, 1, 5] # 1 oz
broccoli =  [34, 0, 7, 3] # 100 grams
olive_oil = [119, 14, 0, 0] # 1 tablespoon
salmon =    [182, 8, 0, 25] # 100 grams, Atlantic
bacon =     [43, 4, 0, 4] # 1 slice, cooked
avocado =   [160, 15, 9, 5] # 100 grams 
mix_nuts =  [190, 10, 26, 2]
shake = 	[150, 0, 0, 37]
smoothie =  [330, 26, 9, 12]
tuna =      [120, 1, 0, 30]
yogurt = 	[100, 0, 7, 15]
turkey =    [30, 1, 1, 6] # 1 slice 
cauli_rice =[37, 0, 5, 2]
pork_chops =[130, 4, 1, 23]
salad_heavy = 	[400 ,24 , 6, 35] #avocado, bacon, cheese, greens, chicken, egg
chia_pudding = [ 230, 15, 5, 8]




#total array of all food types: 
array = np.array([egg, butter, beef, chicken, cheese, broccoli, olive_oil, salmon, bacon, avocado, mix_nuts, shake, smoothie, tuna, yogurt, turkey, cauli_rice, pork_chops, salad_heavy, chia_pudding])
c=0
f=0
cb=0
p=0

for element in array:
  c  +=  element[0]
  f  +=  element[1]
  cb +=  element[2]
  p  +=  element[3]
print('calories: ' + str(c))
print('fat: ' + str(f))
print('carbs: ' + str(cb))
print('protein: '+ str(p))

# total intake based on my personal weight and diet goals 
total_calories_needed = 2000 #kcal
total_protein_needed = 110 #grams
total_carbs_needed = 24 #grams
total_fat_needed = 157 #grams



# TODO: Create an array of food lists for each day! this can be unique to your taste and will incorporate different weight of food intake 

#Monday: 2 eggs, butter, cheese, chicken, broccoli, bacon, avocado
monday_arr = np.array[egg, butter, chicken, cheese, broccolli, bacon, avocado]

#Tuesday: 2 egg, ,avocado, vegetables, salmon, olive_oil, mix_nuts, smoothie
tuesday_arr = np.array[ egg, avocado, salmon, olive_oil, mix_nits, smoothie]

#Wednesday: Vegetable, 2 eggs, cheese, salad + 2 eggs, turkey, avocado, salmon
wednesday_arr = np.array[smoothie, salad_heavy, salmon]

#Thursday:  chia_pudding, butter, beef, celery, shake, avocado, turkey
thursday_arr = np.array[ chia_pudding, butter, beef, shake, turkey, avocado]

#Friday: smoothie, salmon, mushroom, salad, 
friday_arr = np.array[smoothie, salmon, salad_heavy, 

#saturday: mushroom, 2 eggs, tuna, chicken, broccoli, 
saturday_arr = np.array[egg, tuna, cauli_rice, chicken, brocolli, shake]

#sunday: cauliflower, bunless salmon burger, mearballs, zuchini noodles, cheese 
sunday_arr = np.array[egg, salad_heavy, cauli_rice, chicken, smoothie]