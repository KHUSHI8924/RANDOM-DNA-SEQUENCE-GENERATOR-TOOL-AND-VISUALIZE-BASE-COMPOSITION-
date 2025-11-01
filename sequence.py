import random 
import matplotlib.pyplot as plt 
import pandas as pd 

#Function to generate random DNA sequence
def generate_random_DNA_sequence(length):
    bases = ['A', 'G', 'C', 'T']
    return ''.join(random.choices(bases, k=length))


#Base Composition 
def base_composition(seq):
    counts = {base: seq.count(base) for base in "ATGC"}
    total = len(seq)
    percents = {base: (count / total) * 100 for base, count in counts.items()}
    return counts, percents 

#Generate Sequence 
length = int(input("Enter the length for which you want to generate random DNA sequence: "))
dna_seq = generate_random_DNA_sequence(length)
print(f"Random DNA sequence ({length} bp): ")
print(dna_seq[:100] + "....")  # for showing only first 100 bases 


#Computing Composition 
counts, percents = base_composition(dna_seq)
df = pd.DataFrame(list(percents.items()), columns=['Base', 'Percentage'])

print("Base Composition (%): ")
print(df)


#Plotting 
plt.figure(figsize=(6,4))
plt.bar(df['Base'], df['Percentage'], color = ['yellow', 'skyblue', 'red', 'lightgreen'])
plt.title(f"BASE COMPOSITION OF RANDOM DNA ({length} bp)", fontsize=14)
plt.ylabel("Percentage (%)", fontsize=11)
plt.xlabel("Bases", fontsize=11)
plt.ylim(0,100)
plt.tight_layout()
plt.show()

