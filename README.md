# Running the application

### requirements

`Python 3.6`

### install packages
```
pip install -r requirements.txt
```

### run the application:
```
cd pacman-py
python pacman.py

#specify a custom input filename (this file has an error in the input)
python pacman.py -i test_resources/input_coord_error.txt
```

### run tests:
```
cd pacman-py
python -m "nose"
#
#........................
#----------------------------------------------------------------------
#Ran 24 tests in 0.090s
#
#OK
```

### run type checking:
```
cd pacman-py
mypy pacman.py
```

# Comments 

### Logger

The config file in `resources/logging.yaml` for granular logging settings.
Each level can be setup independently and the formatting can be changed.

### Separation of concerns 

- `app.board` is not coupled with any other class which make it easily testable
- `app.the_pacman` is not coupled with any other class which make it easily testable
- `app.game_orchestrator` is using the input_data to setup the game and create the board and pacman. This class only has one function which play the game.

-`resources` package play the role of loading the inputs (just 1 input in this case). I use `typing` and `NamedTuple` for more robustness.
- `test_resources` is used in `resource_loader_test.py`

- `pacman.py` if the main application. It just load the input, create the game orchestrator and call the play method. It uses `argparse` to add command line options such as the input file name.




