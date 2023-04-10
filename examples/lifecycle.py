import os
import logging

from kwil import Kwil

# configuration
os.environ["KWIL_GRPC_PROVIDER_URI"] = "localhost:50051"
os.environ["KWIL_ETH_PRIVATE_KEY"] = "YOUR_PRIVATE_KEY"


def run():
    # assume that account has enough fund
    # here we use test_db.kf as our dataset schema, we'll use test_db.json(compiled schema)
    # change `owner` in test_db.json to `YOUR_PRIVATE_KEY`

    # create client
    client = Kwil()

    # create dataset
    with open("./test_db.json", "r") as f:
        schema_json = f.read()
        try:
            client.deploy_database(schema_json.encode("utf-8"))
        except Exception as e:
            logging.exception(e)

    # list dataset
    dbs = client.list_database()
    print("datasets after create: ", dbs)

    # execute an action
    db_name = "testdb"
    db_identifier = Kwil.generate_dbi(client.wallet.address, db_name)
    action = "create_user"
    tx_receipt = client.execute_action(db_identifier,
                                       action,
                                       # `create_user` is defined in test_db.kf
                                       [{"$id": 1, "$username": "aha", "$age": 18}])
    result = tx_receipt["result"]
    print("create user result: ", result)

    # execute a pre-defined query through action
    action = "list_users"
    tx_receipt = client.execute_action(db_identifier, action, [])
    result = tx_receipt["result"]
    print("list user result:", result)

    # drop dataset
    client.drop_database(db_name)

    # list dataset
    dbs = client.list_database()
    print("datasets after delete: ", dbs)


if __name__ == "__main__":
    run()
