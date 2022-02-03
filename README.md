This repository helps you to exit your unicorn from the dark forest, and then restakes them. Please read the disclaimer before proceeding.

# Disclaimer
This repository was made so that i wouldn't have to manually restake my unicorns. This exposes your wallet's private key locally in the config file. Use this repository only if you understand what you are doing and at your own risk! I will not be responsible for any potential losses.

# What this repository does in specific terms
1. Unstake your unicorns from the dark forest.
2. Restakes your unicorns into the dark forests. $UNIM are automatically collected into your wallet

This repository assumes all tokens are all already approved. This repository does NOT take care of token approvals. If you are unsure how to perform token approvals, simply just go through the whole staking process once.


# Prerequisites
1. `python>3.8`   
2. `pip install web3`

# Setting Up
1. `git clone git@github.com:dhecloud/`
2. `cd darkforest_auto_restake`
3. Modify/change the `config.py` parameters using your text editor to include your unicorn numbers
4. After setting up, run `nohup python restake_unicorns.py &` for the python script to run in the background. Alternatively, you can use `screen` instead of the `nohup`. Depends on your preference.

## Config parameters
1. `ADDR`         - your wallet public address
2. `PRIVATE_KEY`  - your wallet private key. IMPORTANT!
3. `unicorns`     - your unicorn numbers.
4. `RESTAKE_FREQ`- time (seconds) between each restaking run. default: 86400 (1 day)
5. `TX_INTERVALS` - time (seconds) between each transaction. > 30 is best just in case network is congested. default: 30


# Support me
If this repository has helped you in any way, and if you would like to support me, you can send me any crypto (preferably stables) on any EVM chain at `0xC986B1Aa3bFD11069e1e1bC67C712895Bc5DbC40` or sending me UST at `poohbear.ust`
