from tabulate import tabulate
import random


def samplingLoja():
    listaItensComuns = ['Poção de cura menor', 'Espada curta simples', 'Adaga simples', 'Lança simples', 'Escudo simples', 'Adaga arremessável', 'Arco simples', 'Aljava com 20 flechas']
    listaItensRaros = ['Poção bafo de fogo', 'Poção bafo venenoso', 'Espada mágica', 'Adaga mágica', 'Lança mágica', 'Escudo mágico', 'Adaga vorpal', 'Arco encantado', 'Aljava com 20 flechas elementais']

    samplingComum = random.sample(listaItensComuns, k=int(len(listaItensComuns)/2))
    samplingRaros = random.sample(listaItensRaros, k=2)
    quantComum = [None] * len(samplingComum)
    precoComum = [None] * len(samplingComum)
    quantRaros = [None] * len(samplingComum)
    precoRaros = [None] * len(samplingRaros)
    listaFinal  = [None] * (len(samplingComum) +  len(samplingRaros))

    for i in range(0, len(samplingComum)):
        quant = random.randint(1, 19)
        val = 20 - quant
        quantComum[i] = quant
        precoComum[i] = val

    for i in range(0, len(samplingRaros)):
        quant = random.randint(1, 19)
        val = 200 - quant
        quantRaros[i] = quant
        precoRaros[i] = val
    
    for i in range(0, len(samplingComum)):
        listaFinal[i] = [samplingComum[i], quantComum[i], precoComum[i]]

    for i in range(0, len(samplingRaros)):
        listaFinal[len(samplingComum) + i] = [samplingRaros[i], quantRaros[i], precoRaros[i]]

    return listaFinal