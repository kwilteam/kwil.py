import os
import logging

from kwil import Kwil


def run():
    # assume that account has enough fund
    # here we use test_db.kf as our dataset schema, we'll use test_db.json(compiled schema)

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
    dbs = client.list_database()
    print("datasets after create: ", dbs)

    # execute an action
    db_name = "testdb"
    action = "create_user"
    tx_receipt = client.execute_action(
        db_name,
        action,
        # `create_user` is defined in test_db.kf
        [{"$id": 1, "$username": "aha", "$age": 18}],
    )
    print("create user result: ", tx_receipt)

    # execute a pre-defined query through action
    action = "list_users"
    tx_receipt = client.execute_action(db_name, action, [])
    print("list user result:", tx_receipt)

    # drop dataset
    tx_receipt = client.drop_database(db_name)
    print("drop dataset result: ", tx_receipt)

    # list dataset
    dbs = client.list_database()
    print("datasets after delete: ", dbs)


if __name__ == "__main__":
    run()
