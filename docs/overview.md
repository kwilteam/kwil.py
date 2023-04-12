# Overview

## Configuration

### Providers

Providers are used to interact with the blockchain. They are responsible for sending and receiving RPC requests. 
There are following builtin providers:
* GRPCProvider - connects to a remote gRPC based server

## Base API

There is a [example](https://github.com/kwilteam/kwil.py/blob/main/examples/lifecycle.py) that shows how to use these API.

### Dataset Identifier helpers

* `Kwil.generate_dbi(owner_addr, dataset_name)`

### high level API

* `kwil.deploy_database(payload)` - deploys a new database, payload is compiled bytes of schema
* `kwil.get_database(dataset_name, OPTIONAL[owner_address])` - returns the database object
* `kwil.list_database(OPTIONAL[owner_address])` - returns the list of databases under current account
* `kwil.drop_database(dataset_name)` - drops the database under current account
* `kwil.execute_action(dataset_name, action_name, inputs)` - executes the action on the database
* `kwil.query(dataset_name, query)` - executes query(ad-hoc SQL) on the database

## low level API (Kwil.kwild API)

### Fetching data

* `Kwil.kwild.ping()`
* `Kwil.kwild.get_config()` - returns the configuration of the node
* `Kwil.kwild.get_schema(DBIdentifier)` - returns the dataset schema info
* `Kwil.kwild.get_account(Adddress)` - returns the account info(nonce, balance, etc)
* `Kwil.kwild.estimate_price(TxParams)` - returns the estimated price for the transaction
* `Kwil.kwild.query(DBIdentifier, Query)` - returns the query(ad-hoc SQL) result
* `Kwil.kwild.list_database()` - returns the list of databases under current account

### Making transactions

* `Kwil.kwild.broardcase(TxParams)` - broadcasts the transaction to the network
