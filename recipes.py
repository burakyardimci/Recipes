with open("polenta.txt","r") as file:
    liste=[]
    real_liste=[]
    for line in file:
        lines=line.strip()
        lines=lines.split(";")
        liste.append(lines)
    a=0
    for karakter in range(len(liste)-3):
        if a==0:
            a+=1
            real_liste.append(f"{liste[0]:}")
        elif a==1:
            real_liste.append(f"Ingredient name: {liste[karakter][0]}, needed ingredient{liste[karakter][1]} grams.")
    real_liste.append(f"{liste[-2]:}")
    real_liste.append(f"{liste[-1]}")



with open("foods.txt","r") as food:
    semi=[]
    for element in food:
        elemen=element.strip()
        elem=elemen.split(";")
        i=0
        my_list=[]
        for x in range(len(elem)):
            if i==0:
                my_list.append(str(elem[i]))
            elif i==1:
                my_list.append(float(elem[i]))
            elif i==2:
                my_list.append(int(elem[i]))
            i+=1
        semi.append(my_list)

    a=0
    ingridients=[]
    for malzeme in liste:
        for sey in malzeme:
            if sey==semi[a][0]:
                ingridients.append(f"{sey}-{malzeme[1]}")
                a+=1
    prices=[]

    for p in range(len(ingridients)):
        a=1000/int(ingridients[p][-3:])
        prices.append((semi[p][1])/a)

    total=0
    for r in prices:
        total+=float(r)


    kaloriler=[]
    for l in range(len(ingridients)):
        kaloriler.append((semi[l][2])/a)

    x=sum(kaloriler)
def main():
    for y in real_liste:
        print(y)
    print("ingridients:")
    for k in ingridients:
        print(k)
    print(f"number of ingridients: {len(ingridients)}")
    print(f"receipe cost: {total}")
    print(f"receipe calories: {x} ")

main()
