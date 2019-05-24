all:
	mkdir -p build
	rm -f build/*
	cd build; texi2pdf ../dissertation.tex --output dissertation-snegrashov.pdf
clean:
	rm -r build
