age=input("Quel âge avez-vous ? ")
if int(age) < 18:
    prix = 7
    print("Prix : "+str(prix)+"€")
else:
    prix = 12
    print("Prix: "+str(prix)+"€")

pop_corn = input("Voulez vous des pop-corns ? (o/n)")

new_prix = (prix,prix+5)[pop_corn=="o"] #condition ternaire

print ("Cela vous fera : {} €".format(new_prix))