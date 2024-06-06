install:
	poetry install

gendiff:
	poetry run gendiff

selfcheck:
	poetry check

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

check: selfcheck test lint

build:	selfcheck lint
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

reinstall-package:
	python3 -m pip install --user --force-reinstall dist/*.whl
