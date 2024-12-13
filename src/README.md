# notas/src

Códigos-fonte das notas de aula.

## Conteúdos

* ./AnaliseMatematicaI - notas de aula sobre Análise Matemática I

* ./CalculoI - notas de aula sobre Cálculo I

* ./EaD - notas de aula sobre EaD

* ./EDO - notas de aula sobre EDO

* ./GeometriaAnalitica - notas de aula sobre Geometria Analítica

* ./MatematicaNumericaI - notas de aula sobre Matemática Numérica I

* ./MatematicaNumericaII- notas de aula sobre Matemática Numérica II

* ./MatematicaNumericaIII - notas de aula sobre Matemática Numérica III

* ./MatematicaNumericaParalela - notas de aula sobre Matemática Numérica Paralela

* ./MetodoElementosFinitos - notas de aula sobre MEF

* ./MiniCalcPy - minicurso de Cálculo com Python

* ./MiniMPI - minicurso de C++/MPI (descontinuado!)

* ./Vetores - notas de aula sobre Vetores

## Boas Práticas

### Matplotlib Graphics

```
plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 12,
     "font.sans-serif": "Computer Modern Roman",
     "text.latex.preamble": r"\usepackage{amsmath} \usepackage{amssymb}",
     "figure.figsize": [4, 4],
     "figure.dpi": 300
     })
```

### Listings

```
\ifispython
\begin{lstlisting}[style=input, caption={\python}]
...
\end{lstlisting}
%
\begin{lstlisting}[style=output]
...
\end{lstlisting}  
\fi
```

* Obs.: dentro de `itemize/enumerate` use `xrightmargin=0.19in`

## Licença

O texto do material das notas de aula é disponibilizado nos termos da Licença Atribuição-CompartilhaIgual 4.0 Internacional Creative Commons. Para visualizar uma cópia desta licença, visite https://creativecommons.org/licenses/by-sa/4.0/deed.pt_BR ou mande uma carta para Creative Commons, PO Box 1866, Mountain View, CA 94042, USA. Códigos, ícones e outros elementos gráficos podem estar sujeitos a condições adicionais.

