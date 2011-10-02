DojoTuba 5 - 01/10/2011

Problema: Palindromes - http://br.spoj.pl/problems/PAL/

Uma cadeia de caracteres é chamada de palíndrome se seqüência de caracteres da esquerda para a direita é igual à seqüência de caracteres da direita para a esquerda (uma outra definição é que o primeiro caractere da cadeia deve ser igual ao último caractere, o segundo caractere seja igual ao penúltimo caractere, o terceiro caractere seja igual ao antepenúltimo caractere, e assim por diante). Por exemplo, as cadeias de caracteres 'mim', 'axxa' e 'ananaganana' são exemplos de palíndromes.

Se uma cadeia não é palíndrome, ela pode ser dividida em cadeias menores que são palíndromes. Por exemplo, a cadeia 'aaxyx' pode ser dividida de quatro maneiras distintas, todas elas contendo apenas cadeias palíndromes: {'aa', 'xyx'}, {'aa', 'x', 'y', 'x'}, {'a', 'a', 'xyx'} e {'a', 'a', 'x', 'y', 'x'}.

Tarefa

Escreva um programa que determine qual o menor número de partes em que uma cadeia deve ser dividida de forma que todas as partes sejam palíndromes.

