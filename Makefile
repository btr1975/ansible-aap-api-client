# Makefile for project needs
# Author: Ben Trachtenberg
# Version: 2.0.0
#

.PHONY: info build build-container coverage format pylint pytest start-container stop-container remove-container \
        gh-pages check-security pip-export

info:
	@echo "make options"
	@echo "    build               To build a distribution"
	@echo "    build-container     To build a container image"
	@echo "    coverage            To run coverage and display ASCII and output to htmlcov"
	@echo "    format              To format the code with black"
	@echo "    pylint              To run pylint"
	@echo "    pytest              To run pytest with verbose option"
	@echo "    start-container     To start the container"
	@echo "    stop-container      To stop the container"
	@echo "    remove-container    To remove the container"
	@echo "    gh-pages           To create the GitHub pages"

all: format pylint coverage check-security pip-export

build:
	@uv build --wheel --sdist

coverage:
	@uv run pytest --cov --cov-report=html -vvv

format:
	@uv run black ansible_aap_api_client/
	@uv run black tests/

pylint:
	@uv run pylint ansible_aap_api_client/

pytest:
	@uv run pytest --cov -vvv

gh-pages:
	@rm -rf ./docs/source/code
	@uv run sphinx-apidoc -o ./docs/source/code ./ansible_aap_api_client
	@uv run sphinx-build ./docs ./docs/gh-pages

check-security:
	@uv run bandit -c pyproject.toml -r .

pip-export:
	@uv export --no-dev --no-emit-project --no-editable > requirements.txt
	@uv export --no-emit-project --no-editable > requirements-dev.txt

build-container:
	@cd containers && podman build --ssh=default --build-arg=build_branch=main -t ansible-aap-api-client:latest -f Containerfile

start-container:
	@podman run -itd --name ansible-aap-api-client -p 8080:8080 localhost/ansible-aap-api-client:latest

stop-container:
	@podman stop ansible-aap-api-client

remove-container:
	@podman rm ansible-aap-api-client



