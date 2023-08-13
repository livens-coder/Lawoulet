import random
print("Pwogram sa ap pemet ou jwe woulet")
nomb_chwazi = random.randrange(0, 101) 
#print("Odinate chwazi yon nonb nan anteval 0 a 100 ki: ", nomb_chwazi)
print("***************************************************************************")

chans_rete = 5
eseye = 0

while chans_rete > 0:
    chwa_itilizate = float(input("Chwazi yon nomb: "))
    
    if chwa_itilizate < 0 or chwa_itilizate >= 100:
        print("Tanpri, chwazi yon nomb nan anteval 0 a 100 selman.")
        continue
    
    eseye += 1
    
    if chwa_itilizate < nomb_chwazi:
        print("Nonb ou chwazi a pi piti pase nonb pa odinate a.")
    elif chwa_itilizate > nomb_chwazi:
        print("Nonb ou chwazi a pi gwo pase nonb pa odinate a.")
       
    else:
        print("******************************************************************************")
        print("Ou genyen! Bravo!")
      
        break  
    
    chans_rete -= 1
    print("ou rete: ",chans_rete, " chans")
if chans_rete == 0:
    print("-----------------------------------------------------------------------------------------")
    print("Ou pedi! Not la se:", nomb_chwazi)
print("-----------------------------------------------------------------------------------------------")
