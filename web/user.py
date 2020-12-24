from web import client as cl


def tous_pays():
    return cl.client_function("tous")


def un_pays(nom_pays):
    return cl.client_function("pays " + nom_pays)

