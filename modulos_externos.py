"""
Modulos externos  -- https://pypi.org/

utilizamos o gerenciador de pacotes Pip - Python Installer Package

colorama - permite a impressão de textos coloridos no  terminal

from colorama import init, Fore
init()
print(Fore.CYAN + 'Isabela')

"""
import pydf
pdf = pydf.generate_pdf('<h1>this is html</h1>')
with open('test.pdf', 'wb') as f:
    f.write(pdf)


