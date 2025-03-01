dna_sequence = ['A', 'T', 'G', 'C', 'A']
complement_map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

complementary_strand = [complement_map[base] for base in dna_sequence]

print(complementary_strand)