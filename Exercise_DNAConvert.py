# Converts the DNA sequence string:
# ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT
# into a list of three character codon strings:
# ['ACT', 'GAT', 'CGA', 'TTA', 'CGT', 'ATA', 'GTA', 'GAA', ..., 'ATG', 'CGT', 'TCA']
# toss any "short" codons at the end, (e.g. "T")

Seq = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
CodonList = []

while len(Seq) > 2:
	Codon = Seq[0:3]
	CodonList.append(Codon)
	Seq = Seq[3:len(Seq)]

print(CodonList)