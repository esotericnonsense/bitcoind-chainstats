#!/usr/bin/env python
import math
from decimal import *

def strip_block(full_block):
    block = {}
    block['height'] = full_block['height']
    block['hash'] = full_block['hash']
    block['time'] = full_block['time']
    block['size'] = full_block['size']
    block['difficulty'] = full_block['difficulty']
    block['transactions'] = len(full_block['tx'])
    block['chainwork'] = math.log(int(full_block['chainwork'], 16), 2)
    if 'nextblockhash' in full_block:
        block['nextblockhash'] = full_block['nextblockhash']

    if 'coinbase_amount' in full_block:
        block['coinbase_amount'] = full_block['coinbase_amount']
        if block['height'] < 210000:
            block_subsidy = Decimal(50)
        elif block['height'] < 420000:
            block_subsidy = Decimal(25)

        if block_subsidy and (block['transactions'] > 1):
            block['fees'] = block['coinbase_amount'] - block_subsidy
            block['fees_per_tx'] = Decimal(block['fees']) / Decimal(block['transactions'] - 1)
            block['fees_per_kb'] = Decimal(block['fees']) * 1024 / Decimal(block['size'])
        else:
            block['fees'] = 0
            block['fees_per_tx'] = 0
            block['fees_per_kb'] = 0
    else:
        block['coinbase_amount'] = 0
        block['fees'] = 0
        block['fees_per_tx'] = 0
        block['fees_per_kb'] = 0

    if 'nethash144' in full_block:
        block['nethash144'] = full_block['nethash144']
    else:
        block['nethash144'] = 0

    if 'nethash432' in full_block:
        block['nethash432'] = full_block['nethash432']
    else:
        block['nethash432'] = 0

    if 'nethash1008' in full_block:
        block['nethash1008'] = full_block['nethash1008']
    else:
        block['nethash1008'] = 0

    return block
