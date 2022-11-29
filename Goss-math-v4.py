###################################### Equations' creation part ######################################
def creation(nbrVar):
    toutes_equations = []
    simple_equation = []
    for i in range (nbrVar):

        for a in range(nbrVar+1):
            if a == nbrVar:
                coef = round(float(input("Entree la résultat de l'équation : ")),2)
            else:
                coef = round(float(input("Entree le coefficient de la variable : ")),2)
            simple_equation.append(coef)
        
        toutes_equations.insert(i, simple_equation)
        simple_equation = []

    print("Voici les équations que vous avez entrées :")
    return(toutes_equations)
###################################### Arrangement part ######################################
def arrangement(toutes_equations):
    #print("Entré dans arrangement")
    for m in range(nbrVar):
        nbrZero = 0
        if(toutes_equations[m][m]==0):
            for n in range(1,nbrVar-m+1):
                #if(m == nbrVar-1):
                    #toutes_equations.insert(0,toutes_equations[m])
                    #del toutes_equations[-1]
                    #nbrZero -= 1
                    #break
                nbrZero +=1
                if(nbrZero==nbrVar-m):
                    print("Pivot manquant!")
                    affichage(toutes_equations)
                    return(True)
                    
                toutes_equations.insert(m,toutes_equations[m+n])
                del toutes_equations[m+n+1]

                if(toutes_equations[m][m]!=0):
                    break
        else:
            nbrZero -= 1

    print("Voici la matrice arrangée de vos équations (aucun pivot ayant 0 comme valeur) :")
    return(toutes_equations)
###################################### Goss part ######################################
def goss(matrice_sup):
    equation_simplifiee = []
    recommence = True
    while recommence:
        recommence = False
        for j in range(nbrVar-1):
            if recommence:
                break
            for i in range(1,nbrVar-j):
                if matrice_sup[j][j] == 0:
                    print("Un zero semble être à la position d'un pivot")
                    affichage(matrice_sup)
                    matrice_sup = arrangement(matrice_sup)
                    recommence = True
                    if type(matrice_sup) == bool:
                        return(True)
                multiplicateur = matrice_sup[j+i][j]/matrice_sup[j][j]

                #print(multiplicateur)

                for element1, element2 in zip(matrice_sup[j], matrice_sup[j+i]):
                    reduit = element2 - multiplicateur * element1
                    equation_simplifiee.append(reduit)

                #print(equation_simplifiee)
                matrice_sup[j+i] = equation_simplifiee
                #print(toutes_equations)
                equation_simplifiee = []
                if matrice_sup[j+i][j+i] == 0:
                    print("Un zero semble être à la position d'un pivot")
                    affichage(matrice_sup)
                    matrice_sup = arrangement(matrice_sup)
                    recommence = True
                    if type(matrice_sup) == bool:
                        return(True)

    print("Voici la matrice supérieure de vos équations :")
    return (matrice_sup)
###################################### Find the answer part ######################################
def awnser(matrice_sup):
    reponse = [0*a for a in range(nbrVar)]
    #toutes_equations[nbrVar-1][nbrVar-1]

    for i in range (-1, -1-nbrVar, -1):
        for j in range(-1, -1-nbrVar, -1):

            if j == i:
                reponse[i] = matrice_sup[i][-1]/matrice_sup[i][j-1]
                break

            else:
                matrice_sup[i][-1] = matrice_sup[i][-1] - reponse[j]*matrice_sup[i][j-1]
                matrice_sup[i][j-1] = 0
    return(reponse)
###################################### Print anwsers ######################################
#print(reponse)
def show(reponse):
    print("Voici le(s) réponse(S): ", end='')
    for d in range(nbrVar):
        print(f"x{d+1}:",reponse[d],", ", end='')
    print("")
#print(matrice_sup)
###################################### Affichage ######################################
def affichage(matrice):
    for a in range(len(matrice)):
            print(matrice[a])
    return()

nbrVar = int(input("Entrer le nombre de variables dans l'équation linéaire : "))

equations = creation(nbrVar)
affichage(equations)

equation_arrange = arrangement(equations)
if type(equation_arrange) == bool:
    pass
else:
    affichage(equation_arrange)

    matrice_simple = goss(equation_arrange)
    if type(matrice_simple) == bool:
        pass

    else:
        affichage(matrice_simple)

        reponse = awnser(matrice_simple)
        show(reponse)
