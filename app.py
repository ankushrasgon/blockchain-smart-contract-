from web3 import Web3
ganache_url="http://127.0.0.1:7545"
web3 =Web3(Web3.HTTPProvider(ganache_url))
account_1="0xe95784a034aaB26d5D5Bafd2c03DB084800bce9E"
account_2="0x965a4469EB96e0aA88cD67e7E4E04E8837bB831F"

private_key="b9341efa8764f93e8db10bc0bd7eebcbe64d8e016f6857468bcd7e3b155cf4e4"

nonce=web3.eth.getTransactionCount(account_1)

tx={
'nonce':nonce,
'to':account_2,
'value':web3.toWei(2,'ether'),
'gas':2000000,
'gasPrice': web3.toWei('50','gwei')
}

signed_tx=web3.eth.account.signTransaction(tx,private_key)
tx_hash=web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))
