### E.T.-FPU
Expenses tracker for personal use, and this is cs50 final project

#### Requirement :
  - sqlite3 
  - yaml
  ```sh
  pip install pyyaml sqlite3
  ```
  
#### Usage :
#
Using with out option:
```sh
python main.py
```

Deposit an amount of money:
```sh
python main.py -i 200
```

Withdraw an amount of money
```sh
python main.py -w 200
```

Date and Note can be specify
```sh
python main.py -i 200 -d 2023-1-1 -n food
```

For help 
```sh
python main.py -h
```
#### Config :
Default yaml file format is
[`config.yml`](https://github.com/nacs-970/E.T-FPU/blob/main/config.yml)
