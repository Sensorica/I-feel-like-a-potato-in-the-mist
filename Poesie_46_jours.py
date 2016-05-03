#!/opt/local/bin/python2.4

 #!/usr/bin/python
          # -*- coding: latin-1 -*-
import os, sys
import serial
import time
from datetime import datetime

lorem = """ 
Je me ravage comme une seule colonne liberatrice Comme le son
sourire de haut Crachant sa tendre poitrine Avec effraction 
Dans cette journee au plus Tendant les autres Et je trouvais
et la tunique de fer Comme si l'eclair insoupconnable de 
naitre Mon coeur au cou Son bras Qu'est-ce qu'on a renouvele
Sainte Vierge? Mes propres paroles en plein de votre aventure
Pour la meme de mon dernier deux colombes devant toi pareille
a s'arreter. Nous tous ceux qui pleure sur la chambre en vain
la tendresse qui nous n'avons jamais ete cette grande eternite
Si pres de femme au milieu Comme la terre Remontait d'un flot
trop attendu Les musiques de sa tendre cristal Vos revoltes,
Ces signes de leur parler Son epanouissement au fond de mots
fatidiques et le soir, Ou peut-etre une grande ombre Mes 
amours se levait pour notre coeur Pour monture la prodigieuse
vitesse foudroyante et fleurissait Notre delice nous eut fallu
Aligner nos yeux pleins de deux portes des graces de ta 
naissance Je marche a coup surgit alentour de lourds aux 
signes identiques Parmi ce dur Que l'on a tout est Comme des
fruits murs d'une egale fraternite Leurs violons les fissures
du tronc C'est pour une plus douce Chemins perdus Qu'est-ce 
que le midi Elle est invisible terre La sourde confession Des
astres n'est pas assez reculee Car elle Songe fuyant ma 
bouche vermeille Au dela du matin dechire o vous ai connus 
Quand est-ce que le retiendrez Est-ce moi Pour aimer Pour un 
depart de rubis Iles frontees de l'enchantement Qui fouette 
la succession des espaces de ta robe sur les musiques de sa 
presence interieure refermee a Varsovie De vos doigts tiedes 
Liberant mon ame delivree On en ses fautes Sans le vent, Vos 
voiles de fleurs sur la voute Les lois impenetrables Paupieres
de chaque jour ou l`heure ma vie! Tu l'as lu dans des reves 
venu Pourquoi pleurer sous tant de mon chemin trop vibrante 
Qui ne sait pas perdu dont nous sommes sans en s'approchant, 
Vient effacer la chambre Le paysage horizontal. Est-ce l'heure
De Strasbourg a tout a demain Ont tout remplis d'ombre sauvage
Et ces routes indefinissables sous ta montagne Elle jouait 
dans l'eau mal malgre cette journee qui roucoule Au coeur 
Aux sangs de morte la terre respirante qui pleuriez les 
grandes clameurs Des cuves entenebres Nul ange ne m'aimait 
pas eu le dernier cri emplissant ma main au maitre pour une 
etoile fatale et des ombres Nous t'avons tuee avec le plus 
belles jeunes seins branlants des paleurs de la terre 
Remontait d'un jeune frere disparu qui il est peut-etre le 
crepuscule Quand il est la Alors il faut aimer! Amour! ah! 
quel voyage nous avons entendu Chaque mot une eau qui se 
poursuivant, L'heure, passant Tout cela dure Pour aimer 
Que je sais vos yeux droits du jour et sans repit, Ivre de 
l'instant o roi des mille reflets Comme un cable de joie 
D'une mer La plainte des villes illimitees Fiancee tes 
doigts Tremblants de paons Avec la nuit. Ainsi qu'une part 
en nous Efface le feuillage est hier fixe Dont notre mort 
etait ouverte en plein soleil Mais on n'y a la maison bien 
ouverte, Bonne pour qu'il y en pointe de l'octave Pourtant 
ses paupieres en reposoir avec ses pas eu la femme et le 
croirait Qui flotte a s'arreter. Nous refouler au glissement
de frisson passager dans l'espace Et vos chevelures longues 
tenebres voraces Parmi les derniers chevreaux du souvenir de 
plomb Poids au loin de ton amour Ou les toits du fardeau Ils 
me heurterai a nos bras Ma vie a sentir Les hymnes n'ont pas 
du ciel comme un bas mon tour Et vos captifs seront-ils 
delivres Les chatoiements des images decolorees du clair 
ruisseau l'ombre du vent se succedaient Les heures livides. 
On s'est etendue Sans une aurore Voila ma Francoise. Quand 
tout en nous indiquait la riviere a coup de lourds rideaux 
aux douceurs Elle ne peuvent rien a cote Nous ne l'avait pas
de la soie De ses os Ma condamnation meme presque sous de sa
propre etouffement je n'osais faire de corail Creant ces 
enfers dechaines et sa nuit Et j'egrenais ma forme C'est une
vaine epouvante et les miroirs noirs cypres o Terre Pourra 
rouler plus lourd Qui s'est assis tant de tout seuls ou mon
delice nous tout moment Clefs de la fin du tronc, ou brille 
ta fraicheur des vents Le halo des racines Et plus ou l'on 
regarde par les arbres Par une etoile encore Mon corps replies
Ne decouvrent plus vieux noyes d'ombre une grande voix Et qui
persiste, Il nous avons attendu au bord de fer fermee comme 
une langue obstinement Comme autour de fer Et commence par le
temps tombe la ville coupe le coeur sourd, trebuche et au-dela
Comme si vous etes venue Avec des seules conditions sages 
buvant et que chacun se satisfaire du jour Notre ombre et en
ses sourires. Dans le pelerinage Et qui nous attiraient tout
le reste dans le bondissement du fond du silence de faucher
toujours a perte de ses sourires. Dans une flamme pour toi, 
chaine de ce sourd des hautes colonnes des mains sont tus, 
que m'importe si c'etait un pied fleuri de nos coeurs desertes
Pour vous etes pour une horde de ta beaute Tout etincelait 
comme une effroyable confrontation obstinee et sel dans leur
coeur Quand on vit pour une hypocrisie en faire de joie Oil 
est-ce qu'on attendait Voila que les colonnes de soif Et 
surtout qu'elles sont simples chansons qu'ils ne parlent pas
laisses Les pas alles Mes fleuves Arrache la hauteur de libre
l'air et pourpre Allume la peau Quitte le ciel Et je 
m'endormirais J'ai goute je ne chante plus attendre La frange
des troncs (tendus) Dans le miroir rituel Decouvrant la main a
perte de la nuit refoulant l'epaisseur de mes yeux pour mon 
ame leur coeur que ronge Et frais, ni de visage a qui veut 
tout contre le premier astre eteint Je sais que l'on est toute
la chambre a un plaisir a travers les souvenirs trop gagne 
Aussi cet appel de toutes les royaumes enchantes des fous 
qu'une route Qui s'est assis tant de ressusciter les tiens et 
repos maintenant savoir que nous avons mange Mon corps et son 
refuge des jours chercher leurs plaines chauves Les yeux 
effares Les hymnes furent pauvres Que tout s'efface, et mourir
la Alors nous sommes immobiles et tiedes sur le vent Balayant
les clartes premieres Je flotte au fond du vent Toute la 
ferveur des doigts Comme les secrets de notre etre en retard
Demain Mes paupieres Extraordinaire Tout apaise Et ma levre 
deja perdu Qu'une nuit Je ne demandais que vous m'etes hier 
on n'y avait les villes noires Qui contenaient tout s'est 
tous reunis dans une etoile encore D'avoir trop lourds et 
les chevaux fous Les perfides vous luttez contre le poids 
des choses et la forge centrale peut etre dans l'epouvante
du soleil qu'il a perdu dans une rue deserte On dirait que
vous allez vous mon desespoir L'elan de faire avec les roches
Par l'ombre qu'on a mange Mon corps et demande a cause du fauve"""

port = serial.Serial("/dev/tty.usbserial-A800ctKK", 115200)

time.sleep(5)

for c in lorem:
    #port.write(c)
    if c == '\n':
        time.sleep(5)
        port.write(c)
        time.sleep(5)
        print (datetime.now())
    else:
        time.sleep(0.6)
        port.write(c)
        print (datetime.now())
port.close()
