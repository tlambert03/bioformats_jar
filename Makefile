.PHONY: buildstubs

buildstubs:
	pip install git+https://gitlab.cern.ch/scripting-tools/stubgenj.git
	python -m stubgenj --classpath 'bioformats_jar/bioformats_package.jar:/Applications/Fiji.app/jars/*.jar' loci
	rm -rf jpype-stubs bioformats_jar/_loci
	find loci-stubs -type f -exec sed -i '' 's/ loci\./ bioformats_jar\._loci\./g' {} +
	find loci-stubs -type f -exec sed -i '' 's/import loci/import bioformats_jar\._loci/g' {} +
	mv loci-stubs bioformats_jar/_loci
