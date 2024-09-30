cpf = str(input( "Digite os digitos do CPF"))

while len (cpf) !=9:
    print("CPF invalido. Digite apenas 9(nove) numeros")
    cpf = str(input( "Digite os primeiros 9 digitos do CPF"))

um = int(cpf[0])*10; dois = int(cpf[1])*9; tres = int(cpf[2])*8; quatro = int(cpf[3])*7; cinco = int(cpf[4])*6; seis = int(cpf[5])*5; sete = int(cpf[6])*4; oito = int(cpf[7])*3; nove = int(cpf[8])*2;

soma = um + dois + tres + quatro + cinco + seis + sete + oito + nove
resto = soma % 11

if resto < 2:
    digito = "0"
else:
    digito = str(11 - resto)

cpf = cpf + digito

um = int(cpf[0])*11; dois = int(cpf[1])*10; tres = int(cpf[2])*9; quatro = int(cpf[3])*8; cinco = int(cpf[4])*7; seis = int(cpf[5])*6; sete = int(cpf[6])*5; oito = int(cpf[7])*4; nove = int(cpf[8])*3; primeiro_digito = int(digito) * 2

soma = um + dois + tres + quatro + cinco + seis + sete + oito + nove + primeiro_digito

resto = soma % 11

if resto < 2:
    digito = "0"
else:
    digito = str(11 - resto)

print("n\O Numero do CPF é:", cpf + digito)
