data:str
count:int =0
with open('tp0/data/online_inventaire_prevert.txt', 'r') as input_file:
    data = input_file.read()
    liste_phrases = data.split(';')
with open('tp0/data/resultats.txt', 'w') as output_file:
    for phrase in liste_phrases:
        if phrase == "":
            continue
        if count <10:
            output_file.write(" 0"+str(count)+" "+str(phrase)+"\n")
        else:
            output_file.write(" "+str(count)+" "+str(phrase)+"\n")
        count+=1