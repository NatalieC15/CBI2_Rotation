# Length of strings
# Print out the length of this DNA sequence ATTTCGTAACGTTAGGGCATAATCCCGAA

seq = 'ATTTCGTAACGTTAGGGCATAATCCCGAA'
#print(len(seq)) #prints the length of the sequence 

#Write a function to take a given DNA sequence as a variable and return the length.
def length(sequence):
	print(len(sequence))
	return

#length(seq) #used to call the length function

# Counting
# Print out the number of A's, G's, C's and T's in the DNA sequence ATTTCGTAACGTTAGGGCATAATCCCGAA
#print(seq.count('A')) #used to print out the number of A's within the sequence
#print(seq.count('G')) #used to print out the number of G's within the sequence
#print(seq.count('C')) #used to print out the number of C's within the sequence
#print(seq.count('T')) #used to print out the number of T's within the sequence

# Write a function to take a given DNA sequence as a variable and return these numbers.
def counts(sequence):
	print(sequence.count('A'))
	print(sequence.count('G'))
	print(sequence.count('C'))
	print(sequence.count('T'))
	return

#counts(seq) #used to call the counts function

# Dictonaries and lists
# You have a dictionary describing the coverage across various exons {"BRCA1_1": 15, "BRCA1_2": 25, "BRCA2_1": 20, "BRCA2_2": 45}
genedict = dict()
#print(exondict) # shows an empty dictionary that has been created with the code above
genedict = {"BRCA1_1": 15, "BRCA1_2": 25, "BRCA2_1": 20, "BRCA2_2": 45}
#print(genedict) #print out the dictionary to check to see that contains all the information
#print(genedict['BRCA1_1']) #print to check that the correct depth of the exon is being printed when a 'gene_exons' is entered

# Print out the gene_exons from the dictionary which have a depth below the required threshold of 20.
#for gene, depth in genedict.items():
#	if depth < 20 :
#		print(gene, depth) #these lines are used to print out the exon of a gene that does not reach the required depth of 20

# Write a function to take a given dictionary and depth threshold as variables, and return a list of gene_exons which need to be repeated by sanger.
def coverage_threshold(genedict,required_depth):
	for gene, depth in genedict.items():
		if depth < required_depth:
			print(gene, depth, 'to be repeated by Sanger')
	
#coverage_threshold(genedict, 20) #used to call the threshold function, can change the value of depth to alter the threshold

# Reverse complements
# Write a function to take a DNA sequence as a variable and return the reverse complement of it
def reverse_complement(sequence):
	output = ''
	for letter in sequence:
		letter = letter.upper()

		if letter == 'A':
			output += 'T'
		elif letter == 'T':
			output += 'A'
		elif letter == 'C':
			output += 'G'
		else:
			output += 'C'
	print(output[::-1]) #the [::-1] code causes the output to be in reverse so 3'-5' instead pf 5'-3'

#reverse_complement(seq) # call the reverse complement of the sequence so the letters are complemented i.e. A changed to T, C changed to G etc.
						# and the letters are reversed from 5'-3' to 3'-5' direction.

# Pandas (Python module)
# Convert the coverage dictionary above into a Pandas dataframe
import pandas as pd

data_for_table = {"GeneName_Exon": list(genedict.keys()), "Coverage": list(genedict.values())} 
#keys are the gene names in the dictionary and values are the coverage depth

coverageTable = pd.DataFrame.from_dict(data=data_for_table)
#print(coverageTable)

# Export this dataframe to an excel file
#coverageTable.to_csv('Coverage_Table.csv') #this exports the data into a csv file which the data is separated by a comma and could be opened with excel; 
										   #could use (..., sep='\t')to separate the data by tabs or could potentially use tsv instead.

# Write a function to add new entries into the dataframe
def addentries(gene_exon, coverage):
	
	extraData = {"GeneName_Exon": gene_exon, "Coverage": coverage}
	extraTable = pd.DataFrame(extraData)
	#print(extraData)
	#print(extraTable)
	modifiedTable = pd.concat([coverageTable, extraTable]).reset_index(drop=True)
	print(modifiedTable)

#addentries(['PTEN_1', 'MSH2_1'], [30, 45]) #used to call the addentries function, however, values have to be entered as a list with [] otherwise will error

# Ensembl API and JSON
# Use the Ensembl Rest API to look up information on the gene with identifier ENSG00000130635
import requests 
import sys
import json

server = "http://rest.ensembl.org"
ext = "/lookup/id/ENSG00000130635?"

r = requests.get(server+ext, headers={"Content-Type" : "application/json"})

if not r.ok:
	r.raise_for_status()
	sys.exit()

decoded = r.json()
#print(repr(decoded)) #this prints out all of the information on the gene with the identifier ENSG00000130635 in the JSON format

# Parse the JSON output to print out the gene name and start and end coordinates
#print(decoded['display_name'])
#print(decoded['start'])
#print(decoded['end']) #these print the display_name i.e. gene name, start of the gene and end of the gene.