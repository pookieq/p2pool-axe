import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'cee2caff'.decode('hex')
P2P_PORT = 19937
ADDRESS_VERSION = 140
SCRIPT_ADDRESS_VERSION = 19
RPC_PORT = 19998
RPC_CHECK = defer.inlineCallbacks(lambda axed: defer.returnValue(
            'axeaddress' in (yield axed.rpc_help()) and
            (yield axed.rpc_getinfo())['testnet']
        ))
BLOCKHASH_FUNC = lambda data: pack.IntType(256).unpack(__import__('axe_hash').getPoWHash(data))
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('axe_hash').getPoWHash(data))
BLOCK_PERIOD = 150 # s
SYMBOL = 'tAXE'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'AxeCore') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/AxeCore/') if platform.system() == 'Darwin' else os.path.expanduser('~/.axecore'), 'axe.conf')
BLOCK_EXPLORER_URL_PREFIX = 'https://test.explorer.axe.org/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'https://test.explorer.axe.org/address/'
TX_EXPLORER_URL_PREFIX = 'https://test.explorer.axe.org/tx/'
SANE_TARGET_RANGE = (2**256//2**32//1000000 - 1, 2**256//2**20 - 1)
DUST_THRESHOLD = 0.001e8
