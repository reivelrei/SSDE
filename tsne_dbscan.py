# !/usr/bin/python
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
from sklearn.cluster import DBSCAN


# INPUT:: Path to RNAfold file
input = 'structures/Dataset_B.txt'
output_png = 'output/Dataset_B.png'
output_txt = 'output/Dataset_B_count.txt'

# Angabe der k-mer size, potentiell scalable, wenn gewollt
ksize = 3

# Liste mit allen k-meren
allKmers = []

# Anzahl verschiedener k-mere
count = 0

# kmerDict initialisieren, enthält alle k-mer Counts
kmerDict = {}

# Enthält alle Element-String Strukturen nach Einlese-Reihenfolge
allStructures = []


# Erstellt k-mere der Sequenz
def build_kmers(sequence, ksize):
    kmers = []
    n_kmers = len(sequence) - ksize + 1

    for i in range(n_kmers):
        kmer = sequence[i:i + ksize]
        kmers.append(kmer)

    return kmers


# Textfile öffnen, replacen von f und t mit e,
# Mitte Uppercase (noch hardcoded)
# Liste füllen mit allen vorhandenen k-meren
with open(input, 'r') as f:
    for line in f:
        if(line.find('f')):
            line = line.replace('f', 'e')
        if(line.find('t')):
            line = line.replace('t', 'e')
        newline = line[:4] + line[4].upper() + line[5:]
        newline = newline.strip()
        
        allStructures.append(newline)
        
        allKmers += build_kmers(newline, 3)


c = Counter(allKmers)  
   
# Füllt das kmerDict mit allen k-meren und setzt die values auf die gezählten Vorkommen
# Zählt, wie viele verschiedene k-mere es gibt
for key in c:
    kmerDict[key] = c[key]
    count += 1
    
    

"""
MOMENTAN AUSGESETZT, da die Plots nicht so viel Sinn ergeben haben, wie erwartet.

# Überschreibt spezielle k-mere mit den Vorkommen, die extra übergeben wurden
if "eee" in kmerDict:
    kmerDict["eee"] =1322198
if "ees" in kmerDict:    
    kmerDict["ees"] =144995
if "esh" in kmerDict:
    kmerDict["esh"] =74
if "esi" in kmerDict:
    kmerDict["esi"] =1308
if "esm" in kmerDict:
    kmerDict["esm"] =5
if "ess" in kmerDict:
    kmerDict["ess"] =178116
if "hhh" in kmerDict:
    kmerDict["hhh"] =27645732
if "hhs" in kmerDict:
    kmerDict["hhs"] =6888735
if "hse" in kmerDict:
    kmerDict["hse"] =77
if "hsi" in kmerDict:
    kmerDict["hsi"] =45881
if "hsm" in kmerDict:
    kmerDict["hsm"] =9988
if "hss" in kmerDict:
    kmerDict["hss"] =6832789
if "iii" in kmerDict:
    kmerDict["iii"] =15568223
if "iis" in kmerDict:
    kmerDict["iis"] =11600543
if "ise" in kmerDict:
    kmerDict["ise"] =1378
if "ish" in kmerDict:
    kmerDict["ish"] =39938
if "isi" in kmerDict:
    kmerDict["isi"] =208647
if "ism" in kmerDict:
    kmerDict["ism"] =57674
if "iss" in kmerDict:
    kmerDict["iss"] =24470128
if "mmm" in kmerDict:
    kmerDict["mmm"] =15021116
if "mms" in kmerDict:
    kmerDict["mms"] =5272899
if "mse" in kmerDict:
    kmerDict["mse"] =18
if "msh" in kmerDict:
    kmerDict["msh"] =8993
if "msi" in kmerDict:
    kmerDict["msi"] =61801
if "msm" in kmerDict:
    kmerDict["msm"] =20
if "mss" in kmerDict:
    kmerDict["mss"] =9823667
if "see" in kmerDict:
    kmerDict["see"] =150299
if "shh" in kmerDict:
    kmerDict["shh"] =6888735
if "sii" in kmerDict:
    kmerDict["sii"] =11600543
if "sis" in kmerDict:
    kmerDict["sis"] =13177225
if "smm" in kmerDict:
    kmerDict["smm"] =5272899
if "sms" in kmerDict:
    kmerDict["sms"] =4621604
if "sse" in kmerDict:
    kmerDict["sse"] =189375
if "ssh" in kmerDict:
    kmerDict["ssh"] =6839730
if "ssi" in kmerDict:
    kmerDict["ssi"] =24459931
if "ssm" in kmerDict:
    kmerDict["ssm"] =9826814
if "sss" in kmerDict:
    kmerDict["sss"] =134675245
"""

# MOMENTAN AUSGESETZT
# Alle Values in ein np Array, um damit später zu teilen
# allValues = np.array(list(kmerDict.values()))

# Initialisieren des Arrays, in welchem alle Dicts gespeichert werden
allDicts = np.zeros(count)
    
# Replacen, k-mer Konstruktion, Einfügen in das Dict
# k-mer occurence increase, wenn gefunden
# Erstellt den Input für TSNE
with open(input, 'r') as f:
    for line in f:
        if(line.find('f')):
            line = line.replace('f', 'e')
        if(line.find('t')):
            line = line.replace('t', 'e')
        newline = line[:4] + line[4].upper() + line[5:]
        newline = newline.strip()
    
        n_kmers = len(newline) - ksize + 1

        for i in range(n_kmers):
            kmer = newline[i:i + ksize]
            
            if kmer in kmerDict:
                kmerDict[kmer] = kmerDict[kmer] + 1
        
        
        # Alle Werte des momentanen Dicts in ein np-Array
        vals = np.array(list(kmerDict.values()))
        
        # Alle bisherigen Dicts + das neue Dict als np-Array zusammenfügen
        allDicts = np.vstack((allDicts, vals))
        
        # Zurücksetzen der values für die nächste Iteration
        for key in kmerDict:
            kmerDict[key] = 0
        
# Löschen der ersten Zeile des Arrays (Nullzeile wegen Initialisieren)        
y = np.delete(allDicts, (0), axis=0)

# MOMENTAN AUSGESETZT
# Dividieren durch die Vorkommen der k-mere
#z = np.divide(y, allValues)

# Standardscale anwenden
x = StandardScaler().fit_transform(y)

# TSNE anwenden
tsne_result = TSNE(n_components=2, perplexity=100, n_iter=5000).fit_transform(x)


# DBSCAN anwenden
db = DBSCAN(eps=5, min_samples=100).fit(tsne_result)
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_


# Anzahl der Cluster in den Labels, ohne Berücksichtigung von Noise, falls vorhanden
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)
print('Estimated number of noise points: %d' % n_noise_)


# PLOT generieren
# Hier wird jeweils jedes Cluster geplotted und mit einem Cluster-Label versehen
plt.figure(figsize=(15,15))
unique_labels = set(labels)
colors = [plt.cm.Spectral(each)
          for each in np.linspace(0, 1, len(unique_labels))]
          
for k, col in zip(unique_labels, colors):
    if k == -1:
        # Schwarz für Noise
        col = [0, 0, 0, 1]

    class_member_mask = (labels == k)

    xy = tsne_result[class_member_mask & core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col), markeredgewidth=0.0)
    
    list1 = xy[:, 0]
    list2 = xy[:, 1]
    
    a = np.array([list1, list2])
    
    plt.annotate(k, np.mean(a, axis=1), horizontalalignment='center', verticalalignment='center', size=20, weight='bold') 
    
    xy = tsne_result[class_member_mask & ~core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col), markeredgewidth=0.0)
    

# Alle Strukturen in np Array zum Filtern in richtiger Reihenfolge
allS = np.array(allStructures)
    
# OUTPUT generieren
with open(output_txt, 'w') as file:
    for i in range(n_clusters_):
    
        clusterStructures = allS[db.labels_==i]
    
        file.write('Cluster ' + str(i) + ' ')
        file.write(str(Counter(clusterStructures)))
        file.write('\n\n')

# PLOT anzeigen   
plt.title('Estimated number of clusters: %d' % n_clusters_)
plt.savefig(output_png)
