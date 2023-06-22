## examples 

* [test_db.kf](./test_db.kf) - a simple database schema.
* [test_db.json](./test_db.json) - json representation of the schema.
* [lifecycle.py](./lifecycle.py) - shows how to use kwil.py to deploy a database, execute actions, and query data.
* [tasks.py](./tasks.py) - shows how to use kwil.py and [invoke](https://www.pyinvoke.org/) to interact with Kwil. You'll need to configure `KWIL_PROVIDER` and `KWIL_CLI_PRIVATE_KEY` environment variables to run this example.
  * `invoke -l` list all tasks
  * `invoke list-dbs` list all databases
  * `invoke create-user -a 22 -i 1 -u yaiba` create a user
  * `invoke create-post -i 1 -t hello -c "how i made this shit"` create a post
  * `invoke list-posts -u yaiba` 
  * `invoke delete-post -i 1`
  * `invoke list-posts -u yaiba`
  * `invoke list-users`
  * `invoke query -q "select * from users"`
  * `invoke query -q "select * from postss"`
  * `invoke drop -d testdb`
  * `invoke list-dbs`
