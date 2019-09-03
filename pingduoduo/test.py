from luck import User
from luck import dic
import random


ids = []
for i in range(30000000):
    i = str(i)
    ids.append(i)

suc = []
fail = []
for id in ids:
    user = User(id)
    for i in range(20):
        id_index = random.randint(0,29999999)
        v_id = ids[id_index]
        user.lucky_100(v_id)
        if dic[id]['award'] >= 10000:
            suc.append(id)
            break
        else:
            continue
    if dic[id]['award'] < 10000:
        fail.append(id)

print('suc:',len(suc))

print('fail:',len(fail))
