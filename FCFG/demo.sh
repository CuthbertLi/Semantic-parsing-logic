python3 fcfg.py > output.tex
latex --output-format=pdf output
rm *.out *.aux *.log
xdg-open output.pdf