# ex: set ts=8 noet:

all: qt6 test

test:
	python3 -m unittest discover tests

qt6:
	pyrcc6 -o libs/resources.py resources.qrc

clean:
	rm -rf ~/.labelImgSettings.pkl *.pyc dist labelImg.egg-info __pycache__ build

pip_upload:
	python3 setup.py upload

long_description:
	restview --long-description

.PHONY: all
