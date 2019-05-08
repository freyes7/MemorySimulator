import tabulate
from Page import Page
class Output:

	@staticmethod
	def displayPages(pagesArray):
		for page in pagesArray:
			print page.process.size
