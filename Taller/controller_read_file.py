def read_file():
    f = open("log_trabajoya_prod_prueba.txt", "r")
    lines = f.read().split('\n')
    lista = []
    for i in lines:
        x = extract_data(i)
        if x != None:
            lista.append(x)
    return lista


def extract_data(data):
    try:
        i = 0;
        fecha, tipo, archivo, line = "","","",""
        for info in data.split("] "):
            info = info.replace("{", '').replace('"', '').replace('[', '').replace(']', '').replace("log:", '')
            if i == 0:
                fecha = info
                i += 1
            elif i == 1:
                tipo, archivo = info.split(' ')[0], info.split(' ')[1].split(':')[0]
                line = int(info.split(' ')[1].split(':')[1])
                return fecha, tipo, archivo, line
    except:
        return None