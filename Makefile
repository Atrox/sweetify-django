.PHONY: install test

install:
	@poetry install

test:
	@DJANGO_SETTINGS_MODULE=tests.test_settings pytest
