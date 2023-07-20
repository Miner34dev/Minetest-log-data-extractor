# MineTest Log Data Extractor
MT log data extractor is a python module that extracts data from Minetest logs. You can track almost anything like block changes and players getting hurted and transform them into anything you want.
# License
Minetest log data extractor is a Open Source project under the MIT License (see [LICENSE](./LICENSE) file for details).
# Installing
Currently, there is no pip package for this module, so you will need to istall it manually (Steps valid for Linux, MacOS and Windows):
- Download this module from [here](https://github.com/Miner34dev/Minetest-log-data-extractor/releases) or, for the latest development version, [here](https://github.com/Miner34dev/Minetest-log-data-extractor/archive/refs/heads/main.zip)
- Extract the archive
- go into the extracted folder using ```cd```
- Run ```python setup.py install --user``` (Without ```--user``` to install globally)
# Getting started
Import this module:
```python3
from mt_log_data_extractor import import_mt_log
```
Now, to get your data, use:
```python3
import_mt_log(file) #with a path such as /home/username/.minetest/debug.txt (linux example) instead of file
```
example:
```python3
mt_actions = import_mt_log("/home/hugo/.minetest/debug.txt")
```
What does this module output? Well, the answer is not that simple.
Here is the tree of an example output:
```
{"2023":
	| {"07":
	|	| {"20":
	|	|	| {"13":
	|	|	|	| {"01":
	|	|	|	|	| {"24":
	|	|	|	|	|	| [
	|	|	|	|	|	|	| "player1"
	|	|	|	|	|	|	| "joins game"
	|	|	|	|	|	| ]
	|	|	|	|	| }
	|	|	|	|	| {"36":
	|	|	|	|	|	| [
	|	|	|	|	|	|	| "player1"
	|	|	|	|	|	|	| "digs"
	|	|	|	|	|	|	| "(12, 4, 105)"
	|	|	|	|	|	| ]
	|	|	|	|	| }
	|	|	|	| }
	|	|	|	| {"02":
	|	|	|	|	| {"12":
	|	|	|	|	|	| [
	|	|	|	|	|	|	| "Server:"
	|	|	|	|	|	|	| "Shutting down"
	|	|	|	|	|	| ]
	|	|	|	|	| }
	|	|	|	| }
	|	|	| }
	|	| }
	| }
}
```
# Contributing
If you would like to contribute to this project you can do so through GitHub by forking the repository and sending a pull request (PR). You can also simply report bugs.

**We also need a icon for this project.**
