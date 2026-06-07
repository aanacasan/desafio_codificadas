# Desafio Codeforces — Mentoria Codificadas | Além do Código
 
## Sobre este repositório
 
Este repositório contém minha resolução para o desafio de programação proposto na mentoria, utilizando problemas da plataforma [Codeforces](https://codeforces.com/) com auxílio de Inteligência Artificial.
 
---
 
## Problemas escolhidos
 
| # | Nome do problema | Link | Dificuldade |
|---|-----------------|------|-------------|
| 1 | Way Too Long Words | https://codeforces.com/problemset/problem/71/A | 800 |
| 2 | Team | https://codeforces.com/problemset/problem/231/A | 800 |
| 3 | Bit++ | https://codeforces.com/problemset/problem/282/A | 800 |
 
---
 
## Problema 1 — Way Too Long Words
 
### O que o problema pede?
O problema pede para que ao receber uma lista de palavras, é necessário verificar se cada palavra tem mais de dez letras. Caso tenha, ela será abreviada. Neste caso, a primeira e a última letra são mantidas, mas haverá um número correspondente à quantidade de letras entre a primeira letra e a última letra. Se a palavra tiver menos do que dez letras, ela não sofrerá alteração.
 
 
### Como eu resolvi?
Tendo a entrada de uma lista de palavras, usando len(word), eu consigo saber quantas letras essa palavra possui. Assim, se a palavra for maior que 10, ela será abreviada da seguinte forma: o código word[0] pega a primeira letra; com o código len(word) - 2, as duas letras (primeira e última) são subtraídas para saber a quantidade de letras que restamn entre elas; e, por fim, word[-1] é o código para que a última letra apareça na saída. Se a minha condição for satisfatória, levando todos os pontos descritos até aqui como verdadeiros, a palavra será abreviada. Caso contrário, sendo as palavras com a quantidade de letras menor que dez, ela aparecerá escrita normalmente, sem abreviação. 

 
 
### Código

n = int(input())
for _ in range(n):
    word = input()
    if len(word) > 10:
        print(f"{word[0]}{len(word)-2}{word[-1]}")
    else:
        print(word)
 
## Problema 2 — Team
 
### O que o problema pede?

Dada uma quantidade de problemas de programação para serem resolvidos, um trio de amigos, Petya, Vasya e Tonya, comprometem-se a resolvê-los caso pelo menos dois deles tenham certeza da resposta. A representação usada para quando se sabe resolver o problema é o número 1, mas quando não sabe é o número 0. Com isso, o intuito do problema é saber quantos problemas de programação a equipe formada pelo trio de amigos consegue resolver.
 
### Como eu resolvi?

Os amigos precisam da quantidade de problemas, mas avaliar se eles sabem ou não, por isso, o código da primeira linha, n = int(input()), faz a leitura de um número inteiro que será colocado no input. No caso do problema, nós teremos três número separados por espaço, sendo esses números 0 ou 1. Por isso, para imprimir os valores na tela, foi necessário colocar .split para que os números estejam separados por espaço. O map converte o valor que vem como string em número inteiro. Para saber se os amigos vão solucionar os problemas, eu preciso da soma de cada linha. Se a soma for maior ou igual a 2, eles vão solucionar o problema, caso contrário não vão. Para que esse processo se repita para cada um dos problemas, usamos o for _ in range(n) na soma.
 
 
### Código

n = int(input())
print(sum(sum(map(int, input().split())) >= 2 for _ in range(n)))
 
## Problema 3 — Bit++
 
### O que o problema pede?

O exercício dá uma variável x que começa com o valor 0 e n instruções, sendo ou ++X ou X++, estas duas primeiras somam 1 ao valor de x; ou --X ou X--, que subtrai 1 do valor de x. Depois de passar todas as instruções em ordem, sabemos o valor de x.

 
### Como eu resolvi?

O n representa a quantidade de instruções que serão fornecidas e isso dependerá do número que for digitado. O valor começará em zero, ou seja, x = 0. Esse valor será alterado pelas instruções. Eu usei o for, que é um loop que vai rodar a cada instrução. A cada repetição, o programa lê uma string, com isso a última linha do código vai verificar se a instrução soma 1 ou subtrai 1. Aqui é importante saber que independentemente se temos ++X ou X++, a interpretação deverá ser a soma de +1, representado no código como ++. Por isso, tanto no número positivo, quanto no negativo, a posição do ++ ou -- não foi cons
 
### Código

n = int(input())
x = 0
for _ in range(n):
    s = input()
    x += 1 if '++' in s else -1
print(x)

---
 
## IA utilizada
 
**Qual IA você usou?**
Claude
 
**Como a IA te ajudou?**

Eu usei a IA como corretor e auxiliar na compreensão das minhas linhas de código.

---
 
## Reflexão
 
### Dificuldades encontradas

Acredito que uma das maiores dificuldades é nomear a variável. Mas, no final, acabei nomeando genericamente. Usar o terminal para testar se o código está rodando foi um desafio dentro do desafio, mas, com ajuda da IA, eu verifiquei que a meneira como eu estava fazendo estava errada.
 
### O que aprendi

Aprendi que a IA pode ser uma grande auxiliar no aprendizado de como aplicar os códigos. Dúvidas muito primáruias como rodar o código no terminal para que eu consiga verificar se as saídas estão corretas foram extremamente importantes para que eu conseguisse firmar esse processo e propagar para os problemas 2 e 3.
 
 
### Como foi a experiência?

Minha experiência foi incrivelmente satisfatória porque eu me desafiei a resolver os problemas utilizando uma linguagem que é nova para mim e que eu estou descobrindo gostar muito. Ter a oportunidade de participar do Desafio Codificadas dá motivação para continuar focada nos meus estudos além da Universidade.
