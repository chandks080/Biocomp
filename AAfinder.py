
 
import re
DNA = "GCTATGCGTAATGTTGTT"


#I made a dictionary containing the codons and the aa they code for
aadict = {
'GCT':'A','GCC':'A','GCA':'A','GCG':'A',
'CGT':'R','CGC':'R','CGA':'R','CGG':'R','AGA':'R','AGG':'R',
'AAT':'N','AAC':'N',
'GAT':'D', 'GAC':'D',
'TGT':'C', 'TGC':'C',
'GAA':'E', 'GAG':'E',
'CAA':'Q', 'CAG':'Q',
'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
'CAT':'H', 'CAC':'H',
'ATT':'I', 'ATC':'I', 'ATA':'I',
'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L', 'TTA':'L', 'TTG':'L',
'AAA':'K', 'AAG':'K',
'ATG':'M',
'TTT':'F', 'TTC':'F',
'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S', 'AGT':'S', 'AGC':'S',
'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
'TGG':'W',
'TAT':'Y', 'TAC':'Y',
'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V'    
        }
        
        
#I split the seq to read it by triplets
def triplet(DNA):
   #n = 3 to represent 3 nucleotides per codon
   n = 3
   a = [DNA[x:x+n] for x in range(0, len(DNA), n)]
   #print("DNA codons:\n"+str(a))
   return (a)
 
codons = triplet(DNA)
AA = ''
#this while loops iterates through every triplet until the end of the given seq
for codon in codons:
    if codon in aadict.keys():
        x = aadict[codon]
        AA += x

def findaa(Amino):
    b = 0
    for x in AA:
        aafound = re.search(Amino,x)
        if aafound:
            b += 1
    return b

Amino = input('What Amino Acid or Motif are you looking for: ')
b = findaa(Amino)          
print('The amino acid is found '+str(b)+' times')
       
print("DNA Sequence:\n"+DNA)
print("Here are the codons: \n"+str(codons))
print("The amino acid sequence: "+AA)
