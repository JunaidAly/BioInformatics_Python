#transcription
from Bio.Seq import Seq
code_Dna=Seq("ACTGATTCTACTACTAAG")
code=Seq("ACGTACCTA")
print("CODE DNA IS:     ",code_Dna)
tamplate_dna=code_Dna.reverse_complement()
print("TAMPLATE DNA IS: ",tamplate_dna)
massengar_rna=code_Dna.transcribe()
print("MASSANGER RNA IS:",massengar_rna)
protein_seq=massengar_rna.translate()
print("TRANSLATION  IS",protein_seq)
print(code_Dna ,""+"", code)
print(code_Dna.count("A"))
print(code_Dna.lower())

