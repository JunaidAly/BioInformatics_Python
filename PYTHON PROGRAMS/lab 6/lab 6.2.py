from Bio import AlignIO
alignments=AlignIO.parse("resampled.phy", "phylip")
for alignment in alignments:
    print(alignment)
    print("")