# Quickstart

## What is Kwil?

Kwil is a blockchain-based database platform, while keep being blockchain agnostic on Account. 
To use Kwil, you need to do the following:
1. Create a Ethereum account
2. Fund the account with some required TOKEN of your kwil provider
3. Create database schema, through Kwil Kuneiform IDE. From there, you can get compiled schema bytes.
4. Deploy the database schema to the blockchain.
5. Create/Update data through predefined Actions.


## Installation

`$ pip install kwil`

Supported python version:
* 3.9
* 3.10


## Usage

### Provider
This library depends on a connection to an Kwil node. We call these connections Providers.


```
>>> from kwil import Kwil
>>> kwil = Kwil(Kwil.GRPCProvider("localhost:50051")
                Kwil.load_wallet("YOUR_ETH_PRIVATE_KEY"))
>>> kwil.is_connected()
True
```


### More

Check [overview](./overview.md) learn more on APIs.

Check [examples](./examples.md) for a walkthrough.