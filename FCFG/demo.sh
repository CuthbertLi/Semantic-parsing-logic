python3 generate.py > output.tex
latex --output-format=pdf output
rm *.out *.aux *.log
xdg-open output.pdf