# simple keto information guide and meal prep helper 
#top keto friendly food and their caloric information: 

import math
import numpy as np

#format [calories, fat(gram), carb (g), protein (g)
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

egg_cal = egg[0]

#total array of all food types: 
array = np.array([egg, butter, beef, chicken, cheese, broccoli, olive_oil, salmon, bacon, avocado, mix_nuts])
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

#Monday: 2 eggs, butter, chicken, bacon, avocado