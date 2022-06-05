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
c_m=0
f_m=0
cb_m=0
p_m=0
monday_arr = np.array([egg, butter, chicken, cheese, broccoli, bacon, avocado])
for element in monday_arr:
	c_m += element[0]
	f_m += element[1]
	cb_m += element[2]
	p_m += element[3]
print('cal_monday: ' + str(c_m))
print('fat_monday: ' + str(f_m))
print('carbs_monday: ' + str(cb_m))
print('protein_monday: ' + str(p_m))
print('=============================')

#Tuesday: 2 egg, ,avocado, vegetables, salmon, olive_oil, mix_nuts, smoothie
c_t=0
f_t=0
cb_t=0
p_t=0

tuesday_arr = np.array([ egg, avocado, salmon, olive_oil, mix_nuts, smoothie])
for element in tuesday_arr:
	c_t += element[0]
	f_t += element[1]
	cb_t += element[2]
	p_t += element[3]
print('cal_tuesday: ' + str(c_t))
print('fat_tuesday: ' + str(f_t))
print('carbs_tuesday: ' + str(cb_t))
print('protein_tuesday: ' + str(p_t))
print('=============================')

#Wednesday: Vegetable, 2 eggs, cheese, salad + 2 eggs, turkey, avocado, salmon) 
c_w=0
f_w=0
cb_w=0
p_w=0
wednesday_arr = np.array([smoothie, salad_heavy, salmon])
for element in monday_arr:
	c_w += element[0]
	f_w += element[1]
	cb_w += element[2]
	p_w += element[3]
print('cal_wed: ' + str(c_w))
print('fat_wed: ' + str(f_w))
print('carbs_wed: ' + str(cb_w))
print('protein_wed: ' + str(p_w))
print('=============================')

#Thursday:  chia_pudding, butter, beef, celery, shake, avocado, turkey
c_th=0
f_th=0
cb_th=0
p_th=0
thursday_arr = np.array([chia_pudding, butter, beef, shake, turkey, avocado])
for element in thursday_arr:
	c_th += element[0]
	f_th += element[1]
	cb_th += element[2]
	p_th += element[3]
print('cal_thursday: ' + str(c_th))
print('fat_thursday: ' + str(f_th))
print('carbs_thursday: ' + str(cb_th))
print('protein_thursday: ' + str(p_th))
print('=============================')
#Friday: smoothie, salmon, mushroom, salad,
c_f=0
f_f=0
cb_f=0
p_f=0

friday_arr = np.array([smoothie, salmon, salad_heavy])

for element in friday_arr:
	c_f += element[0]
	f_f += element[1]
	cb_f += element[2]
	p_f += element[3]
print('cal_friday: ' + str(c_f))
print('fat_friday: ' + str(f_f))
print('carbs_friday: ' + str(cb_f))
print('protein_friday: ' + str(p_f))
print('=============================')
#saturday: mushroom, 2 eggs, tuna, chicken, broccoli, 
c_s=0
f_s=0
cb_s=0
p_s=0

saturday_arr = np.array([egg, tuna, cauli_rice, chicken, broccoli, shake])

for element in saturday_arr:
	c_s += element[0]
	f_s += element[1]
	cb_s += element[2]
	p_s += element[3]
print('cal_saturday: ' + str(c_s))
print('fat_saturday: ' + str(f_s))
print('carbs_saturday: ' + str(cb_s))
print('protein_saturday: ' + str(p_s))
print('=============================')
#sunday: cauliflower, bunless salmon burger, mearballs, zuchini noodles, cheese 
c_sun=0
f_sun=0
cb_sun=0
p_sun=0

sunday_arr = np.array([egg, salad_heavy, cauli_rice, chicken, smoothie])
for element in sunday_arr:
	c_sun += element[0]
	f_sun += element[1]
	cb_sun += element[2]
	p_sun += element[3]
print('cal_sunday: ' + str(c_sun))
print('fat_sunday: ' + str(f_sun))
print('carbs_sunday: ' + str(cb_sun))
print('protein_sunday: ' + str(p_sun))
print('=============================')


	

		