.PHONY: lint ontology-service decision-engine docker-build

lint:
	flake8 ontology decision-engine
ontology-service:
	cd ontology && python3 -m build && docker build -t ontology-service .
decision-engine:
	cd decision-engine && python3 -m build && docker build -t ontology-service .

docker-build: decision-engine decision-engine
