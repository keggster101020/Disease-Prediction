"""
Keegan Shudy
This class will be used to query the DisGeNet database looking for a given disease name or ID
only the most related Gene associated with the disease will be returned
This class can then be used to retreve information about the disease
"""

import urllib2
class DiseaseUtil:
	query_result = None
	def __init__(self,diseaseName, umls=False):
		global query_result
		if umls:
			query=("""
			DEFINE
				c0='/data/gene_disease_summary',
				c1='/data/diseases',
				c2='/data/genes',
				c3='/data/gene_roles',
				c4='/data/sources'
			ON
				'http://www.disgenet.org/web/DisGeNET'
			SELECT
				c1 (cui, name, diseaseClassName, STY),
				c2 (uniprotId),
				c0 (score, diseaseId, pmids, geneId)
			FROM
				c0
			WHERE
				(
					c1 = '%s'
				AND
					c4 = 'ALL'
				)
			ORDER BY
				c0.score DESC
				""" % diseaseName)
		else:
			query=("""
			DEFINE
				c0='/data/gene_disease_summary',
				c1='/data/diseases',
				c2='/data/genes',
				c3='/data/gene_roles',
				c4='/data/sources'
			ON
				'http://www.disgenet.org/web/DisGeNET'
			SELECT
				c1 (cui, name, diseaseClassName, STY),
				c2 (uniprotId),
				c0 (score, diseaseId, pmids, geneId)
			FROM
				c0
			WHERE
				(
					c1.name = '%s'
				AND
					c4 = 'ALL'
				)
			ORDER BY
				c0.score DESC
				""" % diseaseName)


		req = urllib2.Request("http://www.disgenet.org/oql")
		query_result = urllib2.urlopen(req, query)
		query_result.readline()
		holder = query_result.readline()
		while holder.split('\t')[4] == 'null':
			holder = query_result.readline()

		query_result = holder

	def getCUI(self):
		return query_result.split('\t')[0]

	def getName(self):
		return query_result.split('\t')[1]

	def getDiseaseClass(self):
		return query_result.split('\t')[2]

	def getSTY(self):
		return query_result.split('\t')[3]

	def getUniprotID(self):
		return query_result.split('\t')[4]

	def getScore(self):
		return float(query_result.split('\t')[5])

	def getDiseaseID(self):
		return query_result.split('\t')[6]

	def getPMIDS(self):
		return query_result.split('\t')[7]

	def getGeneID(self):
		return query_result.split('\t')[8]
