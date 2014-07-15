# bitcoind-chainstats
index interesting stats from the blockchain using bitcoind JSON-RPC

produced by Amphibian (azeteki, atelopus_zeteki)

## dependencies
* tested with python 2.7.3, bitcoind 0.9.2.1
* jgarzik's bitcoinrpc library (https://github.com/jgarzik/python-bitcoinrpc)

## usage
rename example.conf to bitcoind-chainstats.conf and enter your details.

the program will die hard if the config file is incorrect or it fails to connect.

this will be improved in a later release.
 
## launch
Replace 'python' with 'python2' if you also have python3 installed.
```
# list all blocks
$ python main.py
$ python main.py -c some_other_config_file.conf

# list blocks in range 100000 - 100999
$ python main.py 100000 1000

# output to file
$ python main.py > some_data_file
```

## example output
```
$ python main.py 0 1
# height                                                           hash        time interval  chainwork            diff     size    tx     coinbase        fees  fee_per_tx  fee_per_kb
000000 000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f  1231006505        0  32.000022               1      285     1   0.00000000  0.00000000  0.00000000  0.00000000
# end
```

## frog food
found bitcoind-chainstats useful? donations are your way of showing that!

my main machine is currently a 6 year old Atom laptop. upgrading that would be rather useful. cheers!

![ScreenShot](/screenshots/donation-qr.png)

**1FrogqMmKWtp1AQSyHNbPUm53NnoGBHaBo**
