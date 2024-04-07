def calcular_promedio(lista):
    """ summary
    Calcula el promedio de una lista de números.

    Args:
        lista (list of int or float): Una lista de números enteros o flotantes.

    Returns:
        float: El promedio de los números en la lista.

    Examples:
        >>> calcular_promedio([1, 2, 3, 4, 5])
        3.0
        >>> calcular_promedio([10, 20, 30, 40, 50])
        30.0
        >>> calcular_promedio([2.5, 3.5, 4.5, 5.5, 6.5])
        4.5
        >>> calcular_promedio([0])
        0.0
    """
    if not lista:
        return 0.0
    return sum(lista) / len(lista)
