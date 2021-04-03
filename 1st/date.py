day = {'01' : 'первое', '02' : 'второе' , '03': 'третье'}
mounth = {'01' : 'января', '02' : 'февраля', '03' : 'марта'}
date = '01.01.1999'
parsed_date = str(date).split('.')
a = day.get(parsed_date[0])
b = mounth.get(parsed_date[1])
c = parsed_date[2]
print(date)
print(parsed_date)
print('{} {} {} года'.format(a,b,c))