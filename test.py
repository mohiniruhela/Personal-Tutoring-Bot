from bardapi import Bard

token = 'YAgajtkgvcXtOUgpMG_dcdgj1I2gDANVsYqHYlLWh9_QUkWO_yxcwOGSK09uDInhM1oXVA.'
bard = Bard(token=token)
print( bard.get_answer("what is ml?")['content'])

