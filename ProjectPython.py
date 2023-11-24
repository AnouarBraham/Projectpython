from tkinter import *
import random

vit_x = 10

vit_y = 0

vit_x2 = -10

vit_y2 = 0

animation_active = False

stop_animation = False


# Fonctions


def modification():
    global vit_x
    global vit_y
    global animation_active
    global stop_animation

    animation_active = True
    mod_angle = 0

    liste_coord = monCanvas.coords(pacman_1)

    # Gestion du mouvement du pacman en fonction de sa position sur le canvas
    if liste_coord[2] > 500:
        vit_x = -10
    elif liste_coord[0] < 0:
        vit_x = 10
    elif liste_coord[1] < 0:
        vit_y = 10
    elif liste_coord[3] > 600:
        vit_y = -10

    # Modification de l'angle de départ du pacman en fonction de sa direction
    if (vit_x < 0 or vit_y > 0):
        mod_angle = 180

    if vit_y == 0:
        if (monCanvas.itemcget(pacman_1, 'start') == '15.0' or monCanvas.itemcget(pacman_1, 'start') == '195.0'):
            monCanvas.itemconfig(pacman_1, start=30 + mod_angle, extent=300)
        else:
            monCanvas.itemconfig(pacman_1, start=15 + mod_angle, extent=330)

    if vit_x == 0:
        if (monCanvas.itemcget(pacman_1, 'start') == '105.0' or monCanvas.itemcget(pacman_1, 'start') == '285.0'):
            monCanvas.itemconfig(pacman_1, start=120 + mod_angle, extent=300)
        else:
            monCanvas.itemconfig(pacman_1, start=105 + mod_angle, extent=330)

    # Déplacement du pacman sur le canvas
    monCanvas.move(pacman_1, vit_x, vit_y)

    # Appel d'une autre fonction modification2()
    modification2()

    # Programmation d'une boucle récursive pour animer le mouvement du pacman
    if stop_animation is False:
        racine.after(50, modification)
    else:
        stop_animation = False
        animation_active = False


def init_couleurs():

    but_avance.config(bg="black")

    but_recule.config(bg="black")

    but_monte.config(bg="black")

    but_descend.config(bg="black")

    but_init.config(bg="red")

    but_arret.config(bg="red")


def avance_x():
    init_couleurs()

    but_avance.config(bg="blue")
    but_avance.config()

    global vit_x

    global vit_y

    global stop_animation

    stop_animation = False

    vit_x = 10

    vit_y = 0

    if animation_active == False :

        modification()


def recule_x():

    init_couleurs()

    but_recule.config(bg="blue")

    global vit_x

    global vit_y

    global stop_animation

    stop_animation = False

    vit_x = -10

    vit_y = 0

    if animation_active == False :

        modification()


def monte_y():

    init_couleurs()

    but_monte.config(bg="blue")

    global vit_x

    global vit_y

    global stop_animation

    stop_animation = False

    vit_x = 0

    vit_y = -10

    if animation_active == False :

        modification()


def descend_y():

    init_couleurs()

    but_descend.config(bg="blue")

    global vit_x

    global vit_y

    global stop_animation

    stop_animation = False

    vit_x = 0

    vit_y = 10

    if animation_active == False :

        modification()


def point_depart():

    init_couleurs()

    but_init.config(bg="blue")

    global vit_x

    global vit_y

    vit_x = 10

    vit_y = 10

    arret()

    monCanvas.coords(pacman_1, 80, 80, 150, 150)

    monCanvas.itemconfig(pacman_1, start=25,extent=330)



def arret():

    init_couleurs()

    but_arret.config(bg="purple")

    global stop_animation

    stop_animation = True


def modification2():

    global vit_x2

    global vit_y2

    if animation_active == True :

        direction = random.randint(1,100)

        if direction > 80 :

            if direction > 95 :

                vit_x2 = 10

                vit_y2 = 0

            elif direction > 90 :

                vit_x2 = -10

                vit_y2 = 0

            elif direction > 85 :

                vit_x2 = 0

                vit_y2 = 10

            else:

                vit_x2 = 0

                vit_y2 = -10

        mod_angle = 0





#Programme


racine = Tk()


racine.title("Pacmac Animation")

racine.geometry("600x600")


monCanvas = Canvas(racine, width=500, height=600, bg='black', bd=0, highlightthickness=0)

monCanvas.grid(row=0, column=0, padx=10, pady=10)

pacman_1 = monCanvas.create_arc(80, 80, 150, 150, fill="yellow", start=15, extent=330,outline="yellow")


zone2 = Frame(racine, bg='#777777')

zone2.place(x=520,y=200)

def right(event):
    avance_x()

def left(event):
    recule_x()

def descend(event):
    descend_y()

def monte(event):
    monte_y()


but_avance = Button(zone2, text="Droite", fg="white", bg="black", command=avance_x)

but_recule = Button(zone2, text="Gauche", fg="white", bg="black", command=recule_x)

but_monte = Button(zone2, text="Monte", fg="white", bg="black", command=monte_y)

but_descend = Button(zone2, text="Descend", fg="white", bg="black", command=descend_y)

but_arret = Button(zone2, text="STOP", fg="white", bg="red", command=arret)

but_init = Button(zone2, text="INIT", fg="white", bg="red", command=point_depart)

but_avance.pack(fill=X)

but_recule.pack(fill=X)

but_monte.pack(fill=X)

but_descend.pack(fill=X)

but_arret.pack(fill=X)

but_init.pack(fill=X)

racine.bind("<Right>", right)
racine.bind("<Left>", left)
racine.bind("<Down>", descend)
racine.bind("<Up>", monte)


racine.mainloop()
