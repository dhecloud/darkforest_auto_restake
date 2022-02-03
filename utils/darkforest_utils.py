from utils.node_utils import get_w3_rpc
from utils.contract_utils import load_contract
import json
import time
import random
import logging


w3 = get_w3_rpc('https://polygon-rpc.com/')

logging.info(f'Connected: {w3.isConnected()}')



def exitForest(info, unicorn_num): #unstake
    addr = info['sender_address']
    pkey = info['private']
    uni_hex = hex(unicorn_num).lstrip('0x').zfill(64)
    data = '0x64e8456b' + uni_hex

    nonce = w3.eth.get_transaction_count(addr)
    tx = {
                'chainId': 137,
                'to': '0x8d528e98A69FE27b11bb02Ac264516c4818C3942',
                'from': addr,
                'data': data,
                'gas': 500000,
                'gasPrice': w3.toWei(50,'gwei'),
                'nonce': nonce,
                }

    signed_txn = w3.eth.account.sign_transaction(tx, private_key=pkey)
    w3.eth.send_raw_transaction(signed_txn.rawTransaction)


def safeTransferFrom(info, unicorn_num):
    addr = info['sender_address']
    pkey = info['private']
    data = '0xb88d4fde' #method
    data += info['sender_address'].lstrip('0x').zfill(64) # padded wallet addres
    data += '0000000000000000000000008d528e98a69fe27b11bb02ac264516c4818c3942' # to
    uni_hex = hex(unicorn_num).lstrip('0x').zfill(64)
    data += uni_hex
    data += '000000000000000000000000000000000000000000000000000000000000008000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000' #dunno whats this but its the same for everyone
    assert(len(data)==394)
    nonce = w3.eth.get_transaction_count(addr)
    tx = {
                'chainId': 137,
                'to': '0xdC0479CC5BbA033B3e7De9F178607150B3AbCe1f',
                'from': addr,
                'data': data,
                'gas': 500000,
                'gasPrice': w3.toWei(50,'gwei'),
                'nonce': nonce,
                }

    signed_txn = w3.eth.account.sign_transaction(tx, private_key=pkey)
    w3.eth.send_raw_transaction(signed_txn.rawTransaction)
