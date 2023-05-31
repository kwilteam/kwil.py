# kwil.py

[![PyPI - Version](https://img.shields.io/pypi/v/kwil.svg)](https://pypi.org/project/kwil)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/kwil.svg)](https://pypi.org/project/kwil)

Borrows heavily from [web3.py](https://github.com/ethereum/web3.py)

------

<!-- TOC -->
* [kwil.py](#kwilpy)
  * [What is Kwil?](#what-is-kwil)
  * [Installation](#installation)
  * [Configuration](#configuration)
    * [Providers](#providers)
    * [Private Key](#private-key)
  * [API](#api)
    * [helpers](#helpers)
    * [high level API](#high-level-api)
    * [low level API (Kwil.kwild API)](#low-level-api-kwilkwild-api)
      * [Fetching data](#fetching-data)
      * [Making transactions](#making-transactions)
  * [Usage](#usage)
    * [Connect to Kwil node](#connect-to-kwil-node)
    * [Deploy Database](#deploy-database)
    * [Working with Actions](#working-with-actions)
  * [License](#license)
<!-- TOC -->

------

## What is Kwil?

Kwil is a blockchain-based database platform, while keep being blockchain agnostic on Account. 
To use Kwil.py, you need to do the following:
1. Create a Ethereum account
2. Fund the account with some required TOKEN of your kwil provider
3. Create database schema, through Kwil Kuneiform IDE. From there, you can get compiled schema bytes.
4. Deploy the database schema to the blockchain.
5. Create/Update data through predefined Actions.

## Installation

```bash
pip install kwil
```

Supported python version:
* 3.9
* 3.10

## Configuration

### Providers

Providers are used to interact with the blockchain. They are responsible for sending and receiving RPC requests. 
There are following builtin providers:
* GRPCProvider - connects to a remote gRPC based server

### Private Key

Kwil now support Ethereum private key to sign transaction. This key is also associated
with an Ethereum account which needed to be funded to use Kwil.


## API

There are [examples](https://github.com/kwilteam/kwil.py/blob/main/examples/README.md) that shows how to use these API.

### helpers

* `Kwil.generate_dbi(owner_addr, dataset_name)`
* `Kwil.load_wallet(private_key)`

### high level API

* `kwil.deploy_database(payload)` - deploys a new database, payload is compiled bytes of schema
* `kwil.get_schema(db_identifier)` - returns the database schema
* `kwil.list_databases(OPTIONAL[owner_address])` - returns the list of databases under current account
* `kwil.drop_database(dataset_name)` - drops the database under current account
* `kwil.execute_action(db_identifier, action_name, inputs)` - executes the action on the database
* `kwil.query(db_identifier, query)` - executes query(ad-hoc SQL) on the database

### low level API (Kwil.kwild API)

#### Fetching data

* `Kwil.kwild.ping()`
* `Kwil.kwild.get_config()` - returns the configuration of the node
* `Kwil.kwild.get_schema(DBIdentifier)` - returns the dataset schema info
* `Kwil.kwild.get_account(Adddress)` - returns the account info(nonce, balance, etc)
* `Kwil.kwild.estimate_price(TxParams)` - returns the estimated price for the transaction
* `Kwil.kwild.query(DBIdentifier, Query)` - returns the query(ad-hoc SQL) result
* `Kwil.kwild.list_databases()` - returns the list of databases under current account

#### Making transactions

* `Kwil.kwild.broadcast(TxParams)` - broadcasts the transaction to the network


## Usage
There are more examples in [examples](./examples) folder.

### Connect to Kwil node

Kwil.py will connect to a Kwil node through a provider. 
Currently, only GRPC provider is supported.

```ipython
>>> from kwil import Kwil
>>> kwil = Kwil(Kwil.GRPCProvider("localhost:50051"),
                Kwil.load_wallet("YOUR_ETH_PRIVATE_KEY"))
>>> kwil.is_connected()
True
```

### Deploy Database
Assume we have our schema defined and compiled(`./test_db.json`). We can deploy the schema to the blockchain.

First, create a provider using `Kwil.GRPCProvider`.

Then, create a `Kwil` instance, can call `deploy_database` to deploy the schema to the blockchain.

Finally, call `list_database` to list all the databases under current account to verify it's there.

```python
import logging

from kwil import Kwil


# assume that account has enough fund
# here we use examples/test_db.kf as our dataset schema, we'll use examples/test_db.json(compiled schema)

# create client
client = Kwil(Kwil.GRPCProvider("localhost:50051"),
              Kwil.load_wallet("YOUR_ETH_PRIVATE_KEY"))

# create dataset
with open("./test_db.json", "r") as f:
    schema_json = f.read()
    try:
        client.deploy_database(schema_json.encode("utf-8"))
    except Exception as e:
        logging.exception(e)

# list dataset
dbs = client.list_databases()
print("datasets after create: ", dbs)
```    

### Working with Actions

```python
# execute an action
db_name = "testdb"  # The name of the database, from the schema file
db_id = Kwil.generate_dbi(client.wallet.address, db_name)

action = "create_user"
tx_receipt = client.execute_action(db_id,
                                   action,
                                   # `create_user` is defined in examples/test_db.kf
                                   [{"$id": 1, "$username": "aha", "$age": 18}])
result = tx_receipt["result"]
print("create user result: ", result)

# execute a pre-defined query through action
action = "list_users"
tx_receipt = client.execute_action(db_id, action, [])
result = tx_receipt["result"]
print("list user result:", result)
```

Let's extend the example above. We can call `execute_action` to execute an action on the database.
In our schema(examples/test_db.kf), we have
```
action create_user($id, $username, $age) public {
    INSERT INTO users (id, username, age, wallet)
    VALUES ($id, $username, $age, @caller);
}
```

`create_user` is a public action, so we can call it without any permission.

To call this action, we need to provide the dataset identifier, action name and inputs.
```python
tx_receipt = client.execute_action(db_id,
                                   action,
                                   [{"$id": 1, "$username": "aha", "$age": 18}])
```

Here, we only create one user, the inputs is just a dict of the input parameters with values.


## License

MIT