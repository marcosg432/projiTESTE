st = float(input("digite o salario de um trabalhador: "))
p = float(input("valor da prestacao: "))
salario = st * 0.20

if(p > salario):
    print("emprestimo nao concedido")
else:
    print("emprestimo concedido")