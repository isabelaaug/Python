"""
Debugando com PDB

PDB - Python Debugger
-necessario importar biblioteca e utilizar set_trace()

comandos:

l - listar onde estamos no codigo
n - proxima linha
p - imprime variavel
c - continua a execuçao - finaliza debugging

--------------------------------------------------
import pdb

nome = 'isabela'
sobrenome = 'oliveira'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
final = nome_completo
print(final)

-> nome_completo = nome + ' ' + sobrenome
(Pdb) l
  9  	import pdb
 10
 11  	nome = 'isabela'
 12  	sobrenome = 'oliveira'
 13  	pdb.set_trace()
 14  ->	nome_completo = nome + ' ' + sobrenome
 15  	final = nome_completo
 16  	print(final)
 17
[EOF]
(Pdb) nome
'isabela'
(Pdb) final
 NameError: name 'final' is not defined
(Pdb) n
> c:\users\isabe\pycharmprojects\guppy\debugando_pdb.py(15)<module>()
-> final = nome_completo
(Pdb) l
 10
 11  	nome = 'isabela'
 12  	sobrenome = 'oliveira'
 13  	pdb.set_trace()
 14  	nome_completo = nome + ' ' + sobrenome
 15  ->	final = nome_completo
 16  	print(final)
 17
[EOF]
(Pdb) c
isabela oliveira

---------------------------------------------
A partir do 3.7 não é necessário importar a biblioteca

nome = 'isabela'
sobrenome = 'oliveira'
breakpoint()
nome_completo = nome + ' ' + sobrenome
final = nome_completo
print(final)

"""



