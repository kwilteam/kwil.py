#!/usr/bin/env python
"""
This file is a demo of how to use kwil by implementing a simple task runner using invoke.
"""

import os
import pprint

from invoke import task
from kwil import Kwil


pp = pprint.PrettyPrinter(indent=4)


def get_kwil(rpc_url: str, private_key: str) -> Kwil:
    return Kwil(Kwil.GRPCProvider(rpc_url),
                Kwil.load_wallet(private_key))


k = get_kwil(os.getenv("KWIL_PROVIDER", "grpc.kwil.com:80"),
             os.getenv("KWIL_CLI_PRIVATE_KEY", "EMPTY_KEY"))


db_name = "testdb"  # The name of the database, from the schema file
db_id = Kwil.generate_dbi(k.wallet.address, db_name)


@task(help={"schema_file": "The schema file of the database"})
def deploy(c,
           schema_file: str = "test_db.json"):
    """
    Deploy a database.
    """
    assert schema_file != "", "schema_file is required"

    with open(schema_file, "r") as f:
        schema_json = f.read()
        try:
            tx_receipt = k.deploy_database(schema_json.encode("utf-8"))
            print(tx_receipt)
        except Exception as e:
            print(e)


@task()
def list_dbs(c):
    """
    List all databases.
    """
    dbs = k.list_databases()
    pp.pprint(dbs)


@task(help={"name": "The name of the database"})
def get_schema(c,
               name: str = "testdb"):
    """
    Get the schema of a database.
    """
    assert name != "", "db_name is required"

    _db_id = Kwil.generate_dbi(k.wallet.address, name)
    dbs = k.get_schema(_db_id)
    pp.pprint(dbs)


@task(help={"name": "The name of the database"})
def drop(c,
         name: str = "testdb"):
    """
    Drop a database.
    """
    assert name != "", "db_name is required"

    tx_receipt = k.drop_database(name)
    pp.pprint(tx_receipt)


@task(help={"id": "The id of the user",
            "username": "The name of the user",
            "age": "The age of the user"})
def create_user(c,
                id: int = 0,
                username: str = "",
                age: int = 0):
    """
    Create a user.
    """
    assert id != 0, "id is required"
    assert username != "", "username is required"
    assert age != 0, "age is required"

    tx_receipt = k.execute_action(db_id,
                                  "create_user",
                                  [{
                                      "$id": id,
                                      "$username": username,
                                      "$age": age
                                  }])
    pp.pprint(tx_receipt)


@task(help={"id": "The id of the post",
            "title": "The title of the post",
            "content": "The content of the post"})
def create_post(c,
                id: int = 0,
                title: str = "",
                content: str = ""):
    """
    Create a post.
    """
    assert id != 0, "id is required"
    assert title != "", "title is required"
    assert content != "", "content is required"

    tx_receipt = k.execute_action(db_id,
                                  "create_post",
                                  [{
                                      "$id": id,
                                      "$title": title,
                                      "$content": content
                                  }])
    pp.pprint(tx_receipt)


@task(help={"id": "The id of the post"})
def delete_post(c,
                id: int = 0):
    """
    Delete a post.
    """
    assert id != 0, "id is required"

    tx_receipt = k.execute_action(db_id,
                                  "delete_post",
                                  [{
                                      "$id": id
                                  }])
    pp.pprint(tx_receipt)


@task()
def list_users(c):
    """
    List all users.
    """
    tx_receipt = k.execute_action(db_id,
                                  "list_users",
                                  [])
    pp.pprint(tx_receipt)


@task(help={"username": "The username of the user"})
def list_posts(c,
               username: str = ""):
    """
    List all posts from you.
    """
    assert username != "", "username is required"

    tx_receipt = k.execute_action(db_id,
                                  "get_user_posts",
                                  [{
                                      "$username": username
                                  }])
    pp.pprint(tx_receipt)


@task(help={"query": "Raw SQL query to execute."})
def query(c, query: str = ""):
    """
    Query the database.
    """
    assert query != "", "query is required"

    tx_receipt = k.query(db_id, query)

    pp.pprint(tx_receipt)
