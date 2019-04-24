import os
import operator

pathControl = '/home/federica/Documents/Thesis/Programs/TextParser/control/control_no_functional_clean/'
pathDementia = '/home/federica/Documents/Thesis/Programs/TextParser/dementia/dementia_no_functional_clean/'

frequencies = {}

filesC = []
filesD = []
sm_words = []

for r, d, f in os.walk(pathControl):
    for file in f:
        if '.cha' in file:
            filesC.append(os.path.join(r, file))

for r, d, f in os.walk(pathDementia):
    for file in f:
        if '.cha' in file:
            filesD.append(os.path.join(r, file))

for file in filesC:
    file = open(file, 'r')
    lines = file.read()
    words = lines.split("\n")[:-1]
    for w in words:
        if not w:
            continue
        word_b = w.split(" ")[:-1]
        for wb in word_b:
            sm_words.append(wb)
    for w in sm_words:
        frequencies.update({w : sm_words.count(w)})

sorted_x = sorted(frequencies.items(), key=operator.itemgetter(1), reverse=True)

f = open("frequencies_control.txt", "x")
for t in sorted_x:
    f.write(' '.join(str(s) for s in t) + '\n')

frequencies.clear()
sorted_x.clear()

for file in filesD:
    file = open(file, 'r')
    lines = file.read()
    words = lines.split("\n")[:-1]
    for w in words:
        if not w:
            continue
        word_b = w.split(" ")[:-1]
        for wb in word_b:
            sm_words.append(wb)
    for w in sm_words:
        frequencies.update({w: sm_words.count(w)})

sorted_x = sorted(frequencies.items(), key=operator.itemgetter(1), reverse=True)

f = open("frequencies_dementia.txt", "x")
for t in sorted_x:
    f.write(' '.join(str(s) for s in t) + '\n')