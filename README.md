Python:

<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg">
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)



# Python Project Template

A basic Python project template. Just what I want to start projects with.


### Base Stuff
The things and stuff it does!

- Bash scripts to handle generic work
    - install, run test, make docs, flake8, clear cache, autoflake, isort
    - easy to create a start app bash script
- requirements folder
 - requirements.txt references prd.txt
 - install script installs both prd and dev libraries
- pre-commit config
- setup.cfg for pytest, black, isort, flake8,ect..
- gunicorn config if needed
- .env_sample for external configuration
    - cp .env_sample .env
- docker
    - simple dockerfile
    - docker-compose


### Mark Down CheatSheet
https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

### Code Block Examples

**Python 3**
```python
# -*- coding: utf-8 -*-
"""
a doc string
"""
from devsetgo_lib.file_functions import create_sample_files


def main(file_name: str):
    # start something like test files :-)
    create_sample_files(file_name, sample_size=100)
    return "complete"


if __name__ == "__main__":
    # start the main process
    main()
```

**JavaScript Example**
```javascript
var s = "JavaScript syntax highlighting";
alert(s);
```

**No Code Type Indicated Example**
```
No language indicated, so no syntax highlighting.
But let's throw in a <b>tag</b>.
```
