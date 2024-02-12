# MineTest Log Data Extractor
MT log data extractor is a python module that extracts data from Minetest logs.
# License
Minetest log data extractor is a Open Source project under the MIT License (see [LICENSE](./LICENSE) file for details).
# Installing
Currently, there is no pip package for this module, so you will need to install it manually:
- Download this module from [here](https://github.com/Miner34dev/Minetest-log-data-extractor/archive/refs/heads/main.zip)
- Extract the archive
- go into the extracted folder using ```cd```
- copy mt_log_data_extractor.py into your python installation's site-packages folder
# Getting started
Import this module:
```python3
from mt_log_data_extractor import import_mt_log
```
Now, to get your data, use:
```python3
import_mt_log(mt_log_path)
```