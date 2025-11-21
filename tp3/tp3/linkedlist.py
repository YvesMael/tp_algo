# content of tp3/linkedlist.py
from __future__ import annotations
from dataclasses import dataclass
from collections.abc import Iterator
from typing import Any



@dataclass
class LinkedList:
    taille:int
    sentinelle:Cell
    
@dataclass(eq=False)
class Cell:
    item: int
    suivant: Cell|None
    precedant: Cell|None


def ll_new1(initial_l: list[int] | None = None) -> LinkedList:
    laSentinelle:Cell = Cell(-1, None, None)
    laSentinelle.precedant = laSentinelle
    laSentinelle.suivant = laSentinelle
    return LinkedList(0, laSentinelle)

def ll_new(initial_l: list[int] | None = None) -> LinkedList:
    initial_l = initial_l if initial_l is not None else []
    laSentinelle:Cell = Cell(-1, None, None)
    laSentinelle.precedant = laSentinelle
    laSentinelle.suivant = laSentinelle
    liste:LinkedList = LinkedList(0, laSentinelle)
    [ll_append(liste, el) for el in initial_l]
    return liste

def ll_is_empty(l: LinkedList) -> bool:
    return l.taille == 0

def ll_head(l: LinkedList) -> Cell:
    if l.taille > 0: return l.sentinelle.suivant
    else: raise IndexError


def ll_tail(l: LinkedList) -> Cell:
    if l.taille >0: return l.sentinelle.precedant
    else: raise IndexError

def ll_append(l: LinkedList, item: int) -> Cell:
    cellule:Cell = Cell(item, l.sentinelle, l.sentinelle)
    if ll_is_empty(l=l):
        l.sentinelle.suivant = cellule
        l.sentinelle.precedant = cellule
    else:
        cellule.precedant = l.sentinelle.precedant
        cellule.suivant = l.sentinelle
        l.sentinelle.precedant.suivant = cellule
        l.sentinelle.precedant = cellule
    l.taille +=1
    return cellule

def ll_iter(l: LinkedList, reverse: bool=False) -> Iterator[Cell]:
    if not ll_is_empty(l):                  # vérifie que la liste n'est pas vide
        if reverse:                             # parcourt la liste en sens inverse
            current: Cell = ll_tail(l)              # initialise la variable current à la tête de liste
            while current is not l.sentinelle:     # tant qu'il y a des maillons
                yield current
                current = current.precedant                   # "return" le maillon courant et gèle l'exécution
        else:
            current:Cell = ll_head(l)                                   # idem, dans le sens de la liste
            while current is not l.sentinelle:
                yield current
                current = current.suivant


def ll_len(l: LinkedList) -> int:
    return l.taille

def ll_str(l: LinkedList) -> str:
    liste:list[int] = []
    try:
        curent = ll_head(l)
        while curent is not l.sentinelle:
            liste+=[curent.item]
            curent = curent.suivant
        return str(liste)
    except IndexError:
        return "[]"

def ll_lookup(l: LinkedList, item: int) -> Cell:
    debut = ll_head(l)
    while debut is not l.sentinelle and debut.item!=item:
        debut = debut.suivant
    if debut.item == item:
        return debut
    return None


def ll_cell_at(l: LinkedList, i: int) -> Cell:
    if i <0 or i >= l.taille or l.taille==0: raise IndexError
    else: 
        cpt = 0
        curent = ll_head(l)
        while cpt!=i:
            curent = curent.suivant
            cpt +=1
        return curent

def ll_prepend(l: LinkedList, item: int) -> Cell:
    liste:Cell = Cell(item, l.sentinelle, l.sentinelle)
    if ll_is_empty(l):
        liste.suivant = l.sentinelle
        liste.precedant = l.sentinelle
        l.sentinelle.suivant = liste
        l.sentinelle.precedant = liste
    else:
        liste.suivant = l.sentinelle.suivant
        liste.precedant = l.sentinelle
        l.sentinelle.suivant.precedant = liste
    l.taille +=1
    return liste

def ll_insert(l: LinkedList, item: int, next_to: Cell) -> Cell:
    if not ll_is_empty(l):
        curent = ll_head(l)
        while curent is not l.sentinelle and curent is not next_to:
            curent = curent.suivant
        if curent is not l.sentinelle:
            cellule:Cell = Cell(item, l.sentinelle, l.sentinelle)
            cellule.suivant = curent.suivant
            cellule.precedant = curent
            curent.suivant = cellule
            cellule.suivant.precedant = cellule
            return cellule
    return None  

def ll_remove(l: LinkedList, cell: Cell) -> int:
    if not ll_is_empty(l): 
        curent = ll_head(l)
        while curent is not l.sentinelle and curent is not cell:
            curent = curent.suivant
        if curent is not l.sentinelle:
            suppression = curent
            curent.suivant.precedant = curent.precedant
            curent.precedant.suivant = curent.suivant
            return suppression.item


def ll_extend(l1: LinkedList, l2: LinkedList) -> None:
    if not ll_is_empty(l2):
        for el in ll_iter(l2):
            ll_append(l1, el.item)
    return None