#!/usr/bin/env python

###############################################################################
# bitcoind-chainstats by esotericnonsense
# thanks to jgarzik for bitcoinrpc
# and of course the bitcoin dev team for that bitcoin gizmo, pretty neat stuff
###############################################################################

import ConfigParser, argparse, sys 

import rpc
import process

def main_loop(rpchandle, args):
    block = rpc.getblock(rpchandle, args.starting_block)
    lastblock = block['time']

    if args.labels:
        header= "height                                                             hash        time interval"
        header += "  chainwork            diff             nethash144             nethash432            nethash1008     size"
        header += "    tx     coinbase        fees  fee_per_tx  fee_per_kb"
        print header

    while block['height'] < args.starting_block + args.blocks_to_get:
        if block:
            block = process.strip_block(block)

            block['interval'] = block['time'] - lastblock
            lastblock = block['time']

            string = "%06d" % block['height']
            string += " " + block['hash']
            string += " " + "% 10d" % block['time']
            string += " " + "% 8d" % block['interval']
            string += " " + "% 9.6f" % block['chainwork']
            string += " " + "% 15d" % block['difficulty']
            string += " " + "% 22d" % block['nethash144']
            string += " " + "% 22d" % block['nethash432']
            string += " " + "% 22d" % block['nethash1008']
            string += " " + "% 8d" % block['size']
            string += " " + "% 5d" % block['transactions']
            string += " " + "% 12.8f" % block['coinbase_amount']
            string += " " + "% 10.8f" % block['fees']
            string += " " + "% 10.8f" % block['fees_per_tx']
            string += " " + "% 10.8f" % block['fees_per_kb']

            print string

            if not (block['height'] % 50) and not block['height'] == args.starting_block:
                string = "progress: block " + "% 6d" % block['height'] + "\n"
                sys.stderr.write(string)

            if 'nextblockhash' in block:
                block = rpc.getblock(rpchandle, block['nextblockhash'])

            else:
                break

        else:
            break
    
    string = "last: block " + "% 6d" % block['height'] + "\n"
    sys.stderr.write(string)

if __name__ == '__main__':
    # parse commandline arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config",
                        help="path to config file [bitcoind-chainstats.conf]",
                        default="bitcoind-chainstats.conf")
    parser.add_argument("-l", "--labels",
                        help="print column labels before data",
                        action="store_true")
    parser.add_argument('starting_block', type=int, nargs="?",
                        help='block to start from',
                        default=0)
    parser.add_argument('blocks_to_get', type=int, nargs="?",
                        help='number of blocks to query',
                        default=1000000)
    args = parser.parse_args()

    # parse config file
    config = ConfigParser.ConfigParser()
    config.read(args.config)

    rpchandle = rpc.init(config)
    if not rpchandle: # TODO: this doesn't appear to trigger, investigate
        print "failed to connect to bitcoind"
        sys.exit(1)
    
    info = rpchandle.getinfo()
    if not info:
        print "first getinfo failed (failed to connect to bitcoind?)"
        sys.exit(1) 

    main_loop(rpchandle, args)
