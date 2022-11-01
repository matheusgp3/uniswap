# Pool Project Bot

this project intend to create a bot that will be operating over uniswap based on conditions to create and exclude pool

## **important**

1. To this script work, you'll need a file .env in this folder, copy the following command and change the values inside of <>

```
secretPhrase=<metamask recovery phrase>
password=<a password of your metamask or just put any that would change for what you've choosed>
```

2. you'll need chromedriver downloaded in the folder where python is installed in your machine, or just clone this git download to this folder and change the script.

3. I've created this project using virtual enviroment that is this folder.

```
python -m venv <enviroment name>
env\script\activate
```

## conditions

* How much you're buying over coins, if is 10% more to any, bot will undo the pool and create a new one

## libraries

to create this project I've been using the following libraries

1. selenium    
2. dotoenv
3. time (default)

## code Installation:
  
 To install the previous libraries use:
 
 ``` 
 pip3 install selenium 
 pip3 install dotoenv
 ```

## Contanct

* name: Matheus Pereira Costa
* email: matheusgp3@hotmail.com
