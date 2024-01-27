"""
Дан словарь email-адресов студентов, в качестве ключа используется домен, а в качестве значения список имен.
Необходимо вывести все email-адреса в формате Имя@домен.
"""
emails = {'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
      	'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
      	'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
      	'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
      	'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
      	'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}
for key, value in emails.items():
	# for i in range(0, len(emails)):
	# 	print(value[i] + '@' + key)
	# 	i += 1
	# 	break
#
# i = 0
# j = 0
# x = 0
# for i in range(0, len(emails)):
# 	print(value[i] + '@' + key[j])
# 	i += 1
# 	if i == len(emails):
# 		j += 1
# 		for i in range(0, len(emails)):
# 			print(value[i] + '@' + key[j])
# 			i += 1
# 			j += 1
# 	break
	for i in value:
		print(value + '@' + key)
# print(*sorted({i + '@' + k for k, v in emails.items() for i in v}), sep = '\n')
