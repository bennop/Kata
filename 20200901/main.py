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

def antisense(seq):
  translate = {"A":"T", "C":"G", "G":"C", "T":"A"}
  rev = seq[::-1]
  return ''.join([translate[letter] for letter in rev ])
  # [k, v for k, v in translate]

def translate_to_rna(seq):
  translate = {"A":"U", "C":"G", "G":"C", "T":"A"}
  rev = seq[::-1]
  return ''.join([translate[letter] for letter in rev ])
  # [k, v for k, v in translate]

def all_rna(seq):
  return [translate_to_rna(seq), translate_to_rna(antisense(seq))]

def codon_to_prot3(codon):
   return cod2prot[codon]

def prot3_to_prot1(p3):
  if(p3 == 'Stop'):
    return '-'
  else: 
    return prot2p1[p3.lower()]

def codon_to_prot(codon):
  return prot3_to_prot1(codon_to_prot3(codon))

def translation(seq):
  start_pos = str.index(seq, "AUG")
  if start_pos == -1:
    return False
  peptide = 'M'
  for codon_pos in range(start_pos+3, len(seq)-2, 3):
    protein = codon_to_prot(seq[codon_pos:codon_pos+3])
    if protein == '-':
      return peptide
    peptide += protein
  return peptide
    
def translate_all(seq):
  return [translation(s) for s in all_rna(seq)]

# ---- T E S T S ------------

def test_antisense():
  assert antisense("TTAGGGCATG") ==  "CATGCCCTAA"

def test_translate_to_rna():
  assert translate_to_rna("TTAGGGCATG") == 'CAUGCCCUAA'
  
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
