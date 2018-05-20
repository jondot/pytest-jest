dist:
	rm -rf dist
	rm -rf build
	python setup.py sdist bdist_wheel
dist-install:
	python setup.py install
dist-release:
	make dist && make release
release:
	twine upload dist/*
wtf:
	rm -rf .cache
.PHONY: init install test dist
