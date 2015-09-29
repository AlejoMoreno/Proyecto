import os
import sys
import random
import shutil
import re
#Lista de todos los textos
texto  = os.listdir(str('Text/'))
#mover los tags que corresponden a la lista de textos
lt = os.listdir(str('../Ptc/tags/'))
for j in range(len(lt)):
	lt[j]=re.compile('tq').sub('q',lt[j])

li.sort()
lt.sort()
url=''
for i in range(len(lt)):
	for j in range(len(li)):
		if re.match(lt[i],li[j]):
			url = '../Ptc/tags/t'+lt[i]
			shutil.move(str(url),'Tags/')
			print 'move '+str(url)+' to '+'Tags/'
#partir para realizar el cross validation 
url=''
texto  = os.listdir(str('Text/'))
carpetas = ['clouster1','clouster2','clouster3','clouster4','clouster5','clouster6','clouster7','clouster8','clouster9','clouster10']
for i in range(10):
	compara = os.listdir(str('Text/'+carpetas[i]))
	while len(compara)<2024:
		Tarchivo = random.choice(texto)
		if re.match('clouster1',Tarchivo) or re.match('clouster2',Tarchivo) or  re.match('clouster3',Tarchivo) or  re.match('clouster4',Tarchivo) or  re.match('clouster5',Tarchivo) or re.match('clouster6',Tarchivo) or re.match('clouster8',Tarchivo) or re.match('clouster9',Tarchivo) or re.match('clouster10',Tarchivo):
			print 'archivo clouster'
		else:
			Larchivo=re.compile('q').sub('tq',Tarchivo)
			Carchivo=re.compile('q').sub('cq',Tarchivo)
			Turl = 'Text/'+Tarchivo
			Lurl = 'Tags/'+Larchivo
			Curl = 'Code/'+Carchivo
			shutil.move(str(Turl),'Text/'+carpetas[i]+'/')
			shutil.move(str(Lurl),'Tags/'+carpetas[i]+'/')
			shutil.move(str(Curl),'Code/'+carpetas[i]+'/')
			#shutil move
			print 'move '+str(Turl)+' to '+carpetas[i]
			compara = os.listdir(str('Text/'+carpetas[i]))
			texto  = os.listdir(str('Text/'))

