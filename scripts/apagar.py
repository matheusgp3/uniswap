import requests
from pandas import read_csv
from operator import itemgetter
import x6


class Pool:
    def __init__(self):
        self.poolId = ''
        self.price0 =''
        self.price1 =''


    def VerifyValue(self):
        query = {'query': '{pool(id:' + self.poolId + '){token0Price token1Price}}'}
        res = requests.post('https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3',
                            json=query).json()['data']['pool']
        token0Price, token1Price = itemgetter('token0Price', 'token1Price')(res)
        #print(token0Price, token1Price)
        return(token0Price, token1Price)
        

    def getValues(self):
        self.poolId,self.price0,self.price1 = read_csv('poolId.csv').values[0]

        self.price0 = float(self.price0)
        self.price1 = float(self.price1)
        
        self.poolId = '"' + self.poolId + '"'


    def decision(self):
        currentPrice0,currentPrice1 = self.VerifyValue()

        currentPrice0=float(currentPrice0)
        currentPrice1=float(currentPrice1)

        r0 = self.price1 - self.price0
        r1 = currentPrice1 - currentPrice0

        res = r1/r0
        if res > 1.05 or res < 0.95:
            x6.uniswap(token0="USDC",token1="WETH",qntd_token0=10).main()


    def printa(self):
        print(self.poolId,self.price0,self.price1,sep='\n')

r = Pool()
r.getValues()
r.decision()
##r.VerifyValue()
