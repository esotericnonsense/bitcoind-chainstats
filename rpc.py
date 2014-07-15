#!/usr/bin/env python
from bitcoinrpc.authproxy import AuthServiceProxy

def init(config):
    rpcuser = config.get('rpc', 'rpcuser')
    rpcpassword = config.get('rpc', 'rpcpassword')
    rpcip = config.get('rpc', 'rpcip')
    rpcport = config.get('rpc', 'rpcport')

    rpcurl = "http://" + rpcuser + ":" + rpcpassword + "@" + rpcip + ":" + rpcport
    try:
        rpchandle = AuthServiceProxy(rpcurl, None, 500)
        return rpchandle
    except:
        return False

def getblock(rpchandle, block_to_get):
    try:
        if (len(str(block_to_get)) < 7) and str(block_to_get).isdigit(): 
            blockhash = rpchandle.getblockhash(block_to_get)
        elif len(block_to_get) == 64:
            blockhash = block_to_get

        block = rpchandle.getblock(blockhash)

        try:
            raw_tx = rpchandle.getrawtransaction(block['tx'][0])
            decoded_tx = rpchandle.decoderawtransaction(raw_tx)

            coinbase_amount = 0
            for output in decoded_tx['vout']:
                if 'value' in output:
                    coinbase_amount += output['value']
            
            block['coinbase_amount'] = coinbase_amount
        except: pass

        try:
            block['nethash144'] = rpchandle.getnetworkhashps(144, block['height'])
            block['nethash432'] = rpchandle.getnetworkhashps(432, block['height'])
            block['nethash1008'] = rpchandle.getnetworkhashps(1008, block['height'])
        except: pass

        return block

    except:
        return 0
