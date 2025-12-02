"""
Registry centralizado para generadores de figuras.

Este módulo re-exporta las funciones del registry para facilitar
el acceso desde main.py sin imports circulares.
"""

from . import (
    generate,
    generate_all,
    list_figures,
    register,
)

__all__ = [
    "generate",
    "generate_all",
    "list_figures",
    "register",
]

