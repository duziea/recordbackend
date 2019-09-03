import random


dic = {}

class User():
    def __init__(self,id):
        self.id = id
        if id in dic:
            self.award = dic[id]['award']
            self.count = dic[id]['count']
        else:
            dic[id] = {} 
            self.count = 0
            self.award = 0
            
    def lucky_100(self,id):
        if self.count == 0:  #哟，第一次抽奖，新用户，给你来多点
            self.award = random.randint(6666,8888)
            dic[self.id]['award'] = self.award       #保存数据
            self.count += 1
            dic[self.id]['count'] = self.count
            print('用户%s第%d次抽奖' % (self.id,self.count))
            print('恭喜您抽到了大大大大红包{0}，还差{1}可提现'.format(self.award/100,(10000-self.award)/100))
            return 'ok'

        else:           #老用户不当人
            if id in dic:           #邀请的老用户啊，那对不起了
                award = 1
                self.award += award
                self.count += 1
                dic[self.id]['award'] = self.award
                dic[self.id]['count'] = self.count 
                print('selfaward',self.award/100)
                print('邀请老用户%s第%d次抽奖' % (self.id,self.count))
            else:
                if self.award <= 10000:
                    if self.count <=5:
                        award = random.randint(300,400)
                        self.award += award
                        self.count += 1
                        dic[self.id]['award'] = self.award
                        dic[self.id]['count'] = self.count 
                        print('selfaward',self.award/100)
                        print('用户%s第%d次抽奖' % (self.id,self.count))
                    else:
                        award = random.randint(10,100)
        
                        self.award += award
                        self.count += 1
                        dic[self.id]['award'] = self.award
                        dic[self.id]['count'] = self.count 
                        print('selfaward',self.award/100)
                        print('用户%s第%d次抽奖' % (self.id,self.count))
                        if self.award <= 10000:
                            print('恭喜您抽到了大大大大红包{0}，还差{1}可提现'.format(self.award/100,(10000-self.award)/100))
                        else:
                            print('恭喜您满100了，拿钱就完事了')
                else:
                    print('恭喜您满100了，拿钱就完事了')


if __name__ == "__main__":
    ids = []
    for i in range(3000):
        i = str(i)
        ids.append(i)

    suc = []
    fail = []
    for id in ids:
        user = User(id)
        for i in range(20):
            id_index = random.randint(0,2999)
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
        