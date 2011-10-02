def palindrome(palavra):
    return palavra[::-1] == palavra

def numero_de_palindromes(palavra):
    palindromes = []

    i = 1

    # Encontra maior palindrome na palavra, remove essa parte da palavra
    # e adiciona na lista de palindromes
    while palavra:
        if palindrome(palavra):
            palindromes.append(palavra)
            break
        elif palindrome(palavra[:-i]):
            palindromes.append(palavra[:-i])
            palavra = palavra[-i:]
            i = 1
        else:
            i += 1

    return len(palindromes)

if __name__ == '__main__':
    teste = 1
    tamanho = int(raw_input())

    while tamanho:
        palavra = raw_input()
        print 'Teste', teste
        print numero_de_palindromes(palavra), '\n'
        tamanho = int(raw_input())
        teste += 1

