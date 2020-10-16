all: plot.pdf

plot.pdf: plot.py
	python plot.py

clean:
	rm -f plot.pdf

.PHONY: all clean
