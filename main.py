#### Fonctions secondaires$ pylint main.py
"""
Module pour tracer et calculer la suite de Syracuse.

Ce module contient les fonctions nécessaires pour générer la suite de Syracuse.
Il inclut également une fonction pour tracer la suite de Syracuse en utilisant Plotly.
"""

# imports
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###$ pylint main.py
def syr_plot(lsyr):
    """Trace la suite de Syracuse.

    Args:
        lsyr (list): La suite de Syracuse.
    """
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )

    x = [i for i in range(len(lsyr))]
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')
    return None
#######################

def syracuse_l(n):
    """retourne la suite de Syracuse de source n

    Args:
        n (int): la source de la suite

    Returns:
        list: la suite de Syracuse de source n
    """
    l = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        l.append(n)
    return l

def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol
    """
    return len(l) - 1

def temps_de_vol_en_altitude(l):
    """Retourne le temps de vol en altitude d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol en altitude
    """
    n_initial = l[0]
    altitude = [x for x in l if x > n_initial]
    return len(altitude)

    # votre code ici

def altitude_maximale(l):
    """retourne l'altitude maximale d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: l'altitude maximale
    """
    if isinstance(l, list):
        return max(l)
    else:
        raise TypeError
    # votre code ici


#### Fonction principale


def main():
    """Fonction principale pour exécuter les calculs et le tracé de la suite de Syracuse."""
    n1 = 15
    lsyr1 = syracuse_l(n1)
    print(f"Suite de Syracuse pour n = {n1} : {lsyr1}")
    syr_plot(lsyr1)
    print(f"Temps de vol pour n = {n1} : {temps_de_vol(lsyr1)}")
    print(f"Temps de vol en altitude pour n = {n1} : {temps_de_vol_en_altitude(lsyr1)}")
    print(f"Altitude maximale pour n = {n1} : {altitude_maximale(lsyr1)}")
    lsyr = syracuse_l(15)
    syr_plot(lsyr)
    print(temps_de_vol(lsyr))
    print(temps_de_vol_en_altitude(lsyr))
    print(altitude_maximale(lsyr))


if __name__ == "__main__":
    main()
