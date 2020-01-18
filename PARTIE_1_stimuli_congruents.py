"""1.1 Stimuli Congruents : Génération de paires d'ensembles de points dont le rapport numérosité/taille est Congruent """

# Importation de pygame :
import pygame

# Importation du module random pour Générer des tailles de points aléatoires :
import random

# Définition des couleurs à utiliser :
black = (0,0,0)


'''1.1.a Définition d'une fonction most_size_side_cong(), qui détermine le côté qui comporte le plus de points : '''

def most_size_side_cong(compteur_gauche_cong, compteur_droit_cong):
	# Création de deux dictionnaires dans l'environnement global:
	global cote_gauche_cong
	global cote_droit_cong
	# Convertion de la valeur des variables en un nombre entier :
	cote_gauche_cong = int()
	cote_droit_cong = int()

# Création d'un rapport taille-numérosité congruent (ratio = 2:3) :

	# Si nombre de points plus important à gauche -> taille supérieure des points à gauche et inversement :
	if compteur_gauche_cong > compteur_droit_cong:
		cote_droit_cong = 10
		cote_gauche_cong = 15
	# Si nombre de points plus important à droite -> taille supérieure des points à droite et inversement :
	else:
		cote_gauche_cong = 10
		cote_droit_cong = 15



'''1.1.b Définition d'une fonction display_dots_size_cong(), qui génère des ensembles de points à numérosité aléatoire puis définit la taille des points de manière congruente : '''

def display_dots_size_cong(file_name_stim_cong):
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
	compteur_gauche_cong = random.randint(5, 15)
	compteur_droit_cong = random.randint(5,15)
	# Génération de deux variables qui contiennent un nombre entier :
	nombre_points_gauches_cong = int()
	nombre_points_droits_cong = int()

	# Appel de la fonction qui détermine quel côté comporte le plus de points :
	most_size_side_cong(compteur_gauche_cong, compteur_droit_cong)
	# Attribution de la taille des points à partir des deux fonctions globales définies en dehors de la fonction :
	rayon_gauche_cong = cote_gauche_cong
	rayon_droit_cong = cote_droit_cong

	# Création d'une liste qui comporte les coordonnées des points pour chaque coté :
	coordonees_points_gauches_cong = int()
	coordonees_points_droits_cong = int()

def check_superposition(couple,liste_couple,radius):
	"""Vérifie si le point couple n'entre dans le rayon minimum d'aucun point de la liste_couple"""
	overlap = False
	compteur = 0
	while not overlap and compteur<len(liste_couple):
		new_couple = liste_couple[compteur] #Prend en compte le couple de coordonées suivant
		overlap = distance_points(couple, new_couple) < radius
		compteur += 1
	return overlap

# Boucle qui ajoute des points de coordonnées aléatoires sur l'aile GAUCHE de la coccinelle, et définit leur taille :
	while nombre_points_gauches_cong < compteur_gauche_cong:
		# Les coordonnées du centre des points sont distribuées aléatoirement à la condition qu'elles soient contenues dans l'aile gauche.
		position_point_x_gauche_cong = random.randint(410, 740)
		position_point_y_gauche_cong = random.randint(180, 690)
		while check_superposition((position_point_x_gauche_cong,position_point_y_gauche_cong), coordonees_points_gauches_cong, rayon_gauche_cong):
			position_point_x_gauche_cong = random.randint(410, 740)
			position_point_y_gauche_cong = random.randint(180, 690)
		# Un point noir est dessiné sur l'aile gauche, jusqu'à ce que le nombre de points soit égal au nombre aléatoire généré dans le compteur (entre 5 et 15) :
		pygame.draw.circle(screen, black, (position_point_x_gauche_cong,position_point_y_gauche_cong), rayon_gauche_cong, 0)
		nombre_points_gauches_cong += 1




# Boucle qui ajoute des points de coordonnées aléatoires sur l'aile DROITE de la coccinelle, et définit leur taille :
	while nombre_points_droits_cong < compteur_droit_cong:
		#Les coordonnées du centre des points sont distribuées aléatoirement à la condition qu'elles soient contenues dans l'aile droite.
		position_point_x_droit_cong = random.randint(860, 1190)
		position_point_y_droit_cong = random.randint(180, 690)
		# Un point noir est dessiné sur l'aile droite, jusqu'à ce que le nombre de points soit égal au nombre aléatoire généré dans le compteur (entre 5 et 15) :
		pygame.draw.circle(screen, black, (position_point_x_droit_cong,position_point_y_droit_cong), rayon_droit_cong, 0)
		nombre_points_droits_cong += 1

# Sauvegarde des ensembles de points sur le disque, sous le nom de fichier défini en paramètre de la fonction :
	pygame.image.save(screen, file_name_stim_cong)
