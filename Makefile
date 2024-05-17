# Makefile for project needs
# Author: Ben Trachtenberg
# Version: 1.0.6
#

.PHONY: info build build-container coverage format pylint pytest start-container stop-container remove-container gh-pages

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

build:
	@python -m build


build-container:
	@cd containers && podman build --ssh=default --build-arg=build_branch=main -t ansible-aap-api-client:latest -f Containerfile




coverage:
	@pytest --cov --cov-report=html -vvv

format:
	@black ansible_aap_api_client/
	@black tests/

pylint:
	@pylint ansible_aap_api_client/

pytest:
	@pytest --cov -vvv


gh-pages:
	@rm -rf ./docs/source/code
	@sphinx-apidoc -o ./docs/source/code ./ansible_aap_api_client
	@sphinx-build ./docs ./docs/gh-pages



start-container:
	@podman run -itd --name ansible-aap-api-client -p 8080:8080 localhost/ansible-aap-api-client:latest

stop-container:
	@podman stop ansible-aap-api-client

remove-container:
	@podman rm ansible-aap-api-client



