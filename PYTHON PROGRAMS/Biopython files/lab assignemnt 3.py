from Bio import SeqIO
SeqIO.convert("D:\COMSATS UNIVERSITY ISLAMABAD ATTOCK CAMPUS\BCS FALL 2020 B\2nd semester\Bioinformatics\PYTHON PROGRAMS\Biopython files, "genbank", "D:\COMSATS UNIVERSITY ISLAMABAD ATTOCK CAMPUS\BCS FALL 2020 B\2nd semester\Bioinformatics\PYTHON PROGRAMS\Biopython files", "fasta")
for i in SeqIO.parse("C:\Users\JUNAID ALI\Desktop\New folder.gbk","fasta"):
    print(i.seq)