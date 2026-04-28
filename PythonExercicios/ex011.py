print('Faça um programa que leia a largura e a altura de uma parede em metros, \ncalcule a sua área e a quantidade de tinta '
      'necessária para pinta-lá, \nsabendo que cada litro de tinta, pinta uma área de 2m**2 (metros quadrados)')
l=float(input('Largura da parede: '))
a=float(input('Altura da parede: '))
area=a*l
#tinta=area/2
print('Sua parede tem a dimensão de {}X{} e sua área é de {}m².'.format(l, a, area))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(area/2))