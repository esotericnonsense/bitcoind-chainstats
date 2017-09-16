# bitcoind-chainstats
index interesting stats from the blockchain using bitcoind JSON-RPC

produced by esotericnonsense

## NOTE - this repository is no longer maintained.

## dependencies
* tested with python 2.7.3, bitcoind 0.9.2.1
* jgarzik's bitcoinrpc library (https://github.com/jgarzik/python-bitcoinrpc)

## usage
rename example.conf to bitcoind-chainstats.conf and enter your details.

the program will die hard if the config file is incorrect or it fails to connect.
 
## usage
Replace 'python' with 'python2' if you also have python3 installed.
```
main.py [-h] [-c CONFIG] [-l] [starting_block] [blocks_to_get]

# list all blocks
$ python main.py

# list from 200000 to 200999 with column labels
$ python main.py -l 200000 1000
```

## example output
```
$ python main.py --labels 200000 5
height                                                             hash        time interval  chainwork            diff             nethash144             nethash432            nethash1008     size    tx     coinbase        fees  fee_per_tx  fee_per_kb
200000 000000000000034a7dedef4a161fa058a2d67a173a90155f3a2fe6fc132e0ebf  1348310759        0  68.741562         2864140         25105260243619         23066050181816         22281735686656   247533   388  50.63517500  0.63517500  0.00164128  0.00262761
200001 00000000000002e3269b8a00caf315115297c626f954770e8398470d7f387e1c  1348310843       84  68.741598         2864140         25576851568601         23096853150357         22299743830620    11068    32  50.00520000  0.00520000  0.00016774  0.00048110
200002 00000000000001d164de39e85839b49d68d55604415b264820de242cb3863f0e  1348312090     1247  68.741634         2864140         25499167450551         23020140938324         22249412353405   182188    18  50.09950000  0.09950000  0.00585294  0.00055925
200003 0000000000000566faa9fa71f77bf56b3494cbc56d5974b9f12cfb1969077582  1348311399     -691  68.741670         2864140         25780838043250         23023311177595         22279760035155    31501    85  50.04905000  0.04905000  0.00058393  0.00159446
200004 000000000000032e1219acd8cdda073f5cbb42a216fede788ad4b555e7969a26  1348311812      413  68.741706         2864140         26040825619842         23064916104200         22315676629662     3535     5  50.00000000  0.00000000  0.00000000  0.00000000
```

## frog food
found bitcoind-chainstats useful? donations are your way of showing that!

my main machine is currently a 6 year old Atom laptop. upgrading that would be rather useful. cheers!

![ScreenShot](/img/donation-qr.png)

**bitcoin 3BYFucUnVNhZjUDf6tZweuZ5r9PPjPEcRv**
