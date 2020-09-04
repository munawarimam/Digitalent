'''
namafile: sba.py
Lembar kerja/script Latihan SBA
'''
# >>>>>>LEMBAR KERJA>>>>>>>>>
# lembar ini hanya berisi pendefinisian fungsi dan class saja
 
#email netacad
email = ''


# No 1
def fungsiIO():
    numbers = sorted(list(map(int, input('Enter numbers: ').split())))
    for i in numbers:
        a = (i * '*')
        print(a)


fungsiIO() # contoh input 7 4 5 3 1 2


# No 2
def caseShopia(txt):
    test = filter(str.isalpha, txt)
    return ''.join(c.lower() if c.isupper() else c.upper() for c in test)
    

print(caseShopia('thXGth876%^$LMn.'))


# No 3  
dcur2idr = {'USD': 14425, 'EUR': 16225, 'AUD': 9925, 'CAD': 10500, 
             'GBP': 17800, 'CHF': 15200, 'SGD': 10375, 'HKD': 1775, 
             'JPY': 132500, 'MYR': 3250, 'SAR': 3500, 'WON': 10750, 
             'IDR': 1}

def usd2eur(usd):
    
    return (dcur2idr['USD'] / dcur2idr['EUR']) * usd

print(usd2eur(100))


# No 4
class MoneyChanger:
    def __init__(self,dcurrency,base='IDR',percent=2):
        self.currs = dcurrency
        self.base = base
        self.percent = percent
        self.change_base(base)
 
    def selling_price(self,nominal,curr):
        convert_value = nominal*self.currs[curr]/self.currs[self.base]
        return convert_value+(convert_value*(self.percent/100))
 
    def buying_price(self,nominal,curr):
        convert_value = nominal*self.currs[curr]/self.currs[self.base]
        return convert_value-(convert_value*(self.percent/100))
 
    def change_base(self,new_base):
        self.base = new_base

mc = MoneyChanger(dcur2idr,base='EUR') # object mc dengan base EUR
print('base', mc.base)
print(mc.selling_price(100,'USD')) # nilai jual 100 USD ke EUR (Base)
print(mc.buying_price(100,'USD')) # nilai beli 100 USD ke EUR (Base)
  
mc.change_base('IDR') # Ganti Base object mc ke IDR
print('base', mc.base)
print(mc.selling_price(100,'USD')) # nilai jual 100 USD ke IDR (Base)
print(mc.buying_price(100,'USD'))  # nilai beli 100 USD ke IDR (Base)