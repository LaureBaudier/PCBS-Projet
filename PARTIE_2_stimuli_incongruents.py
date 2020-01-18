
"""1.2. Stimuli Incongruents : Génération de paires d'ensembles de points dont le rapport numérosité/taille est Incongruent """

# Importation de pygame :
import pygame

# Importation du module random pour Générer des tailles de points aléatoires :
import random

# Définition des couleurs à utiliser :
black = (0,0,0)


'''1.2.a Définition d'une fonction most_size_side_incong(), qui détermine le côté qui comporte le plus de points : '''

def most_size_side_incong(compteur_gauche_incong, compteur_droit_incong):
	# Création de deux dictionnaires dans l'environnement global:
	global cote_gauche_incong
	global cote_droit_incong
	# Convertion de la valeur des variables en un nombre entier :
	cote_gauche_incong = int()
	cote_droit_incong = int()

# Création d'un rapport taille-numérosité incongruent (ratio = 2:3) :

	# Si nombre de points plus important à gauche -> taille supérieure des points à gauche et inversement :
	if compteur_gauche_incong > compteur_droit_incong:
		cote_gauche_incong = 10
		cote_droit_incong = 15
	# Si nombre de points plus important à droite -> taille supérieure des points à droite et inversement :
	else:
		cote_droit_incong = 10
		cote_gauche_incong = 15



'''1.2.b Définition d'une fonction display_dots_size_incong(), qui génère des ensembles de points à numérosité aléatoire puis définit la taille des points de manière incongruente : '''

def display_dots_size_incong(file_name_stim_incong):
	# Initialisation des modules pygame importés :
	pygame.init()
	# Définition de la taille de la surface d'affichage :
	screen = pygame.display.set_mode((1600,900))

	# Affichage en arrière-plan de la coccinelle :
	fond = pygame.image.load('coccinelle.png')
	screen.blit(fond, fond.get_rect())
	pygame.display.flip()

# Génération de deux ensembles de points à numérosité aléatoire :

	# Initialisation de deux variables qui génèrent un ensemble de points aléatoires, entre 5 et 15 points
	compteur_gauche_incong = random.randint(5, 15)
	compteur_droit_incong = random.randint(5,15)
	# Génération de deux variables qui contiennent un nombre entier :
	nombre_points_gauches_incong = int()
	nombre_points_droits_incong = int()

	# Appel de la fonction qui détermine quel côté comporte le plus de points :
	most_size_side_incong(compteur_gauche_incong, compteur_droit_incong)
	# Attribution de la taille des points à partir des deux fonctions globales définies en dehors de la fonction :
	rayon_gauche_incong = cote_gauche_incong
	rayon_droit_incong = cote_droit_incong

	# Création d'une liste qui comporte les coordonnées des points pour chaque coté :
	coordonees_points_gauches_incong = int()
	coordonees_points_droits_incong = int()



# Boucle qui ajoute des points de coordonnées aléatoires sur l'aile GAUCHE de la coccinelle, et définit leur taille :
	while nombre_points_gauches_incong < compteur_gauche_incong:
		# Les coordonnées du centre des points sont distribuées aléatoirement à la condition qu'elles soient contenues dans l'aile gauche.
		position_point_x_gauche_incong = random.randint(410, 740)
		position_point_y_gauche_incong = random.randint(180, 690)
		# Un point noir est dessiné sur l'aile gauche, jusqu'à ce que le nombre de points soit égal au nombre aléatoire généré dans le compteur (entre 5 et 15) :
		pygame.draw.circle(screen, black, (position_point_x_gauche_incong,position_point_y_gauche_incong), rayon_gauche_incong, 0)
		nombre_points_gauches_incong += 1


# Boucle qui ajoute des points de coordonnées aléatoires sur l'aile DROITE de la coccinelle, et définit leur taille :
	while nombre_points_droits_incong < compteur_droit_incong:
		#Les coordonnées du centre des points sont distribuées aléatoirement à la condition qu'elles soient contenues dans l'aile droite.
		position_point_x_droit_incong = random.randint(860, 1190)
		position_point_y_droit_incong = random.randint(180, 690)
		# Un point noir est dessiné sur l'aile droite, jusqu'à ce que le nombre de points soit égal au nombre aléatoire généré dans le compteur (entre 5 et 15) :
		pygame.draw.circle(screen, black, (position_point_x_droit_incong,position_point_y_droit_incong), rayon_droit_incong, 0)
		nombre_points_droits_incong += 1




# Sauvegarde des ensembles de points sur le disque, sous le nom de fichier défini en paramètre de la fonction :
	pygame.image.save(screen, file_name_stim_incong)
