# notas/MiniMPI/03_Euler

## Aplicação

Método de Euler

Problema de valor inicial:

	 u0' = u1 - u2 + t,  u0(0) = 1;
	 u1' = 3t^2,         u1(0) = 1;
	 u2' = u1 + exp(-t), u2(0) = -1; 0 <= t <= 1.

Solução analítica:

	u0(t) = -0.05t^5 + 0.25t^4 + t + 2;
	u1(t) = t^3 + 1;
	u2(t) = 0.25t^4 + t - exp(-t);

## Contato

phkonzen@gmail.com

## Licença

Este trabalho está licenciado sob a Licença Atribuição-CompartilhaIgual 4.0 Internacional Creative Commons. Para visualizar uma cópia desta licença, visite http://creativecommons.org/licenses/by-sa/4.0/ ou mande uma carta para Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.
