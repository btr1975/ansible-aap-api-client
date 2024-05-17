@ECHO OFF
REM Makefile for project needs
REM Author: Ben Trachtenberg
REM Version: 1.0.5
REM

IF "%1" == "build" (
    python -m build
    GOTO END
)

IF "%1" == "coverage" (
    pytest --cov --cov-report=html -vvv
    GOTO END
)

IF "%1" == "pylint" (
    pylint ansible_aap_api_client\
    GOTO END
)

IF "%1" == "pytest" (
    pytest --cov -vvv
    GOTO END
)

IF "%1" == "format" (
    black ansible_aap_api_client/
    black tests/
    GOTO END
)


IF "%1" == "gh-pages" (
    rmdir /s /q docs\source\code
    sphinx-apidoc -o ./docs/source/code ./ansible_aap_api_client
    sphinx-build ./docs ./docs/gh-pages
    GOTO END
)


@ECHO make options
@ECHO     build     To build a distribution
@ECHO     coverage  To run coverage and display ASCII and output to htmlcov
@ECHO     format    To format the code with black
@ECHO     pylint    To run pylint
@ECHO     pytest    To run pytest with verbose option
@ECHO     gh-pages  To create the GitHub pages

:END
