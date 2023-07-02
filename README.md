# Algorithms
* [Binary Search](https://github.com/IaraSelva/study-cases-of-living-coding/blob/main/algorithms/binary_search.js)

# Data Structures
* [Linked List](https://github.com/IaraSelva/study-cases-of-living-coding/blob/main/data_structures/lists/linked_list.js)
* [Stack](https://github.com/IaraSelva/study-cases-of-living-coding/blob/main/data_structures/lists/stack.js)
* [Queue](https://github.com/IaraSelva/study-cases-of-living-coding/blob/main/data_structures/lists/queue.js)

# Problems
* [Minimum Domino Rotations For Equal Row](https://github.com/IaraSelva/study-cases-of-living-coding/blob/main/solved_problems/min_domino_rotations.js): [LeetCode](https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/)
>
* [Valid Parentheses](https://github.com/IaraSelva/study-cases-of-living-coding/blob/main/solved_problems/valid_parentheses.js): [LeetCode](https://leetcode.com/problems/valid-parentheses/)
>Sabe-se que todo parênteses, colchete ou chaves aberto precisa ser fechado na ordem em que ele foi aberto. Se um parênteses for aberto e depois um colchete, o parênteses deve ser fechado primeiro e depois o colchete. Para isso, usar o conceito de pilhas (LIFO). Sempre que um sinal for aberto é colocado na fila. Sempre que for fechado, verifica-se o último elemento da fila e, caso seja seu complementar estará válido. Caso contrário, inválido.
* [Candy Types](https://github.com/IaraSelva/study-cases-of-living-coding/blob/main/solved_problems/candy_types.js): [LeetCode](https://leetcode.com/problems/distribute-candies/)
>
Primeiro, o número de doces permitidos será sempre metade do tamanho da lista de tipos de doces que ela possui. Usando um map onde a chave é o tipo e o valor é a quantidade daquele tipo, iterar a lista e preencher o map com essas informações. Sabendo agora a quantidade de doces de cada tipo, se o tamanho da quantidade permitida for maior que o tamanho do map de tipos, sabe-se que ela poderá comer de todos os tipos então é só retornar o tamanho do map. Caso contrário, iterar sobre o map sempre reduzindo 1 de cada tipo de doce e incrementando 1 ao contador enquanto estive dentro do limite permitido de doces que ela pode comer. Retornar o contador.
* [String Compression](https://github.com/IaraSelva/study-cases-of-living-coding/blob/main/solved_problems/string_compress.js): [LeetCode](https://leetcode.com/problems/string-compression/)
>
A ideia desse exercício é economizar memória. Então os caracteres devem ser reorganizados e **não** criar uma nova string como resposta. Usando dois ponteiros (leitura e escrita) percorrer a string. O ponteiro de leitura incrementa o contador enquanto a letra encontrada for igual à última letra lida. Caso a letra troque, o ponteiro de escrita escreve a letra, anda 1 e escreve o valor do contador e volta o valor do contador para 1.
* [Two Sum](https://github.com/IaraSelva/study-cases-of-living-coding/blob/main/solved_problems/two_sum.js): [LeetCode](https://leetcode.com/problems/two-sum)
>
A ideia é retornar a posição de dois números de um array que somados dão o valor que se quer encontrar (target). Usando um map (chave:valor) onde a chave é o complementar (_target_ menos número atual da lista) e o valor é o index. Percorrer a lista: o map será povoado com o complementar ao número e seu respectivo index. Caso o valor complementar seja encontrado, o array de indexes recebe o índice atual e o índice do complementar guardado no map.
* [Best Time to Buy and Sell Stock](https://github.com/IaraSelva/study-cases-of-living-coding/blob/main/solved_problems/buy_sell_stock.js): [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
>
A ideia é comprar o mais barato possível e vender o mais caro possível para otimizar os lucros. Usando dois ponteiros: venda e compra. A compra começa na posição zero e a venda na posição 1 (pois não posso vender no passado). O ponteiro de compra fica parado em um número até que (e se) for encontrado um número menor. O ponteiro de compra percorre toda a lista tentando encontrar o maior número possível para a venda. E, caso encontre um número menor que o atual de compra, o ponteiro de compra muda de posição.
  
