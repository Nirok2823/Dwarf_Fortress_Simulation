# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 15:26:24 2024

@author: Dell
"""

import random

def generate_story(amistad, per1, per2):
    """
    Genera una narrativa aleatoria basada en el tipo de amistad entre dos personajes.

    Args:
        amistad (str): Tipo de amistad (amorosa, de conveniencia, de oficio, cercana, casual).
        per1 (obj): Primer personaje.
        per2 (obj): Segundo personaje.

    Returns:
        str: Una historia generada sobre la amistad.
    """
    historias = {
        "amorosa": [
            f"{per1.nombre} y {per2.nombre} encontraron el amor cuando menos lo esperaban, cruzando miradas en un festival bajo la luna llena.",
            f"En un tranquilo atardecer, {per1.nombre} y {per2.nombre} comenzaron una conversación que pronto se transformó en un amor eterno.",
            f"A pesar de venir de mundos diferentes, {per1.nombre} y {per2.nombre} descubrieron que el amor no tiene fronteras."
        ],
        "de conveniencia": [
            f"Con un apretón de manos, {per1.nombre} y {per2.nombre} sellaron un acuerdo para protegerse mutuamente en tiempos peligrosos.",
            f"La alianza entre {per1.nombre} y {per2.nombre} comenzó por pura necesidad, pero terminó siendo una unión difícil de romper.",
            f"{per1.nombre} necesitaba recursos, y {per2.nombre} buscaba conocimientos. Juntos, encontraron la manera de ayudarse mutuamente."
        ],
        "de oficio": [
            f"En el bullicioso taller, {per1.nombre} y {per2.nombre} descubrieron que compartían la misma pasión por su trabajo.",
            f"Durante largas horas trabajando juntos, {per1.nombre} y {per2.nombre} forjaron una amistad basada en respeto mutuo.",
            f"{per1.nombre} y {per2.nombre} se dieron cuenta de que su habilidad compartida para el {random.choice(['herrero', 'arte de la alquimia', 'comercio'])} los hacía inseparables."
        ],
        "cercana": [
            f"Un acto de valentía de {per2.nombre} salvó a {per1.nombre} de un peligro inminente, consolidando una amistad cercana.",
            f"Tras un evento inesperado, {per1.nombre} y {per2.nombre} encontraron consuelo el uno en el otro.",
            f"Una noche de confesiones y risas hizo que {per1.nombre} y {per2.nombre} se convirtieran en amigos inseparables."
        ],
        "casual": [
            f"{per1.nombre} y {per2.nombre} se conocieron en una taberna y compartieron unas pocas palabras antes de seguir sus caminos.",
            f"Un encuentro breve entre {per1.nombre} y {per2.nombre} dejó una impresión pasajera pero agradable.",
            f"En una plaza concurrida, {per1.nombre} y {per2.nombre} intercambiaron un saludo antes de continuar sus respectivas aventuras."
        ]
    }
    
    # Selecciona una narrativa aleatoria para el tipo de amistad
    historia = random.choice(historias.get(amistad, ["No se pudo generar una historia para este tipo de amistad."]))
    
    # Imprime la historia generada
    return historia