// SPDX-License-Identifier: MIT

pragma solidity 0.8.19;

import "./interfaces/ILocker.sol";

/**
    @title Yearn Prisma Authentication
    @notice Contracts inheriting `YearnAuthenticated` permit only a trusted set of callers.
 */
contract YearnPrismaAuthenticated {
    ILocker public immutable LOCKER;

    constructor(address _locker) {
        LOCKER = ILocker(_locker);
    }

    modifier enforceAuth() {
        require(isAuthenticated(msg.sender), "!authorized");
        _;
    }

    modifier onlyOwner() {
        require(msg.sender == address(LOCKER), "Only owner");
        _;
    }

    function isAuthenticated(address _caller) public view returns (bool) {
        if (
            _caller == LOCKER.proxy() ||
            _caller == LOCKER.governance() ||
            _caller == address(LOCKER)
        ) return true;

        return false;
    }
}

