import random  #importer la librairie random
import string

def convertLetters(text) :
    for caractere in text :
        if caractere not in string.ascii_letters :
            text = text.replace(caractere,"")
    return text.upper()            #le .upper() permet de transformer en majuscule les lettres minuscules s'il yen a dans text


def mix() :
    chaine= ""
    for i in random.sample(range(len(string.ascii_uppercase)), len(string.ascii_uppercase)):   #string.ascii_uppercase = liste lettres majuscules donc len(string.ascii_uppercase) = 26
        chaine += string.ascii_uppercase[i]                                                    #random.sample(liste,n) donne n valeur aleatoire differente contenue dans 'liste'
    return chaine


def createCylinder(file,n) :
    fichier = open(file, "w")    #remplacer w par a si on veut pas ecraser les données du fichier a chaque ecriture
    for i in range(n) :
        fichier.write(mix()+'\n')
    fichier.close()


def loadCylinder(file) :
    données = {}
    fichier = open(file, "r")
    for ligneno, ligne in enumerate(fichier) :
        données[ligneno+1] = ligne.rstrip('\n\r')
    fichier.close()
    return données

def keyOK(key,n) :
    test = True                        #attention True avec T au debut et sans crochet pour qu'il soit boolean sinon c'est une chaine de caractere
    if key is None :                   #si la liste key est None c'est a dire n'existe pas ou non créé
        test = False
    else :
        for i in range(1,n+1) :
            if i not in key :
                test = False           #attention False avec F au debut et sans crochet pour qu'il soit boolean sinon c'est une chaine de caractere
    return test                        #ajouter "and len(key) == n" si c'est obligatoire d'avoir les deux tailles egales car ya un exemple du prod ou l'on a un texte de 35 lettres et une key de 36 nombres

def createKey(n) :
    return random.sample(range(1,n+1), n)

def find(letter,alphabet) :
    for i in range(len(alphabet)) :
        if alphabet[i] == letter :
            return i

def shift(i) :
    return (i+6)%26

def cipherLetter(letter,alphabet) :
    return alphabet[shift(find(letter,alphabet))]

def cipherText(cylinder,key,text) :
    i = 0
    chaine = ""
    if keyOK(key,len(cylinder)) : #verifier si la clé est valide par rapport au cylindre cad sil contient toutes les clés du dictionnaire cylinder
        for lettre in convertLetters(text) : #pour chaque lettre du resultat de la conversion de text (j'ai rajouté text.upper() dans la fonction convertLetters(text) au cas ou ya des miniscules)
            chaine += cipherLetter(lettre,cylinder[key[i]])
            i += 1
        return chaine
    else :
        return "clé invalide"


#idée cipherText : on pouvait creer un autre dictionnaire ou on range les mix du cylinder selon l'ordre du key et ensuite travailler avec ce dictionnaire, d'ailleurs ce sera fait dans la partie graphique
#mais comme on a trouvé plus simple ... et aussi avec la programmation on travaille sur les indices donc on peut sauter l'etape du rangement des disques comme sur wikipedia
#explication : key[i] donne l'element numero i qui est un entier de la liste key, on commence par 0
#cylinder[key[i]] donne la valeur(qui est un mix) de la clé key[i] du dictionnaire cylinder
#cipherLetter(lettre,cylinder[key[i]]) donne le 6eme caractere du mix apres lettre
#on continue pour chaque element de key, on trouve sa valeur correspondante dans le dictionnaire cylinder sachant que 1ere lettre du text sera recherché dans la valeur
#de la premiere clé du key, 2eme lettre dans la valeur de la 2eme clé du key ainsi de suite
#apres on fait une somme de toutes les lettres trouvées dans chaine pour avoir le text chiffré


#DECHIFFREMENT
def un_shift(i) :
    return (i-6)%26

def un_cipherLetter(letter,alphabet) :
    return alphabet[un_shift(find(letter,alphabet))]

def un_cipherText(cylinder,key,text) :
    i = 0
    chaine = ""
    if keyOK(key,len(cylinder)) : #verifier si la clé est valide par rapport au cylindre cad sil contient toutes les clés du dictionnaire cylinder
        for lettre in convertLetters(text) : #pour chaque lettre du resultat de la conversion de text (j'ai rajouté text.upper() dans la fonction convertLetters(text) au cas ou ya des miniscules)
            chaine += un_cipherLetter(lettre,cylinder[key[i]])
            i += 1
        return chaine
    else :
        return "clé invalide"


#PARTIE TEST( on peut le prendre comme choix)
print()
text = "a.ùBn56%lnDER:Ci"            #on a fait en sorte que la taille du texte apres conversion va etre egale a 10
createCylinder("data.txt",len(convertLetters(text)))        #le fichier data.txt aura alors un cylindre avec 10 disques que l'on pourra utiliser apres
cylinder = loadCylinder("data.txt")
key = createKey(len(convertLetters(text)))   #ou key = createKey(len(cylinder)) c'est la meme chose
print(cylinder)
print(text,convertLetters(text),key,cipherText(cylinder,key,text))
print()
print( cipherText(cylinder,key,text) , key , un_cipherText(cylinder, key , cipherText(cylinder,key,text)) )
print()

exemple = mix()
print(exemple, find("X",exemple) , shift(find("X",exemple)) , cipherLetter("X",exemple))


#Utilisation de ces procédures et fonctions :
cylinder2 = {1: 'UQALDHSFZVOWCIGKMBPTYRJEXN', 2: 'KARWEJHGTMUCSVPFLXDZBIOYNQ', 3: 'KUJTSVWRFHMICAQELBYNPDZOGX', 4: 'DOHBQGULRIFVPEANSZCTWJYMKX', 5: 'UQBGRSMFPZKNJCTLVIOHWAXEYD', 6: 'QWECJLYGHOPASDKXMRBUNVTZIF', 7: 'QTRCPLHUAKMOESNJYWXIFBDVGZ', 8: 'CKEDMWJHLTNVUYXGZOIABQRSPF', 9: 'EWZOPCSBYAVQIHDUJLGMFXNKRT', 10: 'KSHRTJPUXBDVYIEWGNOFLAMCZQ', 11: 'NSZJVOYQRBWAMPXUTEIFLKDHCG', 12: 'FGNKXVYCORJLDABIQPEMHTSUWZ', 13: 'LOJSICTGVXDZHWKNQBAEMRFYUP', 14: 'DMYGQWOTLCRAPVJSUKNXFZHIEB', 15: 'PGADVKYCRJXONULWISZQMHTBFE', 16: 'ESQMDCAKHBWIOLRXNUPYFGZJVT', 17: 'IUGCJHPMRTXWEKSQZFBANDYLVO', 18: 'CJIZAPKEBRQWODLHSMFUVXTNYG', 19: 'CWSHZQNKBIXULORFMTEPADGYJV', 20: 'MBHXEVTAPSCOWZGIKDYLQRFUNJ', 21: 'QBNAYEKJLVRFIMXUOSZDGWHCPT', 22: 'HEGRYLWDKAOSPNFJVCIMZUTBXQ', 23: 'FVPXIWGMLKCHETYJSZADQBRUON', 24: 'QVLNDOXGUJTFMEBIYWRSPCKHAZ', 25: 'TMYBLCSWAINXJROHDZVQEPFUGK', 26: 'THREXDWOPJYKUVLFIZGSQNACMB', 27: 'DHUXWIKLVENMASOGJQBPFYTRZC', 28: 'IPFUALGRKZJOSCQTDWYBHMNXVE', 29: 'LBFVMSTGPJQAXUWCIOYNDHZKER', 30: 'NYASWVXBJTQHFRKDGLOECMIZPU', 31: 'GCOILBMZWYHVEPJFSDTRQNUKAX', 32: 'VJFZSIREYKLMCUOTHNWBAPXGDQ', 33: 'LQNEAXWTVDUZCIJMSHKBFPOYGR', 34: 'YBUECWOAKDZJXRILMNGQPSTHVF', 35: 'NHFSDTKBUCAQJILWGVYEMOXRPZ', 36: 'ADRIEUPJWNCKOSGZLTMXBFQHVY'}
print()
text = "GRMYSGBOAAMQGDPEYVWLDFDQQQZXXVMSZFS"
cylinder = loadCylinder("MP-1ARI.txt")          #cylinder va etre un dictionnaire
key = [12, 16, 29, 6, 33, 9, 22, 15, 20, 3, 1, 30, 32, 36, 19, 10, 35, 27, 25, 26, 2, 18, 31, 14, 34, 17, 23, 7, 8, 21, 4, 13, 11, 24, 28, 5]
print(cylinder)
print(text,convertLetters(text),key,cipherText(cylinder,key,text))
print()
print( cipherText(cylinder,key,text) , key , un_cipherText(cylinder, key , cipherText(cylinder,key,text)) )
print()


print("*** FIN TEST JeffersonShell ***")


print(type("↑"))
