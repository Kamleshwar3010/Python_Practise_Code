""" Question No. 3 (Practise set-3) """
super_hero = ["IronMan", "Thor", "BatMan", "SuperMan"]
# Method-1 # share differnt memory location
copy_list = super_hero.copy()
# Method-2 #share differnt memory location
copy_list_2 = super_hero[:]
# Method-3 #share same memory location
copy_list_3 = super_hero
super_hero.append("Hawk EYE")
# copy_list_2[0]="Hawk EYE" make change in copy_list_2 onlly not in original list
print("Orignal list - ", super_hero)
print("Copied list - ", copy_list)
print("Copied list 2- ", copy_list_2)
print('Copied list 3 "Assinging Value of orignal value to in this list"- ', copy_list_3)
