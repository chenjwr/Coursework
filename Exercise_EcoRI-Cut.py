# (From Chapter 2 of Python for Biologists)  Given the sequence:
# ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT
# Use the .find() string method to locate the EcoRI restriction enzyme site and use slicing to break the sequence into two fragments.  
# Print the length of the two fragments and their individual sequences.

Seq = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
CutCount = Seq.find("GAATTC")

print("5\' fragment of length", int(CutCount + 1), "nt:", Seq[:(CutCount + 1)])
print("3\' fragment of length", int(len(Seq) - (CutCount + 1)), "nt:", Seq[(CutCount + 2):])