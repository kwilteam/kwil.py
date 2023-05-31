## Deploy Database Schema

```python
import logging

from kwil import Kwil

# assume that account has enough fund
# here we use test_db.kf as our dataset schema, we'll use examples/test_db.json(compiled schema)

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

Assume we have our schema defined and compiled. We can deploy the schema to the blockchain.
First, we need to create a provider using `Kwil.GRPCProvider`.
Then, create a `Kwil` instance. We can call `deploy_database` to deploy the schema to the blockchain.
Finally, we can call `list_databases` to list all the databases under current account to verify it's there.


## Working with Dataset

```python
# execute an action
db_name = "testdb"  # The name of the database, from the schema file
db_id = Kwil.generate_dbi(client.wallet.address, db_name)

action = "create_user"
tx_receipt = client.execute_action(db_id,
                                   action,
                                   # `create_user` is defined in test_db.kf
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

To call this action, we need to provide the dataset id, action name and inputs.
```python
tx_receipt = client.execute_action(db_id,
                                   action,
                                   [{"$id": 1, "$username": "aha", "$age": 18}])
```

Here, we only create one user, the inputs is just a dict of the input parameters with values.

