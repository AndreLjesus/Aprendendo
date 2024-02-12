#include <stdio.h>

int main(void) {

  float aposta = 0;
  float dinheiro = 0.0;
  int rodadas = 0;
  int dias = 0;

  printf("Digite o valor a ser apostado: ");
  scanf("%f", &dinheiro);

  printf("Digite o numero de apostas a ser feitas: ");
  scanf("%d", &rodadas);

  printf("Digite a vela desejada: ");
  scanf("%f", &aposta);

  while (rodadas > 0) {
    dinheiro = dinheiro * aposta;
    rodadas -= 1;
    dias += 1;
  }

  if (dinheiro > 50) {
    printf("\nvale a pena apostar\n");
    printf("O valor após %d dias é de: %f\n", dias, dinheiro);
  } else {
    printf("\nnão vale a pena apostar\n");
    printf("O valor após %d apostas é de: %f\n", dias, dinheiro);
  }

  return 0;
}
