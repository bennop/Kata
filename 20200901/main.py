# Source Code
# also first import jsons so we can access translation tables
import json

def read_json_dictionary(jfile):
   file = open(jfile)   
   dict = json.load(file)
   file.close()
   return(dict)

# global to only read once
cod2prot = read_json_dictionary('codons.json')
prot2p1 = read_json_dictionary('peptides.json')


# common code for
#  - antisense conversion
#  - RNA transcription

## pass in partial dictionary for conversion of A and add the common part
#
def reverse_and_translate(seq, dict):
  # add common part of dictionary
  dict.update({"C":"G", "G":"C", "T":"A"})
  rev = seq[::-1]
  return ''.join([dict[letter] for letter in rev ])

## alternative implementation, only pass in what A becomes and
## construct the whole dictionary
#
def reverse_and_translate2(seq, a_becomes):
  # add common part of dictionary
  dict = {"A":a_becomes, "C":"G", "G":"C", "T":"A"}
  rev = seq[::-1]
  return ''.join([dict[letter] for letter in rev ])

def antisense(seq):
  return reverse_and_translate2(seq, "T")

def transcribe_to_rna(seq):
  return reverse_and_translate(seq, {"A":"U"})

def all_rna(seq):
  return [transcribe_to_rna(s) for s in [seq, antisense(seq)]]

# partial translations
def codon_to_prot3(codon):
   return cod2prot[codon]

def prot3_to_prot1(p3):
  if(p3 == 'Stop'):             # special handling of STOP codons
    return '-'
  else: 
    return prot2p1[p3.lower()]

# combined translation
def codon_to_prot(codon):
  return prot3_to_prot1(codon_to_prot3(codon))

# translate one sequence
def translation(seq):
  start_seq = "AUG"             # prior knowledge
  start_pos = str.index(seq, start_seq)
  if start_pos == -1:
    return False
  peptide = codon_to_prot(start_seq)
  for codon_pos in range(start_pos+3,    # codon after found start
                         len(seq)-2,     # last possible codon pos
                         3):             # in steps of 3
    protein = codon_to_prot(seq[codon_pos:codon_pos+3])
    if protein == '-':          # STOP
      return peptide
    peptide += protein
  return peptide                # rather fail? (see Specification 3e)

# translate sequence and it's reverse transposed
def translate_all(seq):
  return [translation(s) for s in all_rna(seq)]

# -------  T E S T S  ------------

def test_antisense():
  assert antisense("TTAGGGCATG") ==  "CATGCCCTAA"

def test_transcribe_to_rna():
  assert transcribe_to_rna("TTAGGGCATG") == 'CAUGCCCUAA'
  
def test_all_rna():
  assert all_rna("TTAGGGCATG") == ['CAUGCCCUAA','UUAGGGCAUG']

def test_codon_to_prot():
  assert codon_to_prot("AUG") == "M"

def test_stop1():
  assert prot3_to_prot1('Stop') == '-'

def test_stop2():
  assert codon_to_prot("UAA") == '-'

def test_translation():
  assert translation('CAUGCCCUAA') == 'MP'

def test_translate_all():
  assert translate_all("TTAGGGCATG") == ['MP', 'M']

def test_overall():
  assert translate_all('AGGACGGGCTAACTCCGCTCGTCACAAAGCGCAATGCAGCTATGGCAGATGTTCATGCCG')[0] == 'MNICHSCIALCDERS'
