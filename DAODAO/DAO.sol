// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DAO {
    address public founder;
    mapping(address => uint256) public memberBalances;

    constructor() {
        founder = msg.sender;
    }

    function contribute() external payable {
        memberBalances[msg.sender] += msg.value;
    }

    function withdraw(uint256 amount) external {
        require(memberBalances[msg.sender] >= amount, "Insufficient balance");
        payable(msg.sender).transfer(amount);
        memberBalances[msg.sender] -= amount;
    }

    function getBalance(address member) external view returns (uint256) {
        return memberBalances[member];
    }
}