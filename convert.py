# !/usr/bin/python
from collections import Counter
import forgi.graph.bulge_graph as cgb


# INPUT:: Path to RNAfold file
input = 'RNAfold/Dataset_B.fasta'

# OUTPUT:: List of structures
output = 'structures/Dataset_B.txt'

dotlist = []
structurelist = []

# Speichert die Dot-Bracket Strukturen in eine Liste
with open(input, 'r') as f:
    for count, line in enumerate(f, start=1):
        if count % 3 == 0:
            line = line.split(" ")[0]
            dotlist.append(line)

# Konvertiert Dot-Bracket zu Element-String Strukturen
for structures in dotlist:
    bg = cgb.BulgeGraph.from_dotbracket(structures)
    elementstring = bg.to_element_string()
    important = elementstring[40:49]
    structurelist.append(important)

# Schreibt den Output
outF = open(output, "w")
for line in structurelist:
  outF.write(line)
  outF.write("\n")
outF.close()
