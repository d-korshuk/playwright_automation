# Tala AQA framework

## Install and Setup
0. Clone the repo https://github.com/d-korshuk/playwright_automation.git

1. Go to the directory with already cloned repo and create a virtual env (https://docs.python.org/3/library/venv.html)

2. Install all the dependencies
pip install -r requirements.txt

## Test execution
Command to run tests:
```commandline
pytest -m <mark> -n <amount>
```
* `-m` - test mark, see [Pytest documentation](https://docs.pytest.org/en/6.2.x/example/markers.html)
* `-n` - amount of threads to parallelize test execution (we use `pytest-xdist` plugin for this). _(Optional flag)_
* `--alluredir` - path to the folder where temporary files for Allure reports will be stored. (for more info about Allure see the section below)

