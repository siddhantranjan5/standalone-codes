from Bio import AlignIO, Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor

# Path to your FASTA file
fasta_file = "C:\\Users\\siddh\\Projects\\TEST\\sequences.fasta"

# Read the alignment from the FASTA file
alignment = AlignIO.read(fasta_file, "fasta")

# Calculate distances between the sequences in the alignment
calculator = DistanceCalculator('identity')
dm = calculator.get_distance(alignment)

# Construct a tree from the distance matrix
constructor = DistanceTreeConstructor()
tree = constructor.upgma(dm)

# Draw a Tree
Phylo.draw(tree)
