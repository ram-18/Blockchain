# Blockchain In Django
This is a simple blockchain project created using python programming. Totally for educational purposes. The code structure of the project's `views.py` file is as below.

## Views.py file structure
It has total 2 parts.
1. Blockchain class
2. Views functions

There is one blockchain object in the global scope and all the other views functions interact with this object.

## Blockchain class
There are total 6 methods available for the class.
| Method | Use |
| --- | --- |
| \_\_init\_\_ | The nitialization method of class |
| create_block | Method to create block in blockchain class |
| get_last_block | Method to get the last block of blokchain in blockchain class |
| proof_of_work | Method to get the nonce value of new block |
| hash | Method to hash the block of blockchain |
| is_chain_valid | The method to chck the validity of blockchain |

## Views functions
There are total 4 views functions.
| Function | Use |
| --- | --- |
| get_chain | Get the full blockchain |
| mine_block | Mine a block in blockchain |
| is_chain_valid | Check the validity of blockchain |
| temper_blockchain | Simple function just to explain the tempering detection in blockchain |