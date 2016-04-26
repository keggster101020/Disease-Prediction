"""
Keegan Shudy
This class will be used to generate a fasta file (in protein format)
associated with the given Disease from the DiseaseUtil class
"""

from BeautifulSoup import BeautifulSoup
import urllib2
import os
from DiseaseUtil import DiseaseUtil
class UniprotUtil:

	utils = None
	def __init__(self, diseaseName, umls=False):
		global utils
		utils = DiseaseUtil(diseaseName, umls)

	def generateFasta(self):
		conn = urllib2.urlopen('http://www.uniprot.org/uniprot/%s.fasta' % utils.getUniprotID())
		soup = BeautifulSoup(conn)
		div = soup.find('pre')
		output =  str(soup).replace('&gt;', '>')
		file = open('FASTA/' + utils.getName() + '.fasta', 'w')
		file.write(output)
		file.close()
