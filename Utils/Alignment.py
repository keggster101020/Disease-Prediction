"""
Keegan Shudy 

This class is to handle the alignment scores for two given protein sequences
using the PAM30 matrix
"""

import Utils.UniprotUtil
from Bio import pairwise2
from Bio.SubsMat import MatrixInfo as matlist

class Alignment:

	matrix = matlist.pam30
	def __init__(self):
		global matrix
		matrix = matlist.pam30

	def align(self,seq1, seq2):
		alns = pairwise2.align.globaldx(seq1,seq2, matrix)
		return alns[0]

	def calculateMutationPercentage(self,seq1, seq2):
		alns = pairwise2.align.globaldx(seq1,seq1, matrix)
		maxScore = alns[0][2]
		alns = pairwise2.align.globaldx(seq1,seq2, matrix)
		lscore = alns[0][2]
		return (1-(lscore / maxScore)) * 100