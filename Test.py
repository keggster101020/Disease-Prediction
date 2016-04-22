import urllib2

query="""
DEFINE
	c0='/data/gene_disease_summary',
	c1='/data/diseases',
	c2='/data/genes',
	c3='/data/gene_roles',
	c4='/data/sources'
ON
	'http://www.disgenet.org/web/DisGeNET'
SELECT
	c1 (cui, name, cui, name, type, diseaseClassName, STY, cui, name),
	c2 (geneId, name, geneId, name, uniprotId, description, pathName, pantherName, geneId, name),
	c3 (PI, PL),
	c0 (score, score, diseaseId, pmids, geneId, diseaseId, geneId, pmids, diseaseId, pmids, pmids, geneId, snps, diseaseId, geneId, sourceId, snps, diseaseId, geneId, sourceId)
FROM
	c0
WHERE
	(
		c1 = 'umls:C0011847'
	AND
		c4 = 'ALL'
	)
ORDER BY
	c0.score DESC"""

req = urllib2.Request("http://www.disgenet.org/oql")
res = urllib2.urlopen(req, query)
print res.read()
