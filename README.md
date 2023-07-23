# word_frequencies
count words and frequencies inside a file.

This little script is used to check bachelor and master thesis against often used words 

First approach was to read latex/lyx files, but this didn't work very well, because it's neccassary to implement a lot of stuff around to avoid words hits, which are latex stuff.

Current approach is to read a normal text file and an ignore_words file and analyse the text.

This is a quick & dirty approach to solve this issue for me ;-)
# History
| date | version | information |
|---|:-:|---|
| 2023-07-23 | 0.1 | solution only for text files |

# Note of example publications
> The examples used are real excerpts from bachelor's or master's theses. They are subject to the copy right of the respective author.
In principle, these are only excerpts.

# ignore_words
every row should be a word or an regulare expresseion. If a word inside the text file hits agains an ignore_word or a regex, this word will be ignored.

## Building a RegEx object list
if regex is used, before starting analysis of a text file, all ignore_words and regexe are read and compiled. During analyze this compiled object list is used to get a better performance
# PrettyTable output
Output is set by PrettyTable and as Markdown, so it's easy to use in web presentations. Default is set to the top 100 words (via parameter this can be changed)

# Example 1
Output of a part of a bachelor thesis.
* Column `normalized word`
contain a normalized word (lower case). This word is used inside the word count list
* Column `count` represents the number of hits
* Column `Word(s)` represents all Words (case insentive) which occurs the hit
 
## List of word frequencies
| normalized Word | Count |         Word(s)         |
|-----------------|-------|-------------------------|
|       und       |   86  |           und           |
|        in       |   67  |         IN,in,In        |
|        zu       |   63  |          zu,ZU          |
|       den       |   55  |           den           |
|       von       |   48  |         von,VON         |
|      werte      |   47  |          Werte          |
|       eine      |   46  |        eine,Eine        |
|       dass      |   46  |           dass          |
|       ist       |   43  |         ist,Ist         |
|       bei       |   40  |         bei,Bei         |
|      nicht      |   39  |       nicht,Nicht       |
|       wird      |   38  |           wird          |
|       ein       |   37  |         ein,Ein         |
|       das       |   37  |         Das,das         |
|       für       |   36  |           für           |
|        im       |   35  |          im,Im          |
|    variablen    |   34  |        Variablen        |
|       des       |   34  |         DES,des         |
|    datensatz    |   32  |        Datensatz        |
|        .        |   31  |            .            |
|    fehlenden    |   30  |        fehlenden        |
|      dieser     |   29  |      dieser,Dieser      |
|        es       |   27  |          Es,es          |
|     werden.     |   26  |         werden.         |
|      werden     |   24  |          werden         |
|        so       |   24  |          so,So          |
|        um       |   23  |          um,Um          |
|       aus       |   23  |         Aus,aus         |
|       als       |   23  |         als,Als         |
|       mit       |   22  |         mit,Mit         |
|    imputation   |   22  |        Imputation       |
|       sich      |   21  |           sich          |
|      durch      |   21  |          durch          |
|       auch      |   21  |        auch,Auch        |
|      welche     |   19  |          welche         |
|        da       |   19  |          da,Da          |
|      einer      |   18  |          einer          |
|       kann      |   17  |           kann          |
|      daten      |   17  |          Daten          |
|        m        |   16  |           M,m           |
|    datensätze   |   16  |        Datensätze       |
|       wert      |   15  |           Wert          |
|       nach      |   15  |        nach,Nach        |
|       dem       |   15  |           dem           |
|       auf       |   15  |           auf           |
|       wenn      |   14  |           wenn          |
|    verteilung   |   14  |        Verteilung       |
|    parameter    |   14  |        Parameter        |
|       nur       |   14  |           nur           |
|      diese      |   14  |       diese,Diese       |
|       dies      |   14  |        Dies,dies        |
|     zwischen    |   13  |         zwischen        |
|      somit      |   13  |       somit,Somit       |
|       ist.      |   13  |           ist.          |
|      einen      |   13  |          einen          |
|      einem      |   13  |          einem          |
|   beobachteten  |   13  |       beobachteten      |
|       zur       |   12  |       ZUR,zur,Zur       |
|      fehlen     |   12  |          Fehlen         |
|        θ        |   11  |            θ            |
|       oder      |   11  |           oder          |
|        =        |   11  |            =            |
|      werten     |   10  |          Werten         |
|     welcher     |   10  |         welcher         |
|   statistical   |   10  | Statistical,statistical |
|     schritt     |   10  |         Schritt         |
|     mithilfe    |   10  |    mithilfe,Mithilfe    |
|    geschätzt    |   10  |        geschätzt        |
|      eines      |   10  |          eines          |
|  antwortausfall |   10  |      Antwortausfall     |
|     analyse     |   10  |         Analyse         |
|     sondern     |   9   |         sondern         |
|     methode     |   9   |         Methode         |
|       man       |   9   |         man,Man         |
|       hier      |   9   |        hier,Hier        |
|  beispielsweise |   9   |      beispielsweise     |
|      beiden     |   9   |          beiden         |
|       also      |   9   |        also,Also        |
|      allbus     |   9   |          ALLBUS         |
|       wie       |   8   |         Wie,wie         |
|       vor.      |   8   |           vor.          |
|    verfahren    |   8   |   Verfahren,verfahren   |
|    singulären   |   8   |        singulären       |
|      sind.      |   8   |          sind.          |
|       sind      |   8   |           sind          |
|     matching    |   8   |         Matching        |
|     kapitel     |   8   |         Kapitel         |
|      jedoch     |   8   |          jedoch         |
|       hat       |   8   |           hat           |
|     fehlende    |   8   |         fehlende        |
|        an       |   8   |          an,An          |
|   zusammenhang  |   7   |       Zusammenhang      |
|     werden,     |   7   |         werden,         |
|       über      |   7   |           über          |
|       soll      |   7   |           soll          |
|        ob       |   7   |          ob,Ob          |
|    multiplen    |   7   |        multiplen        |
|      liegt      |   7   |       liegt,Liegt       |
|-----------------|-------|-------------------------|


# Example 2

## List of word frequencies
|      normalized word       | count |          word(s)           |
|----------------------------|-------|----------------------------|
|            und             |  111  |            und             |
|            von             |  100  |          von,Von           |
|             in             |   57  |           in,In            |
|            ein             |   52  |          ein,Ein           |
|             im             |   50  |           Im,im            |
|            eine            |   49  |         Eine,eine          |
|            auf             |   44  |          auf,Auf           |
|            ist             |   40  |            ist             |
|           indoor           |   39  |       Indoor,indoor        |
|            mit             |   36  |          mit,Mit           |
|            für             |   35  |          für,Für           |
|            das             |   33  |          das,Das           |
|        positioning         |   31  |  positioning,Positioning   |
|            dem             |   31  |            dem             |
|             zu             |   29  |           zu,Zu            |
|            oder            |   28  |            oder            |
|            sind            |   25  |            sind            |
|            des             |   25  |            des             |
|            zur             |   24  |          zur,Zur           |
|            den             |   24  |            den             |
|           smart            |   23  |        Smart,smart         |
|            als             |   21  |          als,Als           |
|            wird            |   20  |            wird            |
|           einer            |   19  |           einer            |
|            zum             |   18  |            zum             |
|        technologien        |   18  |        Technologien        |
|            sich            |   18  |            sich            |
|             es             |   18  |           es,Es            |
|            bei             |   18  |            bei             |
|             of             |   17  |             of             |
|            wie             |   15  |            wie             |
|          position          |   15  |     Position,position      |
|           durch            |   15  |        durch,Durch         |
|           werden           |   14  |           werden           |
|            the             |   14  |          The,the           |
|           mobile           |   14  |           mobile           |
|          glasses           |   14  |      Glasses,glasses       |
|           eines            |   14  |           eines            |
|            auch            |   14  |         auch,Auch          |
|             o              |   13  |             o              |
|       informationen        |   13  |       Informationen        |
|          beispiel          |   13  |          Beispiel          |
|           einem            |   12  |           einem            |
|          adaptive          |   12  |     adaptive,Adaptive      |
|         abbildung          |   12  |         Abbildung          |
|             –              |   11  |             –              |
|           system           |   11  |       System,system        |
|            nach            |   11  |            nach            |
|          mobilen           |   11  |          mobilen           |
|           geräte           |   11  |           Geräte           |
|           dieser           |   11  |       dieser,Dieser        |
|            aus             |   11  |          Aus,aus           |
|             an             |   11  |           an,An            |
|        smartphones         |   10  |        Smartphones         |
|       positionierung       |   10  |       Positionierung       |
|           arbeit           |   10  |           Arbeit           |
|           andere           |   10  |       Andere,andere        |
|          werden.           |   9   |          werden.           |
|        verschiedene        |   9   | Verschiedene,verschiedene  |
|             um             |   9   |           um,Um            |
|           stand            |   9   |           Stand            |
|          nutzung           |   9   |          Nutzung           |
|       bereitstellung       |   9   |       Bereitstellung       |
|          zwischen          |   8   |          zwischen          |
|           wurde            |   8   |           wurde            |
|            über            |   8   |         über,Über          |
|            kann            |   8   |            kann            |
|         innerhalb          |   8   |    innerhalb,Innerhalb     |
| informationsbereitstellung |   8   | Informationsbereitstellung |
|         funktionen         |   8   |         Funktionen         |
|           einen            |   8   |           einen            |
|         bluetooth          |   8   |         Bluetooth          |
|             am             |   8   |             am             |
|             =              |   8   |             =              |
|        technologie         |   7   |        Technologie         |
|            ist.            |   7   |            ist.            |
|    funkfrequenzsignale     |   7   |    Funkfrequenzsignale     |
|             et             |   7   |             et             |
|        anwendungen         |   7   |        Anwendungen         |
|          android           |   7   |          Android           |
|            al.             |   7   |            al.             |
|         adaptiven          |   7   |         adaptiven          |
|         vergleich          |   6   |         Vergleich          |
|           unter            |   6   |        unter,Unter         |
|          systemen          |   6   |          Systemen          |
|            sie             |   6   |            sie             |
|          methoden          |   6   |          Methoden          |
|           menge            |   6   |           Menge            |
|           kleine           |   6   |           kleine           |
|          kenntnis          |   6   |          Kenntnis          |
|          kapitel           |   6   |          Kapitel           |
|        integration         |   6   |  Integration,integration   |
|            gibt            |   6   |            gibt            |
|             cm             |   6   |             cm             |
|           bezug            |   6   |           Bezug            |
|         bestimmung         |   6   |         Bestimmung         |
|          bereich           |   6   |          Bereich           |
|          begriff           |   6   |          Begriff           |
|----------------------------|-------|----------------------------|