import streamlit as st
from datetime import datetime
import pandas as pd
import plotly.express as px
import gspread
import streamlit.components.v1 as components
from google.oauth2.service_account import Credentials
from translations import (
    DIMENSION_LABELS,
    GROUP_LABELS,
    GROUP_TEXTS,
    INTERPRETATIONS,
    LANGUAGE_NAMES,
    QUESTION_TRANSLATIONS,
    SHORT_DESCRIPTIONS,
    SUBDIMENSION_LABELS,
    UI_TEXTS,
)

# ---------------------------
# APP CONFIG
# ---------------------------
st.set_page_config(
    page_title="Adaptiviteit Systeemscan",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown('<div id="top"></div>', unsafe_allow_html=True)

# ---------------------------
# GOOGLE SHEETS CONNECTION
# ---------------------------
@st.cache_resource
def connect_sheet():
    scope = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=scope
    )

    client = gspread.authorize(creds)

    sheet = client.open("Orgscan_adaptivity").sheet1

    return sheet


sheet = connect_sheet()


def ensure_language_column(worksheet):
    headers = worksheet.row_values(1)
    normalized = [str(header).strip().lower() for header in headers]
    if "taal" in normalized:
        return normalized.index("taal") + 1
    language_column = len(headers) + 1
    worksheet.update_cell(1, language_column, "taal")
    return language_column

# ---------------------------
# SESSION STATE
# ---------------------------
if "step" not in st.session_state:
    st.session_state.step = 1

if "answers" not in st.session_state:
    st.session_state.answers = {}

# ---------------------------
# QUESTION MAP
# ---------------------------

question_map = {

# ---------------- CAPACITEIT ----------------
"Ik ben zelfzeker dat ik bij onverwachte veranderingen mijn manier van werken kan aanpassen.": {"dimension":"Capaciteit","subdimension":"Perceived Behavioral Control","code":"COM-C1","direction":"pos"},
"Ik heb de vaardigheden om verschillende oplossingen te beoordelen en de beste te kiezen.": {"dimension":"Capaciteit","subdimension":"Vaardigheid","code":"COM-C2","direction":"pos"},
"Mijn eerdere ervaringen helpen mij om te blijven groeien en mij aan te passen.": {"dimension":"Capaciteit","subdimension":"Vaardigheid","code":"COM-C3","direction":"pos"},
"Ik vind het belangrijk om mijn werkwijze bij te sturen wanneer omstandigheden veranderen.": {"dimension":"Capaciteit","subdimension":"Ervaren belang","code":"COM-C4","direction":"pos"},
"Ik heb het gevoel dat mijn aanpassingsvermogen op het werk vooral afhangt van mezelf, niet van mijn omgeving.": {"dimension":"Capaciteit","subdimension":"Perceived Behavioral Control","code":"COM-C5","direction":"pos"},
"Ik kan snel verbanden leggen en overzicht houden in nieuwe situaties.": {"dimension":"Capaciteit","subdimension":"Vaardigheid","code":"COM-C_new","direction":"pos"},

# ---------------- MOTIVATIE ----------------
"Veranderingen motiveren mij omdat ze kansen bieden om mijn werkwijze bij te stellen.": {"dimension":"Motivatie","subdimension":"Intrinsieke motivatie","code":"COM-M1","direction":"pos"},
"Ik neem zelf initiatief om mijn kennis en vaardigheden te vernieuwen zodat ik beter kan omgaan met nieuwe uitdagingen.": {"dimension":"Motivatie","subdimension":"Intrinsieke motivatie","code":"COM-M2","direction":"pos"},
"Ik ben gemotiveerd om nieuwe manieren van werken uit te proberen, zelfs wanneer ze mijn routine in de war sturen.": {"dimension":"Motivatie","subdimension":"Intrinsieke motivatie","code":"COM-M3","direction":"pos"},
"De verbondenheid die ik met mijn organisatie ervaar, motiveert mij om mijn werkwijze aan te passen wanneer dat nodig is.": {"dimension":"Motivatie","subdimension":"Betrokkenheid","code":"COM-M4","direction":"pos"},
"Ik ervaar het als mij verantwoordelijkheid om mijn werk aan te passen wanneer de situatie verandert.": {"dimension":"Motivatie","subdimension":"Betrokkenheid","code":"COM-M5","direction":"pos"},
"Ook als veranderingen zwaar voelen, blijf ik gemotiveerd om mij aan te passen.": {"dimension":"Motivatie","subdimension":"Volharding","code":"COM-M6","direction":"pos"},
"Het voelt comfortabel om verder te gaan met mijn werk, ook wanneer veranderingen nog niet volledig duidelijk zijn.": {"dimension":"Motivatie","subdimension":"Volharding","code":"COM-M7","direction":"pos"},
"De constante vraag om mij aan te passen, vermindert soms mijn motivatie.": {"dimension":"Motivatie","subdimension":"Volharding","code":"COM-M8R","direction":"neg"},
"Ik ben gemotiveerd om nieuwe dingen te leren.": {"dimension":"Motivatie","subdimension":"Intrinsieke motivatie","code":"LO_M","direction":"pos"},

# ---------------- JOB CHARACTERISTICS ----------------
"Ik vrees dat mijn job op een slechte manier zal veranderen (bv. minder variatie, ontwikkelingskans, of vrijheid).": {"dimension":"Job Karakteristieken","subdimension":"Job onzekerheid","code":"JobCh_jobins_R","direction":"neg"},

"In mijn werk is het vaak onduidelijk wat er precies verwacht wordt of wat er zal veranderen.": {"dimension":"Job Karakteristieken","subdimension":"Rolduidelijkheid","code":"JobCh_rolinsec1R","direction":"neg"},
"Het is duidelijk wat er van mij verwacht wordt wanneer veranderingen optreden.": {"dimension":"Job Karakteristieken","subdimension":"Rolduidelijkheid","code":"JobCh_rolinsec2","direction":"pos"},

"Ik voel me voldoende uitgedaagd, maar niet overbevraagd in mijn werk.": {"dimension":"Job Karakteristieken","subdimension":"Taakcomplexiteit & betekenis","code":"JobCh_TaskComplex","direction":"pos"},
"Mijn werk heeft een duidelijke positieve impact op mensen buiten mijn organisatie.": {"dimension":"Job Karakteristieken","subdimension":"Taakcomplexiteit & betekenis","code":"JobCh_TaskSign","direction":"pos"},

"Mijn job geeft me aanzienlijke autonomie in het nemen van beslissingen.": {"dimension":"Job Karakteristieken","subdimension":"Autonomie","code":"JobCh_AutonDec","direction":"pos"},
"Mijn job geeft mij veel vrijheid en zelfstandigheid in hoe ik mijn werk doe.": {"dimension":"Job Karakteristieken","subdimension":"Autonomie","code":"JobCh_AutonMeth","direction":"pos"},

"Tenzij mijn werk gedaan is kunnen anderen hun taken niet afronden.": {"dimension":"Job Karakteristieken","subdimension":"Afhankelijkheid","code":"JobCh_Interdep","direction":"neg"},

# ---------------- TEAMADAPTIVITEIT ----------------
"Mijn team reageert goed op onverwachte situaties.": {"dimension":"Teamadaptiviteit","subdimension":None,"code":"AD_TR","direction":"pos"},
"Mijn collega's en ik nemen regelmatig tijd om onze werkmethoden te verbeteren.": {"dimension":"Teamadaptiviteit","subdimension":None,"code":"AD_CL","direction":"pos"},
"Wanneer iets misgaat, past mijn team onze werkwijze aan op basis van wat we leren.": {"dimension":"Teamadaptiviteit","subdimension":None,"code":"AD_F","direction":"pos"},
"Bij onverwachte situaties verzamelt mijn team actief informatie om beter te begrijpen wat er speelt.": {"dimension":"Teamadaptiviteit","subdimension":None,"code":"AD_SA","direction":"pos"},
"In mijn team stuurt iedereen hun werkwijze bij naar aanleiding van veranderende omstandigheden.": {"dimension":"Teamadaptiviteit","subdimension":None,"code":"COM-O5","direction":"pos"},
"In mijn team denken we actief na over mogelijke toekomstige veranderingen en hoe we ons daarop kunnen voorbereiden.": {"dimension":"Teamadaptiviteit","subdimension":None,"code":"AD_new1","direction":"pos"},
"In mijn team bespreken we regelmatig welke toekomstige veranderingen (bv. in klant, technologie, regelgeving) mogelijk op ons afkomen en wat dat betekent voor ons werk.": {"dimension":"Teamadaptiviteit","subdimension":None,"code":"AD_new2","direction":"pos"},

# ---------------- TEAMKLIMAAT ----------------
"Bij onverwachte situaties dubbelchecken we of de informatie voor iedereen duidelijk is.": {"dimension":"Teamklimaat","subdimension":None,"code":"AD_HI","direction":"pos"},
"In mijn team zeggen mensen het eerlijk als zij een andere mening hebben over een oplossing.": {"dimension":"Teamklimaat","subdimension":None,"code":"AD_PS","direction":"pos"},
"Bij onverwachte situaties is binnen mijn team duidelijk wie wat doet en van wie wat verwacht wordt.": {"dimension":"Teamklimaat","subdimension":None,"code":"AD_T","direction":"pos"},
"Als team vinden we het belangrijk om verschillende aanpakken te bespreken als we samen problemen oplossen.": {"dimension":"Teamklimaat","subdimension":None,"code":"AD_SL","direction":"pos"},
"Mijn collega’s moedigen mij aan om nieuwe ideeën te testen en proberen.": {"dimension":"Teamklimaat","subdimension":None,"code":"COM-O2","direction":"pos"},
"Mensen met wie ik werk hebben een persoonlijke interesse voor mij.": {"dimension":"Teamklimaat","subdimension":None,"code":"JDSCSS5","direction":"pos"},

# ---------------- LEIDINGGEVENDE ----------------
"Mijn leidinggevende stimuleert creativiteit en nieuwe ideeën.": {"dimension":"Richting & steun leidinggevende","subdimension":"Nieuwigheden stimuleren","code":"COM_ADAP1","direction":"pos"},
"Mijn leidinggevende zorgt dat we leren van fouten en samen kunnen groeien.": {"dimension":"Richting & steun leidinggevende","subdimension":"Nieuwigheden stimuleren","code":"COM_ADAP2","direction":"pos"},
"Mijn leidinggevende geeft het goede voorbeeld in hoe om te gaan met veranderingen.": {"dimension":"Richting & steun leidinggevende","subdimension":"Nieuwigheden stimuleren","code":"COM-O4","direction":"pos"},

"Mijn leidinggevende stelt duidelijke doelen, meet voortgang én bespreekt deze.": {"dimension":"Richting & steun leidinggevende","subdimension":"Structuur aanbrengen","code":"COM_ADM1","direction":"pos"},
"Mijn leidinggevende geeft structuur en planning in ons werk.": {"dimension":"Richting & steun leidinggevende","subdimension":"Structuur aanbrengen","code":"COM_ADM2","direction":"pos"},

"Mijn leidinggevende creëert een context waarin teamleden verschillende meningen openlijk kunnen bespreken.": {"dimension":"Richting & steun leidinggevende","subdimension":"Verbinding maken","code":"COM_ENAB1","direction":"pos"},
"Mijn leidinggevende helpt teamleden met elkaar te verbinden zodat we van elkaar kunnen leren.": {"dimension":"Richting & steun leidinggevende","subdimension":"Verbinding maken","code":"COM_ENAB2","direction":"pos"},

# ---------------- ORGANISATIEADAPTIVITEIT ----------------
"Mijn organisatie past zich effectief aan aan maatschappelijke en economische veranderingen.": {"dimension":"Organisatieadaptiviteit","subdimension":None,"code":"OAP1","direction":"pos"},
"Mijn organisatie blijft werken aan voortdurende verbetering.": {"dimension":"Organisatieadaptiviteit","subdimension":None,"code":"CR_CE1","direction":"pos"},
"Mijn organisatie volgt de voortgang van veranderingen en verbeteringen structureel op.": {"dimension":"Organisatieadaptiviteit","subdimension":None,"code":"CR_CE3","direction":"pos"},
"Mijn organisatie vertaalt signalen uit de omgeving (bv. markt, maatschappij, technologie) tijdig naar keuzes of ondersteuning (bv. prioriteiten, skills, aanpak).": {"dimension":"Organisatieadaptiviteit","subdimension":None,"code":"visie1","direction":"pos"},

# ---------------- ORGANISATIE STEUN ----------------
"Top management betrekken medewerkers vaak bij belangrijke beslissingen.": {"dimension":"Richting & steun van organisatie","subdimension":"Topmanagement steun","code":"OL_MC1","direction":"pos"},
"In mijn organisatie wordt leren door de directie eerder gezien als een kost dan als een investering.": {"dimension":"Richting & steun van organisatie","subdimension":"Topmanagement steun","code":"OL_MC2R","direction":"neg"},
"Het top management staat positief tegenover veranderingen die ervoor zorgen dat we kunnen meegaan met of voor lopen op externe situaties.": {"dimension":"Richting & steun van organisatie","subdimension":"Topmanagement steun","code":"OL_MC3","direction":"pos"},
"Ik begrijp duidelijk waar onze organisatie naartoe wil in de toekomst en wat dat betekent voor mijn werk.": {"dimension":"Richting & steun van organisatie","subdimension":"Topmanagement steun","code":"visie2","direction":"pos"},

"Mijn organisatie slaagt erin mensen te motiveren om hun werkwijze aan te passen aan nieuwe omstandigheden.": {"dimension":"Richting & steun van organisatie","subdimension":"Kennis","code":"CR_CE2","direction":"pos"},
"Mijn organisatie weet hoe zij medewerkers kan ondersteunen om te blijven leren en zich aan te passen.": {"dimension":"Richting & steun van organisatie","subdimension":"Kennis","code":"CR_K1","direction":"pos"},
"Mijn organisatie heeft een duidelijk beeld van wat nodig is om zich aan te passen aan veranderingen in de omgeving.": {"dimension":"Richting & steun van organisatie","subdimension":"Kennis","code":"CR_K2","direction":"pos"},

"Mijn organisatie heeft genoeg middelen om zich aan te passen aan veranderingen.": {"dimension":"Richting & steun van organisatie","subdimension":"Middelen","code":"CR_A1","direction":"pos"},
"Mijn organisatie geeft medewerkers ruimte om te leren en te groeien.": {"dimension":"Richting & steun van organisatie","subdimension":"Middelen","code":"CR_A2","direction":"pos"},
"Mijn organisatie geeft voldoende tijd om mij te kunnen voorbereiden of aanpassen op veranderingen.": {"dimension":"Richting & steun van organisatie","subdimension":"Middelen","code":"CR_A3","direction":"pos"},
"Mijn organisatie heeft instrumenten (handleidingen, routines, databanken) om kennis uit het verleden te bewaren, ook al zijn de collega's niet meer dezelfden.": {"dimension":"Richting & steun van organisatie","subdimension":"Middelen","code":"OL_KT2","direction":"pos"},

"Alle niveau's van de organisatie (bv. afdeling, team, individu) weten hoe zij bijdragen aan de algemene doelen.": {"dimension":"Richting & steun van organisatie","subdimension":"Alignment","code":"OL_S1","direction":"pos"},
"Alle niveau's van de organisatie zijn onderling gelinkt, en werken goed samen.": {"dimension":"Richting & steun van organisatie","subdimension":"Alignment","code":"OL_S2","direction":"pos"},
"Wanneer we met andere teams samenwerken, is duidelijk wie welke beslissingen hoort te nemen.": {"dimension":"Richting & steun van organisatie","subdimension":"Alignment","code":"AD_CD","direction":"pos"},

# ---------------- ORGANISATIEKLIMAAT ----------------
"Mijn organisatie stimuleert experimenteren en vernieuwen om processen te verbeteren.": {"dimension":"Organisatieklimaat","subdimension":None,"code":"OL_O1","direction":"pos"},
"Mijn organisatie kijkt wat andere organisaties doen en neemt nuttige ideeën over.": {"dimension":"Organisatieklimaat","subdimension":None,"code":"OL_O2","direction":"pos"},
"Ideeën en ervaringen van externe partners (bv. adviseurs, klanten) worden gezien als waardevol om van te leren.": {"dimension":"Organisatieklimaat","subdimension":None,"code":"OL_O3","direction":"pos"},
"Het is deel van onze organisatiecultuur dat medewerkers hun mening en ideeën delen over hoe werkprocessen beter kunnen.": {"dimension":"Organisatieklimaat","subdimension":None,"code":"OL_O4","direction":"pos"},
"Nieuwe ideeën die goed werken, worden beloond.": {"dimension":"Organisatieklimaat","subdimension":None,"code":"OL_MC4","direction":"pos"},
"Fouten worden op alle organsatieniveaus besproken en geanalyseerd.": {"dimension":"Organisatieklimaat","subdimension":None,"code":"OL_KT1","direction":"pos"},

# ---------------- HR ----------------
"In mijn organisatie zijn er opleidingen om medewerkers te helpen zich beter aan te passen aan veranderingen.": {"dimension":"HR","subdimension":None,"code":"HR_Train","direction":"pos"},
"Medewerkers die heel (pro)actief met verandering omgaan, krijgen extra kansen of beloningen.": {"dimension":"HR","subdimension":None,"code":"HR_Comp","direction":"pos"},
"Functioneringsgesprekken richten zich op het ontwikkelen van verandervaardigheden.": {"dimension":"HR","subdimension":None,"code":"HR_PerfApp","direction":"pos"},
"Bij werving letten we op de mate waarin kandidaten zich goed kunnen aanpassen.": {"dimension":"HR","subdimension":None,"code":"HR_Selec","direction":"pos"}

}

# Stabiele technische sleutels: zichtbare teksten kunnen later vertaald worden
# zonder scoring of historische gegevens te beïnvloeden.
QUESTION_TEXTS = {"nl": {meta["code"]: text for text, meta in question_map.items()}}
QUESTION_TEXTS.update(QUESTION_TRANSLATIONS)
QUESTION_META = {meta["code"]: {**meta} for meta in question_map.values()}
QUESTION_CODES = list(QUESTION_TEXTS)

# ---------------------------
# CLUSTERING EN FEEDBACK 
# ---------------------------

dimension_meta = {
    "Capaciteit": {
        "title": """Capaciteit""",
        "description": """Capaciteit gaat over de mate waarin je over de juiste vaardigheden, het vertrouwen en het inzicht beschikt om je werk aan te passen wanneer omstandigheden veranderen. Dit omvat zowel praktische probleemoplossende vaardigheden als het geloof dat je zelf invloed hebt op hoe je met verandering omgaat. We nemen deze dimensie mee omdat adaptiviteit moeilijk is zonder de competentie en het zelfvertrouwen om effectief te handelen in nieuwe of complexe situaties. We maken een onderscheid tussen 3 specifieke onderdelen:
"""
    },

    "Motivatie": {
        "title": """Motivatie""",
        "description": """Motivatie gaat over de energie en bereidheid om effectief met verandering om te gaan. Het gaat niet alleen over willen aanpassen, maar ook over blijven volhouden wanneer verandering moeilijk of onzeker aanvoelt. We nemen motivatie mee omdat adaptiviteit niet alleen vraagt om kunnen, maar ook om willen en volhouden. We bekijken opnieuw 3 subfacetten:
"""
    },

    "Job Karakteristieken": {
        "title": """Job Karakteristieken""",
        "description": """Deze dimensie kijkt naar de kenmerken van je job die adaptiviteit ondersteunen of bemoeilijken. Zelfs de meest adaptieve medewerker kan moeilijker omgaan met verandering, onzekerheid en nieuwe uitdagingen als de jobcontext dit belemmert. We lichten 5 elementen toe waarvan we weten dat ze cruciaal zijn voor adaptiviteit.
"""
    },

    "Teamadaptiviteit": {
        "title": """Teamadaptiviteit""",
        "description": """Teamadaptiviteit gaat over de mate waarin een team als geheel flexibel en wendbaar reageert op veranderingen, fouten en onverwachte situaties. Teams zoeken actief naar nieuwe informatie, reflecteren en sturen hun manier van werken bij om beter te presteren in de toekomst. We nemen deze dimensie mee omdat individuele adaptiviteit pas volledig tot uiting komt wanneer teams samen effectief kunnen bijsturen, leren en zich aanpassen in de dagelijkse samenwerking."""
    },

    "Teamklimaat": {
        "title": """Teamklimaat""",
        "description": """Teamklimaat verwijst naar de sociale en psychologische context waarin teamleden samenwerken, inclusief open communicatie, vertrouwen en duidelijke verwachtingen.  In een teamklimaat dat adaptief gedrag sterk ondersteunt, wordt actief nagegaan of iedereen dezelfde interpretatie deelt van nieuwe informatie om zo misverstanden te voorkomen. Ook leren collega's actief samen en stimuleren ze elkaar om nieuwe ideeën te testen en bestaande routines in vraag te stellen. Daarbij voelt iedereen zich veilig om ideeën te delen, fouten te bespreken en elkaar te ondersteunen. We nemen deze dimensie mee omdat adaptief gedrag enkel kan ontstaan wanneer er binnen het team voldoende veiligheid en openheid is om te leren en te veranderen, en wanneer teamleden elkaar actief ondersteunen."""
    },

    "Richting & steun leidinggevende": {
        "title": """Leidinggevende""",
        "description": """Een directe leidinggevende is een belangrijke schakel in het dagelijks functioneren van medewerkers en teams. Ze spelen een cruciale rol in het zorgen van verbinding binnen het team door het creëren van vertrouwen, duidelijkheid en openheid. Daarnaast geeft een leidinggevende richting en structuur waarbinnen leren en ontdekken gestimuleerd wordt. Zo bepalen leidinggevenden in welke mate medewerkers ruimte ervaren om zich aan te passen en mee te bewegen met verandering. We kunnen een onderscheid maken in 3 specifieke rollen die een leidinggevende best opneemt:"""
    },

    "Organisatieadaptiviteit": {
        "title": """Organisatieadaptiviteit""",
        "description": """Organisatieadaptiviteit gaat over de mate waarin de organisatie als geheel effectief inspeelt op maatschappelijke, economische en technologische veranderingen. Dit omvat ook continu verbeteren en het opvolgen van vooruitgang. Adaptiviteit bevindt zich niet alleen op individueel of teamniveau. Ook op organisatieniveau moet het zichtbaar zijn in het vermogen om zich voortdurend aan te passen en te leren.
"""
    },

    "Richting & steun van organisatie": {
        "title": """Richting & steun van organisatie""",
        "description": """Richting & steun van de organisatie gaat over de mate waarin de organisatie als geheel duidelijk richting geeft aan verandering en medewerkers ondersteunt om zich aan te passen. Dit omvat zowel topmanagement steun als de beschikbaarheid van kennis, middelen en de mate van alignment tussen organisatieonderdelen. We nemen deze dimensie mee omdat adaptiviteit sterk wordt beïnvloed door de condities die de organisatie creëert om leren en verandering te ondersteunen. We kunnen een onderscheid maken in 3 specifieke onderdelen:
"""
    },

    "Organisatieklimaat": {
        "title": """Organisatieklimaat""",
        "description": """Organisatieklimaat verwijst naar de mate waarin een organisatie openstaat voor experimenteren, innovatie en het actief zoeken naar nieuwe ideeën, zowel intern als extern. Het gaat ook over hoe sterk leren wordt gestimuleerd via het delen van ideeën, het bespreken van fouten en het waarderen van verbeterinitiatieven. Daarnaast omvat het hoe innovatie wordt erkend en hoe externe inzichten worden gebruikt om te leren en verbeteren. We nemen deze dimensie mee omdat een open en lerend klimaat een belangrijke voorwaarde vormt voor duurzame adaptiviteit en continue verbetering."""
    },

    "HR": {
        "title": """HR beleid""",
        "description": """HR gaat over de mate waarin personeelsbeleid adaptiviteit ondersteunt doorheen de volledige employee journey, van selectie en training tot evaluatie, beloning en participatie. We nemen deze dimensie mee omdat adaptiviteit niet alleen ontstaat op de werkvloer, maar ook actief wordt gestuurd via HR-praktijken."""
    }
}


subdimension_meta = {

    # -------------------------
    # CAPACITEIT
    # -------------------------
    "Perceived Behavioral Control": {
        "description": """Dit gaat over het gevoel dat je zelf invloed hebt op je aanpassingsvermogen. Voel je dat jij je gedrag en aanpak kan sturen, of heb je het gevoel dat vooral externe omstandigheden bepalen wat mogelijk is? Dit is belangrijk omdat mensen sneller initiatief nemen wanneer ze geloven dat ze zelf impact hebben."""
    },
    "Vaardigheid": {
        "description": """Deze subdimensie gaat over je vermogen om informatie te verwerken, oplossingen te beoordelen, verbanden te leggen en te leren uit eerdere ervaringen. Adaptiviteit is sterk afhankelijk is van cognitieve flexibiliteit en het vermogen om met complexiteit om te gaan."""
    },
    "Ervaren belang": {
        "description": """Dit gaat over de mate waarin je aanpassen als iets waardevols en noodzakelijk ziet. Dit is relevant omdat mensen zich sneller aanpassen wanneer ze verandering niet alleen kunnen, maar ook belangrijk vinden."""
    },

    # -------------------------
    # MOTIVATIE
    # -------------------------
    "Intrinsieke motivatie": {
        "description": """Dit verwijst naar je interne drive om te leren, te verbeteren en nieuwe manieren van werken uit te proberen. Je ziet verandering als een kans om sterker of beter te worden. Dit aspect ondersteunt adaptiviteit omdat duurzame verandering vooral gedragen wordt door persoonlijke motivatie."""
    },
    "Betrokkenheid": {
        "description": """Deze subdimensie gaat over de mate waarin verbondenheid met je organisatie en verantwoordelijkheidsgevoel je gedrag sturen. Dit is belangrijk omdat mensen zich sneller inzetten voor verandering wanneer ze zich betrokken voelen bij het grotere geheel."""
    },
    "Volharding": {
        "description": """Dit gaat over je vermogen om gemotiveerd te blijven wanneer verandering zwaar, vermoeiend of nog onduidelijk is. Adaptiviteit vraagt vaak om te blijven doorgaan zonder volledige zekerheid en op moeilijke momenten."""
    },

    # -------------------------
    # JOB CHARACTERISTICS
    # -------------------------
    "Job onzekerheid": {
        "description": """De mate waarin je onzekerheid ervaart over de toekomst van je job of taken. Een lagere score betekent meer jobonzekerheid (en dus minder werkzekerheid), wat vaak gepaard gaat met stress en minder ruimte om te focussen op leren en aanpassen."""
    },
    "Autonomie": {
        "description": """De mate waarin je zelf beslissingen kan nemen om je werk aan te passen wanneer dat nodig is, maar ook om te beslissen hoe je je werk uitvoert en organiseert. Autonomie verhoogt adaptiviteit omdat snelle aanpassing vaak vraagt om lokale beslissingsruimte.
"""
    },
    "Rolduidelijkheid": {
        "description": """De mate waarin verwachtingen, verantwoordelijkheden en veranderingen helder zijn. Duidelijkheid ondersteunt adaptiviteit omdat mensen beter kunnen schakelen wanneer ze weten wat van hen verwacht wordt."""
    },
    "Afhankelijkheid": {
        "description": """De mate waarin je afhankelijk bent van anderen of andere teams om je werk vooruit te krijgen. Sterke afhankelijkheden kunnen adaptiviteit vertragen wanneer afstemming moeilijk verloopt."""
    },
    "Taakcomplexiteit & betekenis": {
        "description": """De mate waarin je werk een voor jou perfect niveau van uitdaging en complexiteit heeft, als betekenisvol en impactvol voor anderen. Dit combineert cognitieve uitdaging met ervaren impact, wat belangrijk is voor leren, motivatie en adaptief gedrag."""
    },

    # -------------------------
    # LEIDINGGEVENDE
    # -------------------------
    "Nieuwigheden stimuleren": {
        "description": """Dit gaat over de mate waarin de leidinggevende ruimte geeft voor nieuwe ideeën, creativiteit en experimenteren. Het draait ook om leren uit fouten en flexibel reageren op verandering. Adaptiviteit wordt binnen teams sterk beïnvloed door de mate waarin leiders vernieuwing actief aanmoedigen en zelf het voorbeeld geven in veranderend gedrag."""
    },
    "Structuur aanbrengen": {
        "description": """Dit verwijst naar het vermogen van de leidinggevende om duidelijke doelen, planning en opvolging te voorzien en zo richting en overzicht in het werk te creëren. Dit is belangrijk omdat adaptiviteit niet alleen vraagt om flexibiliteit, maar ook om duidelijke kaders waarbinnen mensen effectief kunnen handelen."""
    },
    "Verbinding maken": {
        "description": """Dit gaat over de rol van de leidinggevende in het faciliteren van samenwerking, dialoog en het verbinden van teamleden met verschillende perspectieven. Adaptiviteit neemt toe wanneer mensen van elkaar kunnen leren en zich voldoende verbonden voelen met elkaar om ideeën en meningen te delen."""
    },

    # -------------------------
    # RICHTING & STEUN ORGANISATIE
    # -------------------------
    "Topmanagement steun": {
        "description": """Dit verwijst naar de houding en betrokkenheid van het topmanagement ten aanzien van verandering, leren en participatie van medewerkers in besluitvorming. Dit is belangrijk omdat strategische steun vanuit de top bepaalt in welke mate adaptiviteit echt gedragen en gestimuleerd wordt binnen de organisatie.
"""
    },
    "Kennis": {
        "description": """Dit gaat over de mate waarin de organisatie weet hoe ze medewerkers kan ondersteunen in leren, aanpassen en omgaan met verandering. Adaptiviteit is afhankelijk van organisatorische knowhow over hoe leren en verandering effectief ondersteund kunnen worden."""
    },
    "Middelen": {
        "description": """Dit verwijst naar de beschikbare tijd, ruimte en middelen die medewerkers krijgen om zich aan te passen en te ontwikkelen. Dit is belangrijk omdat adaptiviteit enkel haalbaar is wanneer mensen ook effectief de middelen krijgen om flexibel te kunnen werken en leren."""
    },
    "Alignment": {
        "description": """Dit gaat over hoe goed verschillende delen van de organisatie op elkaar afgestemd zijn en samenwerken richting gezamenlijke doelen. Adaptiviteit wordt versterkt wanneer de organisatie als één geheel kan reageren op verandering, in plaats van gefragmenteerd te werken."""
    },

}

def compute_subdimension_scores(df, question_map):
    sub_scores = {}

    for item, meta in question_map.items():
        sub = meta["subdimension"]
        val = df[item].mean()

        sub_scores.setdefault(sub, []).append(val)

    return {k: sum(v)/len(v) for k, v in sub_scores.items()}

st.markdown("""
<style>
div[data-testid="stRadio"] label {
    font-size: 0px; /* verbergt default label maar breekt layout niet */
}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# PERCENTILES LOAD (GOOGLE SHEET)
# ---------------------------

import numpy as np

percentile_data = {
    "Capaciteit": [
        (2.8, 1.785714286),
        (3.0, 5.357142857),
        (3.2, 6.25),
        (3.4, 14.28571429),
        (3.6, 22.32142857),
        (3.8, 38.39285714),
        (4.0, 57.14285714),
        (4.2, 73.21428571),
        (4.4, 84.82142857),
        (4.6, 92.85714286),
        (4.8, 94.64285714),
        (5.0, 100.0),
    ],

    "Motivatie": [
        (2.555555556, 0.8928571429),
        (2.666666667, 1.785714286),
        (2.777777778, 4.464285714),
        (2.888888889, 7.142857143),
        (3.0, 10.71428571),
        (3.111111111, 14.28571429),
        (3.222222222, 18.75),
        (3.333333333, 24.10714286),
        (3.444444444, 29.46428571),
        (3.555555556, 40.17857143),
        (3.666666667, 45.53571429),
        (3.777777778, 55.35714286),
        (3.888888889, 61.60714286),
        (4.0, 68.75),
        (4.111111111, 75.0),
        (4.222222222, 80.35714286),
        (4.333333333, 83.92857143),
        (4.444444444, 91.07142857),
        (4.555555556, 93.75),
        (4.666666667, 97.32142857),
        (4.777777778, 98.21428571),
        (4.888888889, 99.10714286),
        (5.0, 100.0),
    ],

    "Job Karakteristieken": [
        (2.0, 2.678571429),
        (2.5, 8.928571429),
        (3.0, 25.89285714),
        (3.5, 46.42857143),
        (4.0, 86.60714286),
        (4.5, 96.42857143),
        (5.0, 100.0),
    ],

    "Teamadaptiviteit": [
        (1.4, 1.785714286),
        (2.0, 6.25),
        (2.4, 8.035714286),
        (2.8, 16.96428571),
        (3.0, 24.10714286),
        (3.4, 47.32142857),
        (3.6, 61.60714286),
        (4.0, 85.71428571),
        (4.2, 91.07142857),
        (4.4, 92.85714286),
        (4.6, 96.42857143),
        (4.8, 98.21428571),
        (5.0, 100.0),
    ],

    "Teamklimaat": [
        (1.8, 0.8928571429),
        (2.0, 1.785714286),
        (2.4, 6.25),
        (2.8, 13.39285714),
        (3.0, 16.96428571),
        (3.4, 41.07142857),
        (3.6, 51.78571429),
        (4.0, 78.57142857),
        (4.2, 88.39285714),
        (4.4, 91.07142857),
        (4.6, 97.32142857),
        (5.0, 100.0),
    ],

    "Richting & steun leidinggevende": [
        (1.0, 1.785714286),
        (2.0, 5.357142857),
        (2.857142857, 23.21428571),
        (3.0, 30.35714286),
        (3.5, 51.78571429),
        (4.0, 76.78571429),
        (4.5, 89.28571429),
        (5.0, 100.0),
    ],

    "Organisatieadaptiviteit": [
        (1.333333333, 0.9174311927),
        (2.0, 6.422018349),
        (3.0, 32.11009174),
        (3.666666667, 60.55045872),
        (4.0, 83.48623853),
        (4.666666667, 98.16513761),
        (5.0, 100.0),
    ],

    "Richting & steun van organisatie": [
        (1.0, 0.8928571429),
        (2.0, 12.5),
        (3.0, 39.28571429),
        (4.0, 91.96428571),
        (5.0, 100.0),
    ],

    "Alignment": [
        (1.75, 1.834862385),
        (2.5, 17.43119266),
        (3.0, 36.69724771),
        (3.5, 60.55045872),
        (4.0, 92.66055046),
        (5.0, 100.0),
    ],

    "Organisatieklimaat": [
        (1.333333333, 1.834862385),
        (2.5, 9.174311927),
        (3.0, 30.27522936),
        (3.5, 57.79816514),
        (4.0, 87.1559633),
        (5.0, 100.0),
    ],

    "HR": [
        (1.0, 0.9174311927),
        (2.0, 7.339449541),
        (3.0, 43.11926606),
        (4.0, 93.57798165),
        (5.0, 100.0),
    ],

    # subdimensies
    "Perceived Behavioral Control": [
        (2.0, 1.785714286),
        (3.0, 24.10714286),
        (4.0, 75.89285714),
        (5.0, 100.0),
    ],
    "Vaardigheid": [
        (3.0, 6.25),
        (4.0, 63.39285714),
        (5.0, 100.0),
    ],
    "Ervaren belang": [
        (2.0, 0.8928571429),
        (4.0, 58.03571429),
        (5.0, 100.0),
    ],
    "Intrinsieke motivatie": [
        (2.0, 0.8928571429),
        (4.0, 54.46428571),
        (5.0, 100.0),
    ],
    "Betrokkenheid": [
        (2.0, 3.571428571),
        (4.0, 69.64285714),
        (5.0, 100.0),
    ],
    "Volharding": [
        (2.0, 1.785714286),
        (4.0, 85.71428571),
        (5.0, 100.0),
    ],
    "Rolduidelijkheid": [
        (1.0, 0.8928571429),
        (3.0, 39.28571429),
        (5.0, 100.0),
    ],
    "Sociale linken": [
        (1.0, 0.8928571429),
        (3.0, 32.14285714),
        (5.0, 100.0),
    ],
}

def build_dimension_scores(answers):
    dim_scores = {}

    for code, score in answers.items():
        meta = QUESTION_META[code]
        final_score = 6 - score if meta["direction"] == "neg" else score

        dim = meta["dimension"]
        dim_scores.setdefault(dim, []).append(final_score)

    return {
        dim: sum(values) / len(values)
        for dim, values in dim_scores.items()
    }

# ---------------------------
# HIER DE INTERPRETATIES VAN DE PERCENTIELEN
# ---------------------------

def interpret_score(percentile):

    if percentile < 20:
        return "low"

    elif percentile < 40:
        return "below_avg"

    elif percentile < 60:
        return "average"

    elif percentile < 80:
        return "above_avg"

    else:
        return "high"

individual_dims = [
    "Capaciteit",
    "Motivatie",
]

context_dims = [
    "Job Karakteristieken"
    "Teamadaptiviteit",
    "Teamklimaat",
    "Richting & steun leidinggevende",
    "Organisatieadaptiviteit",
    "Richting & steun van organisatie",
    "Organisatieklimaat",
    "HR"
]

interpretation_text_individual = {

    "low": """
    Je scoort lager dan de meeste respondenten op deze dimensie. Dit wijst erop dat deze eigenschap momenteel minder sterk aanwezig is bij jou,
    wat het moeilijker kan maken om flexibel om te gaan met verandering en nieuwe situaties.
    """,

    "below_avg": """
    Je scoort iets lager dan gemiddeld op deze dimensie. Er lijkt hier nog ruimte om jezelf sterker te ondersteunen in het omgaan met verandering,
    onzekerheid of nieuwe verwachtingen.
    """,

    "average": """
    Je score ligt ongeveer rond het gemiddelde van andere respondenten. Deze factor vormt waarschijnlijk een voldoende basis om je aan te passen wanneer omstandigheden veranderen.
    """,

    "above_avg": """
    Je scoort hoger dan gemiddeld op deze dimensie. Deze eigenschap ondersteunt waarschijnlijk je vermogen om flexibel om te gaan met verandering en nieuwe uitdagingen.
    """,

    "high": """
    Je behoort tot de hoogste groep respondenten op deze dimensie. Deze eigenschap vormt duidelijk een sterke ondersteuning voor jouw adaptiviteit in het werk.
    """
}

interpretation_text_context = {

    "low": """
    Je beoordeelt jouw omgeving lager dan de meeste respondenten op deze dimensie.
    Dit wijst erop dat jouw context momenteel minder ondersteuning biedt
    voor jouw adaptivief gedrag.
    """,

    "below_avg": """
    Je ervaart jouw context iets minder ondersteunend dan gemiddeld op deze dimensie. Bepaalde voorwaarden die adaptiviteit versterken lijken vandaag minder aanwezig.
    """,

    "average": """
    Je beoordeling ligt ongeveer rond het gemiddelde van andere respondenten. Jouw omgeving biedt waarschijnlijk een basisniveau van ondersteuning voor adaptiviteit en verandering.
    """,

    "above_avg": """
    Je beoordeelt jouw omgeving positiever dan gemiddeld op deze dimensie. Dit wijst op een context die adaptiviteit, samenwerking en leren relatief goed ondersteunt.
    """,

    "high": """
    Je behoort tot de hoogste groep respondenten in hoe positief je jouw omgeving beoordeelt op deze dimensie. Dit wijst op een sterk ondersteunende context voor adaptiviteit, leren en verandering.
    """
}

def score_to_percentile(score, dim, percentile_data):
    data = percentile_data.get(dim)

    if data is None:
        return None

    # exact match of interpolatie
    data = sorted(data, key=lambda x: x[0])

    for i in range(len(data)):
        s, p = data[i]

        if score == s:
            return p

        if score < s:
            if i == 0:
                return p
            s0, p0 = data[i - 1]
            # lineaire interpolatie
            ratio = (score - s0) / (s - s0)
            return p0 + ratio * (p - p0)

    return data[-1][1]

def build_report(dim_scores, percentiles_df):
    report = {}

    individual_dims = [
        "Capaciteit",
        "Motivatie",
        "Job Karakteristieken"
    ]

    for dim, score in dim_scores.items():

        percentile = score_to_percentile(score, dim, percentiles_df)

        if percentile is None:
            st.warning(f"Geen percentieldata gevonden voor dimension: {dim}")
            continue

        level = interpret_score(percentile)

        interpretation_kind = "individual" if dim in individual_dims else "context"
        if LANGUAGE in INTERPRETATIONS:
            text = INTERPRETATIONS[LANGUAGE][interpretation_kind][level]
        elif interpretation_kind == "individual":
            text = interpretation_text_individual[level]
        else:
            text = interpretation_text_context[level]

        report[dim] = {
            "score": round(score, 2),
            "percentile": round(percentile, 1),
            "level": level,
            "text": text,
            "meta": dimension_meta[dim]
        }

    return report


DIMENSION_GROUPS = {
    "Individuele basis": ["Capaciteit", "Motivatie", "Job Karakteristieken"],
    "Team & leidinggevende": ["Teamadaptiviteit", "Teamklimaat", "Richting & steun leidinggevende"],
    "Organisatie": ["Organisatieadaptiviteit", "Richting & steun van organisatie", "Organisatieklimaat", "HR"],
}

GROUP_INTROS = {
    "Individuele basis": "Je persoonlijke basis voor adaptiviteit: wat je kan, wat je motiveert en hoe je job is ingericht.",
    "Team & leidinggevende": "De dagelijkse context waarin samenwerking, veiligheid, leren en leiding jouw adaptiviteit versterken of afremmen.",
    "Organisatie": "De bredere richting, systemen, cultuur en ondersteuning die duurzaam aanpassen en leren mogelijk maken.",
}

DIMENSION_SHORT_DESCRIPTIONS = {
    "Capaciteit": "Vaardigheden, vertrouwen en inzicht om effectief te handelen in nieuwe of complexe situaties.",
    "Motivatie": "Energie, bereidheid en volharding om met verandering om te gaan.",
    "Job Karakteristieken": "Jobkenmerken die aanpassen, leren en flexibel handelen ondersteunen of bemoeilijken.",
    "Teamadaptiviteit": "Hoe flexibel het team reageert, samen leert en zijn werkwijze bijstuurt.",
    "Teamklimaat": "Open communicatie, vertrouwen, veiligheid en duidelijke samenwerking binnen het team.",
    "Richting & steun leidinggevende": "Hoe de leidinggevende vernieuwing, structuur en verbinding ondersteunt.",
    "Organisatieadaptiviteit": "Hoe effectief de organisatie signalen oppikt, leert en zich aanpast.",
    "Richting & steun van organisatie": "Duidelijke richting, kennis, middelen en afstemming om verandering te ondersteunen.",
    "Organisatieklimaat": "Ruimte voor experimenteren, innovatie, leren en het delen van ideeën.",
    "HR": "Hoe HR-praktijken adaptiviteit ondersteunen via selectie, ontwikkeling, evaluatie en waardering.",
}

DIMENSION_ICONS = {
    "Capaciteit": '<svg viewBox="0 0 64 64"><path d="M21 48c-8-1-12-7-10-14-5-5-2-14 5-15 1-8 11-11 16-5 5-6 15-3 16 5 8 2 10 12 4 17 2 8-5 14-12 13"/><path d="M32 13v39M22 24c4 1 6 4 6 8M42 24c-4 1-6 4-6 8"/></svg>',
    "Motivatie": '<svg viewBox="0 0 64 64"><path d="M35 8c3 11-8 13-5 24 3-4 7-7 10-12 7 7 12 15 10 24-2 9-10 14-19 14S14 51 14 41c0-9 6-15 13-22 0 8 3 12 8 15-1-9 5-14 0-26z"/></svg>',
    "Job Karakteristieken": '<svg viewBox="0 0 64 64"><rect x="8" y="18" width="48" height="34" rx="5"/><path d="M23 18v-6h18v6M8 31h48M27 28h10v7H27z"/></svg>',
    "Teamadaptiviteit": '<svg viewBox="0 0 64 64"><circle cx="22" cy="24" r="7"/><circle cx="42" cy="24" r="7"/><path d="M8 51c1-10 6-16 14-16s13 6 14 16M28 51c1-10 6-16 14-16s13 6 14 16"/></svg>',
    "Teamklimaat": '<svg viewBox="0 0 64 64"><path d="M9 13h46v29H31L20 52V42H9z"/><path d="M18 23h28M18 31h19"/></svg>',
    "Richting & steun leidinggevende": '<svg viewBox="0 0 64 64"><circle cx="32" cy="17" r="8"/><path d="M17 52V40c0-9 7-15 15-15s15 6 15 15v12M8 51h48"/></svg>',
    "Organisatieadaptiviteit": '<svg viewBox="0 0 64 64"><path d="M12 32a20 20 0 0 1 35-13M46 10v12H34M52 32a20 20 0 0 1-35 13M18 54V42h12"/></svg>',
    "Richting & steun van organisatie": '<svg viewBox="0 0 64 64"><path d="M8 54h48M13 54V25h38v29M19 25V14h26v11"/><path d="M24 34h5M35 34h5M24 43h5M35 43h5"/></svg>',
    "Organisatieklimaat": '<svg viewBox="0 0 64 64"><path d="M21 29a11 11 0 1 1 22 0c0 6-3 8-6 12H27c-3-4-6-6-6-12z"/><path d="M27 46h10M29 52h6M32 5v7"/></svg>',
    "HR": '<svg viewBox="0 0 64 64"><circle cx="22" cy="22" r="7"/><circle cx="42" cy="22" r="7"/><circle cx="32" cy="15" r="7"/><path d="M8 52c1-10 6-16 14-16M56 52c-1-10-6-16-14-16M17 52c1-11 6-18 15-18s14 7 15 18"/></svg>',
}

def clean_text(text):
    return " ".join(str(text).split())


def dimension_card_html(dimension, data):
    score = float(data["score"])
    percentile = float(data["percentile"])
    subitems = data.get("subdimension", {})
    sub_html = ""
    if subitems:
        rows = "".join(f'<li><b>{SUBDIMENSION_LABELS[LANGUAGE].get(name, name)}</b>: {float(item["score"]):.2f} / 5</li>' for name, item in subitems.items())
        sub_html = f'<ul class="sub-list">{rows}</ul>'
    level_label = T[f'level_{data["level"]}']
    individual_dimensions = {"Capaciteit", "Motivatie", "Job Karakteristieken"}
    interpretation_kind = "individual" if dimension in individual_dimensions else "context"
    interpretation = (
        INTERPRETATIONS[LANGUAGE][interpretation_kind][data["level"]]
        if LANGUAGE in INTERPRETATIONS else data["text"]
    )
    return (
        '<article class="dimension-card">'
        '<header class="dimension-header">'
        f'<span class="dimension-icon">{DIMENSION_ICONS[dimension]}</span>'
        f'<div><h3>{DIMENSION_LABELS[LANGUAGE][dimension]}</h3><p>{SHORT_DESCRIPTIONS[LANGUAGE][dimension]}</p></div>'
        '</header>'
        '<div class="score-row">'
        f'<div class="score-track"><div class="score-fill" style="width:{score / 5 * 100:.1f}%"></div></div>'
        f'<span class="score-value">{score:.2f} / 5</span></div>'
        f'<span class="percentile-badge"><b>{T["score_interpretation"]}</b> · {level_label} · {T["higher_than"].format(p=f"{percentile:.0f}")}</span>'
        f'{sub_html}'
        f'<div class="interpretation-box"><b>{T["your_interpretation"]}</b><p>{clean_text(interpretation)}</p></div>'
        '</article>'
    )

st.markdown("""
<style>
:root { --primary:#0f566b; --blue:#2aa5ca; --yellow:#ffc271; --light-blue:#eef8fb; --text:#17313b; --muted:#667985; --line:#cfe1e7; }
html, body, [data-testid="stAppViewContainer"] {
    scroll-behavior: smooth;
    color:var(--text);
}
[data-testid="stAppViewContainer"] { background:linear-gradient(180deg,#f5fbfd 0,#fff 320px); }
.block-container { max-width:1220px; padding-top:5rem; padding-bottom:4rem; }
h1,h2,h3 { color:var(--primary)!important; }
.app-header { padding:1.5rem 1.7rem; margin-bottom:1.4rem; border-radius:0 42px 42px 0; background:var(--primary); color:white; }
.app-header h1 { color:white!important; margin:0; font-size:2.15rem; }
.app-header p { color:white; margin:.45rem 0 0; max-width:800px; }
.section-pill { display:inline-block; margin-bottom:.55rem; padding:.28rem .75rem; border-radius:999px; background:var(--primary); color:white; font-size:.78rem; font-weight:800; letter-spacing:.05em; text-transform:uppercase; }
.level-intro { padding:1rem 1.15rem; margin:.8rem 0 1rem; border-left:5px solid var(--primary); border-radius:14px; background:var(--light-blue); }
.dimension-grid { display:grid; gap:1rem; grid-template-columns:repeat(6,minmax(0,1fr)); align-items:stretch; }
.dimension-card { grid-column:span 2; min-height:100%; padding:1.05rem; border:1.5px solid var(--primary); border-radius:16px; background:white; box-shadow:0 8px 22px rgba(15,86,107,.07); display:flex; flex-direction:column; }
.dimension-grid.four .dimension-card { grid-column:span 3; }
.dimension-header { display:grid; grid-template-columns:48px 1fr; gap:.75rem; align-items:start; }
.dimension-icon { width:46px; height:46px; border-radius:50%; background:var(--primary); color:white; display:grid; place-items:center; }
.dimension-icon svg { width:68%; height:68%; fill:none; stroke:currentColor; stroke-width:2.2; stroke-linecap:round; stroke-linejoin:round; }
.dimension-card h3 { margin:0 0 .4rem; font-size:1.05rem; line-height:1.2; }
.dimension-card p { margin:0; font-size:.88rem; line-height:1.42; }
.score-row { display:flex; gap:.7rem; align-items:center; margin:.9rem 0 .65rem; }
.score-track { flex:1; height:9px; border-radius:999px; background:#e5f0f3; overflow:hidden; }
.score-fill { height:100%; background:linear-gradient(90deg,var(--blue),var(--primary)); }
.score-value { color:var(--primary); font-weight:800; white-space:nowrap; }
.percentile-badge { display:inline-flex; gap:.45rem; align-items:center; width:max-content; padding:.38rem .65rem; margin-bottom:.7rem; border-radius:10px; background:#fff7eb; color:var(--primary); font-size:.82rem; }
.interpretation-box { margin-top:auto; padding:.8rem; border-radius:10px; background:var(--light-blue); }
.sub-list { margin:.65rem 0 .8rem; padding-left:1rem; color:var(--text); font-size:.82rem; }
.sub-list li { margin:.28rem 0; }
div[data-testid="stRadio"] label p { font-size:.82rem; }
@media (min-width:900px) { div[data-testid="stRadio"] div[role="radiogroup"] { flex-wrap:nowrap; gap:.45rem; } }
.stButton>button { border:0; border-radius:999px; background:var(--primary); color:white; font-weight:700; padding-left:1.25rem; padding-right:1.25rem; }
.stButton>button:hover { background:#0a4455; color:white; }
@media(max-width:800px){ .block-container{padding:4.5rem 1rem 3rem}.dimension-grid,.dimension-grid.four{grid-template-columns:1fr}.dimension-card,.dimension-grid.four .dimension-card{grid-column:1}.app-header{margin-left:-1rem;border-radius:0 28px 28px 0}.app-header h1{font-size:1.6rem} }
</style>
""", unsafe_allow_html=True)

requested_language = st.query_params.get("lang", "nl")
if requested_language not in LANGUAGE_NAMES:
    requested_language = "nl"
if "language" not in st.session_state:
    st.session_state.language = requested_language

language_spacer, language_picker = st.columns([5, 1])
with language_picker:
    LANGUAGE = st.selectbox(
        "Language · Taal · Langue",
        options=list(LANGUAGE_NAMES),
        format_func=LANGUAGE_NAMES.get,
        key="language",
        label_visibility="collapsed",
    )
if st.query_params.get("lang") != LANGUAGE:
    st.query_params["lang"] = LANGUAGE
T = UI_TEXTS[LANGUAGE]

header_left, header_right = st.columns([5,1.35], vertical_alignment="center")
with header_left:
    st.markdown(f'<div class="app-header"><h1>{T["title"]}</h1><p>{T["intro"]}</p></div>', unsafe_allow_html=True)
with header_right:
    logo_left, logo_right = st.columns(2, vertical_alignment="center")
    with logo_left: st.image("assets/logo Coliberate.png", use_container_width=True)
    with logo_right: st.image("assets/logo KULtivating.webp", use_container_width=True)

scale_labels = T["scale"]

# ---------------------------
# STEP 1 - GEGEVENS
# ---------------------------
if st.session_state.step == 1:
    st.markdown(f'<span class="section-pill">{T["details_step"]}</span>', unsafe_allow_html=True)
    st.subheader(T["details_title"])
    st.write(T["details_intro"])

    naam = st.text_input(T["name"])
    email = st.text_input(T["email"], help=T["email_help"], placeholder="name@example.com")
    functie = st.text_input(T["role"])
    organisatie = st.text_input(T["organisation"])

    if st.button(T["start"]):
        st.session_state.naam = naam
        st.session_state.email = email
        st.session_state.functie = functie
        st.session_state.organisatie = organisatie
        st.session_state.step = 2
        st.rerun()

# ---------------------------
# STEP 2-4 - DRIE VRAGENLIJSTDELEN
# ---------------------------
elif st.session_state.step in (2, 3, 4):
    part_index = st.session_state.step - 2
    group_name = list(DIMENSION_GROUPS)[part_index]
    dimensions = DIMENSION_GROUPS[group_name]
    part_codes = [code for code in QUESTION_CODES if QUESTION_META[code]["dimension"] in dimensions]
    answers = st.session_state.answers

    part_title_keys = ["part_individual", "part_team", "part_organisation"]
    st.markdown(
        f'<span class="section-pill">{T["part"].format(current=part_index + 1)}</span>',
        unsafe_allow_html=True,
    )
    st.subheader(T[part_title_keys[part_index]])
    st.write(T["part_instruction"])
    st.progress((part_index + 1) / 3)

    for code in part_codes:
        question = QUESTION_TEXTS[LANGUAGE][code]
        with st.container():
            col_q, col_a = st.columns([5, 7], gap="large")
            with col_q:
                st.markdown(f"**{question}**")
            with col_a:
                selected = st.radio(
                    label="",
                    options=list(range(1, 6)),
                    format_func=lambda value: T["scale"][value - 1],
                    horizontal=True,
                    key=f"question_{code}",
                    index=None,
                    label_visibility="collapsed",
                )
                if selected:
                    answers[code] = selected
        st.markdown("<hr style='margin:8px 0; opacity:0.6;'>", unsafe_allow_html=True)

    missing = [code for code in part_codes if code not in answers]
    if missing:
        st.warning(T["missing"])
    else:
        st.success(T["complete"])

    back_column, next_column = st.columns([1, 1])
    with back_column:
        if st.button(T["previous"], key=f"back_{part_index}"):
            st.session_state.step -= 1
            st.rerun()

    with next_column:
        button_label = T["show_result"] if part_index == 2 else T["next"]
        if st.button(button_label, disabled=bool(missing), key=f"next_{part_index}"):
            if part_index < 2:
                st.session_state.step += 1
                st.rerun()

            dim_scores = build_dimension_scores(answers)
            sub_scores = {}
            for code, score in answers.items():
                meta = QUESTION_META[code]
                sub = meta["subdimension"]
                final_score = 6 - score if meta["direction"] == "neg" else score
                if sub is not None:
                    sub_scores.setdefault(sub, []).append(final_score)
            sub_scores = {sub: round(sum(values) / len(values), 2) for sub, values in sub_scores.items()}

            report = build_report(dim_scores, percentile_data)
            for dimension in report:
                report[dimension]["subdimension"] = {}
                for sub, score in sub_scores.items():
                    for meta in QUESTION_META.values():
                        if meta["dimension"] == dimension and meta["subdimension"] == sub:
                            report[dimension]["subdimension"][sub] = {
                                "score": score,
                                "description": subdimension_meta.get(sub, {}).get("description", ""),
                            }
                            break
            st.session_state.report = report

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            language_column = ensure_language_column(sheet)
            rows_to_add = []
            for code, score in answers.items():
                meta = QUESTION_META[code]
                raw_score = score
                final_score = 6 - score if meta["direction"] == "neg" else score
                storage_row = [
                    timestamp, st.session_state.naam, st.session_state.email,
                    st.session_state.functie, st.session_state.organisatie,
                    meta["code"], meta["dimension"], meta["subdimension"],
                    raw_score, final_score, QUESTION_TEXTS[LANGUAGE][code],
                ]
                if language_column <= len(storage_row) + 1:
                    storage_row.insert(language_column - 1, LANGUAGE)
                else:
                    storage_row.extend([""] * (language_column - len(storage_row) - 1))
                    storage_row.append(LANGUAGE)
                rows_to_add.append(storage_row)
            sheet.append_rows(rows_to_add)

            st.session_state.response_language = LANGUAGE
            st.session_state.step = 5
            st.rerun()

# ---------------------------
# STEP 3
# ---------------------------
elif st.session_state.step == 5:
    components.html(
        """<script>setTimeout(()=>{const el=window.parent.document.getElementById('top');if(el){el.scrollIntoView({behavior:'smooth',block:'start'});}},200);</script>""",
        height=0,
    )

    report = st.session_state.report
    strongest = max(report.items(), key=lambda item: item[1]["percentile"])
    weakest = min(report.items(), key=lambda item: item[1]["percentile"])
    strongest_percentile = f'{strongest[1]["percentile"]:.0f}'
    weakest_percentile = f'{weakest[1]["percentile"]:.0f}'
    strongest_level = T[f'level_{strongest[1]["level"]}']
    weakest_level = T[f'level_{weakest[1]["level"]}']

    st.markdown(f'<span class="section-pill">{T["profile_pill"]}</span>', unsafe_allow_html=True)
    st.title(T["thanks"])
    st.write(T["result_intro"])

    visual_column, summary_column = st.columns([1.2, .8], gap="large", vertical_alignment="top")
    with visual_column:
        st.subheader(T["model"])
        st.image("assets/Visual.png", use_container_width=True)
    with summary_column:
        st.subheader(T["stands_out"])
        with st.container(border=True):
            st.markdown(
                f"**{T['strongest']}**  \n"
                f"{DIMENSION_LABELS[LANGUAGE][strongest[0]]}: {strongest[1]['score']:.2f} / 5  \n"
                f"{T['higher_than'].format(p=strongest_percentile)} · {strongest_level}"
            )
            st.markdown(
                f"**{T['development']}**  \n"
                f"{DIMENSION_LABELS[LANGUAGE][weakest[0]]}: {weakest[1]['score']:.2f} / 5  \n"
                f"{T['higher_than'].format(p=weakest_percentile)} · {weakest_level}  \n"
                f"{T['lower_context']}"
            )
            st.info(T["summary_note"])

    for group, dimensions in DIMENSION_GROUPS.items():
        st.markdown(f"## {GROUP_LABELS[LANGUAGE][group]}")
        st.markdown(f'<div class="level-intro">{GROUP_TEXTS[LANGUAGE][group]}</div>', unsafe_allow_html=True)
        cards = [dimension_card_html(dimension, report[dimension]) for dimension in dimensions if dimension in report]
        grid_class = "dimension-grid four" if len(cards) == 4 else "dimension-grid"
        st.markdown(f'<div class="{grid_class}">{"".join(cards)}</div>', unsafe_allow_html=True)

    st.caption(T["percentile_guide"])

    # ---------------------------
    # RESET
    # ---------------------------
    if st.button(T["restart"]):
        st.session_state.step = 1
        st.session_state.answers = {}
        st.rerun()
