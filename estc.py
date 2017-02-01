import random

vet = [0, 0, 0]

def main():
    global vetor

    regiao1 = {
                'regiao1' : [0, 0],
                'regiao2' : [0, 2/3.0],
                'regiao3' : [2/3.0, 1]
              }

    regiao2 = {
                'regiao1' : [0, 1/4.0],
                'regiao2' : [1/4.0, 3/4.0],
                'regiao3' : [3/4.0, 1]
              }

    regiao3 = {
                'regiao1' : [0, 1/3.0],
                'regiao2' : [1/3.0, 2/3.0],
                'regiao3' : [2/3.0, 1]
              }

    for i in range(0, 1000):
        fstRegion = random.randint(0, 2)
        vet[fstRegion] += 1
        for j in range(0, 999):
            if fstRegion == 0:
                fstRegion = calculo(regiao1)
            elif fstRegion == 1:
                fstRegion = calculo(regiao2)
            elif fstRegion == 2:
                fstRegion = calculo(regiao3)
            else:
                exit(1)

    media1 = float(vet[0])/1000000.0
    media2 = float(vet[1])/1000000.0
    media3 = float(vet[2])/1000000.0

    print 'As quantidades foram: ' + str(vet)

    print 'As medias foram:\nRegiao 1: ' + str(media1) + '\nRegiao 2: ' + str(media2) + '\nRegiao 3: ' + str(media3)


def calculo(regiao):
    randNumber = random.uniform(0, 1)
    if randNumber >= regiao['regiao1'][0]  and randNumber < regiao['regiao1'][1]:
        vet[0] += 1
        return 0
    elif randNumber >= regiao['regiao2'][0]  and randNumber < regiao['regiao2'][1]:
          vet[1] += 1
          return 1
    elif randNumber >= regiao['regiao3'][0]  and randNumber < regiao['regiao3'][1]:
          vet[2] += 1
          return 2
    else:
        exit(1)

main()
