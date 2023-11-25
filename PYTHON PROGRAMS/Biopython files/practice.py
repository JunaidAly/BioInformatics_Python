from Bio import SeqIO
record_iterator=SeqIO.parse("ls_orchid.fasta", "fasta")
first_record=next(record_iterator)
print(first_record.id)
print(first_record.description)
second_record=next(record_iterator)
print(second_record.id)
print(second_record.description)