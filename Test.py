import urllib2

query="""
DEFINE
	c0='/data/gene_disease_score_onexus',
	c1='/data/diseases',
	c2='/data/genes',
	c3='/data/sources'
ON
	'http://bitbucket.org/janis_pi/disgenet_onexus.git'
SELECT
	c1 (cui, name, cui, name, diseaseClassName, STY, cui, name),
	c2 (geneId, name, geneId, name, uniprotId, description, pathName, pantherName, geneId, name),
	c0 (score, score, diseaseId, pmids, geneId, diseaseId, geneId, pmids, diseaseId, pmids, pmids, geneId)
FROM
	c0
WHERE
	(
		c1 = 'Obeasity'
	AND
		c3 = 'ALL'
	)
ORDER BY
	c0.score DESC"""

req = urllib2.Request("http://www.disgenet.org/oql")
res = urllib2.urlopen(req, query)
print type(res)
print res.read()
