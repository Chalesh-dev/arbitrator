from web3 import Web3


w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/33728cf096dd4ea5afac8b58387b3ff7"))

abi = """[
	{
		"inputs": [
			{
				"internalType": "bytes",
				"name": "path",
				"type": "bytes"
			},
			{
				"internalType": "uint256",
				"name": "amountIn",
				"type": "uint256"
			}
		],
		"name": "quoteExactInput",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "amountOut",
				"type": "uint256"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "tokenIn",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "tokenOut",
				"type": "address"
			},
			{
				"internalType": "uint24",
				"name": "fee",
				"type": "uint24"
			},
			{
				"internalType": "uint256",
				"name": "amountIn",
				"type": "uint256"
			},
			{
				"internalType": "uint160",
				"name": "sqrtPriceLimitX96",
				"type": "uint160"
			}
		],
		"name": "quoteExactInputSingle",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "amountOut",
				"type": "uint256"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "bytes",
				"name": "path",
				"type": "bytes"
			},
			{
				"internalType": "uint256",
				"name": "amountOut",
				"type": "uint256"
			}
		],
		"name": "quoteExactOutput",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "amountIn",
				"type": "uint256"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "tokenIn",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "tokenOut",
				"type": "address"
			},
			{
				"internalType": "uint24",
				"name": "fee",
				"type": "uint24"
			},
			{
				"internalType": "uint256",
				"name": "amountOut",
				"type": "uint256"
			},
			{
				"internalType": "uint160",
				"name": "sqrtPriceLimitX96",
				"type": "uint160"
			}
		],
		"name": "quoteExactOutputSingle",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "amountIn",
				"type": "uint256"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_factory",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "_WETH9",
				"type": "address"
			}
		],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"inputs": [],
		"name": "factory",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "int256",
				"name": "amount0Delta",
				"type": "int256"
			},
			{
				"internalType": "int256",
				"name": "amount1Delta",
				"type": "int256"
			},
			{
				"internalType": "bytes",
				"name": "path",
				"type": "bytes"
			}
		],
		"name": "uniswapV3SwapCallback",
		"outputs": [],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "WETH9",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]"""

address = Web3.to_checksum_address("0xb27308f9F90D607463bb33eA1BeBb41C27CE5AB6")

cont = w3.eth.contract(address=address,abi=abi)

data = cont.functions.quoteExactInputSingle(Web3.to_checksum_address("0xdAC17F958D2ee523a2206206994597C13D831ec7"),Web3.to_checksum_address("0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"),3000,10**7,0).call()

print(data/1e6)


data = cont.functions.quoteExactInputSingle(Web3.to_checksum_address("0xdAC17F958D2ee523a2206206994597C13D831ec7"),Web3.to_checksum_address("0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"),3000,50000*10**6,0).call()

print(data/1e6)
