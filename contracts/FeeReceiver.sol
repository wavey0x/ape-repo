// SPDX-License-Identifier: MIT

pragma solidity 0.8.19;

import {IERC20, SafeERC20} from "@openzeppelin/contracts@v4.9.3/token/ERC20/utils/SafeERC20.sol";
import "./interfaces/ILocker.sol";
import "./YearnAuthenticated.sol";

contract YearnPrismaFeeReceiver is YearnPrismaAuthenticated {
    using SafeERC20 for IERC20;

    constructor(address _locker) YearnPrismaAuthenticated(_locker) {}
    event Test(address token, address spender, uint amount);

    function transferToken(IERC20 token, address receiver, uint256 amount) external enforceAuth {
        token.safeTransfer(receiver, amount);
    }

    function setTokenApproval(IERC20 token, address spender, uint256 amount) external enforceAuth {
        token.safeApprove(spender, amount);
    }

    function setTokenApproval2(IERC20 token, address spender, uint256 amount) external onlyOwner {
        token.safeApprove(spender, amount);
    }
}


