# ODE Solver



Implementação de alguns métodos numéricos de resolução de equações diferenciais ordinárias.



## Especificação da entrada:



A entrada deve ser dada na forma "t0, y0, f, h, tf, metodos", sem as aspas, onde:



* t0 é o valor de t do ponto incial

* y0 é o valor de y do ponto inicial

* f é a função derivada de y(t)

* h é o tamanho do passo desejado

* tf é o valor final que se deseja encontrar

* metodos é uma lista de índices, separados por espaços, dos métodos numéricos que devem ser usados para encontrar y(tf). Os índices podem ser encontrados na tabela abaixo



| Indíce | Método            |

| ------:| ----------------- |

| 0      | Euler Simples     |

| 1      | Euler Inverso     |

| 2      | Euler Composto    |

| 3      | Runge-Kutta       |
| 4      | Adams-Bashforth 2 |
| 5      | Adams-Bashforth 3 |
| 6      | Adams-Bashforth 4 |
| 7      | Adams-Bashforth 5 |
| 8      | Adams-Bashforth 6 |
| 9      | Adams-Moulton 2   |
| 10     | Adams-Moulton 3   |
| 11     | Adams-Moulton 4   |
| 12     | Adams-Moulton 5   |
| 13     | Adams-Moulton 6   |



Nota: Para dar valores de ponto flutuante na entrada usar a notação com ponto (.), ao invés de vírgula (,)



### Exemplo de entrada:



```0, 1, 2*t+3*y, 0.1, 0.5, 0 1 2 3```

```0, 1, cos(t)*y, 5, 20, 3 8 12```




## Especificação da Saída:



O código vai gerar duas saídas, a lista de todos os pontos calculados na forma `y(tn) = yn`, e um gráfico em que esses pontos são plotados.
