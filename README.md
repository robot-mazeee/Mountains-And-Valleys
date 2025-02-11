# Mountains and Valleys - Description

## Territory

A territory is a rectangular NxM shape formed by N vertical paths (identified by letters from A to Z) and M horizontal paths (identified by numbers from 1 to 99).

## Intersection

A point in a territory where a vertical path and a horizontal path cross is called an intersection. Each intersection is identified by the identifiers of the paths that form it. Two intersections are adjacent if they are connected by a vertical or horizontal path with no other intersections between them. Intersections can be free or occupied by mountains.

## Mountain Chains and Valleys

Two occupied or free intersections are connected if it is possible to draw a path between them, containing only occupied or free intersections, respectively. A chain of mountains is a set of connected occupied intersections that are not connected to any other mountain. Similarly, a chain of free intersections adjacent to a mountain or a chain of mountains is called a valley.

## Examples

<img width="477" alt="image" src="https://github.com/user-attachments/assets/f2b85a7f-32f9-4978-a87f-309c5de3dab2" />

Example a) provides a territory with 7 vertical paths and 4 horizontal paths, with mountains in the intersections A2, C3 and D1.

In example b) we have a territory with two mountain chains: 1) (A1, A2, B2, A3); 2) (C3).

In example c) the valley correspondent to mountain chain 1 is denoted by green dots, and the valley correspondent to mountain chain 2 is denoted by yellow dots.

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
