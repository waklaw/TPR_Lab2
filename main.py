import pandas as pd

pd.options.display.max_columns = 9
pd.set_option('display.width', 1400)

with open('A.txt') as fileA:
    M1 = float(fileA.readline())
    D1 = float(fileA.readline())
    P1 = float(fileA.readline())
    D2 = float(fileA.readline())
    P2 = float(fileA.readline())

with open('B.txt') as fileB:
    M2 = float(fileB.readline())
    D11 = float(fileB.readline())
    P11 = float(fileB.readline())
    D22 = float(fileB.readline())
    P22 = float(fileB.readline())

with open('C.txt') as fileC:
    P3 = float(fileC.readline())
    P4 = float(fileC.readline())
    P5 = float(fileC.readline())
    P6 = float(fileC.readline())


print('Варіант 1')

#Будівництво великого заводу (великий попит)

CD1 = D1 * 5 - M1
print('Будівництво великого заводу (великий попит)')
print('Чистий дохід:',CD1, '\n')

#Будівництво великого заводу (малий попит)

MZ1 = D2 * 5 - M1
print('Будівництво великого заводу (малий попит)')
print('Можливі збитки:',MZ1, '\n')


print('Варіант 2')

#Будівництво малого заводу (великий попит)

CD2 = D11 * 5 - M2
print('Будівництво малого заводу (великий попит)')
print('Чистий дохід:',CD2, '\n')

#Будівництво малого заводу (малий попит)

MZ2 = D22 * 5 - M2
print('Будівництво малого заводу (малий попит)')
print('Можливі збитки:',MZ2, '\n')


print('Варіант 3')
print('Затримка в один рік\n')
CD3 = D1 * 4 - M1
print('Будівництво великого заводу (великий попит)')
print('Чистий дохід:',CD3, '\n')
MZ3 = D2 * 4 - M1
print('Будівництво великого заводу (малий попит)')
print('Можливі збитки:',MZ3, '\n')
CD4 = D11 * 4 - M2
print('Будівництво малого заводу (великий попит)')
print('Чистий дохід:',CD4, '\n')
MZ4 = D22 * 4 - M2
print('Будівництво малого заводу (малий попит)')
print('Можливі збитки:',MZ4, '\n')


#Чиста приведена вартість для варіантів рішення:
NVPA = 0.75 * CD1 + 0.25 * MZ1
NVPCB = round(NVPA,2)
print('Результат прибутку Варіанту 1:', NVPA, 'тис.грн', '\n')

NVPB = 0.75 * CD2 + 0.25 * MZ2
NVPCB = round(NVPB,2)
print('Результат прибутку Варіанту 2:', NVPB, 'тис.грн', '\n')

NVPCA = 0.8*(0.9*CD3+0.1*MZ3)+0.2*(M1)
NVPCB = round(NVPCA,2)
print('Результат прибутку Варіанту 2(1):', NVPCA, 'тис.грн', '\n')

NVPCB = 0.8*(0.9*CD4+0.1*MZ4)+0.2*(M2)
NVPCB = round(NVPCB,2)
print('Результат прибутку Варіанту 2(2):', NVPCB, 'тис.грн', '\n')

if (NVPA > NVPB and NVPA > NVPCA and NVPA > NVPCB):
    print('Найкраща стратегія - Варіант 1\n')
elif (NVPB > NVPA and NVPB > NVPCA and NVPB > NVPCB):
    print('Найкраща стратегія - Варіант 2\n')
elif (NVPCA > NVPA and NVPCA > NVPB or NVPCB > NVPB and NVPCB > NVPA):
    print('Найкраща стратегія - Варіант 3\n')
else:
    print('Помилка\n')
