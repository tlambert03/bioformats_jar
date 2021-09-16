.PHONY: buildstubs download

download:
	curl -L -o bioformats_jar/bioformats_package.jar https://downloads.openmicroscopy.org/bio-formats/latest/artifacts/bioformats_package.jar
	python -c "import bioformats_jar; print(bioformats_jar.__version__)"

buildstubs:
	pip install git+https://gitlab.cern.ch/scripting-tools/stubgenj.git
	python -m stubgenj --classpath 'bioformats_jar/bioformats_package.jar:/Applications/Fiji.app/jars/*.jar' loci ome
	rm -rf jpype-stubs bioformats_jar/_loci

	find loci-stubs -type f -exec sed -i '' 's/ loci\./ bioformats_jar\._loci\./g' {} +
	find loci-stubs -type f -exec sed -i '' 's/import loci/import bioformats_jar\._loci/g' {} +
	mv loci-stubs bioformats_jar/_loci

	find ome-stubs -type f -exec sed -i '' 's/ ome\./ bioformats_jar\._ome\./g' {} +
	find ome-stubs -type f -exec sed -i '' 's/import ome/import bioformats_jar\._ome/g' {} +
	mv ome-stubs bioformats_jar/_ome
