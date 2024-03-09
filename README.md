
# Pig-Game
<p align="center">
<a href="https://github.com/SchwarzNikolas/Pig-Game/actions"><img alt="Actions Status" src="https://github.com/SchwarzNikolas/Pig-Game/actions/workflows/python-app.yml/badge.svg"></a>
<a href="https://github.com/psf/black/blob/main/LICENSE"><img alt="License: MIT" src="https://black.readthedocs.io/en/stable/_static/license.svg"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>
Python implementation of the Pig Dice Game.

## Table of contents
- [Pig-Game](#pig-game)
   * [Rules](#rules)
   * [Installation](#installation)
   * [Usage](#usage)
   * [Testing](#testing)
   * [Documentation](#documentation)
   * [License](#license)

## Rules
This is a dice game played to reach a target scoreof 100 points.
Players take turns rolling a dice.
If a player rolls a 1, they lose their points for that turn and then it's the next player's turn.
Otherwise, they can keep rolling and adding points, or choose to hold and keep their accumulated points.
The first player to reach or exceed the target score wins when they hold.

## Installation

Clone the repository:
```bash
git clone https://github.com/SchwarzNikolas/Pig-Game.git
```
Use the [make](https://www.gnu.org/software/make/) to create a virtual python environment:
```bash
make venv
```
Install required libraries:
```bash
make install
```
Start the application:
```bash
make start
```

## Usage

```python
import foobar

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## Testing

To unittest the classes enter venv:
 - For Unix and MacOS:
  ```. .venv/bin/activate```
  - For Windows:
  ```. .venv/Scripts/activate```

Start the Unittests:
```bash
make coverage
```

To test the code structure run:
```bash
make lint
```

## Documentation
All the documentation can be found in the **[doc](https://github.com/SchwarzNikolas/Pig-Game/tree/main/doc)** folder.

## License

[MIT](https://choosealicense.com/licenses/mit/)
