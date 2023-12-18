import ape
from ape import chain, project, Contract
import numpy as np
import time

WEEK = 60 * 60 * 24 * 7

def test_authentication(accounts):
    user = accounts[0]
    locker = Contract('0x90be6DFEa8C80c184C442a36e17cB2439AAE25a7')
    yprisma = Contract('0xe3668873D944E4A949DA05fc8bDE419eFF543882')

    fee_receiver = user.deploy(project.YearnPrismaFeeReceiver, locker)
    amount = 200 * 10 ** 18


    tx = fee_receiver.setTokenApproval1(
        yprisma,
        user,
        amount,
        sender = locker
    )
    print(tx.events)