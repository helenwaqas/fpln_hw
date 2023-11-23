import os

# Diretório para o qual você deseja entrar
diretorio_alvo = "C:\Users\labmulti24\Desktop\23112023-HW\ex1-proc-hw.py"

# Mudar para o diretório desejado
os.chdir(diretorio_alvo)

import os

# Salvar o diretório atual
diretorio_atual = os.getcwd()

# Diretório para o qual você deseja entrar
diretorio_alvo = "C:\Users\labmulti24\Desktop\23112023-HW\ex1-proc-hw.py"

# Mudar para o diretório desejado
os.chdir(diretorio_alvo)

# ... faça alguma coisa no novo diretório ...

# Voltar ao diretório original
os.chdir(diretorio_atual)

import json, sys, re
## json.dump(p,f)  json.dumps(p)  json.load(f) json.loads(str)


with open('ex1.json', encoding="utf8") as f:
    content = json.load(f)

print(content)
for ele in content:
#    if ele["profssao"] == "pedreiro"
#   	print(ele["name"], ele["idade"])
    if ele["idade"]  > 20 :
		print(ele["name"], ele["idade"])
	

##print(content[1]["profissao"]) 




