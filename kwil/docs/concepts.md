
## [method](https://github.com/ethereum/web3.py/pull/1166#issuecomment-448772937)
The Method class is in charge of interpreting a method configuration. Meaning the Method is concerned with collecting the method lookup, mungers, formatters and executing them on the inputs.


### [mungers](https://github.com/ethereum/web3.py/pull/1166#discussion_r241932859)
It is the list of the functions that the python method arguments get piped through, that should output a json_rpc ready param dict. Havent found a name I like better. Because these functions can be validators, normalizers, formatters, occur in any order, with probably a huge variation arity, etc., "munger" seems appropriate. These are being kept separate from the request parameter and result formatters, taken from the middleware formatters.


### formatter
A formatter is a function that takes a value and returns a formatted value. It wraps request function.

## middleware
Middleware sit between public methods(after all mungers/formatters are applied) and Provider.