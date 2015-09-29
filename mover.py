import os
import sys
import random
import shutil
import re

texto=os.listdir(str('../Ptc/Text/'))
tags=os.listdir(str('../Ptc/tags/'))
codigo=os.listdir(str('../Ptc/codigo/'))

while len(compara)<168245:
	Tarchivo = random.choice(texto)
	Larchivo=re.compile('q').sub('tq',Tarchivo)
	Carchivo=re.compile('q').sub('cq',Tarchivo)
	Turl = '../Ptc/Text/'+Tarchivo
	Lurl = '../Ptc/tags/'+Larchivo
	Curl = '../Ptc/codigo/'+Carchivo
	shutil.copy(str(Turl),'Text/')
	shutil.copy(str(Lurl),'tags/')
	shutil.copy(str(Curl),'codigo/')
	print 'copy '+str(Turl)+' to CrossValidation/Text/'
	compara=os.listdir(str('Text/'))
