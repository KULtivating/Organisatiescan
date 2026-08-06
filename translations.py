Today 11:58 AM
Pasted text(20260806-095433).txt
Document
report_taxonomy(6).py
Python
individual(20260806-095728).py
Python
help me kijken naar deze syntax - ik had een link naar Visual.png. ik heb nu 3 files toegevoegd in de assets map - Model NL.png, Model EN.png en Model FR.png. hier ook nog wat comments - 	Het valt me op hoeveel plek 'Het overkoepelende model" inneemt voor de grootte van de afbeelding die het maar is (ten koste van 'Wat valt op'). ik heb ook in mijn fysiek rapport veranderingen al doorgevoerd ivm de feedbackteksten etc. ik denk dat deze in de volgende .py files zit. Kan je daar eens naar kijken om consistenter te maken? Het gaat maar om het deel 2 enkel dus het is een kleiner deel dan de integrape .py files
Pasted text(20260806-101545).txt
Document
in mijn online app staat ook deze json translation file. De vertalingen moeten dus niet in de .txt file van ervoor komen; kunnen we de percentielinfo ook in lijn doen met dit: NL "percentile": {
      "unavailable": "Niet beschikbaar",
      "very_low": "Zeer laag",
      "rather_low": "Eerder laag",
      "middle": "Rond het midden",
      "rather_high": "Eerder hoog",
      "very_high": "Zeer hoog"
   FR    "percentile": {
      "unavailable": "Non disponible",
      "very_low": "Très faible",
      "rather_low": "Plutôt faible",
      "middle": "Autour de la moyenne",
      "rather_high": "Plutôt élevé",
      "very_high": "Très élevé" EN     "percentile": {
      "unavailable": "Not available",
      "very_low": "Very low",
      "rather_low": "Rather low",
      "middle": "Around the middle",
      "rather_high": "Rather high",
      "very_high": "Very high"
1) de eerste vraag komt in het vet door. Dat is niet de bedoeling. ook later op de pagina komen andere vragen opeens vet door. het moet allemaal gewoon hetzelfde zijn 2) de output in het frans komt deels in het engels en nederlands door Facteur de soutien le plus fort 
Politique RH: 4.00 / 5
Score supérieur à celui d’environ 94% du groupe de référence · high

Je behoort tot de hoogste groep respondenten in hoe positief je jouw omgeving beoordeelt op deze dimensie. Dit wijst op een sterk ondersteunende context voor adaptiviteit, leren en verandering.

Principale opportunité de développement
Caractéristiques du poste: 3.62 / 5
Score supérieur à celui d’environ 56% du groupe de référence · average

Je score ligt ongeveer rond het gemiddelde van andere respondenten. Deze factor vormt waarschijnlijk een voldoende basis om je aan te passen wanneer omstandigheden veranderen.

Utilisez surtout le profil à travers les trois niveaux comme point de départ : un score plus faible n’est pas un jugement, mais indique un levier potentiel d’adaptabilité. 3) kunnen we de feedback rond de percentiel niet doen zoals in de andere files die ik gestuurd had? Ik geef hier de huidige output en ook een van mijn andere rapporten die ik beter vind. Idealiter is die button rechtsboven in elke kader bv. 4) een heel aantal interpretatietekstjes zijn in het NL nog. 5) de tekst bij mijn eigen leiderschap is opeens in een ander format. Dat is niet handig. dus niet aanbevelingen maar ook interpretatie en teksten aanpassen
Tekstrooster_IndivRapport_review_compact_meertalig(1).xlsx
Spreadsheet
het eerste tabblad omvat de feedbackteksten die ik je voordien ook al stuurde. Ik zag die er nog niet correct doorkomen online. deze zouden ook moeten overeenkomen met de files die ik je voordien stuurde voor mijn fysieke rapporten. Gberuik deze om de online app aan te passen
nee er staat nu een dubbele uitleg in de json file en de bovenste komt door, niet de gepersonaliseerde uitleg en ook de button komt er niet door ook de vertaling is nog altijd een probleem - 
Worked for 9m 57s

Je hebt gelijk. De vorige versie combineerde twee incompatibele systemen:

de app produceerde oude sleutels zoals high, above_avg en average;
de gepersonaliseerde teksten gebruikten very_high, rather_high en middle.

Daardoor werd de gepersonaliseerde tekst niet gevonden en viel de app terug op de oude, hardgecodeerde Nederlandse uitleg. Ook stond nog de oude kaartcode in het bestand, waardoor de percentielbadge niet rechtsboven verscheen.

Dit is nu structureel opgelost:

INTERPRETATIONS bevat nog maar één tekstbron: taal → dimensie → percentielband;
geen algemene individual/context-feedback meer;
geen Nederlandse hardcoded fallbackteksten meer;
de app gebruikt rechtstreeks de gepersonaliseerde teksten uit het eerste Excel-tabblad en de corresponderende FR/EN-teksten;
de codes zijn overal gelijk: very_low, rather_low, middle, rather_high, very_high;
de badge staat in de rechterbovenhoek van elk kader, bijvoorbeeld P89 · TOP 20 %;
Franse titels, beschrijvingen en interpretaties komen rechtstreeks uit de Franse vertalingen;
eigen leiderschap gebruikt dezelfde kaartindeling, met Auto-évaluation in plaats van een benchmark;
vragen worden niet meer vet weergegeven.

Na de update hoort Capaciteit in het Frans bijvoorbeeld te beginnen met:

Votre score pour Capacité se situe parmi les 20 % les plus élevés du groupe de référence…

Vervang beide actieve projectbestanden en herstart de Streamlit-app volledig. De appfile bevat als controle de marker:

APP_CONTENT_VERSION = "2026-08-06-physical-feedback-v3"

Download het gecorrigeerde pakket met beide bestanden

Losse bestanden:

online_app.txt

translations.py

De bestanden zijn syntactisch gecontroleerd en alle 11 dimensies bevatten in NL, FR en EN teksten voor alle zes statussen, inclusief unavailable.

online_app.txt
Document
translations.py
Code
1) de uitlijning in de boxen loopt niet helemaal goed. De persoonlijke teksten komen ook niet door, in geen van de talen. 2) ook de box bovenaan is nu wel heel compact. 3) er staat geen uitleg bij de eigen leiderschap - daar moet ook een definitie komen
Worked for 5m 52s

Je opmerkingen zijn verwerkt in de huidige versie.

De persoonlijke interpretatieteksten uit het eerste Excel-tabblad worden nu expliciet opgezocht op dimensie én percentielband. De generieke individual/context-teksten worden niet meer gebruikt.
De koppeling ondersteunt ook oudere of afwijkende sleutels zoals Capacité, capacity, by_dimension en Eigen leiderschap, zodat de tekst niet meer leeg blijft door een naamverschil.
De percentielbadge staat vast rechtsboven en de titel, definitie, score en subdimensies zijn consistenter uitgelijnd.
De interpretatievakken hebben een gelijkmatiger minimumformaat, maar groeien mee met de volledige persoonlijke tekst.
“Wat valt op?” / “Que retenir ?” gebruikt nu de volledige paginabreedte met twee ruime feedbackvakken. Het model staat compacter eronder.
Eigen leiderschap krijgt nu altijd een vertaalde definitie én een persoonlijke interpretatie.
De vertaalfile bevat één ondubbelzinnige bron: DIMENSION_INTERPRETATIONS.
Versiemarker: 2026-08-06-personal-feedback-layout-v4.

Beide bestanden zijn syntactisch gecontroleerd.

Download het volledige bijgewerkte pakket

online_app.txt

translations.py

online_app.txt
Document
translations.py
Code
1) de wat valt op stond qua positie goed in vorige versie, ik wilde gewoon dat de tekst uitgebreider werd zodat het makkelijker interpreteerbaar was door een leek, net zoals in mijn fysieke rapport. 2) kunnen we de kleuren van de boxen ook aangepast maken aan de hoogte van het percentiel, zoals het in het fysieke rapport ook was? staat die uitleg in de files die je al hebt of heb je er nieuwe nodig? 

Library
/
translations.py
"""NL/FR/EN-inhoud voor de Adaptiviteit Systeemscan.

De zichtbare teksten voor deel 2 staan één keer in dit bestand. INTERPRETATIONS gebruikt rechtstreeks dimensie- en percentielbandsleutels, zodat de online app geen generieke of dubbele feedbacktekst kan kiezen.
"""
LANGUAGE_NAMES = {'nl': 'Nederlands', 'fr': 'Français', 'en': 'English'}

UI_TEXTS = {'nl': {'title': 'Adaptiviteit Systeemscan',
        'intro': 'Ontdek welke individuele, team- en organisatiefactoren jouw adaptief gedrag ondersteunen of '
                 'belemmeren.',
        'details_step': 'Stap 1 · Je gegevens',
        'details_title': 'Vertel ons kort wie je bent',
        'details_intro': 'Vul de systeemscan in en ontdek wat jij en je omgeving kunnen doen om adaptiever te worden.',
        'name': 'Naam',
        'email': 'E-mailadres (optioneel)',
        'email_help': 'We bewaren dit alleen zodat we je resultaat later eventueel kunnen bezorgen. Er wordt nu geen '
                      'e-mail verstuurd.',
        'role': 'Functie',
        'organisation': 'Organisatie',
        'start': 'Start vragenlijst',
        'manager_question': 'Geef je rechtstreeks leiding aan medewerkers?',
        'yes': 'Ja',
        'no': 'Nee',
        'manager_required': 'Duid aan of je rechtstreeks leiding geeft aan medewerkers.',
        'self_leadership_title': 'Jouw eigen leiderschap',
        'self_leadership_intro': 'Vul dit in met het team waaraan je leiding geeft in gedachten.',
        'own_manager_title': 'Jouw eigen leidinggevende',
        'own_manager_intro': 'Hieronder vragen we je ook om enkele vragen over je eigen leidinggevende in te vullen.',
        'self_leadership_result': 'Jij als leidinggevende',
        'self_leadership_result_intro': 'De mate waarin je zelf als leidinggevende richting, structuur, verbinding en '
                                        'ruimte voor leren biedt aan je team.',
        'self_benchmark_unavailable': 'Benchmarkgegevens voor eigen leiderschap zijn momenteel nog niet beschikbaar.',
        'self_recommendation': 'Aanbeveling',
        'self_recommendation_text': 'Gebruik de drie subdimensies als gespreksstarter: behoud wat al sterk is en kies '
                                    'één concreet gedrag binnen de laagst scorende subdimensie om verder te oefenen en '
                                    'feedback op te vragen.',
        'part': 'Deel {current} van 3',
        'part_individual': 'Individuele basis',
        'part_team': 'Team & leidinggevende',
        'part_organisation': 'Organisatie',
        'part_instruction': 'Duid voor elke uitspraak aan in welke mate je ermee akkoord gaat.',
        'previous': 'Vorige',
        'next': 'Volgende',
        'show_result': 'Toon mijn resultaat',
        'missing': 'Vul alle vragen in dit deel in.',
        'complete': 'Dit deel is volledig ingevuld.',
        'scale': ['Helemaal oneens', 'Oneens', 'Neutraal', 'Eens', 'Helemaal eens'],
        'profile_pill': 'Jouw systeemprofiel',
        'thanks': 'Bedankt voor je deelname',
        'result_intro': 'Je resultaten tonen welke factoren op individueel, team- en organisatieniveau jouw adaptief '
                        'gedrag vandaag ondersteunen of belemmeren.',
        'model': 'Het overkoepelende model',
        'stands_out': 'Wat valt op?',
        'strongest': 'Sterkste ondersteunende factor',
        'development': 'Grootste ontwikkelkans',
        'higher_than': 'Hoger dan ongeveer {p}% van de referentiegroep',
        'lower_context': 'Deze factor wordt relatief minder sterk ervaren en kan een zinvolle ontwikkelhefboom zijn.',
        'summary_note': 'Gebruik vooral het patroon over de drie niveaus als vertrekpunt: een lagere score is geen '
                        'oordeel, maar wijst op een mogelijke hefboom voor meer adaptiviteit.',
        'score_interpretation': 'Externe vergelijking',
        'your_interpretation': 'Jouw interpretatie',
        'restart': 'Opnieuw invullen',
        'percentile_guide': 'De vergelijking toont hoeveel procent van de externe referentiegroep lager scoort. ‘Hoger '
                            'dan ongeveer 76%’ is dus geen percentage juiste antwoorden.',
        'level_low': 'Zeer laag',
        'level_below_avg': 'Eerder laag',
        'level_average': 'Rond het midden',
        'level_above_avg': 'Eerder hoog',
        'level_high': 'Zeer hoog',
        'percentile': {'unavailable': 'Niet beschikbaar',
                       'very_low': 'Laagste 20%',
                       'rather_low': 'Onder gemiddeld',
                       'middle': 'Gemiddeld',
                       'rather_high': 'Boven gemiddeld',
                       'very_high': 'Top 20%'},
        'self_assessment': 'Zelfinschatting'},
 'fr': {'title': 'Scan systémique de l’adaptabilité',
        'intro': 'Découvrez quels facteurs individuels, collectifs et organisationnels soutiennent ou freinent votre '
                 'comportement adaptatif.',
        'details_step': 'Étape 1 · Vos informations',
        'details_title': 'Parlez-nous brièvement de vous',
        'details_intro': 'Complétez le scan et découvrez ce que vous et votre environnement pouvez faire pour '
                         'renforcer votre adaptabilité.',
        'name': 'Nom',
        'email': 'Adresse e-mail (facultatif)',
        'email_help': 'Nous la conservons uniquement afin de pouvoir éventuellement vous transmettre votre résultat '
                      'plus tard. Aucun e-mail n’est envoyé maintenant.',
        'role': 'Fonction',
        'organisation': 'Organisation',
        'start': 'Commencer le questionnaire',
        'manager_question': 'Supervisez-vous directement des collaborateurs ?',
        'yes': 'Oui',
        'no': 'Non',
        'manager_required': 'Indiquez si vous supervisez directement des collaborateurs.',
        'self_leadership_title': 'Votre propre leadership',
        'self_leadership_intro': 'Répondez en pensant à l’équipe que vous dirigez. En tant que responsable...',
        'own_manager_title': 'Votre propre responsable',
        'own_manager_intro': 'Nous vous demandons également de répondre à quelques questions concernant votre propre '
                             'responsable.',
        'self_leadership_result': 'Vous en tant que responsable',
        'self_leadership_result_intro': 'La mesure dans laquelle vous offrez vous-même, en tant que responsable, une '
                                        'direction, une structure, du lien et un espace d’apprentissage à votre '
                                        'équipe.',
        'self_benchmark_unavailable': 'Les données de référence externes pour votre propre leadership ne sont pas '
                                      'encore disponibles.',
        'self_recommendation': 'Recommandation',
        'self_recommendation_text': 'Utilisez les trois sous-dimensions comme point de départ du dialogue : consolidez '
                                    'vos points forts et choisissez un comportement concret dans la sous-dimension la '
                                    'moins élevée afin de le développer et de demander du feedback.',
        'part': 'Partie {current} sur 3',
        'part_individual': 'Base individuelle',
        'part_team': 'Équipe & responsable',
        'part_organisation': 'Organisation',
        'part_instruction': 'Pour chaque affirmation, indiquez dans quelle mesure vous êtes d’accord.',
        'previous': 'Précédent',
        'next': 'Suivant',
        'show_result': 'Afficher mon résultat',
        'missing': 'Répondez à toutes les questions de cette partie.',
        'complete': 'Cette partie est entièrement complétée.',
        'scale': ['Pas du tout d’accord', 'Pas d’accord', 'Neutre', 'D’accord', 'Tout à fait d’accord'],
        'profile_pill': 'Votre profil systémique',
        'thanks': 'Merci pour votre participation',
        'result_intro': 'Vos résultats montrent quels facteurs individuels, collectifs et organisationnels soutiennent '
                        'ou freinent aujourd’hui votre comportement adaptatif.',
        'model': 'Le modèle global',
        'stands_out': 'Que retenir ?',
        'strongest': 'Facteur de soutien le plus fort',
        'development': 'Principale opportunité de développement',
        'higher_than': 'Score supérieur à celui d’environ {p}% du groupe de référence',
        'lower_context': 'Ce facteur est vécu comme relativement moins présent et peut constituer un levier de '
                         'développement pertinent.',
        'summary_note': 'Utilisez surtout le profil à travers les trois niveaux comme point de départ : un score plus '
                        'faible n’est pas un jugement, mais indique un levier potentiel d’adaptabilité.',
        'score_interpretation': 'Comparaison externe',
        'your_interpretation': 'Votre interprétation',
        'restart': 'Recommencer',
        'percentile_guide': 'La comparaison indique le pourcentage du groupe de référence externe qui obtient un score '
                            'inférieur. « Supérieur à environ 76 % » n’est donc pas un pourcentage de bonnes réponses.',
        'level_low': 'Très faible',
        'level_below_avg': 'Plutôt faible',
        'level_average': 'Dans la moyenne',
        'level_above_avg': 'Plutôt élevé',
        'level_high': 'Très élevé',
        'percentile': {'unavailable': 'Non disponible',
                       'very_low': '20 % les plus bas',
                       'rather_low': 'Sous la moyenne',
                       'middle': 'Moyenne',
                       'rather_high': 'Au-dessus de la moyenne',
                       'very_high': 'Top 20 %'},
        'self_assessment': 'Auto-évaluation'},
 'en': {'title': 'Adaptability System Scan',
        'intro': 'Discover which individual, team and organisational factors support or hinder your adaptive '
                 'behaviour.',
        'details_step': 'Step 1 · Your details',
        'details_title': 'Tell us a little about yourself',
        'details_intro': 'Complete the system scan and discover what you and your environment can do to strengthen '
                         'adaptability.',
        'name': 'Name',
        'email': 'Email address (optional)',
        'email_help': 'We only store this so that we may send you your result later. No email is sent now.',
        'role': 'Role',
        'organisation': 'Organisation',
        'start': 'Start questionnaire',
        'manager_question': 'Do you directly manage employees?',
        'yes': 'Yes',
        'no': 'No',
        'manager_required': 'Indicate whether you directly manage employees.',
        'self_leadership_title': 'Your own leadership',
        'self_leadership_intro': 'Answer with the team you lead in mind.',
        'own_manager_title': 'Your own manager',
        'own_manager_intro': 'We also ask you to answer several questions about your own manager.',
        'self_leadership_result': 'You as a manager',
        'self_leadership_result_intro': 'The extent to which you, as a manager, provide your team with direction, '
                                        'structure, connection and room for learning.',
        'self_benchmark_unavailable': 'External benchmark data for your own leadership is not yet available.',
        'self_recommendation': 'Recommendation',
        'self_recommendation_text': 'Use the three subdimensions as a conversation starter: maintain what is already '
                                    'strong and choose one concrete behaviour within the lowest-scoring subdimension '
                                    'to practise further and request feedback on.',
        'part': 'Part {current} of 3',
        'part_individual': 'Individual foundation',
        'part_team': 'Team & manager',
        'part_organisation': 'Organisation',
        'part_instruction': 'For each statement, indicate how strongly you agree.',
        'previous': 'Previous',
        'next': 'Next',
        'show_result': 'Show my result',
        'missing': 'Answer all questions in this part.',
        'complete': 'This part is complete.',
        'scale': ['Strongly disagree', 'Disagree', 'Neutral', 'Agree', 'Strongly agree'],
        'profile_pill': 'Your system profile',
        'thanks': 'Thank you for taking part',
        'result_intro': 'Your results show which individual, team and organisational factors currently support or '
                        'hinder your adaptive behaviour.',
        'model': 'The overarching model',
        'stands_out': 'What stands out?',
        'strongest': 'Strongest supporting factor',
        'development': 'Main development opportunity',
        'higher_than': 'Higher than approximately {p}% of the reference group',
        'lower_context': 'This factor is experienced as relatively less present and may be a meaningful development '
                         'lever.',
        'summary_note': 'Use the pattern across the three levels as your starting point: a lower score is not a '
                        'judgement, but indicates a potential lever for greater adaptability.',
        'score_interpretation': 'External comparison',
        'your_interpretation': 'Your interpretation',
        'restart': 'Start again',
        'percentile_guide': 'The comparison shows what percentage of the external reference group scored lower. '
                            '‘Higher than approximately 76%’ is therefore not a percentage of correct answers.',
        'level_low': 'Very low',
        'level_below_avg': 'Rather low',
        'level_average': 'Around the middle',
        'level_above_avg': 'Rather high',
        'level_high': 'Very high',
        'percentile': {'unavailable': 'Not available',
                       'very_low': 'Bottom 20%',
                       'rather_low': 'Below average',
                       'middle': 'Average',
                       'rather_high': 'Above average',
                       'very_high': 'Top 20%'},
        'self_assessment': 'Self-assessment'}}

QUESTION_TRANSLATIONS = {'fr': {'COM-C1': 'Je suis convaincu(e) de pouvoir adapter ma façon de travailler lorsque des changements inattendus '
                  'surviennent.',
        'COM-C2': ' J’ai les compétences nécessaires pour évaluer différentes solutions et choisir la meilleure. ',
        'COM-C3': ' Mes expériences passées m’aident à continuer à me développer et à m’adapter. ',
        'COM-C4': ' Je considère qu’il est important d’adapter ma façon de travailler lorsque les circonstances '
                  'changent. ',
        'COM-C5': ' Je pense que ma capacité d’adaptation au travail dépend principalement de moi-même plutôt que de '
                  'mon environnement.',
        'COM-C_new': ' Je peux rapidement établir des liens entre différents éléments et garder une vue d’ensemble '
                     'dans de nouvelles situations.',
        'COM-M1': ' Les changements me motivent, car ils me donnent l’occasion d’adapter ma façon de travailler.',
        'COM-M2': ' Je prends moi-même l’initiative de développer mes connaissances et mes compétences afin de mieux '
                  'faire face à de nouveaux défis.',
        'COM-M3': ' Je suis motivé(e) à essayer de nouvelles façons de travailler, même lorsqu’elles perturbent mes '
                  'habitudes.',
        'COM-M4': ' Mon sentiment d’appartenance à mon organisation me motive à adapter ma façon de travailler lorsque '
                  'cela est nécessaire.',
        'COM-M5': ' J’estime qu’il est de ma responsabilité d’adapter mon travail lorsque la situation change.',
        'COM-M6': ' Même lorsque les changements sont difficiles à vivre, je reste motivé(e) à m’adapter.',
        'COM-M7': ' Je reste à l’aise dans mon travail, même lorsque les changements ne sont pas encore totalement '
                  'clairs.',
        'COM-M8R': ' Le fait de devoir constamment m’adapter réduit parfois ma motivation.',
        'LO_M': 'Je suis motivé(e) à apprendre de nouvelles choses.',
        'JobCh_jobins_R': 'Je crains que mon travail évolue de manière défavorable (p. ex. moins de variété, moins '
                          'd’opportunités de développement ou moins d’autonomie).',
        'JobCh_rolinsec1R': 'Il est souvent difficile de savoir exactement ce qui est attendu de moi ou ce qui va '
                            'changer dans mon travail. ',
        'JobCh_rolinsec2': 'Il est clair pour moi ce que l’on attend de moi lorsque des changements surviennent.',
        'JobCh_TaskComplex': 'Je me sens suffisamment stimulé(e) dans mon travail, sans pour autant être surchargé(e).',
        'JobCh_TaskSign': 'Mon travail a un impact positif clair sur des personnes en dehors d’mon organisation.',
        'JobCh_AutonDec': 'Mon travail me donne une grande autonomie dans la prise de décisions.',
        'JobCh_AutonMeth': 'Je dispose d’une grande liberté et d’une grande autonomie dans la manière dont j’effectue '
                           'mon travail.',
        'JobCh_Interdep': 'Les autres dépendent de mon travail pour pouvoir terminer leurs tâches.',
        'AD_TR': 'Mon équipe (dont je suis le/la responsable direct(e)) réagit bien aux situations imprévues.',
        'AD_CL': 'Mes collègues et moi prenons régulièrement le temps d’améliorer nos méthodes de travail.',
        'AD_F': 'Lorsque quelque chose se passe mal, mon équipe adapte sa façon de travailler en fonction de ce '
                'qu’elle apprend.',
        'AD_SA': 'Face à des situations imprévues, mon équipe recueille activement des informations afin de mieux '
                 'comprendre ce qui se passe.',
        'COM-O5': 'Dans mon équipe, chacun adapte sa façon de travailler en fonction de l’évolution des circonstances.',
        'AD_new1': 'Dans mon équipe, nous réfléchissons activement aux changements possibles à l’avenir et à la '
                   'manière de nous y préparer.',
        'AD_new2': 'Dans mon équipe, nous discutons régulièrement des changements futurs possibles (p. ex. en matière '
                   'de clients, de technologie ou de réglementation) et de ce qu’ils impliquent pour notre travail.',
        'AD_HI': 'Face à des situations imprévues, nous vérifions systématiquement que les informations sont claires '
                 'pour tout le monde.',
        'AD_PS': 'Dans mon équipe, les personnes expriment ouvertement leur désaccord lorsqu’elles ont une autre '
                 'opinion sur une solution.',
        'AD_T': 'Face à des situations imprévues, il est clair au sein de mon équipe qui fait quoi et ce que l’on '
                'attend de chacun.',
        'AD_SL': 'En tant qu’équipe, nous considérons qu’il est important de discuter de différentes approches lorsque '
                 'nous résolvons ensemble des problèmes.',
        'COM-O2': 'Mes collègues m’encouragent à tester et à expérimenter de nouvelles idées.',
        'JDSCSS5': 'Les personnes avec lesquelles je travaille manifestent un intérêt personnel à mon égard.',
        'COM_ADAP1': 'Mon responsable encourage la créativité et les nouvelles idées.',
        'COM_ADAP2': 'Mon responsable veille à ce que nous apprenions de nos erreurs et puissions progresser ensemble.',
        'COM-O4': 'Mon responsable montre l’exemple dans la manière de faire face aux changements.',
        'COM_ADM1': 'Mon responsable fixe des objectifs clairs, suis les progrès réalisés et en discute avec notre '
                    'équipe.',
        'COM_ADM2': 'Mon responsable apporte de la structure et de la planification à notre travail.',
        'COM_ENAB1': 'Mon responsable crée un environnement dans lequel les membres de l’équipe peuvent discuter '
                     'ouvertement de points de vue différents.',
        'COM_ENAB2': 'Mon responsable aide les membres de l’équipe à créer des liens entre nous afin que nous '
                     'puissions apprendre les uns des autres.',
        'OAP1': 'Mon organisation s’adapte efficacement aux évolutions sociales et économiques.',
        'CR_CE1': 'Mon organisation poursuit ses efforts d’amélioration continue.',
        'CR_CE3': 'Mon organisation assure un suivi structuré des changements et des améliorations.',
        'visie1': 'Mon organisation traduit en temps utile les signaux provenant de son environnement (p. ex. le '
                  'marché, la société ou la technologie) en choix concrets ou en formes de soutien (p. ex. priorités, '
                  'compétences ou approche).',
        'OL_MC1': 'La direction d’mon organisation implique souvent les collaborateurs dans les décisions importantes.',
        'OL_MC2R': 'La direction considère davantage l’apprentissage comme un coût que comme un investissement.',
        'OL_MC3': 'La direction d’mon organisation est favorable aux changements qui nous permettent de nous adapter '
                  'aux évolutions externes ou de les anticiper.',
        'visie2': 'Je comprends clairement où mon organisation souhaite aller à l’avenir et ce que cela implique pour '
                  'mon travail.',
        'CR_CE2': 'Mon organisation parvient à motiver les collaborateurs à adapter leur façon de travailler aux '
                  'nouvelles circonstances.',
        'CR_K1': 'Mon organisation sait comment soutenir les collaborateurs afin qu’ils continuent à apprendre et à '
                 's’adapter.',
        'CR_K2': 'Mon organisation a une vision claire de ce qui est nécessaire pour s’adapter aux évolutions de son '
                 'environnement.',
        'CR_A1': 'Mon organisation dispose des ressources nécessaires pour s’adapter aux changements.',
        'CR_A2': 'Mon organisation offre aux collaborateurs la possibilité d’apprendre et de se développer.',
        'CR_A3': 'Mon organisation accorde suffisamment de temps pour me permettre de me préparer aux changements ou '
                 'de m’y adapter.',
        'OL_KT2': 'Mon organisation dispose d’outils (guides, procédures, bases de données) permettant de préserver '
                  'les connaissances acquises, même lorsque les collaborateurs changent.',
        'OL_S1': 'Tous les niveaux d’mon organisation (p. ex. département, équipe, individu) comprennent clairement '
                 'comment ils contribuent aux objectifs généraux.',
        'OL_S2': 'Tous les niveaux d’mon organisation sont interconnectés et collaborent efficacement les uns avec les '
                 'autres.',
        'AD_CD': 'Lorsque nous collaborons avec d’autres équipes, il est clair qui est responsable de quelles '
                 'décisions.',
        'OL_O1': 'Mon organisation encourage l’expérimentation et l’innovation afin d’améliorer les processus.',
        'OL_O2': 'Mon organisation observe ce que font les autres organisations et adopte les idées qui peuvent lui '
                 'être utiles.',
        'OL_O3': 'Les idées et les expériences des partenaires externes (p. ex. consultants ou clients) sont '
                 'considérées comme une source précieuse d’apprentissage.',
        'OL_O4': 'Il fait partie de la culture d’mon organisation que les collaborateurs partagent leurs idées et '
                 'leurs points de vue sur la manière d’améliorer les processus de travail.',
        'OL_MC4': 'Les nouvelles idées qui donnent de bons résultats sont valorisées. ',
        'OL_KT1': 'Les erreurs sont discutées et analysées à tous les niveaux de l’organisation.',
        'HR_Train': 'Il existe chez mon organisation des formations visant à aider les collaborateurs à mieux '
                    's’adapter aux changements.',
        'HR_Comp': 'Les collaborateurs qui adoptent une attitude très proactive face au changement bénéficient '
                   'd’opportunités ou de récompenses supplémentaires.',
        'HR_PerfApp': 'Les entretiens d’évaluation et de développement portent également sur le développement des '
                      'compétences liées au changement.',
        'HR_Selec': 'Lors du recrutement, nous tenons compte de la capacité des candidats à bien s’adapter aux '
                    'changements.'},
 'en': {'COM-C1': 'I am confident that I can adapt the way I work when unexpected changes occur.',
        'COM-C2': 'I have the skills to assess different solutions and choose the best one.',
        'COM-C3': 'My previous experiences help me continue to grow and adapt.',
        'COM-C4': 'I consider it important to adjust the way I work when circumstances change.',
        'COM-C5': 'I feel that my adaptability at work mainly depends on me rather than my environment.',
        'COM-C_new': 'I can quickly identify connections and maintain an overview in new situations.',
        'COM-M1': 'Changes motivate me because they offer opportunities to adjust the way I work.',
        'COM-M2': 'I take the initiative to renew my knowledge and skills so that I can deal better with new '
                  'challenges.',
        'COM-M3': 'I am motivated to try new ways of working, even when they disrupt my routine.',
        'COM-M4': 'The connection I feel with my organisation motivates me to adapt the way I work when needed.',
        'COM-M5': 'I see it as my responsibility to adapt my work when the situation changes.',
        'COM-M6': 'Even when changes feel demanding, I remain motivated to adapt.',
        'COM-M7': 'I feel comfortable continuing my work even when changes are not yet completely clear.',
        'COM-M8R': 'The constant need to adapt sometimes reduces my motivation.',
        'LO_M': 'I am motivated to learn new things.',
        'JobCh_jobins_R': 'I fear that my job will change for the worse, for example through less variety, development '
                          'opportunity or freedom.',
        'JobCh_rolinsec1R': 'In my work, it is often unclear what exactly is expected or what will change.',
        'JobCh_rolinsec2': 'It is clear what is expected of me when changes occur.',
        'JobCh_TaskComplex': 'I feel sufficiently challenged, but not overloaded, in my work.',
        'JobCh_TaskSign': 'My work has a clear positive impact on people outside my organisation.',
        'JobCh_AutonDec': 'My job gives me considerable autonomy in making decisions.',
        'JobCh_AutonMeth': 'My job gives me a great deal of freedom and independence in how I do my work.',
        'JobCh_Interdep': 'Unless my work is completed, others cannot finish their tasks.',
        'AD_TR': 'My team responds well to unexpected situations.',
        'AD_CL': 'My colleagues and I regularly take time to improve our working methods.',
        'AD_F': 'When something goes wrong, my team adapts the way we work based on what we learn.',
        'AD_SA': 'In unexpected situations, my team actively gathers information to better understand what is '
                 'happening.',
        'COM-O5': 'Everyone in my team adjusts the way they work when circumstances change.',
        'AD_new1': 'In my team, we actively consider possible future changes and how we can prepare for them.',
        'AD_new2': 'In my team, we regularly discuss future changes that may affect us, such as changes in customers, '
                   'technology or regulation, and what they mean for our work.',
        'AD_HI': 'In unexpected situations, we double-check that the information is clear to everyone.',
        'AD_PS': 'People in my team speak honestly when they disagree about a solution.',
        'AD_T': 'In unexpected situations, it is clear within my team who does what and what is expected of each '
                'person.',
        'AD_SL': 'As a team, we consider it important to discuss different approaches when solving problems together.',
        'COM-O2': 'My colleagues encourage me to test and try new ideas.',
        'JDSCSS5': 'The people I work with take a personal interest in me.',
        'COM_ADAP1': 'My manager encourages creativity and new ideas.',
        'COM_ADAP2': 'My manager ensures that we learn from mistakes and can grow together.',
        'COM-O4': 'My manager sets a good example in dealing with change.',
        'COM_ADM1': 'My manager sets clear goals, measures progress and discusses it.',
        'COM_ADM2': 'My manager provides structure and planning in our work.',
        'COM_ENAB1': 'My manager creates a setting in which team members can openly discuss different opinions.',
        'COM_ENAB2': 'My manager helps team members connect so that we can learn from one another.',
        'OAP1': 'My organisation adapts effectively to social and economic changes.',
        'CR_CE1': 'My organisation continuously works on improvement.',
        'CR_CE3': 'My organisation systematically monitors the progress of changes and improvements.',
        'visie1': 'My organisation translates signals from its environment, such as market, society or technology, '
                  'into timely choices or support.',
        'OL_MC1': 'Top management often involves employees in important decisions.',
        'OL_MC2R': 'In my organisation, management sees learning more as a cost than an investment.',
        'OL_MC3': 'Top management supports changes that allow us to keep pace with or stay ahead of external '
                  'developments.',
        'visie2': 'I clearly understand where our organisation wants to go in the future and what this means for my '
                  'work.',
        'CR_CE2': 'My organisation succeeds in motivating people to adapt the way they work to new circumstances.',
        'CR_K1': 'My organisation knows how to support employees in continuing to learn and adapt.',
        'CR_K2': 'My organisation has a clear understanding of what is needed to adapt to changes in its environment.',
        'CR_A1': 'My organisation has sufficient resources to adapt to change.',
        'CR_A2': 'My organisation gives employees room to learn and grow.',
        'CR_A3': 'My organisation gives me enough time to prepare for or adapt to changes.',
        'OL_KT2': 'My organisation has tools, such as manuals, routines and databases, to preserve knowledge from the '
                  'past even when colleagues change.',
        'OL_S1': 'All levels of the organisation know how they contribute to the overall goals.',
        'OL_S2': 'All levels of the organisation are connected and work well together.',
        'AD_CD': 'When we work with other teams, it is clear who should make which decisions.',
        'OL_O1': 'My organisation encourages experimentation and innovation to improve processes.',
        'OL_O2': 'My organisation looks at what other organisations do and adopts useful ideas.',
        'OL_O3': 'Ideas and experiences from external partners, such as advisers or customers, are considered valuable '
                 'sources of learning.',
        'OL_O4': 'Sharing opinions and ideas about improving work processes is part of our organisational culture.',
        'OL_MC4': 'New ideas that work well are rewarded.',
        'OL_KT1': 'Mistakes are discussed and analysed at every level of the organisation.',
        'HR_Train': 'My organisation provides training to help employees adapt better to change.',
        'HR_Comp': 'Employees who deal with change very proactively receive additional opportunities or rewards.',
        'HR_PerfApp': 'Performance reviews focus on developing change-related skills.',
        'HR_Selec': 'When recruiting, we consider how well candidates can adapt.'}}

SELF_LEADERSHIP_TRANSLATIONS = {'nl': {'SELF_COM_ADAP1': 'Ik stimuleer creativiteit en nieuwe ideeën in mijn team.',
        'SELF_COM_ADAP2': 'Ik zorg dat we leren van fouten en samen kunnen groeien.',
        'SELF_COM-O4': 'Ik geef het goede voorbeeld in hoe om te gaan met veranderingen.',
        'SELF_COM_ADM1': 'Ik stel duidelijke doelen, meet voortgang én bespreek deze met mijn team.',
        'SELF_COM_ADM2': 'Ik geef structuur en planning aan het werk van mijn team.',
        'SELF_COM_ENAB1': 'Ik creëer een context waarin teamleden verschillende meningen openlijk kunnen bespreken.',
        'SELF_COM_ENAB2': 'Ik help teamleden met elkaar te verbinden zodat ze van elkaar kunnen leren.'},
 'fr': {'SELF_COM_ADAP1': 'J’encourage la créativité et les nouvelles idées.',
        'SELF_COM_ADAP2': 'Je veille à ce que nous apprenions de nos erreurs et que nous puissions progresser '
                          'ensemble.',
        'SELF_COM-O4': 'Je montre l’exemple dans la manière de faire face aux changements.',
        'SELF_COM_ADM1': 'Je fixe des objectifs clairs, je suis les progrès réalisés et j’en discute avec mon équipe.',
        'SELF_COM_ADM2': 'J’apporte de la structure et de la planification à notre travail.',
        'SELF_COM_ENAB1': 'Je crée un environnement dans lequel les membres de l’équipe peuvent discuter ouvertement '
                          'de points de vue différents.',
        'SELF_COM_ENAB2': 'J’aide les membres de l’équipe à créer des liens entre eux afin que nous puissions '
                          'apprendre les uns des autres.'},
 'en': {'SELF_COM_ADAP1': 'I encourage creativity and new ideas in my team.',
        'SELF_COM_ADAP2': 'I ensure that we learn from mistakes and can grow together.',
        'SELF_COM-O4': 'I set a good example in how to deal with change.',
        'SELF_COM_ADM1': 'I set clear goals, measure progress and discuss it with my team.',
        'SELF_COM_ADM2': 'I provide structure and planning for my team’s work.',
        'SELF_COM_ENAB1': 'I create a setting in which team members can openly discuss different opinions.',
        'SELF_COM_ENAB2': 'I help team members connect so that they can learn from one another.'}}

DIMENSION_LABELS = {'nl': {'Capaciteit': 'Capaciteit',
        'Motivatie': 'Motivatie',
        'Job Karakteristieken': 'Job Karakteristieken',
        'Teamadaptiviteit': 'Teamadaptiviteit',
        'Teamklimaat': 'Teamklimaat',
        'Richting & steun leidinggevende': 'Jouw leidinggevende',
        'Organisatieadaptiviteit': 'Organisatieadaptiviteit',
        'Richting & steun van organisatie': 'Richting & steun van organisatie',
        'Organisatieklimaat': 'Organisatieklimaat',
        'HR': 'HR',
        'Eigen leiderschap': 'Jij als leidinggevende'},
 'fr': {'Capaciteit': 'Capacité',
        'Motivatie': 'Motivation',
        'Job Karakteristieken': 'Caractéristiques du travail',
        'Teamadaptiviteit': 'Adaptabilité de l’équipe',
        'Teamklimaat': 'Climat d’équipe',
        'Richting & steun leidinggevende': 'Votre propre responsable',
        'Organisatieadaptiviteit': 'Adaptabilité organisationnelle',
        'Richting & steun van organisatie': 'Orientation et soutien de l’organisation',
        'Organisatieklimaat': 'Climat organisationnel',
        'HR': 'RH',
        'Eigen leiderschap': 'Vous en tant que responsable'},
 'en': {'Capaciteit': 'Capability',
        'Motivatie': 'Motivation',
        'Job Karakteristieken': 'Job characteristics',
        'Teamadaptiviteit': 'Team adaptability',
        'Teamklimaat': 'Team climate',
        'Richting & steun leidinggevende': 'Your own manager',
        'Organisatieadaptiviteit': 'Organisation adaptability',
        'Richting & steun van organisatie': 'Organisation direction & support',
        'Organisatieklimaat': 'Organisation climate',
        'HR': 'HR',
        'Eigen leiderschap': 'You as a manager'}}

SHORT_DESCRIPTIONS = {'nl': {'Capaciteit': 'Vaardigheden, vertrouwen en inzicht om de werkwijze aan te passen.',
        'Motivatie': 'Energie en bereidheid om te leren, bij te sturen en vol te houden.',
        'Job Karakteristieken': 'Kenmerken van het werk die adaptiviteit ondersteunen of bemoeilijken.',
        'Teamadaptiviteit': 'De mate waarin teams samen leren en hun werkwijze aanpassen.',
        'Teamklimaat': 'Openheid, vertrouwen, veiligheid en samenwerking binnen teams.',
        'Richting & steun leidinggevende': 'Hoe medewerkers de richting, structuur, verbinding en ruimte voor leren '
                                           'vanuit hun eigen leidinggevende ervaren.',
        'Organisatieadaptiviteit': 'Het vermogen van de organisatie om veranderingen op te pikken en om te zetten in '
                                   'actie.',
        'Richting & steun van organisatie': 'Duidelijkheid, middelen, kennis en afstemming vanuit de organisatie.',
        'Organisatieklimaat': 'De mate waarin leren, experimenteren en ideeën delen worden aangemoedigd.',
        'HR': 'De manier waarop HR-praktijken adaptiviteit ondersteunen via selectie, ontwikkeling en waardering.',
        'Eigen leiderschap': 'De mate waarin je zelf als leidinggevende richting, structuur, verbinding en ruimte voor '
                             'leren biedt aan je team.'},
 'fr': {'Capaciteit': 'Les compétences, la confiance et la compréhension nécessaires pour adapter les méthodes de '
                      'travail.',
        'Motivatie': 'L’énergie et la volonté d’apprendre, de s’ajuster et de persévérer.',
        'Job Karakteristieken': 'Les caractéristiques du travail qui soutiennent ou entravent l’adaptabilité.',
        'Teamadaptiviteit': 'La mesure dans laquelle les équipes apprennent ensemble et adaptent leurs méthodes de '
                            'travail.',
        'Teamklimaat': 'L’ouverture, la confiance, la sécurité et la collaboration au sein des équipes.',
        'Richting & steun leidinggevende': 'La manière dont les collaborateurs perçoivent l’orientation, la structure, '
                                           'la connexion et l’espace d’apprentissage offerts par leur propre '
                                           'responsable.',
        'Organisatieadaptiviteit': 'La capacité de l’organisation à détecter les changements et à les transformer en '
                                   'action.',
        'Richting & steun van organisatie': 'La clarté, les ressources, les connaissances et l’alignement fournis par '
                                            'l’organisation.',
        'Organisatieklimaat': 'La mesure dans laquelle l’apprentissage, l’expérimentation et le partage d’idées sont '
                              'encouragés.',
        'HR': 'La manière dont les pratiques RH soutiennent l’adaptabilité par la sélection, le développement et la '
              'reconnaissance.',
        'Eigen leiderschap': 'La mesure dans laquelle vous offrez vous-même, en tant que responsable, une direction, '
                             'une structure, du lien et un espace d’apprentissage à votre équipe.'},
 'en': {'Capaciteit': 'Skills, confidence and insight needed to adapt working methods.',
        'Motivatie': 'Energy and willingness to learn, adjust and persevere.',
        'Job Karakteristieken': 'Features of the work that support or hinder adaptability.',
        'Teamadaptiviteit': 'The extent to which teams learn together and adapt their ways of working.',
        'Teamklimaat': 'Openness, trust, safety and collaboration within teams.',
        'Richting & steun leidinggevende': 'How employees experience the direction, structure, connection and room for '
                                           'learning provided by their own manager.',
        'Organisatieadaptiviteit': 'The organisation’s ability to detect changes and turn them into action.',
        'Richting & steun van organisatie': 'Clarity, resources, knowledge and alignment provided by the organisation.',
        'Organisatieklimaat': 'The extent to which learning, experimentation and sharing ideas are encouraged.',
        'HR': 'How HR practices support adaptability through selection, development and recognition.',
        'Eigen leiderschap': 'The extent to which you, as a manager, provide your team with direction, structure, '
                             'connection and room for learning.'}}

GROUP_TEXTS = {'nl': {'Individuele basis': 'Je persoonlijke basis voor adaptiviteit: wat je kan, wat je motiveert en hoe je job is '
                             'ingericht.',
        'Team & leidinggevende': 'De dagelijkse context waarin samenwerking, veiligheid, leren en leiding jouw '
                                 'adaptiviteit versterken of afremmen.',
        'Organisatie': 'De bredere richting, systemen, cultuur en ondersteuning die duurzaam aanpassen en leren '
                       'mogelijk maken.'},
 'fr': {'Individuele basis': 'Votre base personnelle : ce que vous pouvez faire, ce qui vous motive et la manière dont '
                             'votre poste est conçu.',
        'Team & leidinggevende': 'Le contexte quotidien dans lequel collaboration, sécurité, apprentissage et '
                                 'leadership renforcent ou freinent votre adaptabilité.',
        'Organisatie': 'L’orientation, les systèmes, la culture et le soutien qui rendent possible une adaptation '
                       'durable.'},
 'en': {'Individuele basis': 'Your personal foundation: what you can do, what motivates you and how your job is '
                             'designed.',
        'Team & leidinggevende': 'The daily context in which collaboration, safety, learning and leadership support or '
                                 'hinder adaptability.',
        'Organisatie': 'The wider direction, systems, culture and support that enable sustainable adaptation and '
                       'learning.'}}

GROUP_LABELS = {'nl': {'Individuele basis': 'Individuele basis',
        'Team & leidinggevende': 'Teamuitkomsten',
        'Organisatie': 'Organisatiefactoren'},
 'fr': {'Individuele basis': 'Base individuelle',
        'Team & leidinggevende': 'Résultats de l’équipe',
        'Organisatie': 'Facteurs organisationnels'},
 'en': {'Individuele basis': 'Individual foundation',
        'Team & leidinggevende': 'Team outcomes',
        'Organisatie': 'Organisational factors'}}

SUBDIMENSION_LABELS = {'nl': {'Perceived Behavioral Control': 'Ervaren gedragscontrole',
        'Vaardigheid': 'Vaardigheid',
        'Ervaren belang': 'Ervaren belang',
        'Intrinsieke motivatie': 'Intrinsieke motivatie',
        'Betrokkenheid': 'Betrokkenheid',
        'Volharding': 'Volharding',
        'Job onzekerheid': 'Jobonzekerheid',
        'Rolduidelijkheid': 'Rolduidelijkheid',
        'Taakcomplexiteit & betekenis': 'Taakcomplexiteit & betekenis',
        'Autonomie': 'Autonomie',
        'Afhankelijkheid': 'Afhankelijkheid',
        'Nieuwigheden stimuleren': 'Nieuwigheden stimuleren',
        'Structuur aanbrengen': 'Structuur aanbrengen',
        'Verbinding maken': 'Verbinding maken',
        'Topmanagement steun': 'Steun van het topmanagement',
        'Kennis': 'Kennis',
        'Middelen': 'Middelen',
        'Alignment': 'Afstemming'},
 'fr': {'Perceived Behavioral Control': 'Contrôle comportemental perçu',
        'Vaardigheid': 'Compétences',
        'Ervaren belang': 'Importance perçue',
        'Intrinsieke motivatie': 'Motivation intrinsèque',
        'Betrokkenheid': 'Engagement',
        'Volharding': 'Persévérance',
        'Job onzekerheid': 'Insécurité d’emploi',
        'Rolduidelijkheid': 'Clarté du rôle',
        'Taakcomplexiteit & betekenis': 'Complexité & sens des tâches',
        'Autonomie': 'Autonomie',
        'Afhankelijkheid': 'Interdépendance',
        'Nieuwigheden stimuleren': 'Stimuler l’innovation',
        'Structuur aanbrengen': 'Apporter de la structure',
        'Verbinding maken': 'Créer des liens',
        'Topmanagement steun': 'Soutien de la direction',
        'Kennis': 'Connaissances',
        'Middelen': 'Ressources',
        'Alignment': 'Alignement'},
 'en': {'Perceived Behavioral Control': 'Perceived behavioural control',
        'Vaardigheid': 'Skills',
        'Ervaren belang': 'Perceived importance',
        'Intrinsieke motivatie': 'Intrinsic motivation',
        'Betrokkenheid': 'Commitment',
        'Volharding': 'Persistence',
        'Job onzekerheid': 'Job insecurity',
        'Rolduidelijkheid': 'Role clarity',
        'Taakcomplexiteit & betekenis': 'Task complexity & meaning',
        'Autonomie': 'Autonomy',
        'Afhankelijkheid': 'Interdependence',
        'Nieuwigheden stimuleren': 'Encouraging innovation',
        'Structuur aanbrengen': 'Providing structure',
        'Verbinding maken': 'Building connection',
        'Topmanagement steun': 'Top-management support',
        'Kennis': 'Knowledge',
        'Middelen': 'Resources',
        'Alignment': 'Alignment'}}

# Eén bron voor alle dimensiespecifieke feedbackteksten.
INTERPRETATIONS = {'nl': {'Capaciteit': {'unavailable': 'Voor deze dimensie zijn momenteel geen externe benchmarkgegevens beschikbaar.',
                       'very_low': 'Je score op Capaciteit ligt bij de laagste 20% van de benchmarkgroep. Je ervaart momenteel relatief '
                                   'weinig houvast om je aanpak doeltreffend aan te passen. Vooral vertrouwen in je invloed, het verwerken '
                                   'van informatie of het zien van het belang kan je vermogen om te schakelen beperken.',
                       'rather_low': 'Je score op Capaciteit ligt onder het gemiddelde van de benchmarkgroep. Je beschikt over een aantal '
                                     'bruikbare aanknopingspunten, maar voelt je nog niet in elke situatie voldoende in staat om te '
                                     'schakelen. Complexiteit of onduidelijkheid kunnen je vertrouwen en handelingsperspectief snel '
                                     'verkleinen.',
                       'middle': 'Je score op Capaciteit ligt rond het gemiddelde van de benchmarkgroep. Je beschikt doorgaans over '
                                 'voldoende inzicht, vaardigheden en vertrouwen om je aan te passen. In nieuwe of complexe situaties kan '
                                 'extra voorbereiding of ondersteuning helpen om die basis consistenter te benutten.',
                       'rather_high': 'Je score op Capaciteit ligt boven het gemiddelde van de benchmarkgroep. Je voelt je meestal bekwaam '
                                      'om informatie te verwerken, verbanden te leggen en je aanpak bij te sturen. Dit vormt een stevige '
                                      'persoonlijke basis om verandering actief vast te nemen.',
                       'very_high': 'Je score op Capaciteit behoort tot de hoogste 20% van de benchmarkgroep. Je capaciteit om met '
                                    'verandering om te gaan is uitzonderlijk sterk ontwikkeld. Je combineert inzicht, vaardigheid en '
                                    'vertrouwen, waardoor je ook in complexe en onzekere situaties gericht kan schakelen en anderen '
                                    'houvast kan bieden.'},
        'Motivatie': {'unavailable': 'Voor deze dimensie zijn momenteel geen externe benchmarkgegevens beschikbaar.',
                      'very_low': 'Je score op Motivatie ligt bij de laagste 20% van de benchmarkgroep. Verandering roept momenteel '
                                  'relatief weinig energie of volharding bij je op. Je betrokkenheid of interne drive biedt daardoor nog '
                                  'weinig draagkracht wanneer aanpassen inspanning en onzekerheid vraagt.',
                      'rather_low': 'Je score op Motivatie ligt onder het gemiddelde van de benchmarkgroep. Je bent bereid om mee te '
                                    'bewegen wanneer de noodzaak duidelijk is, maar je energie en volharding zijn niet altijd stabiel. Bij '
                                    'langdurige of onzekere verandering kan je motivatie sneller afnemen.',
                      'middle': 'Je score op Motivatie ligt rond het gemiddelde van de benchmarkgroep. Je motivatie biedt doorgaans '
                                'voldoende basis om met verandering aan de slag te gaan. Hoe sterk je betrokken blijft en volhoudt, hangt '
                                'mee af van betekenis, haalbaarheid en zicht op vooruitgang.',
                      'rather_high': 'Je score op Motivatie ligt boven het gemiddelde van de benchmarkgroep. Je haalt meestal energie uit '
                                     'leren en verbeteren en blijft ook bij moeilijkheden betrokken. Die motivatie helpt je om verandering '
                                     'niet alleen te starten, maar ook vol te houden.',
                      'very_high': 'Je score op Motivatie behoort tot de hoogste 20% van de benchmarkgroep. Je motivatie voor aanpassing '
                                   'en ontwikkeling is uitzonderlijk sterk. Je combineert interne drive, betrokkenheid en volharding, en '
                                   'kan daarmee ook energie en geloof in verandering bij anderen versterken.'},
        'Job Karakteristieken': {'unavailable': 'Voor deze dimensie zijn momenteel geen externe benchmarkgegevens beschikbaar.',
                                 'very_low': 'Je beoordeling van Job Karakteristieken ligt bij de laagste 20% van de benchmarkgroep. Je '
                                             'ervaart in je job relatief weinig voorwaarden die aanpassen, leren en initiatief '
                                             'ondersteunen. Een combinatie van onduidelijkheid, beperkte autonomie, afhankelijkheden of '
                                             'weinig betekenisvolle uitdaging kan je eigen inspanningen duidelijk afremmen.',
                                 'rather_low': 'Je beoordeling van Job Karakteristieken ligt onder het gemiddelde van de benchmarkgroep. '
                                               'Je job biedt enkele bruikbare voorwaarden voor adaptief handelen, maar die zijn nog niet '
                                               'stabiel of evenwichtig aanwezig. Bepaalde taakkenmerken maken het daardoor lastiger om '
                                               'zelfstandig en tijdig bij te sturen.',
                                 'middle': 'Je beoordeling van Job Karakteristieken ligt rond het gemiddelde van de benchmarkgroep. Je job '
                                           'biedt doorgaans een werkbare basis om je aan te passen. Sommige kenmerken geven ruimte en '
                                           'duidelijkheid, terwijl andere in specifieke situaties nog vertraging, onzekerheid of '
                                           'afhankelijkheid kunnen veroorzaken.',
                                 'rather_high': 'Je beoordeling van Job Karakteristieken ligt boven het gemiddelde van de benchmarkgroep. '
                                                'Je ervaart je job meestal als duidelijk, betekenisvol en voldoende autonoom om flexibel '
                                                'te handelen. De taakkenmerken ondersteunen leren en bijsturen relatief sterk.',
                                 'very_high': 'Je beoordeling van Job Karakteristieken behoort tot de hoogste 20% van de benchmarkgroep. '
                                              'Je job biedt uitzonderlijk gunstige voorwaarden voor adaptief gedrag. Duidelijkheid, '
                                              'betekenis, autonomie en werkbare afhankelijkheden versterken elkaar, waardoor je snel kan '
                                              'leren en doelgericht kan bijsturen.'},
        'Teamadaptiviteit': {'unavailable': 'Voor deze dimensie zijn momenteel geen externe benchmarkgegevens beschikbaar.',
                             'very_low': 'Je beoordeling van Teamadaptiviteit ligt bij de laagste 20% van de benchmarkgroep. Je ervaart '
                                         'dat je team veranderingen relatief moeilijk opvangt. Samen leren, flexibel afstemmen en '
                                         'werkwijzen bijsturen gebeuren weinig, waardoor aanpassing sterk op individuele inspanningen kan '
                                         'leunen.',
                             'rather_low': 'Je beoordeling van Teamadaptiviteit ligt onder het gemiddelde van de benchmarkgroep. Je team '
                                           'kan zich in vertrouwde situaties aanpassen, maar collectief leren en tijdig bijsturen zijn nog '
                                           'niet consequent. Bij onverwachte veranderingen ontstaat daardoor sneller vertraging of '
                                           'versnippering.',
                             'middle': 'Je beoordeling van Teamadaptiviteit ligt rond het gemiddelde van de benchmarkgroep. Je team '
                                       'beschikt over een werkbare basis om samen te reageren en de aanpak bij te sturen. Hoe vlot dat '
                                       'gebeurt, hangt nog af van de situatie, de betrokken collega’s en de beschikbare ruimte.',
                             'rather_high': 'Je beoordeling van Teamadaptiviteit ligt boven het gemiddelde van de benchmarkgroep. Je '
                                            'ervaart dat je team meestal flexibel reageert, kennis deelt en de werkwijze samen verbetert. '
                                            'Dat maakt verandering beter hanteerbaar en ondersteunt individuele adaptiviteit.',
                             'very_high': 'Je beoordeling van Teamadaptiviteit behoort tot de hoogste 20% van de benchmarkgroep. Je team '
                                          'wordt ervaren als uitzonderlijk adaptief. Het pikt signalen snel op, leert collectief en past '
                                          'werkwijzen doelgericht aan, waardoor het ook onder onzekerheid slagkrachtig blijft.'},
        'Teamklimaat': {'unavailable': 'Voor deze dimensie zijn momenteel geen externe benchmarkgegevens beschikbaar.',
                        'very_low': 'Je beoordeling van Teamklimaat ligt bij de laagste 20% van de benchmarkgroep. Je ervaart relatief '
                                    'weinig openheid, vertrouwen of psychologische veiligheid in het team. Daardoor wordt het moeilijker '
                                    'om twijfels te delen, fouten te bespreken en nieuwe ideeën uit te proberen.',
                        'rather_low': 'Je beoordeling van Teamklimaat ligt onder het gemiddelde van de benchmarkgroep. Er zijn '
                                      'aanknopingspunten voor samenwerking, maar open communicatie en veiligheid zijn nog wisselend. '
                                      'Mensen wegen mogelijk af wat ze wel of niet delen, wat gezamenlijk leren en bijsturen vertraagt.',
                        'middle': 'Je beoordeling van Teamklimaat ligt rond het gemiddelde van de benchmarkgroep. Het teamklimaat biedt '
                                  'doorgaans voldoende basis voor samenwerking en gesprek. In gevoelige of onzekere situaties is extra '
                                  'aandacht nodig om openheid, vertrouwen en duidelijke afstemming te behouden.',
                        'rather_high': 'Je beoordeling van Teamklimaat ligt boven het gemiddelde van de benchmarkgroep. Je ervaart meestal '
                                       'open communicatie, vertrouwen en ruimte om vragen of fouten bespreekbaar te maken. Dit klimaat '
                                       'ondersteunt samenwerking, leren en tijdig bijsturen.',
                        'very_high': 'Je beoordeling van Teamklimaat behoort tot de hoogste 20% van de benchmarkgroep. Je teamklimaat '
                                     'wordt ervaren als uitzonderlijk veilig en verbindend. Mensen delen informatie en ideeën vrij, '
                                     'spreken spanningen aan en benutten verschillen om samen sneller te leren.'},
        'Richting & steun leidinggevende': {'unavailable': 'Voor deze dimensie zijn momenteel geen externe benchmarkgegevens beschikbaar.',
                                            'very_low': 'Je beoordeling van je eigen leidinggevende ligt bij de laagste 20% van de '
                                                        'benchmarkgroep. Je ervaart relatief weinig richting, structuur of leer- en '
                                                        'experimenteerruimte vanuit je eigen leidinggevende. Daardoor ontbreekt '
                                                        'belangrijke dagelijkse steun om verandering veilig en doelgericht vast te nemen.',
                                            'rather_low': 'Je beoordeling van je eigen leidinggevende ligt onder het gemiddelde van de '
                                                          'benchmarkgroep. Je eigen leidinggevende biedt op sommige momenten houvast, maar '
                                                          'richting, verbinding en ruimte voor nieuwe aanpakken zijn nog wisselend. Dat '
                                                          'maakt het moeilijker om met vertrouwen te experimenteren en bij te sturen.',
                                            'middle': 'Je beoordeling van je eigen leidinggevende ligt rond het gemiddelde van de '
                                                      'benchmarkgroep. Je eigen leidinggevende biedt een bruikbare basis van richting, '
                                                      'structuur en verbinding. Die ondersteuning kan in complexe of onzekere situaties '
                                                      'nog consistenter en zichtbaarder worden.',
                                            'rather_high': 'Je beoordeling van je eigen leidinggevende ligt boven het gemiddelde van de '
                                                           'benchmarkgroep. Je ervaart doorgaans duidelijke richting, werkbare structuur '
                                                           'en ruimte om te leren. Je eigen leidinggevende verbindt mensen en '
                                                           'perspectieven op een manier die verandering relatief goed ondersteunt.',
                                            'very_high': 'Je beoordeling van je eigen leidinggevende behoort tot de hoogste 20% van de '
                                                         'benchmarkgroep. Je eigen leidinggevende wordt ervaren als een uitzonderlijk '
                                                         'sterke steun voor adaptiviteit. Richting, structuur, verbinding en '
                                                         'experimenteerruimte worden doordacht gecombineerd, waardoor mensen met '
                                                         'vertrouwen kunnen leren en veranderen.'},
        'Eigen leiderschap': {'unavailable': 'Voor deze dimensie zijn momenteel geen externe benchmarkgegevens beschikbaar.',
                              'very_low': 'Je zelfinschatting van je eigen leiderschap is laag. Je ervaart dat je in je leidinggevende rol '
                                          'nog relatief weinig consistente richting, structuur of ruimte voor leren biedt. Daardoor krijgt '
                                          'je team weinig houvast om verandering veilig en doelgericht vast te nemen.',
                              'rather_low': 'Je zelfinschatting van je eigen leiderschap is eerder laag. Je biedt je team op sommige '
                                            'momenten houvast, maar richting, verbinding en ruimte voor nieuwe aanpakken zijn nog '
                                            'wisselend. Je leiderschap ondersteunt adaptiviteit daardoor nog niet in elke situatie even '
                                            'sterk.',
                              'middle': 'Je zelfinschatting van je eigen leiderschap is gemiddeld. Je beoordeling van jezelf als '
                                        'leidinggevende ligt rond het gemiddelde van de benchmarkgroep. Je biedt als leidinggevende een '
                                        'bruikbare basis van richting, structuur en verbinding. In complexe of onzekere situaties kan je '
                                        'die ondersteuning nog consistenter en zichtbaarder maken.',
                              'rather_high': 'Je zelfinschatting van je eigen leiderschap is boven gemiddeld. Je biedt je team doorgaans '
                                             'duidelijke richting, werkbare structuur en ruimte om te leren. Je verbindt mensen en '
                                             'perspectieven op een manier die verandering relatief goed ondersteunt.',
                              'very_high': 'Je zelfinschatting van je eigen leiderschap is hoog. Je ziet je eigen leiderschap als een '
                                           'uitzonderlijk sterke steun voor adaptiviteit. Je combineert richting, structuur, verbinding en '
                                           'experimenteerruimte doordacht, waardoor je team met vertrouwen kan leren en veranderen.'},
        'Richting & steun van organisatie': {'unavailable': 'Voor deze dimensie zijn momenteel geen externe benchmarkgegevens beschikbaar.',
                                             'very_low': 'Je beoordeling van Richting & Steun van Organisatie ligt bij de laagste 20% van '
                                                         'de benchmarkgroep. Je ervaart relatief weinig duidelijke richting, kennis, '
                                                         'middelen of afstemming vanuit de organisatie. Daardoor kan verandering '
                                                         'versnipperd aanvoelen en wordt het moeilijk om goede intenties in uitvoerbaar '
                                                         'gedrag om te zetten.',
                                             'rather_low': 'Je beoordeling van Richting & Steun van Organisatie ligt onder het gemiddelde '
                                                           'van de benchmarkgroep. De organisatie biedt enkele vormen van steun, maar '
                                                           'richting, middelen en afstemming sluiten nog niet consequent op elkaar aan. '
                                                           'Dit vergroot de kans op onduidelijkheid of vertraging bij verandering.',
                                             'middle': 'Je beoordeling van Richting & Steun van Organisatie ligt rond het gemiddelde van '
                                                       'de benchmarkgroep. Je ervaart een werkbare basis van richting en ondersteuning. '
                                                       'Bij complexere veranderingen kan extra duidelijkheid, kennis, tijd of afstemming '
                                                       'nodig zijn om uitvoering en prioriteiten op één lijn te houden.',
                                             'rather_high': 'Je beoordeling van Richting & Steun van Organisatie ligt boven het gemiddelde '
                                                            'van de benchmarkgroep. Je ervaart doorgaans duidelijke richting, bruikbare '
                                                            'kennis, voldoende middelen en goede afstemming. Die samenhang helpt mensen en '
                                                            'teams om verandering doelgericht uit te voeren.',
                                             'very_high': 'Je beoordeling van Richting & Steun van Organisatie behoort tot de hoogste 20% '
                                                          'van de benchmarkgroep. De organisatie biedt volgens jou uitzonderlijk sterke en '
                                                          'samenhangende steun voor verandering. Richting, kennis, middelen en alignment '
                                                          'versterken elkaar en maken snelle, duurzame aanpassing mogelijk.'},
        'Organisatieadaptiviteit': {'unavailable': 'Voor deze dimensie zijn momenteel geen externe benchmarkgegevens beschikbaar.',
                                    'very_low': 'Je beoordeling van Organisatieadaptiviteit ligt bij de laagste 20% van de benchmarkgroep. '
                                                'Je ervaart dat de organisatie signalen en veranderingen relatief laat oppikt of beperkt '
                                                'vertaalt naar concrete verbetering. Daardoor blijven kansen of risico’s langer liggen en '
                                                'verloopt verbetering vooral reactief.',
                                    'rather_low': 'Je beoordeling van Organisatieadaptiviteit ligt onder het gemiddelde van de '
                                                  'benchmarkgroep. De organisatie reageert op duidelijke veranderingen, maar het vroeg '
                                                  'herkennen, opvolgen en vertalen naar verbetering is nog niet consequent. Leren uit '
                                                  'signalen gebeurt daardoor eerder lokaal of incidenteel.',
                                    'middle': 'Je beoordeling van Organisatieadaptiviteit ligt rond het gemiddelde van de benchmarkgroep. '
                                              'De organisatie beschikt over een werkbaar vermogen om veranderingen op te volgen en bij te '
                                              'sturen. De snelheid en doorwerking verschillen nog naargelang onderwerp, afdeling of '
                                              'urgentie.',
                                    'rather_high': 'Je beoordeling van Organisatieadaptiviteit ligt boven het gemiddelde van de '
                                                   'benchmarkgroep. Je ervaart dat de organisatie veranderingen meestal tijdig herkent, '
                                                   'opvolgt en omzet in concrete verbetering. Dat ondersteunt een proactieve en '
                                                   'samenhangende manier van aanpassen.',
                                    'very_high': 'Je beoordeling van Organisatieadaptiviteit behoort tot de hoogste 20% van de '
                                                 'benchmarkgroep. De organisatie wordt ervaren als uitzonderlijk adaptief. Ze detecteert '
                                                 'signalen vroeg, verbindt inzichten snel aan besluiten en verankert verbeteringen breed '
                                                 'in de werking.'},
        'Organisatieklimaat': {'unavailable': 'Voor deze dimensie zijn momenteel geen externe benchmarkgegevens beschikbaar.',
                               'very_low': 'Je beoordeling van Organisatieklimaat ligt bij de laagste 20% van de benchmarkgroep. Je '
                                           'ervaart relatief weinig ruimte om te experimenteren, ideeën te delen of uit fouten te leren. '
                                           'Daardoor krijgen vernieuwing en open kennisuitwisseling weinig voedingsbodem.',
                               'rather_low': 'Je beoordeling van Organisatieklimaat ligt onder het gemiddelde van de benchmarkgroep. Er '
                                             'zijn voorbeelden van leren en innovatie, maar de ruimte ervoor is nog wisselend of '
                                             'afhankelijk van lokale initiatiefnemers. Voorzichtigheid en bestaande gewoonten krijgen vaak '
                                             'voorrang.',
                               'middle': 'Je beoordeling van Organisatieklimaat ligt rond het gemiddelde van de benchmarkgroep. Het '
                                         'organisatieklimaat biedt een bruikbare basis voor leren, ideeën delen en experimenteren. De '
                                         'ervaren ruimte verschilt nog per team, thema of moment.',
                               'rather_high': 'Je beoordeling van Organisatieklimaat ligt boven het gemiddelde van de benchmarkgroep. Je '
                                              'ervaart dat leren, innovatie en het delen van ideeën doorgaans worden aangemoedigd. Dit '
                                              'klimaat maakt het makkelijker om verbeteringen te testen en kennis breder te benutten.',
                               'very_high': 'Je beoordeling van Organisatieklimaat behoort tot de hoogste 20% van de benchmarkgroep. De '
                                            'organisatie kent volgens jou een uitzonderlijk sterk leer- en innovatieklimaat. '
                                            'Experimenteren is veilig, inzichten worden breed gedeeld en nieuwe ideeën krijgen zichtbaar '
                                            'ruimte om uit te groeien.'},
        'HR': {'unavailable': 'Voor deze dimensie zijn momenteel geen externe benchmarkgegevens beschikbaar.',
               'very_low': 'Je beoordeling van HR-beleid ligt bij de laagste 20% van de benchmarkgroep. Je ervaart dat selectie, '
                           'ontwikkeling, evaluatie en waardering adaptief gedrag relatief weinig ondersteunen. Wat van mensen wordt '
                           'gevraagd en wat HR-systemen stimuleren, sluit daardoor onvoldoende op elkaar aan.',
               'rather_low': 'Je beoordeling van HR-beleid ligt onder het gemiddelde van de benchmarkgroep. Sommige HR-praktijken '
                             'ondersteunen leren en aanpassen, maar het geheel is nog niet consistent. Ontwikkeling, feedback of '
                             'waardering maken adaptief gedrag daardoor niet altijd zichtbaar aantrekkelijk.',
               'middle': 'Je beoordeling van HR-beleid ligt rond het gemiddelde van de benchmarkgroep. Het HR-beleid biedt een werkbare '
                         'basis om adaptiviteit te ondersteunen. De samenhang tussen selectie, ontwikkeling, evaluatie en waardering kan '
                         'nog duidelijker en consequenter worden ervaren.',
               'rather_high': 'Je beoordeling van HR-beleid ligt boven het gemiddelde van de benchmarkgroep. Je ervaart dat HR-praktijken '
                              'leren, ontwikkeling en flexibel gedrag doorgaans goed ondersteunen. Medewerkers krijgen relatief duidelijke '
                              'signalen en kansen om zich aan te passen en te groeien.',
               'very_high': 'Je beoordeling van HR-beleid behoort tot de hoogste 20% van de benchmarkgroep. Het HR-beleid wordt ervaren '
                            'als uitzonderlijk sterk afgestemd op adaptiviteit. Selectie, ontwikkeling, evaluatie en waardering versterken '
                            'elkaar en maken leren en veranderen zichtbaar onderdeel van goed werk.'}},
 'fr': {'Capaciteit': {'unavailable': 'Aucune donnée de référence externe n’est actuellement disponible pour cette dimension.',
                       'very_low': 'Votre score pour Capacité se situe parmi les 20 % les plus bas du groupe de référence. Vous disposez '
                                   'actuellement de relativement peu de repères pour adapter efficacement votre approche. La confiance '
                                   'dans votre influence, le traitement de l’information ou la perception de l’importance peuvent limiter '
                                   'votre capacité à changer.',
                       'rather_low': 'Votre score pour Capacité se situe sous la moyenne du groupe de référence. Vous disposez de points '
                                     'd’appui utiles, mais ne vous sentez pas suffisamment équipé dans chaque situation. La complexité ou '
                                     'l’ambiguïté peuvent rapidement réduire votre confiance et votre marge d’action.',
                       'middle': 'Votre score pour Capacité se situe autour de la moyenne du groupe de référence. Vous disposez '
                                 'généralement de suffisamment de compréhension, de compétences et de confiance pour vous adapter. Une '
                                 'préparation ou un soutien supplémentaire peut aider à utiliser cette base plus systématiquement.',
                       'rather_high': 'Votre score pour Capacité se situe au-dessus de la moyenne du groupe de référence. Vous vous sentez '
                                      'généralement capable de traiter l’information, d’établir des liens et d’ajuster votre approche. '
                                      'Cela constitue une base personnelle solide pour prendre le changement en main.',
                       'very_high': 'Votre score pour Capacité se situe parmi les 20 % les plus élevés du groupe de référence. Votre '
                                    'capacité à faire face au changement est exceptionnellement développée. Vous combinez compréhension, '
                                    'compétence et confiance, ce qui vous permet de vous adapter dans les situations complexes et d’aider '
                                    'les autres.'},
        'Motivatie': {'unavailable': 'Aucune donnée de référence externe n’est actuellement disponible pour cette dimension.',
                      'very_low': 'Votre score pour Motivation se situe parmi les 20 % les plus bas du groupe de référence. Le changement '
                                  'génère actuellement relativement peu d’énergie ou de persévérance. Votre engagement ou motivation '
                                  'interne offre donc peu de soutien lorsque l’adaptation demande des efforts et comporte de '
                                  'l’incertitude.',
                      'rather_low': 'Votre score pour Motivation se situe sous la moyenne du groupe de référence. Vous êtes disposé à '
                                    'avancer lorsque la nécessité est claire, mais votre énergie et votre persévérance ne sont pas '
                                    'toujours stables. Votre motivation peut diminuer lors de changements longs ou incertains.',
                      'middle': 'Votre score pour Motivation se situe autour de la moyenne du groupe de référence. Votre motivation offre '
                                'généralement une base suffisante pour agir face au changement. La continuité de votre engagement dépend '
                                'notamment du sens, de la faisabilité et de progrès visibles.',
                      'rather_high': 'Votre score pour Motivation se situe au-dessus de la moyenne du groupe de référence. Vous tirez '
                                     'généralement de l’énergie de l’apprentissage et de l’amélioration et restez engagé dans les '
                                     'difficultés. Cette motivation vous aide à commencer et à poursuivre le changement.',
                      'very_high': 'Votre score pour Motivation se situe parmi les 20 % les plus élevés du groupe de référence. Votre '
                                   'motivation pour l’adaptation et le développement est exceptionnellement forte. Vous combinez '
                                   'motivation interne, engagement et persévérance et pouvez renforcer l’énergie et la confiance des '
                                   'autres.'},
        'Job Karakteristieken': {'unavailable': 'Aucune donnée de référence externe n’est actuellement disponible pour cette dimension.',
                                 'very_low': 'Votre évaluation de Caractéristiques du travail se situe parmi les 20 % les plus bas du '
                                             'groupe de référence. Vous vivez relativement peu de conditions de travail qui soutiennent '
                                             'l’adaptation, l’apprentissage et l’initiative. L’ambiguïté, une autonomie limitée, les '
                                             'dépendances ou le manque de défi significatif peuvent clairement freiner vos efforts.',
                                 'rather_low': 'Votre évaluation de Caractéristiques du travail se situe sous la moyenne du groupe de '
                                               'référence. Votre travail offre certaines conditions utiles à l’action adaptative, mais '
                                               'elles ne sont pas encore stables ou équilibrées. Certaines caractéristiques rendent '
                                               'l’ajustement autonome et rapide plus difficile.',
                                 'middle': 'Votre évaluation de Caractéristiques du travail se situe autour de la moyenne du groupe de '
                                           'référence. Votre travail offre généralement une base fonctionnelle pour vous adapter. '
                                           'Certaines caractéristiques donnent de l’espace et de la clarté, tandis que d’autres peuvent '
                                           'encore créer retard, incertitude ou dépendance.',
                                 'rather_high': 'Votre évaluation de Caractéristiques du travail se situe au-dessus de la moyenne du '
                                                'groupe de référence. Vous vivez généralement votre travail comme clair, porteur de sens '
                                                'et suffisamment autonome pour agir avec flexibilité. Ses caractéristiques soutiennent '
                                                'relativement bien l’apprentissage et l’ajustement.',
                                 'very_high': 'Votre évaluation de Caractéristiques du travail se situe parmi les 20 % les plus élevés du '
                                              'groupe de référence. Votre travail offre des conditions exceptionnellement favorables au '
                                              'comportement adaptatif. Clarté, sens, autonomie et dépendances maîtrisables se renforcent '
                                              'et facilitent l’apprentissage rapide et l’ajustement ciblé.'},
        'Teamadaptiviteit': {'unavailable': 'Aucune donnée de référence externe n’est actuellement disponible pour cette dimension.',
                             'very_low': 'Votre évaluation de Adaptabilité de l’équipe se situe parmi les 20 % les plus bas du groupe de '
                                         'référence. Vous avez le sentiment que votre équipe gère le changement relativement '
                                         'difficilement. L’apprentissage commun, l’alignement flexible et l’ajustement des méthodes sont '
                                         'rares, laissant l’adaptation reposer sur les efforts individuels.',
                             'rather_low': 'Votre évaluation de Adaptabilité de l’équipe se situe sous la moyenne du groupe de référence. '
                                           'Votre équipe peut s’adapter dans des situations familières, mais l’apprentissage collectif et '
                                           'l’ajustement rapide manquent de constance. Les changements inattendus créent donc plus vite '
                                           'retard ou fragmentation.',
                             'middle': 'Votre évaluation de Adaptabilité de l’équipe se situe autour de la moyenne du groupe de référence. '
                                       'Votre équipe dispose d’une base fonctionnelle pour réagir ensemble et ajuster son approche. La '
                                       'fluidité dépend encore de la situation, des collègues concernés et de l’espace disponible.',
                             'rather_high': 'Votre évaluation de Adaptabilité de l’équipe se situe au-dessus de la moyenne du groupe de '
                                            'référence. Vous avez le sentiment que votre équipe réagit généralement avec flexibilité, '
                                            'partage ses connaissances et améliore collectivement ses méthodes. Cela rend le changement '
                                            'plus gérable et soutient l’adaptabilité individuelle.',
                             'very_high': 'Votre évaluation de Adaptabilité de l’équipe se situe parmi les 20 % les plus élevés du groupe '
                                          'de référence. Votre équipe est perçue comme exceptionnellement adaptative. Elle repère '
                                          'rapidement les signaux, apprend collectivement et ajuste ses méthodes de manière ciblée, tout '
                                          'en restant efficace dans l’incertitude.'},
        'Teamklimaat': {'unavailable': 'Aucune donnée de référence externe n’est actuellement disponible pour cette dimension.',
                        'very_low': 'Votre évaluation de Climat d’équipe se situe parmi les 20 % les plus bas du groupe de référence. Vous '
                                    'vivez relativement peu d’ouverture, de confiance ou de sécurité psychologique dans l’équipe. Il '
                                    'devient donc plus difficile de partager les doutes, discuter les erreurs et tester de nouvelles '
                                    'idées.',
                        'rather_low': 'Votre évaluation de Climat d’équipe se situe sous la moyenne du groupe de référence. Il existe des '
                                      'points d’appui pour collaborer, mais la communication ouverte et la sécurité restent variables. Les '
                                      'personnes peuvent hésiter sur ce qu’elles partagent, ce qui ralentit l’apprentissage et '
                                      'l’ajustement collectifs.',
                        'middle': 'Votre évaluation de Climat d’équipe se situe autour de la moyenne du groupe de référence. Le climat '
                                  'd’équipe offre généralement une base suffisante pour collaborer et dialoguer. Les situations sensibles '
                                  'ou incertaines demandent une attention supplémentaire pour préserver ouverture, confiance et '
                                  'alignement.',
                        'rather_high': 'Votre évaluation de Climat d’équipe se situe au-dessus de la moyenne du groupe de référence. Vous '
                                       'vivez généralement une communication ouverte, de la confiance et l’espace nécessaire pour discuter '
                                       'des questions ou erreurs. Ce climat soutient la collaboration, l’apprentissage et l’ajustement '
                                       'rapide.',
                        'very_high': 'Votre évaluation de Climat d’équipe se situe parmi les 20 % les plus élevés du groupe de référence. '
                                     'Votre climat d’équipe est perçu comme exceptionnellement sûr et rassembleur. Les personnes partagent '
                                     'librement informations et idées, abordent les tensions et utilisent les différences pour apprendre '
                                     'plus vite ensemble.'},
        'Richting & steun leidinggevende': {'unavailable': 'Aucune donnée de référence externe n’est actuellement disponible pour cette '
                                                           'dimension.',
                                            'very_low': 'Votre évaluation de votre propre responsable se situe parmi les 20 % les plus bas '
                                                        'du groupe de référence. Vous recevez relativement peu de direction, de structure '
                                                        'ou d’espace d’apprentissage et d’expérimentation de votre propre responsable. Un '
                                                        'soutien quotidien important au changement sûr et ciblé fait donc défaut.',
                                            'rather_low': 'Votre évaluation de votre propre responsable se situe sous la moyenne du groupe '
                                                          'de référence. Votre propre responsable offre parfois des repères, mais la '
                                                          'direction, la connexion et l’espace pour de nouvelles approches restent '
                                                          'variables. Il est donc plus difficile d’expérimenter et d’ajuster avec '
                                                          'confiance.',
                                            'middle': 'Votre évaluation de votre propre responsable se situe autour de la moyenne du '
                                                      'groupe de référence. Votre propre responsable offre une base fonctionnelle de '
                                                      'direction, de structure et de connexion. Ce soutien pourrait devenir plus constant '
                                                      'et visible dans les situations complexes ou incertaines.',
                                            'rather_high': 'Votre évaluation de votre propre responsable se situe au-dessus de la moyenne '
                                                           'du groupe de référence. Vous vivez généralement une direction claire, une '
                                                           'structure fonctionnelle et de l’espace pour apprendre. Votre propre '
                                                           'responsable relie personnes et perspectives d’une manière qui soutient '
                                                           'relativement bien le changement.',
                                            'very_high': 'Votre évaluation de votre propre responsable se situe parmi les 20 % les plus '
                                                         'élevés du groupe de référence. Votre propre responsable est perçu comme un '
                                                         'soutien exceptionnellement fort à l’adaptabilité. Direction, structure, '
                                                         'connexion et expérimentation sont combinées avec soin, permettant d’apprendre et '
                                                         'de changer avec confiance.'},
        'Eigen leiderschap': {'unavailable': 'Aucune interprétation n’est actuellement disponible pour votre propre leadership.',
                              'very_low': 'Votre auto-évaluation de votre propre leadership est faible. Vous estimez offrir encore '
                                          'relativement peu de direction cohérente, de structure ou d’espace d’apprentissage dans votre '
                                          'rôle de responsable. Votre équipe dispose ainsi de peu de repères pour aborder le changement de '
                                          'manière sûre et ciblée.',
                              'rather_low': 'Votre auto-évaluation de votre propre leadership est plutôt faible. Vous offrez parfois des '
                                            'repères à votre équipe, mais la direction, le lien et l’espace pour de nouvelles approches '
                                            'restent variables. Votre leadership ne soutient donc pas encore l’adaptabilité avec la même '
                                            'force dans toutes les situations.',
                              'middle': 'Votre auto-évaluation de votre propre leadership se situe dans la moyenne. En tant que '
                                        'responsable, vous offrez une base fonctionnelle de direction, de structure et de connexion. Dans '
                                        'les situations complexes ou incertaines, vous pouvez encore rendre ce soutien plus constant et '
                                        'plus visible.',
                              'rather_high': 'Votre auto-évaluation de votre propre leadership est supérieure à la moyenne. Vous offrez '
                                             'généralement à votre équipe une direction claire, une structure fonctionnelle et de l’espace '
                                             'pour apprendre. Vous reliez les personnes et les perspectives d’une manière qui soutient '
                                             'relativement bien le changement.',
                              'very_high': 'Votre auto-évaluation de votre propre leadership est élevée. Vous considérez votre leadership '
                                           'comme un soutien exceptionnellement fort à l’adaptabilité. Vous combinez avec discernement '
                                           'direction, structure, connexion et espace d’expérimentation, ce qui permet à votre équipe '
                                           'd’apprendre et de changer avec confiance.'},
        'Richting & steun van organisatie': {'unavailable': 'Aucune donnée de référence externe n’est actuellement disponible pour cette '
                                                            'dimension.',
                                             'very_low': 'Votre évaluation de Orientation et soutien de l’organisation se situe parmi les '
                                                         '20 % les plus bas du groupe de référence. Vous vivez relativement peu de '
                                                         'direction claire, de connaissances, de moyens ou d’alignement de la part de '
                                                         'l’organisation. Le changement peut donc sembler fragmenté et les bonnes '
                                                         'intentions sont plus difficiles à traduire en comportement réalisable.',
                                             'rather_low': 'Votre évaluation de Orientation et soutien de l’organisation se situe sous la '
                                                           'moyenne du groupe de référence. L’organisation offre certaines formes de '
                                                           'soutien, mais direction, moyens et alignement ne sont pas reliés de manière '
                                                           'cohérente. Cela accroît le risque d’ambiguïté ou de retard lors du changement.',
                                             'middle': 'Votre évaluation de Orientation et soutien de l’organisation se situe autour de la '
                                                       'moyenne du groupe de référence. Vous vivez une base fonctionnelle de direction et '
                                                       'de soutien. Les changements complexes peuvent nécessiter davantage de clarté, de '
                                                       'connaissances, de temps ou d’alignement pour relier mise en œuvre et priorités.',
                                             'rather_high': 'Votre évaluation de Orientation et soutien de l’organisation se situe '
                                                            'au-dessus de la moyenne du groupe de référence. Vous vivez généralement une '
                                                            'direction claire, des connaissances utiles, des moyens suffisants et un bon '
                                                            'alignement. Cette cohérence aide les personnes et les équipes à mettre le '
                                                            'changement en œuvre de manière ciblée.',
                                             'very_high': 'Votre évaluation de Orientation et soutien de l’organisation se situe parmi les '
                                                          '20 % les plus élevés du groupe de référence. Selon vous, l’organisation offre '
                                                          'un soutien exceptionnellement fort et cohérent au changement. Direction, '
                                                          'connaissances, moyens et alignement se renforcent et permettent une adaptation '
                                                          'rapide et durable.'},
        'Organisatieadaptiviteit': {'unavailable': 'Aucune donnée de référence externe n’est actuellement disponible pour cette dimension.',
                                    'very_low': 'Votre évaluation de Adaptabilité organisationnelle se situe parmi les 20 % les plus bas '
                                                'du groupe de référence. Vous avez le sentiment que l’organisation repère relativement '
                                                'tard les signaux et changements ou les traduit peu en action. Les occasions ou risques '
                                                'restent donc plus longtemps sans réponse et l’amélioration est surtout réactive.',
                                    'rather_low': 'Votre évaluation de Adaptabilité organisationnelle se situe sous la moyenne du groupe '
                                                  'de référence. L’organisation réagit aux changements clairs, mais leur détection '
                                                  'précoce, leur suivi et leur traduction en amélioration manquent de constance. '
                                                  'L’apprentissage à partir des signaux reste donc local ou ponctuel.',
                                    'middle': 'Votre évaluation de Adaptabilité organisationnelle se situe autour de la moyenne du groupe '
                                              'de référence. L’organisation dispose d’une capacité fonctionnelle à suivre les changements '
                                              'et à s’ajuster. La vitesse et l’impact varient encore selon le sujet, le département ou '
                                              'l’urgence.',
                                    'rather_high': 'Votre évaluation de Adaptabilité organisationnelle se situe au-dessus de la moyenne du '
                                                   'groupe de référence. Vous avez le sentiment que l’organisation reconnaît généralement '
                                                   'les changements à temps, les suit et les transforme en amélioration concrète. Cela '
                                                   'soutient une adaptation proactive et cohérente.',
                                    'very_high': 'Votre évaluation de Adaptabilité organisationnelle se situe parmi les 20 % les plus '
                                                 'élevés du groupe de référence. L’organisation est perçue comme exceptionnellement '
                                                 'adaptative. Elle détecte tôt les signaux, relie rapidement les enseignements aux '
                                                 'décisions et ancre largement les améliorations.'},
        'Organisatieklimaat': {'unavailable': 'Aucune donnée de référence externe n’est actuellement disponible pour cette dimension.',
                               'very_low': 'Votre évaluation de Climat organisationnel se situe parmi les 20 % les plus bas du groupe de '
                                           'référence. Vous vivez relativement peu d’espace pour expérimenter, partager des idées ou '
                                           'apprendre des erreurs. Le renouvellement et l’échange ouvert de connaissances disposent donc '
                                           'de peu de terrain.',
                               'rather_low': 'Votre évaluation de Climat organisationnel se situe sous la moyenne du groupe de référence. '
                                             'Il existe des exemples d’apprentissage et d’innovation, mais l’espace reste variable ou '
                                             'dépend d’initiatives locales. La prudence et les habitudes existantes restent souvent '
                                             'prioritaires.',
                               'middle': 'Votre évaluation de Climat organisationnel se situe autour de la moyenne du groupe de référence. '
                                         'Le climat organisationnel offre une base fonctionnelle pour apprendre, partager des idées et '
                                         'expérimenter. L’espace vécu varie encore selon l’équipe, le thème ou le moment.',
                               'rather_high': 'Votre évaluation de Climat organisationnel se situe au-dessus de la moyenne du groupe de '
                                              'référence. Vous avez le sentiment que l’apprentissage, l’innovation et le partage d’idées '
                                              'sont généralement encouragés. Ce climat facilite le test d’améliorations et l’utilisation '
                                              'plus large des connaissances.',
                               'very_high': 'Votre évaluation de Climat organisationnel se situe parmi les 20 % les plus élevés du groupe '
                                            'de référence. Selon vous, l’organisation possède un climat d’apprentissage et d’innovation '
                                            'exceptionnellement fort. L’expérimentation est sûre, les enseignements sont largement '
                                            'partagés et les nouvelles idées ont un espace visible pour grandir.'},
        'HR': {'unavailable': 'Aucune donnée de référence externe n’est actuellement disponible pour cette dimension.',
               'very_low': 'Votre évaluation de Politique RH se situe parmi les 20 % les plus bas du groupe de référence. Vous avez le '
                           'sentiment que la sélection, le développement, l’évaluation et la reconnaissance soutiennent relativement peu '
                           'le comportement adaptatif. Les attentes et les systèmes RH sont donc insuffisamment alignés.',
               'rather_low': 'Votre évaluation de Politique RH se situe sous la moyenne du groupe de référence. Certaines pratiques RH '
                             'soutiennent l’apprentissage et l’adaptation, mais l’ensemble manque encore de cohérence. Développement, '
                             'feedback ou reconnaissance ne rendent pas toujours le comportement adaptatif visiblement attractif.',
               'middle': 'Votre évaluation de Politique RH se situe autour de la moyenne du groupe de référence. La politique RH offre une '
                         'base fonctionnelle pour soutenir l’adaptabilité. Le lien entre sélection, développement, évaluation et '
                         'reconnaissance pourrait être vécu de manière plus claire et cohérente.',
               'rather_high': 'Votre évaluation de Politique RH se situe au-dessus de la moyenne du groupe de référence. Vous avez le '
                              'sentiment que les pratiques RH soutiennent généralement bien l’apprentissage, le développement et la '
                              'flexibilité. Les collaborateurs reçoivent des signaux et des occasions relativement clairs pour s’adapter '
                              'et progresser.',
               'very_high': 'Votre évaluation de Politique RH se situe parmi les 20 % les plus élevés du groupe de référence. La politique '
                            'RH est perçue comme exceptionnellement bien alignée sur l’adaptabilité. Sélection, développement, évaluation '
                            'et reconnaissance se renforcent et rendent l’apprentissage et le changement visibles dans le bon travail.'}},
 'en': {'Capaciteit': {'unavailable': 'External benchmark data is currently unavailable for this dimension.',
                       'very_low': 'Your score for Capability is in the bottom 20% of the benchmark group. You currently experience '
                                   'relatively little support in adapting your approach effectively. Confidence in your influence, '
                                   'information processing or recognising importance may limit your ability to switch.',
                       'rather_low': 'Your score for Capability is below the benchmark group average. You have useful starting points but '
                                     'do not feel sufficiently equipped in every situation. Complexity or ambiguity can quickly reduce '
                                     'confidence and room for action.',
                       'middle': 'Your score for Capability is around the benchmark group average. You generally have sufficient insight, '
                                 'skills and confidence to adapt. Extra preparation or support can help use this foundation more '
                                 'consistently in new or complex situations.',
                       'rather_high': 'Your score for Capability is above the benchmark group average. You usually feel capable of '
                                      'processing information, seeing connections and adjusting your approach. This provides a solid '
                                      'personal foundation for taking ownership of change.',
                       'very_high': 'Your score for Capability is in the top 20% of the benchmark group. Your capability for dealing with '
                                    'change is exceptionally well developed. You combine insight, skill and confidence, enabling '
                                    'purposeful adjustment in complex situations and support for others.'},
        'Motivatie': {'unavailable': 'External benchmark data is currently unavailable for this dimension.',
                      'very_low': 'Your score for Motivation is in the bottom 20% of the benchmark group. Change currently generates '
                                  'relatively little energy or perseverance. Engagement or inner drive therefore provides limited support '
                                  'when adaptation requires effort and uncertainty.',
                      'rather_low': 'Your score for Motivation is below the benchmark group average. You are willing to move when the need '
                                    'is clear, but energy and perseverance are not always stable. Motivation may decline during prolonged '
                                    'or uncertain change.',
                      'middle': 'Your score for Motivation is around the benchmark group average. Your motivation generally provides a '
                                'sufficient basis for engaging with change. Sustained involvement depends partly on meaning, feasibility '
                                'and visible progress.',
                      'rather_high': 'Your score for Motivation is above the benchmark group average. You usually gain energy from '
                                     'learning and improvement and remain involved when things are difficult. This helps you both start '
                                     'and sustain change.',
                      'very_high': 'Your score for Motivation is in the top 20% of the benchmark group. Your motivation for adaptation and '
                                   'development is exceptionally strong. You combine inner drive, engagement and perseverance and can '
                                   'strengthen others’ energy and belief in change.'},
        'Job Karakteristieken': {'unavailable': 'External benchmark data is currently unavailable for this dimension.',
                                 'very_low': 'Your assessment of Job Characteristics is in the bottom 20% of the benchmark group. You '
                                             'experience relatively few job conditions that support adaptation, learning and initiative. '
                                             'Ambiguity, limited autonomy, dependencies or insufficient meaningful challenge may clearly '
                                             'slow your efforts.',
                                 'rather_low': 'Your assessment of Job Characteristics is below the benchmark group average. Your job '
                                               'offers some useful conditions for adaptive action, but they are not yet stable or '
                                               'balanced. Certain task features make independent and timely adjustment harder.',
                                 'middle': 'Your assessment of Job Characteristics is around the benchmark group average. Your job '
                                           'generally offers a workable basis for adaptation. Some features provide space and clarity, '
                                           'while others may still create delays, uncertainty or dependencies in specific situations.',
                                 'rather_high': 'Your assessment of Job Characteristics is above the benchmark group average. You '
                                                'generally experience your job as clear, meaningful and sufficiently autonomous for '
                                                'flexible action. Its characteristics support learning and adjustment relatively strongly.',
                                 'very_high': 'Your assessment of Job Characteristics is in the top 20% of the benchmark group. Your job '
                                              'offers exceptionally favourable conditions for adaptive behaviour. Clarity, meaning, '
                                              'autonomy and workable dependencies reinforce one another and support rapid learning and '
                                              'purposeful adjustment.'},
        'Teamadaptiviteit': {'unavailable': 'External benchmark data is currently unavailable for this dimension.',
                             'very_low': 'Your assessment of Team Adaptability is in the bottom 20% of the benchmark group. You experience '
                                         'that your team finds change relatively difficult. Joint learning, flexible alignment and '
                                         'adjusting working methods occur infrequently, leaving adaptation heavily dependent on individual '
                                         'effort.',
                             'rather_low': 'Your assessment of Team Adaptability is below the benchmark group average. Your team can adapt '
                                           'in familiar situations, but collective learning and timely adjustment are not consistent. '
                                           'Unexpected change therefore creates delay or fragmentation more quickly.',
                             'middle': 'Your assessment of Team Adaptability is around the benchmark group average. Your team has a '
                                       'workable basis for responding together and adjusting its approach. How smoothly this happens still '
                                       'depends on the situation, colleagues involved and available space.',
                             'rather_high': 'Your assessment of Team Adaptability is above the benchmark group average. You experience '
                                            'that your team generally responds flexibly, shares knowledge and improves ways of working '
                                            'together. This makes change more manageable and supports individual adaptability.',
                             'very_high': 'Your assessment of Team Adaptability is in the top 20% of the benchmark group. Your team is '
                                          'experienced as exceptionally adaptive. It detects signals quickly, learns collectively and '
                                          'purposefully adjusts working methods, remaining effective under uncertainty.'},
        'Teamklimaat': {'unavailable': 'External benchmark data is currently unavailable for this dimension.',
                        'very_low': 'Your assessment of Team Climate is in the bottom 20% of the benchmark group. You experience '
                                    'relatively little openness, trust or psychological safety in the team. This makes sharing doubts, '
                                    'discussing mistakes and testing new ideas more difficult.',
                        'rather_low': 'Your assessment of Team Climate is below the benchmark group average. There are starting points for '
                                      'collaboration, but open communication and safety remain inconsistent. People may weigh what to '
                                      'share, slowing joint learning and adjustment.',
                        'middle': 'Your assessment of Team Climate is around the benchmark group average. The team climate generally '
                                  'provides a sufficient basis for collaboration and dialogue. Sensitive or uncertain situations require '
                                  'extra attention to preserve openness, trust and clear alignment.',
                        'rather_high': 'Your assessment of Team Climate is above the benchmark group average. You generally experience '
                                       'open communication, trust and room to discuss questions or mistakes. This climate supports '
                                       'collaboration, learning and timely adjustment.',
                        'very_high': 'Your assessment of Team Climate is in the top 20% of the benchmark group. Your team climate is '
                                     'experienced as exceptionally safe and connecting. People freely share information and ideas, address '
                                     'tensions and use differences to learn faster together.'},
        'Richting & steun leidinggevende': {'unavailable': 'External benchmark data is currently unavailable for this dimension.',
                                            'very_low': 'Your assessment of your own manager is in the bottom 20% of the benchmark group. '
                                                        'You experience relatively little direction, structure or room for learning and '
                                                        'experimentation from your own manager. Important day-to-day support for safe, '
                                                        'purposeful change is therefore missing.',
                                            'rather_low': 'Your assessment of your own manager is below the benchmark group average. Your '
                                                          'own manager provides support at times, but direction, connection and space for '
                                                          'new approaches are inconsistent. This makes confident experimentation and '
                                                          'adjustment more difficult.',
                                            'middle': 'Your assessment of your own manager is around the benchmark group average. Your own '
                                                      'manager provides a workable foundation of direction, structure and connection. '
                                                      'Support could become more consistent and visible in complex or uncertain '
                                                      'situations.',
                                            'rather_high': 'Your assessment of your own manager is above the benchmark group average. You '
                                                           'generally experience clear direction, workable structure and room to learn. '
                                                           'Your own manager connects people and perspectives in a way that supports '
                                                           'change relatively well.',
                                            'very_high': 'Your assessment of your own manager is in the top 20% of the benchmark group. '
                                                         'Your own manager is experienced as exceptionally strong support for '
                                                         'adaptability. Direction, structure, connection and room to experiment are '
                                                         'combined thoughtfully, enabling confident learning and change.'},
        'Eigen leiderschap': {'unavailable': 'No interpretation is currently available for your own leadership.',
                              'very_low': 'Your self-assessment of your own leadership is low. You feel that, in your management role, you '
                                          'currently provide relatively little consistent direction, structure or room for learning. Your '
                                          'team therefore has limited guidance for approaching change safely and purposefully.',
                              'rather_low': 'Your self-assessment of your own leadership is rather low. You provide your team with '
                                            'guidance at some moments, but direction, connection and room for new approaches remain '
                                            'inconsistent. Your leadership therefore does not yet support adaptability equally strongly in '
                                            'every situation.',
                              'middle': 'Your self-assessment of your own leadership is average. As a manager, you provide a workable '
                                        'basis of direction, structure and connection. In complex or uncertain situations, you can make '
                                        'this support more consistent and visible.',
                              'rather_high': 'Your self-assessment of your own leadership is above average. You generally provide your '
                                             'team with clear direction, workable structure and room to learn. You connect people and '
                                             'perspectives in a way that supports change relatively well.',
                              'very_high': 'Your self-assessment of your own leadership is high. You see your leadership as exceptionally '
                                           'strong support for adaptability. You thoughtfully combine direction, structure, connection and '
                                           'room for experimentation, enabling your team to learn and change with confidence.'},
        'Richting & steun van organisatie': {'unavailable': 'External benchmark data is currently unavailable for this dimension.',
                                             'very_low': 'Your assessment of Organisation Direction & Support is in the bottom 20% of the '
                                                         'benchmark group. You experience relatively little clear direction, knowledge, '
                                                         'resources or alignment from the organisation. Change may therefore feel '
                                                         'fragmented and good intentions are harder to turn into executable behaviour.',
                                             'rather_low': 'Your assessment of Organisation Direction & Support is below the benchmark '
                                                           'group average. The organisation offers some support, but direction, resources '
                                                           'and alignment are not consistently connected. This increases ambiguity or '
                                                           'delay during change.',
                                             'middle': 'Your assessment of Organisation Direction & Support is around the benchmark group '
                                                       'average. You experience a workable foundation of direction and support. More '
                                                       'clarity, knowledge, time or alignment may be needed to keep execution and '
                                                       'priorities connected in complex change.',
                                             'rather_high': 'Your assessment of Organisation Direction & Support is above the benchmark '
                                                            'group average. You generally experience clear direction, useful knowledge, '
                                                            'sufficient resources and good alignment. This coherence helps people and '
                                                            'teams implement change purposefully.',
                                             'very_high': 'Your assessment of Organisation Direction & Support is in the top 20% of the '
                                                          'benchmark group. In your view, the organisation offers exceptionally strong and '
                                                          'coherent support for change. Direction, knowledge, resources and alignment '
                                                          'reinforce one another and enable rapid, sustainable adaptation.'},
        'Organisatieadaptiviteit': {'unavailable': 'External benchmark data is currently unavailable for this dimension.',
                                    'very_low': 'Your assessment of Organisation Adaptability is in the bottom 20% of the benchmark group. '
                                                'You experience that the organisation detects signals and changes relatively late or '
                                                'converts them into limited action. Opportunities or risks remain unresolved longer and '
                                                'improvement is mainly reactive.',
                                    'rather_low': 'Your assessment of Organisation Adaptability is below the benchmark group average. The '
                                                  'organisation responds to clear changes, but early detection, follow-up and translation '
                                                  'into improvement are inconsistent. Learning from signals is therefore local or '
                                                  'incidental.',
                                    'middle': 'Your assessment of Organisation Adaptability is around the benchmark group average. The '
                                              'organisation has a workable capacity to follow up change and adjust. Speed and impact still '
                                              'vary by topic, department or urgency.',
                                    'rather_high': 'Your assessment of Organisation Adaptability is above the benchmark group average. You '
                                                   'experience that the organisation generally recognises changes in time, follows them up '
                                                   'and turns them into concrete improvement. This supports proactive, coherent '
                                                   'adaptation.',
                                    'very_high': 'Your assessment of Organisation Adaptability is in the top 20% of the benchmark group. '
                                                 'The organisation is experienced as exceptionally adaptive. It detects signals early, '
                                                 'quickly connects insights to decisions and embeds improvements broadly.'},
        'Organisatieklimaat': {'unavailable': 'External benchmark data is currently unavailable for this dimension.',
                               'very_low': 'Your assessment of Organisation Climate is in the bottom 20% of the benchmark group. You '
                                           'experience relatively little room to experiment, share ideas or learn from mistakes. Renewal '
                                           'and open knowledge exchange therefore have limited ground to grow.',
                               'rather_low': 'Your assessment of Organisation Climate is below the benchmark group average. There are '
                                             'examples of learning and innovation, but space remains inconsistent or dependent on local '
                                             'initiators. Caution and established habits often take priority.',
                               'middle': 'Your assessment of Organisation Climate is around the benchmark group average. The organisation '
                                         'climate offers a workable basis for learning, sharing ideas and experimentation. Experienced '
                                         'space still varies by team, theme or moment.',
                               'rather_high': 'Your assessment of Organisation Climate is above the benchmark group average. You '
                                              'experience that learning, innovation and sharing ideas are generally encouraged. This '
                                              'climate makes testing improvements and using knowledge more broadly easier.',
                               'very_high': 'Your assessment of Organisation Climate is in the top 20% of the benchmark group. In your '
                                            'view, the organisation has an exceptionally strong learning and innovation climate. '
                                            'Experimentation is safe, insights are widely shared and new ideas have visible room to grow.'},
        'HR': {'unavailable': 'External benchmark data is currently unavailable for this dimension.',
               'very_low': 'Your assessment of HR Policy is in the bottom 20% of the benchmark group. You experience that selection, '
                           'development, evaluation and recognition provide relatively little support for adaptive behaviour. Expectations '
                           'and HR systems are therefore insufficiently aligned.',
               'rather_low': 'Your assessment of HR Policy is below the benchmark group average. Some HR practices support learning and '
                             'adaptation, but the whole is not yet consistent. Development, feedback or recognition do not always make '
                             'adaptive behaviour visibly attractive.',
               'middle': 'Your assessment of HR Policy is around the benchmark group average. HR policy offers a workable basis for '
                         'supporting adaptability. The connection between selection, development, evaluation and recognition could be '
                         'experienced more clearly and consistently.',
               'rather_high': 'Your assessment of HR Policy is above the benchmark group average. You experience that HR practices '
                              'generally support learning, development and flexible behaviour well. Employees receive relatively clear '
                              'signals and opportunities to adapt and grow.',
               'very_high': 'Your assessment of HR Policy is in the top 20% of the benchmark group. HR policy is experienced as '
                            'exceptionally well aligned with adaptability. Selection, development, evaluation and recognition reinforce '
                            'one another and make learning and change a visible part of good work.'}}}
