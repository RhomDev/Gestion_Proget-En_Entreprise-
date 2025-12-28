### 	   **Scénario + Missions**

#### 

#### &nbsp;		En Entreprise



Je trouve que c'est un jeu vraiment "utile" : 

&nbsp;Ninho dit , si tu connais le boulot dis nous comment faire sinon on se passera de tous les commentaires Binks!!



* il apprend à gérer les priorités de manière fun
* il montre les conflits d'objectifs en entreprise
* sensibilise à la charge de travail

-----------------------------------------------------------------------------

**Principe général**



Le joueur incarne **un employé unique** dans une entreprise où **3 employeurs** lui donnent des ordres en temps réel.

La partie représente **une journée de travail de 30 minutes**.



Le joueur (l'employé) ne peut exécuter **qu'une seule mission (ou ordre) à la fois**, pendant que les autres s'accumulent, deviennent urgentes … ou explosent.



---------------------------------------------------------------------------

**Les 3 employeurs**



* **Le Manager pressé** (Ses missions sont courtes et très urgentes)
* 
**&nbsp;**-Donne souvent des ordres 

&nbsp;-Veut tout, tout de suite

&nbsp;-Punit fortement les retards



* **La stratège**

 -Donne moins d'ordres

&nbsp;-Missions longues mais importantes

&nbsp;-Récompense le travail bien fait



* **Le créatif Chaotique**

 -Imprévisible

&nbsp;-Peut aider ou ruiner la journée (la partie)

&nbsp;-Missions parfois modifiées en cours 



-------------------------------------------------------------------------------

**Déroulement de la partie (30 min)**



  **+ Début de journée (0 à 10 min)  chaque mission survient toutes les 60 sec**

* Peu de missions
* Le joueur prend ses marques
* Ordres espacés
* Stress faible



  **+ Milieu de journée (10 à 20 min) chaque mission survient toutes 50 sec**

* Missions plus fréquentes
* Les choix stratégiques de l'employé deviennent cruciaux
* Les files d'attente se remplissent
* Premières urgences



&nbsp; **+ Fin de journée (20 à 30 min) chaque mission survient toutes les 40 sec**

* Ordres très fréquents
* Doubles demandes possibles
* Les erreurs deviennent couteuses
* Pression maximale



---------------------------------------------------------------------------------



**Conditions de jeu:** 

* Energie : un compteur à 100
* Temps de la partie : 30 min
* Stress: Compteur à 0 au début de la partie. (A 100, l'employé craque et c'est la fin de la partie)
* Liste d'attente ( 3 missions max peuvent y être stockées)
* L'employé peut faire 1 mission à la fois
* Chaque mission consomme du **temps** et de **l'énergie**
* Si énergie = 0 --burn out (défaite des 3 employeurs)
* les missions de chaque employeur sont tirées au hasard
* L'employeur donneur de mission est tiré également au hasard (une fonction random.randint (1,3) de python)
* Un tour = la demande d'effectuer une mission





-------------------------------------------------------------------------------------



**Les différentes missions** 





1. **Le Manager pressé**



**Mission                !       Durée            !      Difficulté          !         Cout d'énergie**

---------------------------------------------------------------------------------------------------

Répondre aux mails     !        45 sec          !       Facile             !              -5

---------------------------------------------------------------------------------------------------

Réunion improvisée     !        50 sec          !        Moyen             !              -10

--------------------------------------------------------------------------------------------------

Rapport express        !        60 sec          !      Difficile           !              -20





**Malus**



Si une mission n’est pas commencée dans les 100 sec : perte d’énergie supplémentaire (-10)





**Bonus**



Si 2 missions faites à la suite : +10 énergie (Le Manager “apprécie ton implication”)





**2.  La stratège**



**Mission                !       Durée            !      Difficulté          !         Cout d'énergie**

-------------------------------------------------------------------------------------------------

Analyse marché         !        60 sec          !        Moyen             !              -10

-------------------------------------------------------------------------------------------------

Plan stratégique       !        90sec          !      Difficile           !              -20

-------------------------------------------------------------------------------------------------

Présentation finale    !        70 sec          !      Difficile           !              -15





**Malus**



Si une mission est interrompue : elle doit être recommencée (par exemple au moment de la pause café...)



**Bonus**

Mission terminée sans interruption : +15 énergie et réduction du temps de la prochaine mission de cet employeur (- 10 sec)







**3. Le créatif chaotique**





**Mission                !       Durée            !      Difficulté          !         Cout d'énergie**

---------------------------------------------------------------------------------------------------

Brainstorming          !        50 sec          !        Moyen             !              -10

---------------------------------------------------------------------------------------------------

Design prototype       !        60 sec          !        Moyen             !              -15

---------------------------------------------------------------------------------------------------

Pitch client           !        80 sec          !      Difficile           !              -20





**Malus**



30% de chance que la mission change en cours (pour le codage, un système random booléen: Au tour de l'employeur créatif chaotique, oui la mission change, non la mission ne change pas) .. Si oui la mission change, elle doit changer en plein milieu de la mission.

Celle qui a été commencée est considérée comme perdue et celle prise en compte est la mission après changement.



La mission perdue n'entraine pas de dommages



**Bonus**



Chance de bonus créatif : Si deux missions sont terminées sans interruption, mission suivante plus courte (-10 sec) et + 15 énergie



------------------------------------------------------------------------------------------------------------------------------------------------

**Gestion du temps** 



Le temps avance continuellement



Certaines missions deviennent urgentes



Trop ignorer un employeur = pénalités (ignorer les missions d'un même employeur 3 tours d'affilés = -10 énergie)



---------------------------------------------------------------------------------------------------------------------------------------------

**Énergie \& stress**



Énergie: Chaque mission en consomme

Peut être récupérée par :bonus, temps mort, missions réussies



Stress: Augmente si : la file d'attente est pleine (+10 stress)





**Choix du joueur** 



À chaque ordre :

* Accepter maintenant
* Mettre en attente
* Refuser (rare, mais parfois nécessaire et engendre une pénalité: +5 stress)



Chaque choix a une conséquence immédiate.



-------------------------------------------------------------------------------------------



**ÉVÉNEMENTS ALÉATOIRES (1 à 2 par partie)**



Ces événements surviennent à des moments imprévus et bouleversent la partie.



* **Incident serveur**



Toutes les missions en cours prennent + 10 sec (même celles dans la file d'attente) : Stress +10



* &nbsp;**Pause café**



Énergie +15



Aucune mission pendant 90 sec 



* &nbsp;**Bug critique**



Mission urgente forcée



Doit être traitée immédiatement (aucune mission difficile ne peut être effectué pendant 60 sec)



* &nbsp;**Félicitations de la direction**



Stress -20



La prochaine mission terminée est comptée double (+1 A l'employeur dont la mission suivra)



* &nbsp;**Réunion surprise**



Impossible de travailler pendant 120 sec



Missions en attente continuent d’accumuler du stress (+5 durant les 120 sec)



* &nbsp;**Coup de fatigue** (durée 120 sec)



Énergie consommée doublée





**Conditions de victoire**



A chaque mission accomplie un employeur gagne 1 point. Le vainqueur est l'employeur aura le plus de points au bout des 30 min



L’employé doit survivre jusqu’à la fin de la journée



**Conditions de défaite**



Stress à 100 → burn-out



Énergie à 0



Trop de missions échouées (échouée signifie ignorée pendant 120 sec dans la file d'attente = la mission disparait de la file d'attente )













**Arthur**







































































































