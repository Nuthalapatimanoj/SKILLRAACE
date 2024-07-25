#INTIALISING VARIABLES
subjects=["I" ,"You"]
verbs=["Play","Love"]
objects=["Cricket","Ludo"]

#CREATING EMPTY SENTENCE
sentence=[]

#GENERATING SENTENCE
for subj in subjects:
    for verb in verbs:
        for obj in objects:

#SENTENCE FORMING
            sentence.append(f"{subj} {verb} {obj}")

#PRINTING SENTENCE
for sentence in sentence:
    print(sentence)
                
        

