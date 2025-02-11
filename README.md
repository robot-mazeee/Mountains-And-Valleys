# Mountains and Valleys - Description

## Territory

A territory is a rectangular shape formed by vertical (identified by letters from A to Z) and horizontal (identified by numbers from 1 to 99) paths.

## Intersection

A point in a territory where a vertical path and a horizontal path cross is called an intersection. Each intersection is identified by the identifiers of the paths that form it. Two intersections are adjacent if they are connected by a vertical or horizontal path with no other intersections between them. Intersections can be free or occupied by mountains.

## Mountain Chains and Valleys

Two occupied or free intersections are connected if it is possible to draw a path between them, containing only occupied or free intersections, respectively. A chain of mountains is a set of connected occupied intersections that are not connected to any other mountain. Similarly, a chain of free intersections adjacent to a mountain or to a chain of mountains that contains that mountain is called a valley.

## Example

<img width="477" alt="image" src="https://github.com/user-attachments/assets/f2b85a7f-32f9-4978-a87f-309c5de3dab2" />

Num territ ́orio, todas as interse ̧c ̃oes podem estar livres ou ocupadas por montanhas.
O exemplo da Figura 1a) mostra um territ ́orio formado por 7 caminhos verticais (Nv = 7)
por 4 caminhos horizontais (Nh = 4), com montanhas situadas nas interse ̧c ̃oes A2, C3 e
D1.

No exemplo da Figura 1b) a montanha em A1 est ́a conetada `a montanha
em A3, mas n ̃ao est ́a conetada `a montanha em C3.

 Os exemplos das Figuras 1b) e 1c) mostram duas cadeias de
montanhas com os respetivos vales.

Figura 1: a) Territ ́orio com trˆes montanhas situadas nas interse ̧c ̃oes A2, C3 e D1. b)
Territ ́orio com duas cadeias de montanhas: uma formada por quatro montanhas (A1,
A2, B2 e A3) e a outra formada por uma montanha (C3). c) Territ ́orio com as interse ̧c ̃oes
do vale da montanha A1 (igual para A2, B2 e A3) marcadas com um ponto verde e
as interse ̧c ̃oes do vale da montanha C3 marcadas em amarelo. As interse ̧c ̃oes C2 e B3
formam parte dos dois vales.

# Testing

This repository includes:

✅ A project description in Portuguese.
<br>
✅ A project solution in Python.
<br>
✅ Two sets of automatic tests (not developed by me).

You can run the automatic tests provided in this repository using the following commands:

```
pip install pytest
pytest tests.py
pytest extra_tests.py
```
