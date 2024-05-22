#    ___________________________________________________
#   |    10        9            8             7         \
#   |                                                   \
#   |                                                6  \
#   |                                                   \
#   |   11        ___            ___                    \
#   |            |   \          |   \                   \
#   |            |   \          |   \ 5                 \
#   |            |   \ 12     13|   \                 3 \
#   |            |   \          |   \                   \
#   |         14 |   \          |   \      4            \
#   |            |   \          |   \----------\      2 \
#   |   15       -----          ---------------|        \
#   |                                                   \
#   |                                                 1 \
#   |                                                   \
#   |                                                   \
#   |           ----        ----        ----            \
#   |         exit                          | entrance  \
#
#1-3 = ovoce a zelelnina
#4-5 = pečivo
#6-8 = maso
#9-10 = mléčné výrobky
#11-15 = sladkosti

seznam = ["Banány","sýr","chleba","čokoláda", "mléko", "jahoda"]
seznam = [x.lower() for x in seznam]



# individual products sorted into subsections
ovoceZelenina = ["banány", "okurky", "jablka"]
pecivo =        ["rohlik", "chleba", "housky"]
maso =          ["šunka", "klobása", "kuřecí prso"]
mlecneVyrobky = ["sýr", "mléko", "máslo"]
sladkosti =     ["čokoláda", "bonbóny", "zmrzlina"]
# store subsections
poradiVObchode = [ovoceZelenina, pecivo, maso, mlecneVyrobky, sladkosti]



#working variables
allProducts=[]
seznamPos=[]
unavailable=[]

# function turning list into workable isle numbers / product positions
def sort(seznam):
        for x in poradiVObchode:
            for y in x:
                allProducts.append(y)
                #print(allProducts) #for debugging
        for z in seznam:
            #print(allProducts.index(z)) #for debugging
            try:
                 seznamPos.append(allProducts.index(z))
            except:
                unavailable.append(z)
                break

        #print(seznamPos)
        #print(seznam)
        seznamPos.sort(reverse=False)
        #print(seznamPos)
        #for loop to write text for every new number in seznamPos to make a human readable list
        for i in seznamPos:
            print (allProducts[i], " - ", i)
        for i in unavailable:
            print(i, " - ", "not available")

sort(seznam)