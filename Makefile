all:
	mkdir -p build
	rm -f build/*
	cd build; texi2pdf ../dissertation.tex --output dissertation-snegrashov.pdf
	cd ..
	evince build/dissertation-snegrashov.pdf &
clean:
	git clean -fdX
