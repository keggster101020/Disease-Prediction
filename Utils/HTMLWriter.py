import os
from shutil import copyfile

"""
Keegan Shudy
This class is used for all html file output writing
"""
class HTMLWriter():

	row = ''
	def __init__(self):
		global row
		row = """
				<tr>
					<td>{0}</td>
					<td>{1}</td>
				</tr>
			  """

	#Write the disease name and percent likely chance to the HTML table 
	#then overwrite the origional to make it an ongoing document
	def writeTableOutput(self, diseaseName, percentLikely):
		global row
		print os.getcwd()
		with open('HTML/clean.html') as fout, open('HTML/index.html', 'w') as nfout:
			for line in fout:
				nfout.write(line)
				if 'id="table-body"' in line:
					nfout.write(row.format(diseaseName,percentLikely))

		os.remove('HTML/clean.html')
		copyfile('HTML/index.html', 'HTML/clean.html')

		fout.close()
		nfout.close()


