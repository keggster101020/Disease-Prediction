from Utils.DiseaseUtil import DiseaseUtil
from Utils.UniprotUtil import UniprotUtil
from Utils.Alignment import Alignment
import os.path
import glob


def main():
	

	search_disease = raw_input('Enter the name or umls of the disease: ')
	umls = False
	if 'umls' in search_disease:
		umls = True

	diseaseU = DiseaseUtil(search_disease, umls=umls)
	uniprot = UniprotUtil(search_disease, umls=umls)
	align = Alignment()

	if not os.path.isfile('FASTA/%s.fasta' % diseaseU.getName()):
		uniprot.generateFasta()

	likelyhood = diseaseU.getScore()

	clean,dirty = getFastaFiles(diseaseU.getName())

	if clean == None or dirty == None:
		return

	align_score = align.calculateMutationPercentage(clean,dirty)

	print 'Your likelyhood for devloping {0} is: \033[31m{1:.2f}\033[0m%'.format(diseaseU.getName(), round(likelyhood*align_score,2))


def getFastaFiles(diseaseName):
	seq1 = open('FASTA/%s.fasta' % diseaseName)
	header = seq1.readline()
	seq1 = seq1.read().replace('\n','')

	if os.path.isfile('YOU/%s.fasta' % diseaseName):
		seq2 = open('YOU/%s.fasta' % diseaseName)
		seq2.readline()
		seq2 = seq2.read().replace('\n','')

	else:
		file = findFastaFile(header.split('|'))
		if file == None:
			print "Unable to locate file in YOU/ directory ending..."
			return [None,None]
		file.readline()
		seq2 = file.read().replace('\n','')

	return [seq1, seq2]

#Checks to see if any of the identifiers in the first line of a file are the name of a file in the YOU/ directory
def findFastaFile(header):
	os.chdir("YOU/")
	for file in glob.glob("*.fasta"):
		for section in header:
			if section in file:
				return open(file)
	return None


if __name__ == '__main__':main()