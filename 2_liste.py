#générateur de phrases

from random import shuffle


word_list = input("Entrez votre liste de mot : ")
tab=word_list.split("/")
print(tab)


#new_tab=shuffle(tab)

#print(new_tab)


if len(tab)<5:
    print("les deux premiers mots de la liste sont : {} et {}".format(tab[0],tab[1]))
else:
    print("les trois derniers mots sont : {}, {} et {}".format(tab[len(tab)-3],tab[len(tab)-2],tab[len(tab)-1]))
