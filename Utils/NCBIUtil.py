from BeautifulSoup import BeautifulSoup
import urllib2
import os
from DiseaseUtil import DiseaseUtil
class UniprotUtil():

	utils = None
	def __init__(self, diseaseName):
		global utils
		utils = DiseaseUtil(diseaseName)

	def generateFasta(self):
		conn = urllib2.urlopen('http://www.uniprot.org/uniprot/%s.fasta' % utils.getUniprotID())
		soup = BeautifulSoup(conn)
		div = soup.find('pre')
		output =  str(soup).replace('&gt;', '>')
		file = open('../FASTA/' + utils.getUniprotID() + '.fasta', 'w')
		file.write(output)
		file.close()

def main():
	x = UniprotUtil('Diabetes')
	x.generateFasta()

if __name__ == '__main__':
	main()