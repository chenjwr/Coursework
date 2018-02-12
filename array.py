# Reverse the contents of the array using three methodologies

AminoAcid = ["glutamine", "lysine", "proline"]
print(AminoAcid)

# FIRST method 
ReverseAminoAcid_01 = AminoAcid[::-1]

print(ReverseAminoAcid_01)

# SECOND method
ReverseAminoAcid_02 = []

for i in reversed(AminoAcid):
	ReverseAminoAcid_02.append(i)

print(ReverseAminoAcid_02)

# THIRD method
def ReverseAminoAcid_03(array):
	return [array.pop() for i in range(len(array))]

print(ReverseAminoAcid_03(AminoAcid))