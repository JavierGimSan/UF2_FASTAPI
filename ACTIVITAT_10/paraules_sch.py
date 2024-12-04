def paraula_schema(paraula) -> dict:
    return {""}

def tematica_schema(tematica) -> dict:
    return {"opcio": tematica[0]}

def tematiques_schema(tematiques) -> dict:
    return [tematica_schema(tematica) for tematica in tematiques]