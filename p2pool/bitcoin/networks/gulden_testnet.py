import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'fcfef700'.decode('hex') #pchmessagestart
P2P_PORT = 9923
ADDRESS_VERSION = 98 #pubkey_address
RPC_PORT = 9924
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'Guldenaddress' in (yield bitcoind.rpc_help()) and
            (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 100*100000000 >> (height + 1)//840000
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD = 150 # s
SYMBOL = 'NLG'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Gulden') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Gulden/') if platform.system() == 'Darwin' else os.path.expanduser('~/.Gulden'), 'Gulden.conf')
BLOCK_EXPLORER_URL_PREFIX = 'https://blockchain.gulden.com/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'https://blockchain.gulden.com/address/'
TX_EXPLORER_URL_PREFIX = 'https://blockchain.gulden.com/tx/'
SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.03e8
