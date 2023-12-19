from ape import project, Contract

def test_authentication(accounts):
    user = accounts[0]
    locker = Contract('0x90be6DFEa8C80c184C442a36e17cB2439AAE25a7')
    yprisma = Contract('0xe3668873D944E4A949DA05fc8bDE419eFF543882')

    fee_receiver = user.deploy(project.YearnPrismaFeeReceiver, locker)
    amount = 200 * 10 ** 18

    tx = fee_receiver.setTokenApproval2(
        yprisma,
        user,
        amount,
        sender = locker
    )

    # This one passes.
    print('This one passes an produces events --> ', len(tx.events))
    assert yprisma.allowance(fee_receiver, user) > 0
    print('Now we need to reset approval 0')
    tx = fee_receiver.setTokenApproval2(
        yprisma,
        user,
        0,
        sender = locker
    )
    print('This one also passes and produces an event --> ', len(tx.events))
    assert len(tx.events) > 0

    tx = fee_receiver.setTokenApproval(
        yprisma,
        user,
        amount,
        sender = locker
    )

    # This txn succeeds, but somehow does not detect the approval event.
    print('No events to be found --> ', len(tx.events))
    assert yprisma.allowance(fee_receiver, user) > 0
    assert len(tx.events) > 0