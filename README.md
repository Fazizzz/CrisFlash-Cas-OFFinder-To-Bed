# Cas-OFFinder gRNA Sequence BED File Generator

This python script processes the output from tools such as Crisflash in Cas-OFFinder format containing gRNA sequences, chromosome positions, and strand information to generate a BED file suitable for bioinformatics analysis and visualization. The script is designed for use with Crisflash run with the -C option. The output BED file includes the target regions expanded to specified lengths (default 23bp) based on the provided positions, strand orientation, and chromosome boundaries.

_______________________________________________________
## Table of Contents
- [Installation](#installation)
- [Requirements](#requirements)
- [Usage](#usage)
- [Input File Formats](#input-file-formats)
- [Output Format](#output-format)
- [Example](#example)
- [License](#license)
- [Acknowledgments](#acknowledgments)

_______________________________________________________
## Installation
Clone this repository to your local machine:

```bash
git clone https://github.com/Fazizzz/CrisFlash-Cas-OFFinder-To-Bed.git
cd CrisFlash-Cas-OFFinder-To-Bed
```
________________________________________________________
## Requirements

* `Python 3.8+`
* `An input file in Cas-OFFinder format containing gRNA sequence, chromosome, position, candidate sequence, strand information and number of mismatches`
* `A genome file containing chromosome name and maximum length`

_______________________________________________________ 
## Usage

This script was written to be used with [Crisflash](https://github.com/crisflash/crisflash) run with the -C option but may be used with any file with the Cas-OFFinder format. 

```
crisflash -g {Sample-genome.fa} -s {Candidate-sequences.fa} -p {PAM} -m {mismatches} -C -t {threads} -o {output}

```

Run the script with:

```
python CrisFlash-Cas-OFFinder-To-Bed.py  -i {input_file}  -g {genome_file.genome} -o {output_file.bed} -L {gRNA Length (default: 23)}

```

The script takes four main arguments:

*	`-i or --input:` Path to the input file generated by CrisFlash or similar tool with gRNA sequences, target positions, strand information, etc.
*	`-g or --genome:` Path to the genome file that contains chromosome lengths.
*	`-o or --output:` Path to save the output BED file. 
*	`-L or --length:` Optional flag for gRNA length in output BED file (default: 23)
	Note: The script checks the length of the guide sequence in column 1 against the given length (-L) and will throw a warning for each discrepancy.

________________________________________________________

## Input File Formats

# 1. gRNA Input File (from CrisFlash or similar)

The input file should be tab-separated with columns in the following order:

Column 1: gRNA Candidate Sequence
Column 2: Chromosome Target in Reference (e.g., NC_000021.9)
Column 3: Position Match in Candidate
Column 4: Matched sequence in reference (not used by the script)
Column 5: Strand Information (+ or -)
Column 6: Number of Mismatches

Example:
```
GTGGGGCCCGGTGGGCTTCCNNN    NC_000021.9    8208389    GTGGGGCCCGGTGGGCTTCCCGG    +    0

```

# 2. Genome File

The genome file should contain chromosome names and their maximum lengths in tab-separated format.

Example:
```
NC_000021.9    48129895
NC_000022.9    51304566
...
```

_________________________________________________________

## Output Format

The script generates a BED file with the following columns:

Chromosome: Chromosome name as given in the input file.
Start: Start position of the gRNA cut site based on strand orientation and length provided.
End: End position of the gRNA cut site based on strand orientation and length provided.
Strand: Strand information (+ or -).
gRNA Sequence: The original gRNA candidate sequence.
Mismatches: Number of mismatches as given in the input file.

Example Output:
```
NC_000021.9    8208389    8208412    +    GTGGGGCCCGGTGGGCTTCCNNN    0

```
___________________________________________________________
## Example

Here's an example command for running the script:

```
python CrisFlash-Cas-OFFinder-To-Bed.py  -i {input_file}  -g {genome_file.genome} -o {output_file.bed} -L {gRNA Length (default: 23)}

```
___________________________________________________________

## License

This project is licensed under the GPL-3.0 License - see the [LICENSE](https://github.com/crisflash/crisflash/blob/master/LICENSE) file for details.


___________________________________________________________

## Acknowledgments

* **M.Faizan Khalid** - *Author and current maintainer of the code*

This script was developed by Muhammad Faizan Khalid without input or feedback from the [Crisflash](https://github.com/crisflash/crisflash) team. The script is intended to be a utility for use in CRISPR guide design and analysis. Maintenance and usage of this script is currently not supported or validated by the developers of Crisflash. For any information on Crisflash or the Cas-OFFinder format please refer to the [Crisflash](https://github.com/crisflash/crisflash) Github and use their guide for citing and referencing their tools.
  
For citing this tool, please use Khalid M.Faizan or Khalid MF. You can follow my research using my [Google Scholar profile](https://scholar.google.com/citations?hl=en&user=qFZQ5wYAAAAJ&sortby=title&view_op=list_works&gmla=AL3_zigRWGX9g8Jc22idbBUMFuy7cVN_pEIyL6_DXSA-qWkJbcaONzhRNSmAwmQXKEm-3-WYGouZZC2pCE6zD9tZLxizbM7jQzzZMOgtkgsuL825u4lvSs9kwsccajhJbBg2Mrc37at_HCQ).

This project is made possible thanks to the open-source bioinformatics community for their resources and support.

