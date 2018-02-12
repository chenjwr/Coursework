## Create list of all codons 
bases = ["A","U","G","C"]
Codon_List = []

for first in bases:
	for second in bases:
		for third in bases:
			Codon = (first + second + third)
			Codon_List.append(Codon)

## Create corresponding list of amino acids  
AminoAcid_List = []
for i in range(0, len(Codon_List)):
	
	if Codon_List[i][0] == "G":
		if Codon_List[i][1] == "U":
			AminoAcid_List.append("valine")
		elif Codon_List[i][1] == "C":
			AminoAcid_List.append("alanine")
		elif Codon_List[i][1] == "G":
			AminoAcid_List.append("glycine")
		elif Codon_List[i][1:3] in ["AU", "AC"]:
			AminoAcid_List.append("aspartic acid")
		elif Codon_List[i][1:3] in ["AA", "AG"]:
			AminoAcid_List.append("glutamic acid")
	
	elif Codon_List[i][0] == "C":
		if Codon_List[i][1] == "U":
			AminoAcid_List.append("leucine")
		elif Codon_List[i][1] == "C":
			AminoAcid_List.append("proline")
		elif Codon_List[i][1] == "G":
			AminoAcid_List.append("arginine")
		elif Codon_List[i][1:3] in ["AU", "AC"]:
			AminoAcid_List.append("histidine")
		elif Codon_List[i][1:3] in ["AA", "AG"]:
			AminoAcid_List.append("glutamine")
	
	elif Codon_List[i][0] == "U":
		if Codon_List[i][1] == "C":
			AminoAcid_List.append("serine")
		elif Codon_List[i][1:3] in ["UU", "UC"]:
			AminoAcid_List.append("phenylalanine")
		elif Codon_List[i][1:3] in ["UA", "UG"]:
			AminoAcid_List.append("leucine")
		elif Codon_List[i][1:3] in ["GU", "GC"]:
			AminoAcid_List.append("cysteine")
		elif Codon_List[i][1:3] == "GG":
			AminoAcid_List.append("tryptophan")
		elif Codon_List[i][1:3] in ["AU", "AC"]:
			AminoAcid_List.append("tyrosine")
		elif Codon_List[i][1:3] in ["AA", "AG", "GA"]:
			AminoAcid_List.append("stop")

	elif Codon_List[i][0] == "A":
		if Codon_List[i][1] == "C":
			AminoAcid_List.append("threonine")
		elif Codon_List[i][1] == "U":
			if Codon_List[i][2] == "G":
				AminoAcid_List.append("start")
			else:
				AminoAcid_List.append("isoleucine")
		elif Codon_List[i][1:3] in ["AU", "AC"]:
			AminoAcid_List.append("asparagine")
		elif Codon_List[i][1:3] in ["AA", "AG"]:
			AminoAcid_List.append("lysine")
		elif Codon_List[i][1:3] in ["GU", "GC"]:
			AminoAcid_List.append("serine")
		elif Codon_List[i][1:3] in ["GA", "GG"]:
			AminoAcid_List.append("arginine")

## Create dictionary to match keys (codons) to values (amino acids)
Codon_Table = {}

Codon_Table = dict(zip(Codon_List, AminoAcid_List))

## Translate codon to corresponding amino acid
CodonSeq = input("Enter codon sequence:")
result = Codon_Table.get(CodonSeq.upper())

print("{} : {}".format(CodonSeq, result))