import os
from Bio.Align.Applications import ClustalwCommandline

from Bio import Phylo, AlignIO

#clustalw_exe = r"D:\COMSATS UNIVERSITY ISLAMABAD ATTOCK CAMPUS\BCS FALL 2020 B\2nd semester\Bioinformatics\online Bi lab\Lab-7\programs\clustalw2.exe"
#assert os.path.isfile(clustalw_exe), "Clustal W executable missing"
#clustalw_cline = ClustalwCommandline(clustalw_exe, infile="opuntia.fasta")
clustalw_cline = ClustalwCommandline("clustalw2", infile="opuntia.fasta")
stdout, stderr = clustalw_cline()
#align = AlignIO.read("opuntia.aln", "clustal")
#print(align)

