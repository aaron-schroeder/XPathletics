venv:
	rm -rf env/
	python3 -m venv env

init:
	pip install -r requirements_dev.txt

apidoc:
	rm -f docs/source/*.rst
	sphinx-apidoc -f -o docs/source/ adspackage

doc:
	make apidoc
	make -C docs/ clean
	make -C docs/ html

test:
	python -m unittest discover -s 'tests' -p 'test*.py' -v

clean:
	rm -Rf *.egg-info build dist

testpublish:
	# git push origin && git push --tags origin
	$(MAKE) clean
	# pip install --quiet twine wheel
	# pip install twine wheel
	# python setup.py bdist_wheel
	python setup.py sdist bdist_wheel
	twine check dist/*
	twine upload -r testpypi dist/*
	# $(MAKE) clean

publish:
	# git push origin && git push --tags origin
	$(MAKE) clean
	# pip install --quiet twine wheel
	pip install twine wheel
	python setup.py sdist bdist_wheel
	twine check dist/*
	twine upload dist/*
	# $(MAKE) clean

# EXAMPLE TASKS FOR FUTURE

# clean-pyc:
#   find . -name '*.pyc' -exec rm --force {} +
#   find . -name '*.pyo' -exec rm --force {} +
#   name '*~' -exec rm --force  {}

# clean-build:
#   rm --force --recursive build/
#   rm --force --recursive dist/
#   rm --force --recursive *.egg-info

# isort:
#   sh -c "isort --skip-glob=.tox --recursive . "

# lint:
#   flake8 --exclude=.tox

# run:
#   python manage.py runserver
