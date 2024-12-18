def paraula_schema(paraula) -> dict:
    return {"paraula": paraula[0]}

def paraules_schema(paraules) -> dict:
    return [paraula_schema(paraula) for paraula in paraules]

def tematica_schema(tematica) -> dict:
    return {"opcio": tematica[0]}

def tematiques_schema(tematiques) -> dict:
    return [tematica_schema(tematica) for tematica in tematiques]

def lletra_schema(lletra) -> dict:
    return {"lletra": lletra[0]}

def lletres_schema(lletres) -> dict:
    return [lletra_schema(lletra) for lletra in lletres]

def text_comencar_schema(text_comencar) -> dict:
    return {"text_comencar": text_comencar[0]}

def imatge_intents_schema(nom_imatge) -> dict:
    return {"nom_imatge": nom_imatge[0]}

def partides_guanyades_schema(partides_guanyades) -> dict:
    return {"partides_guanyades": partides_guanyades}