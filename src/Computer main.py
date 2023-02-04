from matplotlib import pyplot
import serial

numx = []
numy = []
good = [False, False]

kp = input("what is the value of kp? ")
endpos = input("what is the final position? ")

with serial.serial("COM3",115200) as file:

    file.write("start\n")
    file.write(f"{kp}\n")
    file.write(f"{endpos}\n")
    
    while not(file.any()):
        pass
    titlestr = file.readline()
    titlesep = titlestr.split(",")
    titlex = titlesep[0]
    titley = titlesep[1]
    
    for line in file:
        str = line
        sep = str.split(",")

        try:
            sep[0] = sep[0].strip()
            sep[0] = sep[0].strip(" #Aabcdefghijklmnopqrstuvwxyz ")
            x = float(sep[0])  
        except ValueError:
            good[0] = False
        except IndexError:
            good[0] = False
        else:
            good[0] = True
            
        try:
            sep[1] = sep[1].strip()
            strip = sep[1].strip(" #Aabcdefghijklmnopqrstuvwxyz ")
            y = float(strip)
        except ValueError:
            good[1] = False
        except IndexError:
            good[1] = False
        else:
            good[1] = True

        if good == [True,True]:
            numx.append(x)
            numy.append(y)
        elif good == [False,True]:
            print(f"bad string {sep[0]}")
        elif good == [True,False]:
            print(f"bad string {sep[1]}")
        else:
            print(f"both strings bad {sep}")

            
titley = titley.strip()
pyplot.plot(numx,numy)
pyplot.xlabel(titlex)
pyplot.ylabel(titley)
pyplot.show()