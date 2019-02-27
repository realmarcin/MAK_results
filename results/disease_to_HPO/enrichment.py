# coding=utf-8
import sys
import os
import pickle
import pandas
import numpy as np

from ontobio.ontol_factory import OntologyFactory
from ontobio.assoc_factory import AssociationSetFactory
import requests


HUMAN = 'NCBITaxon:9606'

#ontology paths
##''/Users/marcin/Documents/VIMSS/ontology/NCATS/HPO/hp.obo')#mondo#hp

ofactory = OntologyFactory()
afactory = AssociationSetFactory()
print("creating...")

ont = ofactory.create('hp')
aset = afactory.create(ontology=ont,
                       subject_category='disease',
                       object_category='phenotype',
                       taxon=HUMAN)

#ont = ofactory.create('mondo')
#aset = afactory.create(ontology=ont,
#                       subject_category='disease',
#                       object_category='phenotype',
#                       taxon=HUMAN)

###aset = afactory.create_from_gaf('my.gaf', ontology=ont)

                
disease_ids = ["DECIPHER:1", "DECIPHER:16", "OMIM:614696", "OMIM:614699", "Orphanet:99978", "Orphanet:1934"]
phenotype_ids = ["HP:0000007", "Orphanet:93299", "Orphanet:90794"]
print("annotations\t"+disease_ids[5])

print(aset.annotations("MONDO:0020332"))#disease_ids[5]))
#print(ont.equiv_graph())

#print(type(aset))
#print(aset.association_map)

#print(aset.as_dataframe())



url = "https://api-dev.monarchinitiative.org/api/ontol/subgraph/hp/HP:0002829"
data = {"cnode": ["HP:0003477", "HP:0000099", "HP:0002018", "HP:0002586", "HP:0002788", "HP:0003470", "HP:0006528",
				  "HP:0002721", "HP:0001284", "HP:0002013", "HP:0100598", "HP:0000238", "HP:0002613", "HP:0000554",
				  "HP:0003453", "HP:0002014", "HP:0000979", "HP:0005681", "HP:0006846", "HP:0001937", "HP:0001875",
				  "HP:0000709", "HP:0001658", "HP:0005558", "HP:0004418", "HP:0100778", "HP:0001735", "HP:0001394",
				  "HP:0000964", "HP:0002204", "HP:0003447", "HP:0000999", "HP:0002383", "HP:0000365", "HP:0002105",
				  "HP:0002076", "HP:0005059", "HP:0000751", "HP:0001973", "HP:0004944", "HP:0100769", "HP:0001269",
				  "HP:0002102", "HP:0200029", "HP:0100584", "HP:0007141", "HP:0001635", "HP:0011944", "HP:0002907",
				  "HP:0001289", "HP:0001882", "HP:0003401", "HP:0000763", "HP:0001878", "HP:0000573", "HP:0001824",
				  "HP:0002093", "HP:0001025", "HP:0001888", "HP:0005318", "HP:0001114", "HP:0002960", "HP:0100324",
				  "HP:0002171", "HP:0000965", "HP:0006530", "HP:0002719", "HP:0011947", "HP:0011946", "HP:0002206",
				  "HP:0001369", "HP:0002099", "HP:0001085", "HP:0011034", "HP:0100614", "HP:0012211", "HP:0100699",
				  "HP:0000819", "HP:0000083", "HP:0001945", "HP:0002617", "HP:0006532", "HP:0003493", "HP:0011096",
				  "HP:0000112", "HP:0004950", "HP:0000789", "HP:0003765", "HP:0010783", "HP:0001370", "HP:0000822",
				  "HP:0002863", "HP:0002090", "HP:0005547", "HP:0002922", "HP:0003365", "HP:0007354", "HP:0001909",
				  "HP:0011857", "HP:0001890", "HP:0001482", "HP:0002097", "HP:0003040", "HP:0002098", "HP:0000790",
				  "HP:0009830", "HP:0007902", "HP:0012622", "HP:0100256", "HP:0000613", "HP:0001919", "HP:0000793",
				  "HP:0001287", "HP:0000762", "HP:0003774", "HP:0200042", "HP:0001324", "HP:0002716", "HP:0000093",
				  "HP:0003326", "HP:0002725", "HP:0002665", "HP:0001000", "HP:0002092", "HP:0004844", "HP:0007359",
				  "HP:0004943", "HP:0010702", "HP:0000969", "HP:0000718", "HP:0100758", "HP:0002923", "HP:0001513",
				  "HP:0000872", "HP:0001903", "HP:0000123", "HP:0006562", "HP:0001907", "HP:0100280", "HP:0001297",
				  "HP:0008653", "HP:0002331", "HP:0002459", "HP:0002621", "HP:0002138", "HP:0000155", "HP:0003202",
				  "HP:0009831", "HP:0002037", "HP:0002633", "HP:0002094", "HP:0100749", "HP:0000967", "HP:0003565",
				  "HP:0002113", "HP:0001873", "HP:0003249", "HP:0100665", "HP:0001342", "HP:0002448", "HP:0001701",
				  "HP:0003124", "HP:0002027", "HP:0100806", "HP:0000794", "HP:0001271", "HP:0002574", "HP:0010871",
				  "HP:0002516", "HP:0003651", "HP:0006510", "HP:0100532", "HP:0003259", "HP:0003881", "HP:0002527",
				  "HP:0100279", "HP:0100647", "HP:0001974", "HP:0000752", "HP:0000855", "HP:0002063", "HP:0000100",
				  "HP:0100724", "HP:0000988", "HP:0006515", "HP:0002196", "HP:0011945", "HP:0006775", "HP:0005523",
				  "HP:0000246", "HP:0001250", "HP:0002239", "HP:0001970", "HP:0000491", "HP:0001880", "HP:0002202",
				  "HP:0000978", "HP:0100533", "HP:0011953", "HP:0100608", "HP:0011972", "HP:0006536", "HP:0003613",
				  "HP:0004420", "HP:0100827", "HP:0000836", "HP:0005310", "HP:0005305", "HP:0002955", "HP:0002625"]}

response = requests.post(url, data)
response.json()


#sys.exit()
                
all_disease_ids = disease_ids

#print(disease_ids)

enr = aset.enrichment_test(subjects=phenotype_ids, threshold=1, labels=True)#background=phenotype_ids,

print(enr)





bg_file = open("disease__by__HPO_matrix_v3_yids.txt", "r")
bg_data = bg_file.read().split('\n')

del bg_data[-1]
#print(bg_data)
#print(type(bg_data))
#sys.exit()


phenotype_labels_df= pandas.DataFrame.from_csv("phenotype_labels_v2.txt", sep='\t') 
#print(phenotype_labels_df["label"])
#sys.exit()


#print(sys.argv)
#print(sys.argv[1])

#print(os.listdir(sys.argv[1]))

files = [f for f in os.listdir(sys.argv[1])]
#print(files)

for f in files:
	if f.endswith("colorder.txt"):
		print(f)
		text_file = open(sys.argv[1]+"/"+f, "r")
		lines = text_file.read().split('\n')
		print(lines)
		#print(" len(lines) " + str( len(lines)))
		
		curids = [None] * (len(lines)-1)
		#print("len(curids) "+ str(len(curids)))
		count = 1
		for l in range(1, len(lines)-1):
			s = lines[l]
			print(s)
			split = s.split('\" \"')
			#print("split")
			#print(len(split))
			#print(split)
			#print(split[1])
			curids[count] = split[1].replace("\"","")
			count = count+1
			
#		curids = curids[-1]
		curids.pop(0)
		print(type(curids))
		print(len(curids))
		print("curids "+str(curids))

		bicluster_phenotype_ids = []
		for k in range(0, len(curids)):
			print(curids[k])
			#print(phenotype_labels_df["id"][1])
			#print(type(phenotype_labels_df["id"] ))

			#innerindex = (phenotype_labels_df["id"] == phenotype_ids[k].replace(".",":"))
			innerindex = (phenotype_labels_df["label"] == curids[k])
	
			#print(innerindex)
	
			whichisit = np.nonzero(innerindex == True)
			#print("whichisit")
			#print(whichisit)
			#print(len(whichisit))
	
			done = False
	
			if whichisit is not None and len(whichisit) > 0:
				#print("ADDING")
				#print(whichisit)	
				#print(type(whichisit[0]))
				keys = list(phenotype_labels_df["id"][whichisit[0]])
				if(len(keys) > 0):
					#print(keys)
					#print(keys[0])
					#print(phenotype_labels_df["label"][whichisit[0]])
		
					bicluster_phenotype_ids.append(keys[0])
					done = True
			#else:
			#	bicluster_phenotype_labels.append("none")
		
			#print(done)
			#if not done:
				#print("NONE")
				#bicluster_phenotype_ids.append("none")	
		
		print(bicluster_phenotype_ids)		
		print(bg_data[1:10])
		enr = aset.enrichment_test(subjects=bicluster_phenotype_ids, background=bg_data, threshold=1, labels=True)

		print(enr)
		sys.exit()