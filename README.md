# ODE Solver

Implementação de alguns métodos numéricos de resolução de equações diferenciais ordinárias.

## Requisitos:

O programa depende de duas bibliotecas de python:

* `matplotlib.pyplot` para a criação e apresentação dos gráficos de cada método

* `sympy` para transformar a expressão de f em uma função de python

Ambas bibliotecas podem ser instaladas com `sudo pip install matplotlib sympy`

_Nota:_ A biblioteca matplotlib requer a instalação do pacote de GUI Tk. [Guia de Instalação do Tk](http://www.tkdocs.com/tutorial/install.html)

## Uso:

Para executar o programa basta colocar essa linha no seu terminal:

`$ python main.py [input_file] <-v -p> <output_file>`

Onde 

* `-v` faz a apresentação dos valores no modo verboso (todos os ts de `t0` a `tf`)
* `-p` faz a apresentação do gráfico de cada problema

## Especificação da entrada:

A entrada deve ser dada na forma `metodo y0 y1 ... t0 h tf f <o>`, sem as aspas, onde:

* `metodo` é o código do método que deve ser utilizado

| Método           | Código           |
| ----------------:| ---------------- |
| Euler Simples    | euler            |
| Euler Inverso    | euler_inverso    |
| Euler Aprimorado | euler_aprimorado |
| Runge-Kutta      | runde_kutta      |
| Adams-Bashforth  | adam_bashforth   |
| Adams-Moulton    | adam_moulton     |

_Obs.:_ No caso dos métodos de passos múltiplos pode ser especificado um método de passo simples para gerar os `o` primeiros pontos da seguinte forma:

    `[metodo_de_passos_multiplos]_by_[metodo_de_passo_simples]`

_Obs. 2:_ O método de Adams-Bashforth 1 é equivalente ao método de Euler Simples; o método de Adams-Moulton 1 é equivalente ao método de Euler Inverso; o método de Adams-Moulton 2 é equivalente ao método de Euler Composto.

* `y0 y1 ...` é uma sequência de valores iniciais conhecidos de y (y(t0), y(t1), ...)

* `t0` é o valor inicial de t

* `h` é o tamanho do passo desejado

* `tf` é o valor final que se deseja encontrar

* `f` é a função derivada de y(t) que deve ser dada na formatação de expressão da biblioteca `math`, ou seja, t² é escrito `t**2`

_Obs.:_ Para dar valores de ponto flutuante na entrada usar a notação com ponto (.), ao invés de vírgula (,)

* `<o>` é a ordem do método no caso de métodos de passos múltiplos

### Exemplo de entrada:

```
adam_bashforth 0.0 0.1 0.23 0.402 0.6328 0 0.1 20 1-t+4*y 5
```

```
euler 0 0 20 1-t+4*y
```

## Especificação da Saída:

O código pode gerar até duas saídas: o resultado de y(tf), e um gráfico dos pontos encontrados.

_Obs.:_ Os pontos intermediários podem ser também apresentados 

### Exemplo de Saída:

A entrada `0, 1, cos(t)*y, 0.1, 20, 3 8 13` gera a seguinte saída:

```
Runge-Kutta
y( 20.0 ) = 2.49164881245

Adams-Bashforth 6
y( 20.0 ) = 2.49165201274

Adams-Moulton 6
y( 20.0 ) = 2.49164908305
```

e o gráfico a seguir:

![y' = cos(t)*y](grafico_exemplo.png)
