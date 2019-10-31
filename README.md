# pipelining-pycon-talk
This repo contains the source code of the demos of the talk on `End to End Workflows` presented at Pycon Nigeria 2019
View the [Powerpoint presentation](https://drive.google.com/open?id=17-w5oIWQ-O4aVWivOGecywH2eb3IHn9jx-l5fxwnR6g)

<!--[![PyPI version](https://badge.fury.io/py/search-engine-parser.png)](https://badge.fury.io/py/search-engine-parser)-->
[![Build Status](https://travis-ci.com/bisoncorps/pipelining-pycon-talk.svg?branch=master)](https://travis-ci.com/bisoncorps/pipelining-pycon-talk)
[![Heroku App Status](http://heroku-shields.herokuapp.com/pycon-2019)](https://pycon-2019.herokuapp.com)
[![PyPI version](https://badge.fury.io/py/pycon.svg)](https://badge.fury.io/py/pycon)
<hr/>


## Installation
Installation can be done from [Test PyPi](https://test.pypi.org)
```bash
pip install --index-url https://test.pypi.org/simple/ pycon-ng2019 
```
### Development
- Install Development dependencies. Update the settings in the [manage.py](https://github.com/bisoncorps/pipelining-pycon-talk/blob/a3067872d7c8bb4f9d5f62273a71946691d69131/manage.py#L8) file to `django.settings.common` 

```bash
# install Dev dependencies
pip install -r dev-requirements.txt
```

- Start Server

```bash
python manage.py runserver
```

## Usage

### For cli demo
```python
  import pycon
  pycon.demo()
```
![CLI Image](assets/cli.gif)

### Django App
- Add `pycon` to `installed_apps`
- Add `path('', include('pycon.urls'))` to urls file

![Django Image](assets/django.gif)
Pycon-NG page should be available in http://localhost:8000/pycon
