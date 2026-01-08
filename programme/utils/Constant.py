from enum import Enum
from utils.Tache import Tache

class Screen(Enum):
    MENU = 0
    GAME = 1
    OPTION = 2
    LOBBY = 3

class Tache(Enum):
    MACHINE = {"Démarrer une machine":[20],
               "Réparer une petite panne ": [30],
               "Changer une pièce": [35],
               "Maintenance complète ": [45,"toutes les tâches coûtent +10 crédits pendant 1 tour"],
               "Réparer une machine critique ": [50,"salle fermée 2 tours"]
               }

    ELECT = {"Tester l'électricité":[20],
             "Remplacer un fusible": [25,"machines arrêtées ce tour"],
             "Réparer une panne": [40,"électricité coupée 1 tour"],
             "Sécuriser l’installation": [45],
             "Grosse réparation électrique ": [50," Salle info et elec bloqué pendant 3 tours"]
             }