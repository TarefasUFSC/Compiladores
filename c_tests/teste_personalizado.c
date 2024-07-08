#include <stdio.h>
#include <stdlib.h>
#include "teste.h"
#define MAX 100

// Estrutura para um ponto em um espaço 2D
typedef struct
{
    float x;
    float y;
} Ponto2D;

// Função para calcular a distância entre dois pontos
float distanciaEntrePontos(Ponto2D p1, Ponto2D p2)
{
    float dx = p1.x - p2.x;
    float dy = p1.y - p2.y;
    return sqrt(dx * dx + dy * dy); // Uso da função sqrt da biblioteca math
}

int main()
{
    Ponto2D ponto1 = {2.5, 3.1};
    Ponto2D ponto2 = {4.6, 5.0};

    /* Cálculo e exibição da distância entre dois pontos */
    float distancia = distanciaEntrePontos(ponto1, ponto2);
    printf("A distância entre os pontos é: %.2f\n", distancia);

    // Exemplo de loop e condicionais
    for (int i = 0; i < MAX; i++)
    {
        if (i % 2 == 0)
        {
            printf("Número par: %d\n", i);
        }
        else
        {
            // Comentário dentro de um bloco else
            printf("Número ímpar: %d\n", i);
        }
    }
    int i = 0;
    i++;
    i--;
    return 0;
}