# REPRESENTAÇÃO DE UM TERRITÓRIO E DAS INTERSEÇÕES

def eh_territorio(t): 
    '''
    Esta função recebe um argumento universal como argumento e verifica 
    se é um território válido de acordo com a notação definida no enunciado.
    ---------------
    {any} -> {bool}
    '''

    # Verificar se terriório é um tuplo
    if type(t) != tuple:
        return False
    
    # Verificar se não está vazio e não ultrapassa o tamanho máximo
    if len(t) <= 0 or len(t) > 26:
        return False

    # Percorrer cada elemento no territorio
    for el in t:
        # Verificar se os elementos do território são tuplos
        if type(el) != tuple:
            return False
        
        # Verficar se não está vazio e não ultrapassa o tamanho máximo
        if len(el) <= 0 or len(el) > 99:
            return False
        
        # Verificar se o tamanho de cada tuplo é igual
        # Tamanho do primeiro tuplo do território
        size = len(t[0])
        size_el = len(el)
        if size_el != size:
            return False
        
        # Percorrer cada tuplo do território
        for i in el:
            # Verificar se o tipo de cada elemento do território é inteiro
            if type(i) != int:
                return False
            # Verificar se cada elemento do território é um 0 ou um 1
            if i != 0 and i != 1:
                return False
            
    # Se estiver tudo verificado, é um território válido
    return True

def obtem_ultima_intersecao(t): 
    ''' 
    Esta função recebe um território como argumento e retorna a última 
    interseção desse território.
    ------------------
    {tuple} -> {tuple}
    '''

    # A = 65; Z = 90; começamos no 64 e adicionamos a posição da letra
    # Obter a posição da letra e o número
    letra = chr(len(t)+64)
    num = len(t[0])

    return (letra, num)

def eh_intersecao(i): 
    '''
    Esta função recebe um argumento universal e verifica se é uma interseção
    válida de acordo com a notação descrita no enunciado.
    ---------------
    {any} -> {bool}
    '''
     
    # Verificar se é um tuplo
    if type(i) != tuple:
        return False
    
    # Verificar se tem tamanho 2
    size = len(i)
    if size != 2:
        return False
    
    # Verificar se tem primeiro uma string e depois um int
    if type(i[0]) != str or type(i[1]) != int:
        return False
    
    # Verificar se a string tem length 1
    if len(i[0]) > 1 or len(i[0]) == 0:
        return False
    
    # Verificar se a string é uma letra entre A e Z
    if  ord(i[0]) < 65 or ord(i[0]) > 90:
        return False
    
    # Verificar se o inteiro é entre 1 e 99
    if i[1] < 1 or i[1] > 99:
        return False
    
    # Se tudo estiver verificado, é uma interseção
    return True

def eh_intersecao_valida(t, i): 
    '''
    Esta função recebe um território e uma interseção como argumentos e 
    verifica se a interseção é válida de acordo com esse território.
    -------------------------
    {tuple x tuple} -> {bool}
    '''

    # Se i não é interseção, não é válida
    if not eh_intersecao(i):
        return False
    
    else:
        # Obter a letra e o número máximos
        letra_max = 64+len(t)
        num_max = len(t[0])

        # Verficar se a letra está entre A e a letra máxima
        if ord(i[0]) < 65 or ord(i[0]) > letra_max:
            return False
        
        # Verificar se o número está entre 1 e o número de tuplos
        if i[1] < 1 or i[1] > num_max:
            return False
        
        # Se estiver tudo verificado, a interseção pertence ao território
        return True

def eh_intersecao_livre(t, i): 
    '''
    Esta função recebe um território e uma interseção como argumentos e
    verifica se essa interseção do território é livre.
    -------------------------
    {tuple x tuple} -> {bool}
    '''

    # Primeiro index
    prim_index = ord(i[0])-65

    # Segundo index
    seg_index = i[1]-1

    # Retornar True se i estiver vazia
    if t[prim_index][seg_index] == 0:
        return True
    
    # Retornar False se tiver montanha
    else:
        return False
    
def obtem_intersecoes_adjacentes(t, i): 
    '''
    Esta função recebe um território e uma interseção como argumentos e
    obtém as interseções do território adjacentes a essa interseção.
    --------------------------
    {tuple x tuple} -> {tuple}
    '''

    # Tuplo das interseções adjacentes
    inter_adj = ()

    # Calcular interseções adjacentes mesmo que não pertençam ao território
    adj1 = (i[0], i[1]-1)
    adj2 = (chr(ord(i[0])-1), i[1])
    adj3 = (chr(ord(i[0])+1), i[1])
    adj4 = (i[0], i[1]+1)

    # Ver se as interseções são válidas; se sim, adicionar
    if (eh_intersecao_valida(t, adj1)):
        inter_adj += (adj1,)
    if (eh_intersecao_valida(t, adj2)):
        inter_adj += (adj2,)
    if (eh_intersecao_valida(t, adj3)):
        inter_adj += (adj3,)
    if (eh_intersecao_valida(t, adj4)):
        inter_adj += (adj4,)

    # Retornar o tuplo com as interseções adjacentes
    return inter_adj

def ordena_intersecoes(tup): 
    '''
    Esta função recebe um tuplo de interseções como argumento e ordena-as
    de acordo com a ordem de prioridade definida no enunciado.
    ------------------
    {tuple} -> {tuple}
    '''

    # Se o tuplo estiver vazio
    if len(tup) == 0:
        return tup
    
    # Ordenar por prioridade nos números
    else:
        lista = []

        # Por os elementos numa lista
        for i in tup:
            lista.append(i)

        # Ordenar a lista por letra
        lista.sort(key = lambda x: x[0])
        # Ordenar a lista por números 
        lista.sort(key = lambda x: x[1])

        # Transformar num tuplo
        final_tup = tuple(lista)

        # Retornar o tuplo
        return final_tup

def territorio_para_str(t): 
    '''
    Esta função recebe um território como argumento e cria uma representação
    desse território do tipo string, de acordo com a notação definida no
    enunciado. Esta função valida o argumento.
    -------------------
    {tuple} -> {string}
    '''

    # Verificar se é território válido
    if not eh_territorio(t):
        raise ValueError('territorio_para_str: argumento invalido')
    
    else:
        # Variável que guarda a string do território
        ter = " "
        # Número de linhas
        size = len(t)
        # Número de interseções em cada linha
        nums = len(t[0])

        # Se tiver linhas com dois algarismos, alinhar com o segundo algarismo
        if nums > 9:
            ter += " "

            # Adicionar as letras
            for letra in range(size):
                ter += " " + chr(letra+65)
            ter += "\n"

            # Adicionar os números
            for n in range(nums, 0, -1):
                # Se houver tiver só um algarsimo, adicionar um espaço extra
                if n < 10:
                    ter += " " + str(n)
                else:
                    ter += str(n)

                # Adicionar os carateres
                for i in range(size):
                    # Se for montanha
                    if t[i][n-1] == 1:
                        ter += " " + "X"
                    # Se for interseção livre
                    else:
                        ter += " " + "."

                # Readicionar os números, novamente com atenção aos espaços
                if n > 9:
                    ter += " " + str(n) + "\n"
                else:
                    ter += "  " + str(n) + "\n"

            # Adicionar novamente as letras
            ter += "  "
            for letra in range(size):
                    ter += " " + chr(letra+65)

            # Retornar a string do território
            return ter

        # Se todas as linhas tiverem apenas um algarismo
        else:
            ter += " "

            # Adicionar as letras
            for letra in range(size):
                ter += " " + chr(letra+65)
            ter += "\n"

            # Adicionar os números
            for n in range(nums, 0, -1):
                ter += " " + str(n)

                # Adicionar os carateres
                for i in range(size):
                    # Se for montanha
                    if t[i][n-1] == 1:
                        ter += " " + "X"
                    # Se for interseção livre
                    else:
                        ter += " " + "."

                # Adicionar novamente os números
                ter += "  " + str(n) + "\n"
            
            # Adicionar novamente as letras
            ter += "  "
            for letra in range(size):
                ter += " " + chr(letra+65)

            # Retornar a string do território
            return ter

# FUNÇÕES DAS CADEIAS DE MONTANHAS E DOS VALES

def obtem_cadeia(t, i): 
    '''
    Esta função recebe um território e uma interseção como argumentos e
    retorna um tuplo com a cadeia de interseções do território que contém
    essa interseção. Esta função valida os argumentos.
    --------------------------
    {tuple x tuple} -> {tuple}
    '''

    # Verificar se t é território e i é interseção válida
    if not eh_territorio(t) or not eh_intersecao_valida(t, i):
        raise ValueError('obtem_cadeia: argumentos invalidos')
    
    else:
        # Lista com a cadeia
        cad = [i]
        # Ver se estamos a contruir uma cadeia de interseções livres ou 
        # montanha
        tipo = eh_intersecao_livre(t, i)

        for j in cad:
            # Para cada interseção na cadeia obter as adjacentes
            for adj in obtem_intersecoes_adjacentes(t, j):
                # Se for do mesmo tipo da inicial e não estiver já na cadeia
                if eh_intersecao_livre(t, adj) == tipo and adj not in cad:
                    cad.append(adj)

        # Transformar em tuplo
        tup_cad = tuple(cad)

        # Retornar o tuplo ordenado
        return ordena_intersecoes(tup_cad)

def obtem_vale(t, i): 
    '''
    Esta função recebe um território e uma interseção como argumentos e
    retorna um tuplo com os vales dessa interseção. Esta função valida os 
    argumentos.
    --------------------------
    {tuple x tuple} -> {tuple}
    '''

    # Verificar se é t é território e i é interseção válida com montanha
    if not eh_territorio(t) or not eh_intersecao_valida(t, i) or \
        eh_intersecao_livre(t, i):
        raise ValueError('obtem_vale: argumentos invalidos')
    
    else:
        # Tuplo com os vales
        vales = ()

        # Para cada interseção na cadeia
        for a in obtem_cadeia(t, i):
            # Para cada interseção adjacente
            for b in obtem_intersecoes_adjacentes(t, a):
                # Se estiver vazia e não estiver no tuplo ainda
                if t[ord(b[0])-65][b[1]-1] == 0 and b not in vales:
                    vales += (b,)

        # Ordenar as interseções dos vales
        vales = ordena_intersecoes(vales)

        # Retornar os vales
        return vales

# FUNÇÕES DE INFORMAÇÃO DE UM TERRITÓRIO

def verifica_conexao(t, i1, i2): 
    '''
    Esta função recebe um teritório e duas interseções do mesmo como argumentos 
    e verifica se as interseções estão conectadas. Esta função valida os 
    argumentos.
    ---------------------------------
    {tuple x tuple x tuple} -> {bool}
    '''

    # Validar os argumentos
    if not eh_territorio(t) or not eh_intersecao_valida(t, i1) \
    or not eh_intersecao_valida(t, i2):
        raise ValueError('verifica_conexao: argumentos invalidos')
    
    else:
        # Para cada elemento da cadeia de i1 verificar se é igual a i2
        for l in obtem_cadeia(t, i1):
            if l == i2:
                # Se sim retornar True
                return True
            
        # Se i2 não pertence à cadeia de i1, retornar False
        return False

def calcula_numero_montanhas(t): 
    '''
    Esta função recebe um território como argumento e retorna o número de
    montanhas desse território. Esta função valida o argumento.
    ----------------
    {tuple} -> {int}
    '''

    # Gerar erro se não for território
    if not eh_territorio(t):
        raise ValueError('calcula_numero_montanhas: argumento invalido')
    
    else:
        # Definir contador para o num de montanhas
        counter = 0

        # Para cada tuplo no território
        for inter in t:
            # Para cada elemento no tuplo
            for i in inter:
                # Se for montanha incrementar o contador
                if i == 1:
                    counter += 1

        # Retornar o número de montanhas
        return counter
    
def calcula_numero_cadeias_montanhas(t): 
    '''
    Esta função recebe um território como argumento e retorna o número de
    cadeias de montanhas desse território. Esta função valida o argumento.
    ----------------
    {tuple} -> {int}
    '''

    # Gerar erro se não for território
    if not eh_territorio(t):
        raise ValueError('calcula_numero_cadeias_montanhas: argumento invalido')
    
    else:
        # Contador do num de cadeias
        num_cads = 0

        # Obter tamanhos
        size = len(t)
        size_l = len(t[0])

        # A lista permite garantir que não estamos a contar uma montanha 
        # duas vezes
        cads = []

        # Iterar por cada tuplo do território
        for l in range(size):
            # Iterar por cada casa do território
            for j in range(size_l):
                # Passar para notação de interseção
                i = (chr(l+65), j+1)
                # Verificar se a interseção tem montanha
                if not eh_intersecao_livre(t, i):
                    # Se ainda não estiver na lista
                    if i not in cads:
                        num_cads += 1
                        # Iterar pela cadeia dessa interseção
                        cad = obtem_cadeia(t, i)
                        for c in cad:
                            # Adicionar as interseções da cadeia à lista
                            cads.append(c)

        # Retornar o num de cadeias de montanhas
        return num_cads

def calcula_tamanho_vales(t): 
    '''
    Esta função recebe um território como argumento e retorna o tamanho dos
    vales desse território. Esta função valida o argumento.
    ----------------
    {tuple} -> {int}
    '''

    # Gerar erro se não for território
    if not eh_territorio(t):
        raise ValueError('calcula_tamanho_vales: argumento invalido')

    else:
        # Esta lista permite garantir que não estamos a contar uma 
        # montanha  duas vezes
        tamanho_vales = []

        # Obter tamanhos
        size = len(t)
        size_l = len(t[0])

        # Iterar por cada tuplo do território
        for l in range(size):
            # Iterar por cada casa do território
            for j in range(size_l):
                # Passar para notação de interseções
                i = (chr(l+65), j+1)
                # Verificar se a interseção tem montanha
                if eh_intersecao_valida(t, i) and not eh_intersecao_livre(t, i):
                    # Iterar pelos vales dessa interseção
                    for v in obtem_vale(t, i):
                        # Se não estiver na lista dos vales, adicionar
                        if v not in tamanho_vales:
                            tamanho_vales.append(v)

                # Se não for interseção livre, continuar
                else:
                    continue

        # Retornar o tamanho da lista dos vales de todas as interseções
        return len(tamanho_vales)