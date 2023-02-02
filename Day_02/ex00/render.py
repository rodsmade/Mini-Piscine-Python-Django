import settings as cv_vars
import sys 

# validar argc argv, precisa entrar 1 argumento que termina com .template
# python3 render.py file.template

# escrever o arquivo de template com uma estrutura básica parametrizada que inclui no mínimo:
# doctype, head, body, the page’s title; name, surname, age, profession of resume owner.
# <p>"-Who are you?
# -A {name}!"</p>

# ler arquivo de settings pra pegar um dicionário de termos pra injetar no html (name = qqcoisa, etc)

# montar um html a partir do template, injetando os valores encontrados no settings


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit()
    
    if not sys.argv[1].endswith(".template"):
        sys.exit()

    template_path = sys.argv[1]

    with open(template_path) as template_file:
        contents = template_file.read()
        contents = contents.replace("{name}", str(cv_vars.name))
        contents = contents.replace("{surname}", str(cv_vars.surname))
        contents = contents.replace("{age}", str(cv_vars.age))
        contents = contents.replace("{profession}", str(cv_vars.profession))
        
        output_file = open("cv.html", "w")
        output_file.write(contents)
        output_file.close()