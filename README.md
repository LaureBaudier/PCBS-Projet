
	I. Tâche de comparaison numérique non-symbolique

Source : 
Viarouge, A., Courtier, P., Hoppe, M., Melnik, J., Houdé, O., & Borst, G. (2018). Spontaneous orientation towards irrelevant dimensions of magnitude and numerical acuity. Learning and Instruction, 54, 156-163. http://dx.doi.org/10.1016/j.learninstruc.2017.09.004



Dans leur expérience, Viarouge et al.(2018) utilisent une tâche dite "de comparaison numérique" afin d'évaluer les capacités d'estimation des quantités numériques chez des enfants de 6 ans. Face à deux ensembles de points, les participants doivent décider sans les compter, quel ensemble comporte le plus de point. L'efficience du système d'estimation des grandeurs numériques augmente avec l'âge, et serait lié aux performances scolaires futures en mathématiques (source : Halberda et al., 2008).
Dans l'expérience originale, les nuages de points à comparer varient selon trois dimensions, ou "magnitudes": leur numérosité, leur taille ainsi que l'espacement entre les points. A des fins de simplification, la tâche présentement réalisée varie selon deux magnitudes uniquement :  la numérosité et la taille des points.
Un "score de comparaison numérique" peut être calculé à partir des réussites aux essais "congruents" et "incongruents". Dans les essais dits "incongruents", la taille des points vient perturber le jugement numérique, car l'ensemble qui comporte le plus grand nombre de points est également celui dont les points sont les plus petits.

L'objectif du présent projet est de répliquer la tâche utilisée par Viarouge et al., selon les paramètres décrits dans leur papier et selon la restriction à deux magnitudes explicitées ci-dessus. Les auteurs ont adapté la tâche à une jeune population : à des fins ludiques, les paires de points à comparer sont présentés sur les ailes d'une coccinelle. 









	II. Plan 

1) Préparation des stimuli (avec Pygame)


	1.1) Stimuli congruents : script "PARTIE 1 : Stimuli congruents.py"
	Objectif = Génération de paires d'ensembles de points dont le rapport numérosité/taille est Congruent : points plus gros du côté où il y en a le plus
	
	1.1.a) Définition d'une fonction most_size_side_cong(), qui détermine le côté qui comporte le plus de points 
	
	1.1.b) Définition d'une fonction display_dots_size_cong(), qui génère des ensembles de points à numérosité aléatoire puis définit la taille des points de manière congruente
	
	1.2) Stimuli incongruents : script "PARTIE 2 : Stimuli incongruents.py"
	Objectif = Génération de paires d'ensembles de points dont le rapport numérosité/taille est Incongruent : points plus petits du côté où il y en a le plus
	
	1.2.a) Définition d'une fonction most_size_side_incong(), qui détermine le côté qui comporte le plus de points
	
	1.2.b) Définition d'une fonction display_dots_size_incong(), qui génère des ensembles de points à numérosité aléatoire puis définit la taille des points de manière incongruente


2) L'expérience (avec Expyriment)

	2.1) Construction et exécution de la tâche expérimentale : script "PARTIE 3 : Opérationnalisation de la tâche expérimentale.py"
	
	2.1.a) Génération des ensembles de points au format .png, grâce aux fonctions display_dots_size_cong() et display_dots_size_incong()
	
	2.1.b) Opérationnalisation de la tâche avec Expyriment
	
	
	2.2) Commentaires et conclusion



3) Annexe
 Consignes -énoncées à l'oral- de l'expérience originale de Viarouge et al. (2018)




	III. Déroulé du programme

1) Préparation des stimuli (avec Pygame)

1.2) Stimuli congruents : script "PARTIE 1 : Stimuli congruents.py"
Objectif = Génération de paires d'ensembles de points dont le rapport numérosité/taille est Congruent : points plus gros du côté où il y en a le plus

1.1.a) Définition d'une fonction most_size_side_cong(), qui détermine le côté qui comporte le plus de points 

Les essais dits "congruents" sont mieux réussis à tous âges car l'estimation de la numérosité n'est pas perturbée par la taille des points. En effet, l'ensemble qui comporte le plus de points est également celui dont les points sont les plus gros, et inversement.

Une première fonction most_size_side_cong() est d'abord définie. Elle permet de comparer le nombre de deux ensembles de points, généré aléatoirement, sur les deux côtés de l'écran, afin de déterminer où se trouve l'ensemble le plus grand. Elle permettra d'attribuer un ratio de taille congruent avec la numérosité : les points qui composent le plus grand ensemble auront un rayon supérieur à ceux du plus petit ensemble. Le ratio de la taille des points est de 2:3, car c'est celui qui est facilement discriminable pour les enfants de 6 ans (Viarouge et al., 2018)

		

1.1.b) Définition d'une fonction display_dots_size_cong(), qui génère des ensembles de points à numérosité aléatoire puis définit la taille des points de manière congruente

Une seconde fonction display_dots_size_cong() est ensuite définie. C'est elle qui permet de générer aléatoirement un nombre de points attribué à gauche et à droite (de 5 à 15 points). Elle génère des coordonnées aléatoires du centre de chaque point dans un espace définit par la taille des ailles de la coccinelle qui se trouve en arrière plan, et applique le ratio de taille congruent, déterminé par la fonction most_size_side_cong() via la taille de leur rayon.
Elle permettra aussi de sauvegarder les stimuli sur le disque, sous le nom défini en paramètre de la fonction

		
.
		


1.2) Stimuli incongruents : script "PARTIE 2 : Stimuli incongruents.py"
Objectif = Génération de paires d'ensembles de points dont le rapport numérosité/taille est Incongruent : points plus petits du côté où il y en a le plus


Dans les essais dits "incongruents", la tâche est plus difficile, car cette fois le coté qui comporte le plus de points est celui dont les points sont les plus petits.

Un script identique à celui qui vient d'être décrit est définit, en inversant les fonctions de manière à ce que les ratios de numérosité et de taille soient incongruents.

Nous disposons désormais de scripts qui permettent de générer des ensembles de points dont le ratio numérique est randomisé, avec un ratio de taille de 2:3 contrebalancé de manière égale entre les essais congruents et incongruents.


2) L'expérience (avec Expyriment)

2.1) Construction et exécution de la tâche expérimentale : script "PARTIE 3 : Opérationnalisation de la tâche expérimentale.py"

2.1.a) Génération des ensembles de points au format .png, grâce aux fonctions display_dots_size_cong() et display_dots_size_incong()

Les analyses de l'expérience originale portent sur 3 blocs de 16 essais, soit 48 essais au total. Seul le script du premier bloc est présenté, les deuxième et troisième bloc étant construits de manière identique.
Une boucle génère puis enregistre (au format .png) successivement un essai congruent et un essai incongruent dans une liste, jusqu'à ce que le bloc comporte 8 essais de chaque sorte. L'ensemble des 16 essais est ensuite randomisé au sein de la liste.
		

2.1.b) Opérationnalisation de la tâche avec Expyriment

Les modules expyriment permettant d'opérationnaliser la tâche sont successivement appelés. La procédure de l'expérience est définie comme suit :

	1° Avant de commencer, un bref rappel des consignes (qui ont été explicitées à l'oral par l'expérimentateur) permet à l'enfant de se concentrer, et d'appuyer lui-même sur la barre d'espace pour commencer l'expérience
	
	- 
	
	2° Présentation du premier bloc de 16 essais. Modalités de réponse identiques à l'expérience originale : touche D(gauche) et touche K(droite). Chaque stimulus (un stimulus = deux ensembles de points à comparer sur les ailes de la coccinelle) est précédé d'une croix de fixation (500 ms) et s'affiche pendant 1200 ms. Ensuite, un écran noir est affiché jusqu'à ce qu'une réponse soit produite.
	
	

	3° Afin de permettre à l'enfant de rester concentré, un écran de pause s'affiche après la passation du premier bloc. L'enfant décide lui-même de continuer l'expérience en appuyant sur la barre d'espace
	
	
	
	
	4° Présentation du deuxième bloc de 16 essais (généré et opérationnalisé de manière identique au premier)
	
	5° Un second écran de pause s'affiche après la complétion du second bloc
	
	6° Présentation du troisième bloc de 16 essais
	
L'expérience se termine par un message qui félicite l'enfant (peu importe sa réussite) et le remercie. Afin de clore la passation, l'expérimentateur pressera la barre d'espace.


	


2.2) Commentaires et conclusion

Je tiens à préciser que je me suis appuyée sur le travail d'une précédente étudiante, sans lequel je n'aurais pas réussi à écrire ces scripts. 
Le lien de son projet : https://github.com/JudiKL/PCBS-NumerosityComparison/blob/master/README.md 
Bien qu'en comparaison, le mien soit relativement simple et pourtant loin d'être rigoureux, tout ceci m'a demandé énormément de travail. Je n'avais jamais écrit une seule ligne de code avant cette année.

Néanmoins, cet exercice m'a beaucoup appris parce qu'il m'a forcée à entreprendre un réel travail de compréhension.
Mon travail a d'abord consisté à déchiffrer le code rédigé par l'étudiante précitée, afin de pouvoir le simplifier (à mon niveau), réécrire certaines fonctions, en supprimer d'autres, parfois même, en paramétrer moi-même. J'ai notamment passé beaucoup de temps à régler la superposition des points sur les ailes de la coccinelle, que j'ai essayé de dessiner les plus larges possibles sur l'espace de travail dont je disposais.
J'ai beaucoup travaillé sur la rédaction et la clarté des #commentaires, qui m'ont aussi permis de guider mon travail.
J'ai aussi perdu beaucoup de temps à essayer de produire un travail dont je ne suis tout simplement pas capable ; notamment, j'ai longuement essayé d'empêcher la superposition des points noirs entre eux et de comprendre pourquoi l'exécution de mon script était si long, en vain.
J'ai conscience que ma production est globalement médiocre, mais je suis satisfaite de la quantité de travail que j'ai fourni. 



3) Annexe
Consignes -énoncées à l'oral- de l'expérience originale
Je ne suis donc pas la première étudiante à avoir cherché à reproduire cette tâche de l'expérience de Viarouge et al. (2018). Je partage en annexe les consignes originales (énoncées à l'oral) associées à la tâche. Je les ai en ma possession parce qu'Arnaud Viarouge a encadré mon projet étudiant de L3 lors duquel nous avons pu reconduire cette tâche ensemble avec de jeunes enfants. Peut-être que cela servira un jour à quelqu'un d'autre 


« Tu vas voir apparaître une coccinelle à l’écran. Il va y avoir des points de ce côté sur l’aile gauche de la coccinelle, et des points de ce côté sur l’aile droite de la coccinelle » (indiquer le côté de l’écran correspondant en pointant du doigt)
« Il faut que tu décides si tu penses qu’il y a un plus grand nombre de points à gauche ou un plus grand nombre de points à droite. Si tu penses qu’il y a un plus grand nombre de points de ce côté (montrer l’aile gauche), tu appuies là (montrer le bouton D), si tu penses qu’il y a un plus grand nombre de points de ce côté (montrer l’aile droite), tu appuies là (montrer le bouton K) ».
« Tu n’auras pas le temps de compter tous les points. Tu vas juste bien les regarder pour voir de quel côté il y a le plus grand nombre de points »
« Tu as compris ? Tu es prêt.e ? On va d’abord s'entraîner un peu. »
Pendant les 4 essais d’entrainement, l’enfant a un feedback (coccinelle contente ou triste). En cas de réponse fausse sur essais incongruents, préciser « Attention c’est le nombre qui compte, de quel côté tu en vois le plus ? » « Je vois que tu as bien compris. Reste concentré.e. C’est parti ! »













