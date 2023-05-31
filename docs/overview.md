# Overview

## Configuration

### Providers

Providers are used to interact with the blockchain. They are responsible for sending and receiving RPC requests. 
There are following builtin providers:
* GRPCProvider - connects to a remote gRPC based server

### Private Key

Kwil now support Ethereum private key to sign transaction. This key is also associated
with an Ethereum account which needed to be funded to use Kwil.


## Base API

There is a [example](https://github.com/kwilteam/kwil.py/blob/main/examples/lifecycle.py) that shows how to use these API.

### Dataset Identifier helpers

* `Kwil.generate_dbi(owner_addr, dataset_name)`
* `Kwil.load_wallet(private_key)`

### high level API

* `kwil.deploy_database(payload)` - deploys a new database, payload is compiled bytes of schema
* `kwil.get_schema(db_identifier)` - returns the database schema
* `kwil.list_databases(OPTIONAL[owner_address])` - returns the list of databases under current account
* `kwil.drop_database(dataset_name)` - drops the database under current account
* `kwil.execute_action(db_identifier, action_name, inputs)` - executes the action on the database
* `kwil.query(db_identifier, query)` - executes query(ad-hoc SQL) on the database

## low level API (Kwil.kwild API)

### Fetching data

* `Kwil.kwild.ping()`
* `Kwil.kwild.get_config()` - returns the configuration of the node
* `Kwil.kwild.get_schema(DBIdentifier)` - returns the dataset schema info
* `Kwil.kwild.get_account(Adddress)` - returns the account info(nonce, balance, etc)
* `Kwil.kwild.estimate_price(TxParams)` - returns the estimated price for the transaction
* `Kwil.kwild.query(DBIdentifier, Query)` - returns the query(ad-hoc SQL) result
* `Kwil.kwild.list_databases()` - returns the list of databases under current account

### Making transactions

* `Kwil.kwild.broadcast(TxParams)` - broadcasts the transaction to the network
