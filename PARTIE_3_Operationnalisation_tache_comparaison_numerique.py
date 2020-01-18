'''2.1) Construction et exécution de la tâche expérimentale '''
# Rappel : avant le début de l'expérience, la consigne est explicitée à l'oral par l'expérimentateur (voir "CONSIGNES" dans README.md)


# importation des packages, modules et scripts nécessaires à la génération et l'enregistrement des stimuli :

import pygame
import PARTIE_1_stimuli_congruents
import PARTIE_2_stimuli_incongruents
import random
import expyriment

from  expyriment.stimuli import FixCross # pour implémenter une croix de fixation entre les essais
from  expyriment.stimuli import BlankScreen # pour implémenter un écran blanc
from  expyriment.stimuli import Picture # pour implémenter un stimulus image

from expyriment import control


''' 2.1.a Génération des ensembles de points au format .png, grâce aux fonctions display_dots_size_cong() et display_dots_size_incong() :'''
# Création de trois blocs de 16 stimuli (16 paires d'ensembles de points), soit 48 au total. les fichiers images (png) sont enregistrés au fur et à mesure


# Bloc 1 :

# Enregistrement des fichiers images (png) au format .png, à mesure qu'ils sont générés :
list_stim_bloc_1 = []
if __name__ == "__main__": #  permet de définir les conditions d'exécution du script ci-dessous
	n = 1
	while n<=16:
	    # les noms de fichier générés sont numérotés de 1 à 16, suivant l'ordre dans lequel ils sont créés
		PARTIE_1_stimuli_congruents.display_dots_size_cong("stimulus_cong%d.png"%(n)) # Pour les paires de stimuli congruents
		list_stim_bloc_1.append("stimulus_cong%d.png"%(n)) # Ajout du fichier à la liste des stimuli du bloc1
		PARTIE_2_stimuli_incongruents.display_dots_size_incong("stimulus_incong%d.png"%(n)) # Pour les paires de stimuli incongruents
		list_stim_bloc_1.append("stimulus_incong%d.png"%(n)) # Ajout du fichier à la liste des stimuli du bloc1
		n += 1

# Randomisation des éléments de la liste afin de pouvoir les présenter de manière aléatoire :
random.shuffle(list_stim_bloc_1)




# Bloc 2 :

# Enregistrement des fichiers images (png) au format .png, à mesure qu'ils sont générés :
list_stim_bloc_2 = []
if __name__ == "__main__":
	n = 1
	while n<=16:
	    # les noms de fichier générés sont numérotés de 1 à 16, suivant l'ordre dans lequel ils sont créés
		PARTIE_1_stimuli_congruents.display_dots_size_cong("stimulus_cong%d.png"%(n)) # Pour les paires de stimuli congruents
		list_stim_bloc_2.append("stimulus_cong%d.png"%(n))
		PARTIE_2_stimuli_incongruents.display_dots_size_incong("stimulus_incong%d.png"%(n)) # Pour les paires de stimuli incongruents
		list_stim_bloc_2.append("stimulus_incong%d.png"%(n))
		n += 1

# Randomisation des éléments de la liste afin de pouvoir les présenter de manière aléatoire :
random.shuffle(list_stim_bloc_2)





# Bloc 3 :

# Enregistrement des fichiers images (png) au format .png, à mesure qu'ils sont générés :
list_stim_bloc_3 = []
if __name__ == "__main__":
	n = 1
	while n<=16:
	    # les noms de fichier générés sont numérotés de 1 à 16, suivant l'ordre dans lequel ils sont créés
		PARTIE_1_stimuli_congruents.display_dots_size_cong("stimulus_cong%d.png"%(n)) # Pour les paires de stimuli congruents
		list_stim_bloc_3.append("stimulus_cong%d.png"%(n))
		PARTIE_2_stimuli_incongruents.display_dots_size_incong("stimulus_incong%d.png"%(n)) # Pour les paires de stimuli incongruents
		list_stim_bloc_3.append("stimulus_incong%d.png"%(n))
		n += 1

# Randomisation des éléments de la liste afin de pouvoir les présenter de manière aléatoire :
random.shuffle(list_stim_bloc_3)



'''2.1.b Opérationnalisation de la tâche avec Expyriment '''

# Création d'un objet Experiment :
exp = expyriment.design.Experiment(name="Tâche de comparaison numérique non-symbolique")

# Initialisation de l'expérience comme étant active (develop_mode = false) :
expyriment.control.initialize(exp)

# Exécution de l'expérience :
expyriment.control.start()



# 1° Rappel de la consigne :
# Création d'un stimulus "rappel des consignes". N.B.: Celles-ci sont rapidement rappelées aux enfants mais elles ont été explicitées plus en détails à l'oral.
rappel_consignes = expyriment.stimuli.TextLine(text= "Si tu vois plus de points à gauche, appuie sur D. Si tu vois plus de points à droite, appuie sur K. Appuie sur la barre d'espace pour commencer", text_size=24, text_colour = (240, 195, 0))

# Affichage de la consigne à l'écran
rappel_consignes.present()
key, rt = exp.keyboard.wait([expyriment.misc.constants.K_SPACE]) # Permet de commencer en appuyant sur la barre espace




# 2° Présentation du Bloc 1 :
for stim_bloc_1 in list_stim_bloc_1:

	# Affichage d'une croix de fixation (durée : 500 ms) avant la présentation du stimulus suivant :
	fixcross = expyriment.stimuli.FixCross()
	fixcross.preload()
	fixcross.present()
	exp.clock.wait(500)
    # Présentation du stimulus (durée : 1200 ms) :
	stim = expyriment.stimuli.Picture(stim_bloc_1)
	stim.present()
	exp.clock.wait(1200)
	# Affichage d'un interstimulus écran noir afin que le sujet puisse répondre (durée illimitée) :
	inter_stimulus = expyriment.stimuli.BlankScreen()
	inter_stimulus.present()

	key, rt = exp.keyboard.wait([expyriment.misc.constants.K_d,expyriment.misc.constants.K_k]) # Permet de répondre avec les touches D (aile gauche) et K (aile droite)


# 3° Pause entre les blocs 1 et 2.
message_pause1 = expyriment.stimuli.TextLine(text="Bien joué ! Tu peux te reposer quelques instants. Reste bien concentré. Appuies sur la barre d'espace quand tu es prêt",
text_size=24, text_colour = (240, 195, 0))
message_pause1.present() # Présentation du message à l'écran
key, rt = exp.keyboard.wait([expyriment.misc.constants.K_SPACE]) # Permet de reprendre en appuyant sur la barre espace

# 4° Présentation du Bloc 2 :
for stim_bloc_2 in list_stim_bloc_2:

	# Affichage d'une croix de fixation (durée : 500 ms) avant la présentation du stimulus suivant :
	fixcross = expyriment.stimuli.FixCross()
	fixcross.preload()
	fixcross.present()
	exp.clock.wait(500)
    # Présentation du stimulus (durée : 1200 ms) :
	stim = expyriment.stimuli.Picture(stim_bloc_2)
	stim.present()
	exp.clock.wait(1200)
	# Affichage d'un interstimulus écran noir afin que le sujet puisse répondre (durée illimitée) :
	inter_stimulus = expyriment.stimuli.BlankScreen()
	inter_stimulus.present()

	key, rt = exp.keyboard.wait([expyriment.misc.constants.K_d,expyriment.misc.constants.K_k]) # Permet de répondre avec les touches D (aile gauche) et K (aile droite)


# 5° Pause entre les blocs 2 et 3 :
message_pause2 = expyriment.stimuli.TextLine(text="Bravo ! Tu peux à nouveau te reposer quelques instants si tu le souhaites. Appuies sur la barre d'espace quand tu es prêt",
text_size=24, text_colour = (240, 195, 0))
message_pause2.present() # Présentation du message à l'écran
key, rt = exp.keyboard.wait([expyriment.misc.constants.K_SPACE]) # Permet de reprendre en appuyant sur la barre espace



# 6° Présentation du Bloc 3 :
for stim_bloc_3 in list_stim_bloc_3:

	# Affichage d'une croix de fixation (durée : 500 ms) avant la présentation du stimulus suivant :
	fixcross = expyriment.stimuli.FixCross()
	fixcross.preload()
	fixcross.present()
	exp.clock.wait(500)
    # Présentation du stimulus (durée : 1200 ms) :
	stim = expyriment.stimuli.Picture(stim_bloc_3)
	stim.present()
	exp.clock.wait(1200)
	# Affichage d'un interstimulus écran noir afin que le sujet puisse répondre (durée illimitée) :
	inter_stimulus = expyriment.stimuli.BlankScreen()
	inter_stimulus.present()

	key, rt = exp.keyboard.wait([expyriment.misc.constants.K_d,expyriment.misc.constants.K_k]) # Permet de répondre avec les touches D (aile gauche) et K (aile droite)



# Message de fin :
message_fin = expyriment.stimuli.TextLine(text="Félicitations ! Le jeu est terminé. Merci pour ta participation !", text_size=24, text_colour = (240, 195, 0))
message_fin.present() # Présentation du message à l'écran
key, rt = exp.keyboard.wait([expyriment.misc.constants.K_SPACE]) # Permet à l'expérimentateur de terminer l'expérience en appuyant sur la barre espace



# Fin de l'expérience
expyriment.control.end()
