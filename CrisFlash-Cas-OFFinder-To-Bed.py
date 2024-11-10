import argparse

# Function to parse the genome file to get chromosome lengths
def parse_genome_file(genome_file):
    genome_lengths = {}
    with open(genome_file, 'r') as f:
        for line in f:
            parts = line.strip().split('\t')
            chrom = parts[0]
            length = int(parts[1])
            genome_lengths[chrom] = length
    return genome_lengths

# Function to process the input file (gRNA sequences, positions, and strand info)
def process_input_file(input_file, genome_lengths, output_file, gRNA_length):
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        for line in f_in:
            # Split the line by tabs to get the columns
            row = line.strip().split('\t')

            # Extract values from the input row
            gRNA_sequence = row[0]                # gRNA candidate sequence
            chromosome = row[1]                   # Chromosome (e.g., NC_000021.9)
            position_match = int(row[2])          # Position in the candidate
            strand = row[4]                       # Strand information (+ or -)
            mismatches = row[5]                   # Number of mismatches

            # Check gRNA length consistency
            if len(gRNA_sequence) != gRNA_length:
                print(f"Warning: gRNA sequence length ({len(gRNA_sequence)}) in row does not match the specified length (-L {gRNA_length}).")

            # Check the chromosome length from the genome file
            chrom_max_length = genome_lengths.get(chromosome, None)

            # Process based on strand orientation
            if strand == '+':
                # If strand is positive, add the gRNA length to the position_match (if within limits)
                end_pos = position_match + gRNA_length
                if chrom_max_length and end_pos > chrom_max_length:
                    end_pos = chrom_max_length  # If exceeding chromosome length, set to max
                f_out.write(f"{chromosome}\t{position_match}\t{end_pos}\t{strand}\t{gRNA_sequence}\t{mismatches}\n")

            elif strand == '-':
                # If strand is negative, subtract the gRNA length (ensure start is not negative)
                start_pos = position_match - gRNA_length
                if start_pos < 0:
                    start_pos = 0  # Prevent negative positions
                f_out.write(f"{chromosome}\t{start_pos}\t{position_match}\t{strand}\t{gRNA_sequence}\t{mismatches}\n")

# Main function to set up argument parsing and execute the program
def main():
    parser = argparse.ArgumentParser(description='Process gRNA sequences and generate a BED file.')

    # Define the input arguments
    parser.add_argument('-i', '--input', required=True, help='Input file from CrisFlash run with the -C option containing gRNA sequences and target positions.')
    parser.add_argument('-g', '--genome', required=True, help='Genome file containing chromosome lengths.')
    parser.add_argument('-o', '--output', required=True, help='Output BED file.')
    parser.add_argument('-L', '--length', type=int, default=23, help='gRNA length (default: 23)')

    # Parse the arguments from the command line
    args = parser.parse_args()

    # Parse the genome file to get chromosome lengths
    genome_lengths = parse_genome_file(args.genome)

    # Process the input file and write the output BED file
    process_input_file(args.input, genome_lengths, args.output, args.length)

if __name__ == '__main__':
    main()

