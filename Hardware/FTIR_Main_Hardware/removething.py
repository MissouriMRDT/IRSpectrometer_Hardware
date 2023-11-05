import re

#xmin = 6.346
#ymin = 2.448
#xmax = 6.348
#ymax = 2.450

xmin = 6.1940
ymin = 2.4200
xmax = 6.1960
ymax = 2.4220

with open("FTIR_Main_Hardware.kicad_pcb", "r") as file:
    lines = file.readlines()
    for line in lines:
        tokens = re.split(r"[)(\s]+", line)
        #print(*tokens, sep=" || ")
        for token in tokens:
            try:
                number = float(token)
                #print('candidate:', number)
                if xmin < number < xmax:
                    print("x:", number)
                if ymin < number < ymax:
                    print("y:", number)
            except Exception as e:
                #print(type(e))
                pass
print("done")

