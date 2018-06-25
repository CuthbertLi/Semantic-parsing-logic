report.pdf: report.tex report.bib
	latex --output-format=pdf report
	bibtex report
	latex --output-format=pdf report
	latex --output-format=pdf report
	rm *.aux *.bbl *.log *.out *.blg *.toc