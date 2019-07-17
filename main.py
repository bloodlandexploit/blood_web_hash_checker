import requests
import json


api_server_pool = 'https://wallet.blood.land/api/mining/miner/pool'
api_server_diff = 'https://wallet.blood.land/api/mining/miner/difficulty'

headers = {"Connection": "keep-alive",
           "Accept": "application/json, text/plain, */*",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
           "Referer": "https://wallet.blood.land/",
           "Accept-Encoding": "gzip, deflate, br",
           "Accept-Language": "en-US,en;q=0.9,ko;q=0.8,es;q=0.7"}

server_json = requests.get(url=api_server_pool, headers=headers).json()
server_json_dump = json.dumps(server_json)
pool_diff = requests.get(url=api_server_diff).json()['difficulty']

hashrate_un = json.loads(server_json_dump)['data']['totalHashrate'] #Hash
hashrate = hashrate_un / 1000000 #MHash
connection = json.loads(server_json_dump)['data']['connectionCount']
hashperconnection = hashrate / connection * 1000
workerc = json.loads(server_json_dump)['data']['workerCount']
totalPoint = json.loads(server_json_dump)['data']['totalPoint']
totalReward = json.loads(server_json_dump)['data']['totalReward']
totalDistributed = json.loads(server_json_dump)['data']['totalDistributed']
totalAllReward = json.loads(server_json_dump)['data']['totalAllReward']
hashperworker = hashrate / workerc * 1000

print("Total Miner : ", workerc, "Mining Difficuity : ", pool_diff, "Total Hashrate(Mh/s) : ", hashrate)
print("Total Reward Weight : ", totalPoint, "Total Reward by Mining : ", totalReward, "Total Reward by Weight : ", totalDistributed)
print("Total Reward : ", totalAllReward)
