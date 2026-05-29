import streamlit as st
from datetime import datetime
import pandas as pd
import plotly.express as px
import gspread
import streamlit.components.v1 as components
from google.oauth2.service_account import Credentials
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# ---------------------------
# EMAIL VERSTUREN & ACCOUNT
# ---------------------------
def send_email(to_email, subject, html_content):
    sender_email = st.secrets["gmail_user"]
    sender_password = st.secrets["gmail_password"]

    msg = MIMEMultipart("related")
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = to_email

    msg_alternative = MIMEMultipart("alternative")
    msg.attach(msg_alternative)
    msg_alternative.attach(MIMEText(html_content, "html"))

    # Voeg Visual.png toe als inline image
    with open("assets/Visual.png", "rb") as img:
        mime_img = MIMEImage(img.read(), _subtype="png")
        mime_img.add_header("Content-ID", "<visual>")
        mime_img.add_header("Content-Disposition", "inline", filename=\"Visual.png\"")
        mime_img.add_header("X-Attachment-Id", "visual")
        msg.attach(mime_img)
    # LOGO 1
    with open("assets/logo Coliberate.png", "rb") as img:
        mime_img = MIMEImage(img.read(), _subtype="png")
        mime_img.add_header("Content-ID", "<logo_coliberate>")
        mime_img.add_header("Content-Disposition", "inline", filename=\"logo_coliberate.png\"")
        mime_img.add_header("X-Attachment-Id", "logo_coliberate")
        msg.attach(mime_img)

    # LOGO 2
    with open("assets/logo KULtivating.png", "rb") as img:
        mime_img = MIMEImage(img.read(), _subtype="png")
        mime_img.add_header("Content-ID", "<logo_kultivating>")
        mime_img.add_header("Content-Disposition", "inline", filename="\"logo_kultivating.png\"")
        mime_img.add_header("X-Attachment-Id", "logo_kultivating")
        msg.attach(mime_img)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.send_message(msg)
    server.quit()

# ---------------------------
# EMAIL TEKST
# ---------------------------
def build_email_report(report, naam):
    html = f"""
    <html>
    <body>

        <div style="width:100%; display:block; text-align:right;">
            <img src="cid:logo_coliberate" height="60"  style="margin-right:10px;">
            <img src="cid:logo_kultivating" height="60">
        </div>
          
        <h1>Feedbackrapport Organisatiescan Adaptiviteit</h1>

        <h2>Beste {naam},</h2>

        <p>Hieronder vind je jouw persoonlijke adaptiviteitsrapport.</p>

        <h2>Inleiding: het overkoepelende model</h2>

        <p>
        Adaptiviteit is het vermogen om effectief om te gaan met verandering, onzekerheid en nieuwe uitdagingen,
        en daarbij niet alleen goed te blijven functioneren, maar ook bewust te blijven leren, verbeteren en vooruitdenken.
        Het gaat dus niet alleen over reageren wanneer verandering zich aandient, maar ook over de mate waarin iemand,
        een team of een organisatie verandering actief kan opnemen, vormgeven en zelfs anticiperen op wat nog komt.
        </p>

        <p>
        Binnen ons model bekijken we adaptiviteit als een ontwikkelbare maturiteit: van eerder reactief omgaan met verandering,
        naar proactief vooruitdenken en uiteindelijk verandering mee helpen creëren. Adaptiviteit is dus geen vast persoonlijk kenmerk,
        maar iets dat groeit door ervaring, context, ondersteuning en bewust gedrag. In dit rapport willen we vooral kijken naar alle elementen die samen jouw adaptief gedrag helpen vormen.
        </p>

        <p>In dit rapport bekijken we hoe jouw persoonlijke adaptiviteit beïnvloedt kan worden vanuit drie samenhangende niveaus:</p>

        <ol>
            <li><b>Individu</b> : in welke mate beschik je zelf over de capaciteit, motivatie en werkomstandigheden om je aan te passen.</li>
            <li><b>Team & directe leidinggevende</b> : in welke mate ondersteunt je team en je leidinggevende een flexibele, lerende en wendbare manier van werken.</li>
            <li><b>Organisatie</b> : in welke mate creëert de bredere organisatie de juiste cultuur, systemen en ondersteuning om adaptiviteit mogelijk te maken.</li>
        </ol>

        <p>
        Deze drie niveaus zijn van elkaar afhankelijk en beïnvloeden elkaar voortdurend. Individuele adaptiviteit groeit sterker
        in een team dat openstaat voor leren. Teams functioneren beter in een organisatie die ruimte geeft voor aanpassing en ontwikkeling.
        </p>

        <p>
        We nemen deze dimensies op omdat onderzoek én praktijk tonen dat adaptiviteit nooit alleen individueel bepaald wordt.
        Wie duurzaam wil groeien in aanpassingsvermogen, heeft zowel persoonlijke sterktes als sociale en organisatorische ondersteuning nodig.
        In onderstaande figuur vatten we samen wat de kernvoorspellers zijn van adaptief gedrag:
        </p>

        <img src="cid:visual" width="800">

        <h2>Persoonlijke resultaten</h2>
    """

    current_block = None

    block_intro = {
        "individu": """
        <h2>1. Individueel niveau</h2>
        <p>
        Hier ligt jouw persoonlijke basis voor adaptiviteit:
        je vaardigheden, je motivatie en de kenmerken van je job.
        Dit gaat over de vraag of je jezelf in staat voelt om veranderingen aan te pakken,
        of je daar ook energie uit haalt, en of jouw specifieke job dit ook mogelijk maakt.
        </p>
        """,

        "team": """
        <h2>2. Team & directe leidinggevende</h2>
        <p>
        Adaptief zijn doe je niet alleen. Een erg belangrijke rol is voorzien voor diegenen
        waar een werknemer op dagelijkse basis het meeste contact heeft: collega's en directe leidinggevende(n).
        Zij tonen door hun eigen gedrag of adaptiviteit belangrijk is en gewaardeerd wordt.
        Daarbij zorgt de teamsfeer en relatie met de leidinggevende ervoor of mensen zich veilig voelen om bij te sturen,
        nieuwe ideeën te testen en te leren uit fouten.
        In dit blok kijken we dus naar het team dat jou direct omringt en ondersteunt.
        </p>
        """,

        "organisatie": """
        <h2>3. Organisatie</h2>
        <p>
        Adaptiviteit binnen een organisatie wordt niet alleen bepaald door individuen of teams,
        maar ook door de bredere structuren, systemen en cultuur waarin zij werken.
        Organisatorische factoren bepalen in grote mate of verandering wordt gefaciliteerd,
        ondersteund en duurzaam verankerd.
        In dit blok kijken we naar de manier waarop de organisatie als geheel richting geeft aan verandering,
        leren ondersteunt en samenwerking, middelen en systemen inzet om zich aan te passen
        aan een veranderende omgeving.
        </p>
        """
    }

    individu_dims = ["Capaciteit", "Motivatie", "Job Karakteristieken"]
    team_dims = ["Teamadaptiviteit", "Teamklimaat", "Richting & steun van leidinggevende"]
    organisatie_dims = ["Organisatieadaptiviteit", "Richting & Steun van Organisatie", "Organisatieklimaat", "HR"]

    # ---------------------------
    # DIMENSIES LOOP
    # ---------------------------
    for dim, d in report.items():

        if dim in individu_dims and current_block != "individu":
            if current_block is not None:
                    html += '<hr style="margin:20px 0;">'
            html += block_intro["individu"]
            current_block = "individu"

        elif dim in team_dims and current_block != "team":
            if current_block is not None:
                    html += '<hr style="margin:20px 0;">'
            html += block_intro["team"]
            current_block = "team"

        elif dim in organisatie_dims and current_block != "organisatie":
            if current_block is not None:
                    html += '<hr style="margin:20px 0;">'
            html += block_intro["organisatie"]
            current_block = "organisatie"

        html += f"""
        <h3>{d['meta']['title']}</h3>

        <p>
            <b>Score:</b> {d['score']} /5 |
            <b>Percentiel:</b> {d['percentile']}%
        </p>

        <p>
        <b>Interpretatie percentiel:</b>
        Je scoort hoger dan ongeveer {d['percentile']}% van de respondenten.
        {d['text']}
        </p>

        <p>{d['meta']['description']}</p>
        """

        # subdimensies
        if d.get("subdimension"):
            html += '<ul style="margin:0; padding-left:18px; line-height:1.3;">'

            for sub, subdata in d["subdimension"].items():
                html += f"""
                <li style="margin-bottom:6px;">
                    <b>{sub}</b><br>
                    Score: {subdata['score']} /5<br>
                    {subdata['description']}
                </li>
                """

            html += "</ul>"

    html += """
    <hr>

    <h3>Vragen of samen verder aan de slag?</h3>

    <p>
    We hopen dat dit rapport je helpt om inzicht te krijgen in hoe adaptiviteit zich in jouw context ontwikkelt, en waar mogelijke groeikansen liggen.
    </p>

    <p>
    Heb je vragen over de resultaten, of wil je samen verkennen wat dit kan betekenen voor jouw team of organisatie, dan kan je ons gerust contacteren.
    We gaan graag in gesprek om de inzichten te duiden en mee te denken over mogelijke vervolgstappen.
    </p>

    <p>
    Daarnaast begeleiden we organisaties ook in het ruimer uitrollen van deze scan en het vertalen van de resultaten naar concrete acties op team- en organisatieniveau.
    </p>

    <p>
    Dank je wel voor je deelname.
    </p>

    </body>
    </html>
    """

    return html
# ---------------------------
# APP CONFIG
# ---------------------------
st.markdown('<div id="top"></div>', unsafe_allow_html=True)

st.set_page_config(
    page_title="Adaptiviteit Organisatiescan",
    layout="wide"
)

col1, col2 = st.columns([4, 1])

with col1:
    st.title("Adaptiviteit Organisatiescan")
#   st.markdown("### Hoe futureproof ben jij?")

with col2:
    st.image("assets/logo Coliberate.png", width=100)
    st.image("assets/logo KULtivating.webp", width=100)

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

# ---------------------------
# SESSION STATE
# ---------------------------
if "step" not in st.session_state:
    st.session_state.step = 1

if "answers" not in st.session_state:
    st.session_state.answers = {}

if "email_sent" not in st.session_state:
    st.session_state.email_sent = False

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

def build_dimension_scores(answers, question_map):
    dim_scores = {}

    for question, score in answers.items():
        meta = question_map[question]
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
    "Richting & steun van leidinggevende",
    "Organisatieadaptiviteit",
    "Richting & Steun van Organisatie",
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

        # juiste tekst kiezen
        if dim in individual_dims:
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

st.markdown("""
<style>
html, body, [data-testid="stAppViewContainer"] {
    scroll-behavior: smooth;
}
</style>
""", unsafe_allow_html=True)

questions = list(question_map.keys())

scale_map = {"Helemaal oneens":1,"Oneens":2,"Neutraal":3,"Eens":4,"Helemaal eens":5}

# ---------------------------
# STEP 1
# ---------------------------
if st.session_state.step == 1:
    st.subheader ("Vul deze korte vragenlijst (10') in en kom te weten wat jij en je omgeving kunnen doen om je te helpen adaptiever te worden.")

    st.subheader("Stap 1: Je gegevens")

    naam = st.text_input("Naam")
    email = st.text_input("Email - hierop ontvang je jouw persoonlijke feedbackrapport")
    functie = st.text_input("Functie")
    organisatie = st.text_input("Organisatie")

    if st.button("Start vragenlijst"):
        st.session_state.naam = naam
        st.session_state.email = email
        st.session_state.functie = functie
        st.session_state.organisatie = organisatie

        st.session_state.step = 2
        st.rerun()

    questions = list(question_map.keys())

# ---------------------------
# STEP 2 (SINGLE PAGE VERSION)
# ---------------------------
elif st.session_state.step == 2:

    # ---------------------------
    # INIT
    # ---------------------------
    answers = st.session_state.answers

    st.subheader("Stap 2: Adaptiviteitsscan")

    # ---------------------------
    # QUESTIONS (ALL IN ONE PAGE)
    # ---------------------------
    for q in questions:
        with st.container():
            col_q, col_a = st.columns([5, 5])

            with col_q:
                st.markdown(f"**{q}**")

            with col_a:
                selected = st.radio(
                    label="",
                    options=list(scale_map.keys()),
                    horizontal=True,
                    key=q,
                    label_visibility="collapsed"
                )

                if selected:
                    answers[q] = scale_map[selected]

        st.markdown("<hr style='margin:8px 0; opacity:0.6;'>", unsafe_allow_html=True)

    # ---------------------------
    # CHECK COMPLETENESS
    # ---------------------------
    missing = [q for q in questions if q not in answers]

    if missing:
        st.warning("Vul alle vragen in.")
    else:
        st.success("Alle vragen ingevuld.")

    # ---------------------------
    # SUBMIT
    # ---------------------------
    if st.button("Versturen") and not missing:

        percentiles_df = percentile_data

        dim_scores = build_dimension_scores(answers, question_map)
        sub_scores = {}

        for question, score in answers.items():
            meta = question_map[question]
            sub = meta["subdimension"]

            final_score = 6 - score if meta["direction"] == "neg" else score

            if sub is not None:
                sub_scores.setdefault(sub, []).append(final_score)

        sub_scores = {
            sub: round(sum(values) / len(values), 2)
            for sub, values in sub_scores.items()
        }

        report = build_report(dim_scores, percentiles_df)

        # subdimensies toevoegen aan report
        for dim in report:
            report[dim]["subdimension"] = {}

            for sub, score in sub_scores.items():
                # check of sub bij deze dimensie hoort
                for q, meta in question_map.items():
                    if meta["dimension"] == dim and meta["subdimension"] == sub:
                        report[dim]["subdimension"][sub] = {
                            "score": score,
                            "description": subdimension_meta.get(sub, {}).get("description", "")
                        }
                        break

        st.session_state.report = report

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        rows_to_add = []

        for q, score in answers.items():
            meta = question_map[q]

            raw_score = score
            final_score = 6 - score if meta["direction"] == "neg" else score

            rows_to_add.append([
                timestamp,
                st.session_state.naam,
                st.session_state.email,
                st.session_state.functie,
                st.session_state.organisatie,
                meta["code"],
                meta["dimension"],
                meta["subdimension"],
                raw_score,
                final_score,
                q
            ])

        sheet.append_rows(rows_to_add)

        # reset + next step
        st.session_state.step = 3
        st.session_state.scroll_top = True
        st.rerun()

# ---------------------------
# STEP 3
# ---------------------------
elif st.session_state.step == 3:

    if not st.session_state.email_sent:
        report = st.session_state.report

        html_report = build_email_report(
            report,
            st.session_state.naam
        )

        send_email(
            st.session_state.email,
            "Jouw Rapport van de Adaptiviteit Organisatiescan",
            html_report
        )

        st.session_state.email_sent = True

    st.success("Je rapport werd per e-mail verzonden! Check je spam folder als je hem niet ziet verschijnen.")
    st.info("Je kan dit venster nu sluiten.")

    # ---------------------------
    # RESET
    # ---------------------------
    if st.button("Opnieuw invullen"):
        st.session_state.step = 1
        st.session_state.answers = {}
        st.rerun()
