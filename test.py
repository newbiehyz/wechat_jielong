import collections
import unicodedata
import re

s = u'''1. 刘老五 春饼套餐（东方明珠）超市147258
2. Z r 超市 998749 Uni取
3. 伤心的龙卷风别听慢歌 茄盒 麻辣锅仔肥肠鸡(东方) uni
4. Bombebon ️ 三香豆干，麻酱粉皮，豆花羊肉️莴笋炒腊肉 白辣椒鸡杂 辣子鸡丁（炸的那种）莲花的菜
1. 刘老五 春饼套餐（东方明珠）超市147258
2. Jonas 996807超市，uni 微信
3. ww 南瓜烧仔鸡，酸豆角炒肉末 Uni 现金
4. 一南 10荠菜云吞 20鲜肉馄炖 uni paypal
5. 林子贤 超市997501
6. Bombebon 莲花的菜➕东方明珠的菜➕超市订单
1. 刘老五 春饼套餐（东方明珠）超市147258
2. Felix 鸭蛋10个 Uni 现金
3. Vera🍒 鸭蛋20个 超市996493 uni现金
4. 亚森先生 青椒小炒肉（东方）梅菜扣肉（东方）uni PayPal
5.  超市订单 996547 uni
6. 陈鹏旭 超市订单996568 Uni取 微信
7. Coney997 超市订单 996164 möhringen
8. KK 超市996630 uni 现金
1. 刘老五 春饼套餐（东方明珠）超市147258
2. Lulina 超市订单995014(另加500克新鲜芋头，备注已写), 小炒辣子鸡，葱爆羊肉(不辣)  东方明珠 uni 现金
3. 噔噔 超市995095，加超市995103，干烧鲈鱼，笋干黄焖鸡Uni paypal
4. 大橘 超市994797，上门 paypal
5. wowow 莲花辣鸡子，鱼香肉丝 uni
6. FWJ 京酱肉丝（东方）uni paypal已转
7. ww 酸菜鱼片，鱼香肉丝(东方) Uni'''

# convert chinese punctuation

s = unicodedata.normalize('NFKC', s) 

s = s.replace('\n',' ')
s = s.replace(',',' ') 
s = s.replace('.','')

# delete letters numbers

s = re.sub(r'[A-Za-z]+', '', s)
s = re.sub(r'[\u00DF\u00F6\u00FC\u00E4]+', '', s)
s = re.sub(r'[\u002D]+', '', s)
s = re.sub(r'[0-9]+', '', s)

# counter
list1 = s.split()
m = collections.Counter(list1)

# delete unrelevant
del m['现金']

print(m,end='\n\n')

most = m.most_common(10)
print(most)
