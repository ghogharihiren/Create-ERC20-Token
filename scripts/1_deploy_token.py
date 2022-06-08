from eth_account import Account
from brownie import OurToken
from .helpfull import*
from web3 import Web3

initial_Supply=Web3.toWei(1000,"ether")


def main():
    account=get_account()
    ourtoken=OurToken.deploy(initial_Supply,{"from":account})
    print(ourtoken.name())