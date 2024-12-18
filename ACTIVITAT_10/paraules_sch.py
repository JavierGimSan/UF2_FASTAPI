def paraula_schema(paraula) -> dict:
    return {"paraula": paraula[0]}

def paraules_schema(paraules) -> dict:
    return [paraula_schema(paraula) for paraula in paraules]

def tematica_schema(tematica) -> dict:
    return {"opcio": tematica[0]}

def tematiques_schema(tematiques) -> dict:
    return [tematica_schema(tematica) for tematica in tematiques]