from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

# Function to get sequence details from user
def get_sequence_details():
    sequences = []
    num_sequences = int(input("Enter the number of sequences: "))

    for i in range(num_sequences):
        seq_id = input(f"Enter ID for sequence {i+1}: ")
        seq_description = input(f"Enter description for sequence {i+1}: ")
        
        # Validation loop for sequence data
        while True:
            seq_data = input(f"Enter sequence data for sequence {i+1}: ").upper()
            if all(nucleotide in 'ATGC' for nucleotide in seq_data):
                break  # Exit loop if the sequence is valid
            else:
                print("Invalid sequence. Please enter a sequence containing only A, T, G, C.")
        
        sequences.append(SeqRecord(Seq(seq_data), id=seq_id, description=seq_description))

    return sequences

# Get the sequences from user input
sequences = get_sequence_details()

# Create a FASTA file
with open("sequences.fasta", "w") as f:
    SeqIO.write(sequences, f, "fasta")

print("FASTA file created successfully!")
