# Generated by Django 2.1.8 on 2019-04-10 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Garments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=255)),
                ('brand', models.CharField(choices=[('NATIVEYOUTH', 'Native Youth'), ('LEVIS', "Levi's®"), ('MICHAELMICHAELKORS', 'MICHAEL Michael Kors'), ('POLORALPHLAUREN', 'Polo Ralph Lauren'), ('LKBENNETT', 'LK Bennett'), ('MISSSELFRIDGEPETITE', 'Miss Selfridge Petite'), ('DOROTHYPERKINS', 'Dorothy Perkins'), ('TIGEROFSWEDEN', 'Tiger of Sweden'), ('ZALANDOESSENTIALS', 'Zalando Essentials'), ('ANNAFIELD', 'Anna Field'), ('EDCBYESPRIT', 'edc by Esprit'), ('MANGO', 'Mango'), ('WESC', 'WeSC'), ('GAP', 'GAP'), ('NIKESPORTSWEAR', 'Nike Sportswear'), ('VIOLETABYMANGO', 'Violeta by Mango'), ('ADIDASORIGINALS', 'adidas Originals'), ('CORTEFIEL', 'Cortefiel'), ('ZIZZI', 'Zizzi'), ('NEWLOOK', 'New Look'), ('FOGAL', 'Fogal'), ('ENVII', 'Envii'), ('ONLY', 'ONLY'), ('PIECES', 'Pieces'), ('FALKE', 'Falke'), ('FILATALL', 'Fila Tall'), ('NOISYMAY', 'Noisy May'), ('BYMALENEBIRGER', 'By Malene Birger'), ('MARCOPOLO', "Marc O'Polo"), ('FILAPETITE', 'Fila Petite'), ('IVYREVEL', 'Ivyrevel'), ('EVENODD', 'Even&Odd'), ('DESIGNERSREMIX', 'DESIGNERS REMIX'), ('FREEPEOPLE', 'Free People'), ('MINTVELVET', 'Mint Velvet'), ('GESTUZ', 'Gestuz'), ('PATRIZIAPEPE', 'Patrizia Pepe'), ('VERSACEJEANS', 'Versace Jeans'), ('MADSNRGAARD', 'Mads Nørgaard'), ('NOANOA', 'Noa Noa'), ('RIVERISLAND', 'River Island'), ('IBLUES', 'iBlues'), ('CALVINKLEINJEANS', 'Calvin Klein Jeans'), ('JDY', 'JDY'), ('URBANCLASSICS', 'Urban Classics'), ('STEFANEL', 'Stefanel'), ('QUEENMUM', 'Queen Mum'), ('AMERICANVINTAGE', 'American Vintage'), ('VILA', 'Vila'), ('FRIDAYSPROJECT', "Friday's Project"), ('RICHROYAL', 'Rich & Royal'), ('MISSGUIDED', 'Missguided'), ('NEWLOOKCURVES', 'New Look Curves'), ('ZALANDOESSENTIALSMATERNITY', 'Zalando Essentials Maternity'), ('ESPRIT', 'Esprit'), ('SET', 'SET'), ('WEEKDAY', 'Weekday'), ('TOMMYHILFIGER', 'Tommy Hilfiger'), ('AAIKO', 'Aaiko'), ('SPARKZ', 'Sparkz'), ('GLAMOROUSCURVE', 'Glamorous Curve'), ('DAISYSTREETPETITE', 'Daisy Street Petite'), ('SUPERDRY', 'Superdry'), ('LIVEUNLIMITEDLONDON', 'Live Unlimited London'), ('VEROMODA', 'Vero Moda'), ('LITTLEMISTRESS', 'Little Mistress'), ('LOVETRIANGLE', 'Love Triangle'), ('HUGO', 'HUGO'), ('LAURENRALPHLAUREN', 'Lauren Ralph Lauren'), ('TEDBAKER', 'Ted Baker'), ('MAXCO', 'MAX&Co.'), ('BENETTON', 'Benetton'), ('HILFIGERDENIM', 'Hilfiger Denim'), ('HOBBS', 'Hobbs'), ('NEEDLETHREAD', 'Needle & Thread'), ('MINTBERRY', 'mint&berry'), ('KARENMILLEN', 'Karen Millen'), ('KIOMI', 'KIOMI'), ('MOSSCOPENHAGEN', 'Moss Copenhagen'), ('WALLIS', 'Wallis'), ('LACEBEADS', 'Lace & Beads'), ('CHICHILONDON', 'Chi Chi London'), ('WALG', 'WAL G.'), ('FRENCHCONNECTION', 'French Connection'), ('CHEAPMONDAY', 'Cheap Monday'), ('GOOSECRAFT', 'Goosecraft'), ('WAREHOUSE', 'Warehouse'), ('HOLLISTERCO', 'Hollister Co.'), ('PEPEJEANS', 'Pepe Jeans'), ('ONEPIECE', 'Onepiece'), ('JUNAROSE', 'Junarose'), ('ICHI', 'ICHI'), ('OHMYLOVE', 'Oh My Love'), ('NANUSHKA', 'Nanushka'), ('MOLLYBRACKEN', 'Molly Bracken'), ('LOSTINK', 'Lost Ink'), ('KAFFE', 'Kaffe'), ('ENDLESSROSE', 'Endless Rose'), ('TRESOPHIE', 'Tresophie'), ('BANANAREPUBLIC', 'Banana Republic'), ('LEE', 'Lee'), ('MISSSELFRIDGE', 'Miss Selfridge'), ('FASHIONUNION', 'Fashion Union'), ('MODSTRM', 'Modström'), ('BOSSORANGE', 'BOSS Orange'), ('DOROTHYPERKINSPETITE', 'Dorothy Perkins Petite'), ('WVEN', 'Wåven'), ('TRUERELIGION', 'True Religion'), ('CLUBMONACO', 'Club Monaco'), ('SECONDFEMALE', 'Second Female'), ('COAST', 'Coast'), ('LASCANA', 'LASCANA'), ('TALKABOUT', 'talkabout'), ('THREEFLOOR', 'Three Floor'), ('QSDESIGNEDBY', 'Q/S designed by'), ('GSTAR', 'G-Star'), ('SELECTEDFEMME', 'Selected Femme'), ('TWINTIP', 'TWINTIP'), ('LACEBEADSTALL', 'Lace & Beads Tall'), ('STINEGOYA', 'Stine Goya'), ('FASHIONUNIONPETITE', 'Fashion Union Petite'), ('THEKOOPLES', 'The Kooples'), ('ELISABETTAFRANCHI', 'Elisabetta Franchi'), ('ZALANDOESSENTIALSCURVY', 'Zalando Essentials Curvy'), ('BARDOT', 'Bardot'), ('IVYPARK', 'Ivy Park'), ('LOVEMOSCHINO', 'Love Moschino'), ('TOPSHOPTALL', 'Topshop Tall'), ('EVANS', 'Evans'), ('DIESEL', 'Diesel'), ('DRDENIM', 'Dr.Denim'), ('JUSTCAVALLI', 'Just Cavalli'), ('BIKBOK', 'Bik Bok'), ('NEWLOOKTALL', 'New Look Tall'), ('LTB', 'LTB'), ('NUDIEJEANS', 'Nudie Jeans'), ('LUHTA', 'Luhta'), ('NAFNAF', 'NAF NAF'), ('MINIMUM', 'Minimum'), ('RAINS', 'Rains'), ('ILSEJACOBSEN', 'Ilse Jacobsen'), ('GUESS', 'Guess'), ('STEVEJYONIPSJYP', 'Steve J & Yoni P / SJYP'), ('PSBYPAULSMITH', 'PS by Paul Smith'), ('VERSACECOLLECTION', 'Versace Collection'), ('VANS', 'Vans'), ('CHAMPIONREVERSEWEAVE', 'Champion Reverse Weave'), ('RAGWEAR', 'Ragwear'), ('WOODWOOD', 'Wood Wood'), ('JUVIA', 'Juvia'), ('BROOKLYNSOWNBYROCAWEAR', "Brooklyn's Own by Rocawear"), ('SOMEDAY', 'someday.'), ('OPUS', 'Opus'), ('FENTYPUMABYRIHANNA', 'Fenty PUMA by Rihanna'), ('REEBOKCLASSIC', 'Reebok Classic'), ('TOMTAILORDENIM', 'TOM TAILOR DENIM'), ('KARLLAGERFELD', 'KARL LAGERFELD'), ('REPLAY', 'Replay'), ('HOUSEOFSUNNY', 'House of Sunny'), ('CONVERSE', 'Converse'), ('COMMA', 'comma'), ('LOVEWAIT', 'LOVE2WAIT'), ('LOSTINKPLUS', 'Lost Ink Plus'), ('PLEINSUDJEANIUS', 'Plein Sud Jeanius'), ('MOSMOSH', 'Mos Mosh'), ('CREAM', 'Cream'), ('DESIGUAL', 'Desigual'), ('PUMA', 'Puma'), ('BILLABONG', 'Billabong'), ('LAURENRALPHLAURENWOMAN', 'Lauren Ralph Lauren Woman'), ('WEEKENDMAXMARA', 'WEEKEND MaxMara'), ('ALLSAINTS', 'AllSaints'), ('JCREW', 'J.CREW'), ('NOISYMAYPETITE', 'Noisy May Petite'), ('YAS', 'YAS'), ('YASTALL', 'YAS Tall'), ('VEROMODATALL', 'Vero Moda Tall'), ('ONLYPETITE', 'Only Petite'), ('NDDAY', '2nd Day'), ('IVYOAK', 'IVY & OAK'), ('KIOMITALL', 'KIOMI TALL'), ('ELLESSE', 'Ellesse'), ('FILA', 'Fila'), ('WHISTLES', 'Whistles'), ('BRUUNSBAZAAR', 'Bruuns Bazaar'), ('SOLIVERREDLABEL', 's.Oliver RED LABEL'), ('LIQUORNPOKERTALL', 'Liquor N Poker Tall'), ('DENHAM', 'Denham'), ('MAVI', 'Mavi'), ('WRANGLER', 'Wrangler'), ('FORALLMANKIND', '7 for all mankind'), ('GLAMOROUS', 'Glamorous'), ('LEVISPLUS', "Levi's® Plus"), ('LOISJEANS', 'LOIS Jeans'), ('CITYCHIC', 'City Chic'), ('MISSGUIDEDPLUS', 'Missguided Plus'), ('LIQUORNPOKERCURVE', 'Liquor N Poker Curve'), ('WRANGLERBYPETERMAX', 'Wrangler by Peter Max'), ('CIRCLEOFTRUST', 'Circle of Trust'), ('FREEMANTPORTER', 'Freeman T. Porter'), ('CULTURE', 'Culture'), ('CARTOON', 'Cartoon'), ('MONKEEGENES', 'Monkee Genes'), ('SCOTCHSODA', 'Scotch & Soda'), ('LETEMPSDESCERISES', 'Le Temps Des Cerises'), ('DENIMSUPPLYRALPHLAUREN', 'Denim & Supply Ralph Lauren'), ('WONHUNDRED', 'Won Hundred'), ('OBEYCLOTHING', 'Obey Clothing'), ('FRAMEDENIM', 'Frame Denim'), ('WEMOTO', 'Wemoto'), ('KAPORAL', 'Kaporal'), ('KINGSOFINDIGO', 'Kings Of Indigo'), ('SAMSESAMSE', 'Samsøe & Samsøe'), ('EXPRESSO', 'Expresso'), ('KENGSTAR', 'Kengstar'), ('BEEDGY', 'Be Edgy'), ('ISLAIBIZABONITA', 'Isla Ibiza Bonita'), ('LIUJOJEANS', 'Liu Jo Jeans'), ('LEVISMADECRAFTED', "Levi's® Made & Crafted"), ('JBRAND', 'J Brand'), ('NEWLOOKPETITE', 'New Look Petite'), ('HIS', 'H.I.S'), ('CLOSED', 'CLOSED'), ('BAUMUNDPFERDGARTEN', 'Baum und Pferdgarten'), ('HOLZWEILER', 'Holzweiler'), ('TOPSHOPPETITE', 'Topshop Petite'), ('LACEBEADSPETITE', 'Lace & Beads Petite'), ('MBYM', 'mbyM'), ('MALAIKARAISS', 'MALAIKARAISS'), ('PINKO', 'Pinko'), ('PHASEEIGHT', 'Phase Eight'), ('TOMTAILOR', 'TOM TAILOR'), ('CARHARTTWIP', 'Carhartt WIP'), ('BARBOUR', 'Barbour'), ('PAULEKA', 'Paule Ka'), ('NAVYLONDON', 'Navy London'), ('OBJECT', 'Object'), ('VANESSABRUNO', 'Vanessa Bruno'), ('HOUSEOFDAGMAR', 'House of Dagmar'), ('ELVI', 'Elvi'), ('MISSGUIDEDPETITE', 'Missguided Petite'), ('SPORTMAXCODE', 'Sportmax Code'), ('MORGAN', 'Morgan'), ('CLOSET', 'Closet'), ('JILSANDERNAVY', 'Jil Sander Navy'), ('DRYKORN', 'DRYKORN'), ('TIBI', 'Tibi'), ('FILIPPAK', 'Filippa K'), ('OAKWOOD', 'Oakwood'), ('VSP', 'VSP'), ('MAZE', 'Maze'), ('FREAKYNATION', 'Freaky Nation'), ('GLAMOROUSTALL', 'Glamorous Tall'), ('NAPAPIJRI', 'Napapijri'), ('ONEMORESTORY', 'one more story'), ('RELIGION', 'Religion'), ('SISLEY', 'Sisley'), ('SCHOTTNYC', 'Schott NYC'), ('DRYLAKE', 'Dry Lake'), ('JLINDEBERG', 'J.LINDEBERG'), ('GIPSY', 'Gipsy'), ('DKNY', 'DKNY'), ('TAMARIS', 'Tamaris'), ('IBANA', 'Ibana'), ('FREEQUENT', 'Freequent'), ('DOROTHYPERKINSTALL', 'Dorothy Perkins Tall'), ('PAULJOESISTER', 'Paul & Joe Sister'), ('PIERONE', 'Pier One'), ('BUFFALO', 'Buffalo'), ('KMB', 'KMB'), ('STEVEMADDEN', 'Steve Madden'), ('SKECHERS', 'Skechers'), ('SOREL', 'Sorel'), ('MINELLI', 'Minelli'), ('BILLIBI', 'Billi Bi'), ('MARCOTOZZI', 'Marco Tozzi'), ('PALLADIUM', 'Palladium'), ('BRUNOPREMI', 'Bruno Premi'), ('MAIPIUSENZA', 'Mai Piu Senza'), ('TIMBERLAND', 'Timberland'), ('AS', 'A.S.98'), ('AIGLE', 'Aigle'), ('UGG', 'UGG'), ('CLARKS', 'Clarks'), ('BULLBOXER', 'Bullboxer'), ('LESTROPZIENNESPARMBELARBI', 'Les Tropéziennes par M Belarbi'), ('ZIGN', 'Zign'), ('PANAMAJACK', 'Panama Jack'), ('BIANCO', 'Bianco'), ('BRONX', 'Bronx'), ('CALVINKLEIN', 'Calvin Klein'), ('GANT', 'GANT'), ('MUSTANG', 'Mustang'), ('CAPRICE', 'Caprice'), ('ALDO', 'ALDO'), ('AQUATALIA', 'Aquatalia'), ('PARFOIS', 'PARFOIS'), ('GEOX', 'Geox'), ('MIISTA', 'MIISTA'), ('LOSTINKWIDEFIT', 'Lost Ink Wide Fit'), ('BOSS', 'BOSS'), ('PRETTYBALLERINAS', 'Pretty Ballerinas'), ('KENNELSCHMENGER', 'Kennel + Schmenger'), ('CALLITSPRING', 'Call it Spring'), ('HEADOVERHEELSBYDUNE', 'Head over Heels by Dune'), ('FAITH', 'Faith'), ('HGL', 'Högl'), ('NEWLOOKWIDEFIT', 'New Look Wide Fit'), ('FURLA', 'Furla'), ('GABOR', 'Gabor'), ('REBECCAMINKOFF', 'Rebecca Minkoff'), ('DOROTHYPERKINSWIDEFIT', 'Dorothy Perkins Wide Fit'), ('RAID', 'RAID'), ('VAGABOND', 'Vagabond'), ('PETERKAISER', 'Peter Kaiser'), ('ONLYSHOES', 'ONLY SHOES'), ('OFFICE', 'Office'), ('BEMINE', 'Be Mine'), ('DUNELONDON', 'Dune London'), ('VIVIENNEWESTWOODANGLOMANIAMELISSA', 'Vivienne Westwood Anglomania + Melissa'), ('MADDENGIRL', 'Madden Girl'), ('KENDALLKYLIE', 'KENDALL + KYLIE'), ('MTNG', 'mtng'), ('SLACKSCO', 'Slacks & Co.'), ('LOVECHILD', 'Lovechild'), ('LACOSTE', 'Lacoste'), ('ABERCROMBIEFITCH', 'Abercrombie & Fitch'), ('UNDERARMOUR', 'Under Armour'), ('SPM', 'SPM'), ('MENBUR', 'Menbur'), ('KGBYKURTGEIGER', 'KG by Kurt Geiger'), ('ALBERTOZAGO', 'Alberto Zago'), ('CHIEMIHARA', 'Chie Mihara'), ('CLARKSORIGINALS', 'Clarks Originals'), ('ANNAFIELDPREMIUM', 'Anna Field Premium'), ('DRMARTENS', 'Dr. Martens'), ('ANOTHERPROJECT', 'another project'), ('ARMANICOLLEZIONI', 'Armani Collezioni'), ('KATYPERRY', 'Katy Perry'), ('ARENA', 'Arena'), ('CROCS', 'Crocs'), ('KATMACONIE', 'Kat Maconie'), ('HAVAIANAS', 'Havaianas'), ('SENSO', 'Senso'), ('ADIDASPERFORMANCE', 'adidas Performance'), ('ASICS', 'ASICS'), ('REEBOK', 'Reebok'), ('KAPPA', 'Kappa'), ('EVENODDACTIVE', 'Even&Odd active'), ('MIZUNO', 'Mizuno'), ('SCARPA', 'Scarpa'), ('NIKEPERFORMANCE', 'Nike Performance'), ('TEVA', 'Teva'), ('SALOMON', 'Salomon'), ('SKECHERSPERFORMANCE', 'Skechers Performance'), ('COLUMBIA', 'Columbia'), ('THENORTHFACE', 'The North Face'), ('VIKING', 'Viking'), ('CHAMPION', 'Champion'), ('AKU', 'Aku'), ('SAUCONY', 'Saucony'), ('HUMMEL', 'Hummel'), ('ONEILL', "O'Neill"), ('ADIDASBYSTELLAMCCARTNEY', 'adidas by Stella McCartney'), ('MILLET', 'Millet'), ('FINERYLONDON', 'Finery London'), ('KANNA', 'Kanna'), ('CAMPER', 'Camper'), ('VEJA', 'Veja'), ('NIKESB', 'Nike SB'), ('SUPERGA', 'Superga'), ('ONITSUKATIGER', 'Onitsuka Tiger'), ('NOVESTA', 'Novesta'), ('FELMINI', 'Felmini'), ('SISTERJANE', 'Sister Jane'), ('MARCOPOLODENIM', "Marc O'Polo DENIM"), ('JUSTFEMALE', 'JUST FEMALE'), ('JOA', 'J.O.A'), ('MARKUSLUPFER', 'Markus Lupfer'), ('MIDNIGHT', '12 Midnight'), ('EQUIPMENT', 'Equipment'), ('CATWALKJUNKIE', 'Catwalk Junkie'), ('SEIDENSTICKER', 'Seidensticker'), ('ANNAFIELDCURVY', 'Anna Field Curvy'), ('SOYACONCEPT', 'Soyaconcept'), ('HERRLICHER', 'Herrlicher'), ('ISCENERY', 'I.scenery'), ('ZOEKARSSEN', 'Zoe Karssen'), ('VANLAACK', 'van Laack'), ('KOOKAI', 'Kookai'), ('MOREMORE', 'More & More'), ('SANDCOPENHAGEN', 'Sand Copenhagen'), ('GLAMOROUSPETITE', 'Glamorous Petite'), ('CUSTOMMADE', 'Custommade'), ('ROSEMUNDE', 'Rosemunde'), ('ESCADASPORT', 'Escada Sport'), ('ROXY', 'Roxy'), ('SOLIVERBLACKLABEL', 's.Oliver BLACK LABEL'), ('NEWLOOKMATERNITY', 'New Look Maternity'), ('SAINTTROPEZ', 'Saint Tropez'), ('KARENBYSIMONSEN', 'Karen by Simonsen'), ('ESPRITCOLLECTION', 'Esprit Collection'), ('TAIFUN', 'Taifun'), ('DOROTHYPERKINSCURVE', 'Dorothy Perkins Curve'), ('ADIA', 'ADIA'), ('MINTBERRYMOM', 'mint&berry mom'), ('FASHIONUNIONTALL', 'Fashion Union Tall'), ('STRENESSE', 'Strenesse'), ('PARTTWO', 'Part Two'), ('TIFFOSI', 'Tiffosi'), ('LAVISHALICE', 'Lavish Alice'), ('PERSONABYMARINARINALDI', 'Persona by Marina Rinaldi'), ('TIGHA', 'Tigha'), ('SPRINGFIELD', 'Springfield'), ('TEDDYSMITH', 'Teddy Smith'), ('DPMATERNITY', 'DP Maternity'), ('COMMACASUALIDENTITY', 'comma casual identity'), ('OPENEND', 'Open End'), ('EMILYVANDENBERGH', 'Emily van den Bergh'), ('PRINCESSGOESHOLLYWOOD', 'Princess goes Hollywood'), ('NMPH', 'Nümph'), ('GAUDI', 'Gaudi'), ('INWEAR', 'InWear'), ('WALLISPETITE', 'Wallis Petite'), ('PORTS', 'Ports 1961'), ('SPRINGMATERNITY', 'Spring Maternity'), ('DAYBIRGERETMIKKELSEN', 'DAY Birger et Mikkelsen'), ('NEONROSE', 'Neon Rose'), ('BETTYCO', 'Betty & Co'), ('GAPMATERNITY', 'GAP Maternity'), ('VIVIENNEWESTWOODANGLOMANIA', 'Vivienne Westwood Anglomania'), ('SOFTREBELS', 'Soft Rebels'), ('OVS', 'OVS'), ('RUEDEFEMME', 'Rue de Femme'), ('MRZ', 'MRZ'), ('ENGLISHFACTORY', 'English Factory'), ('OASIS', 'Oasis'), ('THEKOOPLESSPORT', 'The Kooples SPORT'), ('ESPRITMATERNITY', 'Esprit Maternity'), ('MAMALICIOUS', 'MAMALICIOUS'), ('PAULINA', 'Paulina'), ('ISABELLAOLIVER', 'ISABELLA OLIVER'), ('BELLYBUTTON', 'bellybutton'), ('ANNAFIELDMAMA', 'Anna Field MAMA'), ('FASHION', '9Fashion'), ('SUPERMOM', 'Supermom'), ('UNOPIUUNO', 'Uno Piu Uno'), ('BAUKJEN', 'Baukjen'), ('LIEBESKIND', 'Liebeskind'), ('COMPAAFANTSTICA', 'Compañía fantástica'), ('VEROMODAPETITE', 'Vero Moda Petite'), ('TWISTTANGO', 'Twist & Tango'), ('LIQUORNPOKER', 'Liquor N Poker'), ('TOMJOULE', 'Tom Joule'), ('KHUJO', 'khujo'), ('STUDIO', 'Studio 75'), ('JETTE', 'JETTE'), ('DAISYSTREETPLUS', 'Daisy Street Plus'), ('STUDIO', 'Studio 8'), ('CAMEOCOLLECTIVE', 'Cameo Collective'), ('JOSEPHINECO', 'Josephine & Co'), ('HUNKYDORY', 'Hunkydory'), ('CURRENTELLIOTT', 'Current/Elliott'), ('ZACZACPOSEN', 'ZAC Zac Posen'), ('MOVES', 'Moves'), ('MARELLA', 'Marella'), ('ICEBERG', 'Iceberg'), ('BOUTIQUEMOSCHINO', 'Boutique Moschino'), ('IKKS', 'IKKS'), ('MARCIANOLOSANGELES', 'MARCIANO LOS ANGELES'), ('STORMMARIE', 'Storm & Marie'), ('ESCADA', 'Escada'), ('MISSGUIDEDTALL', 'Missguided Tall'), ('NORR', 'NORR'), ('ARMANIEXCHANGE', 'Armani Exchange'), ('TRUEDECADENCE', 'True Decadence'), ('VIVEMARIA', 'Vive Maria'), ('ONETEASPOON', 'One Teaspoon'), ('SEEUSOON', 'See u Soon'), ('ENVIEDEFRAISE', 'Envie de Fraise'), ('WHITESTUFF', 'White Stuff'), ('LOUCHE', 'Louche'), ('TIGEROFSWEDENJEANS', 'Tiger of Sweden Jeans'), ('SOAKEDINLUXURY', 'Soaked in Luxury'), ('DANIELHECHTER', 'Daniel Hechter'), ('SONIABYSONIARYKIEL', 'Sonia by Sonia Rykiel'), ('NOPPIES', 'Noppies'), ('SECONDSCRIPTCURVE', 'Second Script Curve'), ('DERHY', 'Derhy'), ('SOFIESCHNOOR', 'Sofie Schnoor'), ('GAASTRA', 'Gaastra'), ('AMORPHBERLIN', 'Amorph Berlin'), ('MOGUL', 'Mogul'), ('ANDLESS', 'And Less'), ('REISS', 'Reiss'), ('NOISYMAYTALL', 'Noisy May Tall'), ('DEREKLAMCROSBY', 'Derek Lam 10 Crosby'), ('POMKIN', 'Pomkin'), ('ARMORLUX', 'Armor lux'), ('SMARTEEZ', 'Smarteez'), ('PINKOJEAN', 'Pinko Jean'), ('PATAGONIA', 'Patagonia'), ('DOUBLEAGENT', 'Double Agent'), ('GINATRICOT', 'Gina Tricot'), ('MAXMARALEISURE', 'Max Mara Leisure'), ('NORMAKAMALI', 'Norma Kamali'), ('BOOB', 'Boob'), ('PIETROBRUNELLI', 'Pietro Brunelli'), ('MAJESTIC', 'Majestic'), ('FORLOVELEMONS', 'For Love & Lemons'), ('CHICHILONDONPETITE', 'Chi Chi London Petite'), ('JARLO', 'Jarlo'), ('MMISSONI', 'M Missoni'), ('MASCARA', 'Mascara'), ('CHICHILONDONCURVY', 'Chi Chi London Curvy'), ('CHICHILONDONTALL', 'Chi Chi London Tall'), ('HYPE', 'Hype'), ('SMASH', 'Smash'), ('ADRIANNAPAPELL', 'Adrianna Papell'), ('WHYRED', 'Whyred'), ('LAONA', 'Laona'), ('MYMASCARACURVES', 'My Mascara Curves'), ('FROCKANDFRILL', 'Frock and Frill'), ('TFNC', 'TFNC'), ('PAPERDOLLS', 'Paper Dolls'), ('LEVISLINE', "Levi's® Line 8"), ('CAROLINACAVOUR', 'Carolina Cavour'), ('LUXUARFASHION', 'Luxuar Fashion'), ('JADEDLONDON', 'Jaded London'), ('LITTLEMISTRESSCURVY', 'Little Mistress Curvy'), ('KINGLOUIE', 'King Louie'), ('DAISYSTREET', 'Daisy Street'), ('RAGWEARPLUS', 'Ragwear Plus'), ('SWING', 'Swing'), ('SECONDSCRIPTPETITE', 'Second Script Petite'), ('UNIQUE', 'Unique'), ('BCBGENERATION', 'BCBGeneration'), ('LITTLEMISTRESSPETITE', 'Little Mistress Petite'), ('SARA', "Sara'"), ('LACEBEADSCURVY', 'Lace & Beads Curvy'), ('SWINGCURVE', 'Swing Curve'), ('PAPERDOLLSCURVY', 'Paper Dolls Curvy'), ('LITTLEWHITELIES', 'Little White Lies'), ('RACHELZOE', 'Rachel Zoe'), ('YOUNGCOUTUREBYBARBARASCHWARZER', 'Young Couture by Barbara Schwarzer'), ('IVKO', 'Ivko'), ('BCBGMAXAZRIA', 'BCBGMAXAZRIA'), ('PLEINSUD', 'Plein Sud'), ('PIERREBALMAIN', 'Pierre Balmain'), ('BENCH', 'Bench'), ('TRUEVIOLET', 'True Violet'), ('MISSPARISIENNE', 'Miss Parisienne'), ('MADDERSON', 'Madderson'), ('CLOSETCURVES', 'Closet Curves'), ('FTCCASHMERE', 'FTC Cashmere'), ('HALSTONHERITAGE', 'Halston Heritage'), ('PRANA', 'PrAna'), ('FROCKANDFRILLCURVE', 'Frock and Frill Curve'), ('PINKCLOVE', 'Pink Clove'), ('REPEAT', 'Repeat'), ('CACHAREL', 'Cacharel'), ('ROBERTOCOLLINA', 'Roberto Collina'), ('LACOSTELIVE', 'Lacoste LIVE'), ('VOLCOM', 'Volcom'), ('THERAGGEDPRIEST', 'The Ragged Priest'), ('INTROPIA', 'Intropia'), ('ANECDOTE', 'Anecdote'), ('FRACOMINA', 'Fracomina'), ('PETITBATEAU', 'Petit Bateau'), ('LOREAK', 'Loreak'), ('GWYNEDDS', 'Gwynedds'), ('THEFIFTHLABEL', 'The Fifth Label'), ('NDONE', '2ndOne'), ('CITIZENSOFHUMANITY', 'Citizens of Humanity'), ('FIVEUNITS', 'Fiveunits'), ('AGJEANS', 'AG Jeans'), ('MAC', 'MAC'), ('MOTHER', 'Mother'), ('DRDENIMPETITE', 'Dr.Denim Petite'), ('LIQUORNPOKERPETITE', 'Liquor N Poker Petite'), ('DRDENIMTALL', 'Dr.Denim Tall'), ('HARMONY', 'Harmony'), ('FORVERT', 'Forvert'), ('BLAUER', 'Blauer'), ('BOGNER', 'Bogner'), ('BELLFIELD', 'Bellfield'), ('JACKWOLFSKIN', 'Jack Wolfskin'), ('ELVINE', 'Elvine'), ('KWAY', 'K-Way'), ('BOMBOOGIE', 'Bomboogie'), ('PACKMACK', 'Packmack'), ('HOODLAMB', 'Hoodlamb'), ('HELLYHANSEN', 'Helly Hansen'), ('HAGLFS', 'Haglöfs'), ('LAFUMA', 'Lafuma'), ('BRIXTOL', 'Brixtol'), ('DIDRIKSONS', 'Didriksons'), ('FRIEDAFREDDIES', 'Frieda & Freddies'), ('CANADIANCLASSICS', 'Canadian Classics'), ('DERBE', 'Derbe'), ('ALPHAINDUSTRIES', 'Alpha Industries'), ('VAUDE', 'Vaude'), ('MERU', 'Meru'), ('MARMOT', 'Marmot'), ('PEUTEREY', 'Peuterey'), ('SPOOM', 'Spoom'), ('COVERTOVERT', 'Covert Overt'), ('CRAGHOPPERS', 'Craghoppers'), ('SVEA', 'Svea'), ('VENTCOUVERT', 'Ventcouvert'), ('PENDLETON', 'Pendleton'), ('REGATTA', 'Regatta'), ('SALEWA', 'Salewa'), ('SONIUSH', 'Soniush'), ('ZIENER', 'Ziener'), ('BOMBERS', 'Bombers'), ('PYUA', 'PYUA'), ('GOREBIKEWEAR', 'Gore Bike Wear'), ('ICEPEAK', 'Icepeak'), ('BERGHAUS', 'Berghaus'), ('CMP', 'CMP'), ('MAMMUT', 'Mammut'), ('SUPERNATURAL', 'super.natural'), ('SMARTWOOL', 'Smartwool'), ('GIGADX', 'G.I.G.A. DX'), ('POLORALPHLAURENGOLF', 'Polo Ralph Lauren Golf'), ('NIKEGOLF', 'Nike Golf'), ('PEARLIZUMI', 'Pearl Izumi'), ('CRAFT', 'Craft'), ('BERGANS', 'Bergans'), ('DYNAFIT', 'Dynafit'), ('ONLYPLAY', 'Only Play'), ('RAISKI', 'Raiski'), ('BLACKDIAMOND', 'Black Diamond'), ('KARITRAA', 'KariTraa'), ('FRAAS', 'Fraas'), ('JUICYCOUTURE', 'Juicy Couture'), ('ZIMTSTERN', 'Zimtstern'), ('ZALANDOSPORTS', 'Zalando Sports'), ('JUICYCOUTUREPLUS', 'Juicy Couture Plus'), ('GRACE', 'Grace'), ('SUNDRY', 'Sundry'), ('PACOGIL', 'Paco Gil'), ('LEMONJELLY', 'LEMON JELLY'), ('BLACKSTONE', 'Blackstone'), ('ARA', 'ara'), ('SANMARINA', 'San Marina'), ('BRENDAZARO', 'Brenda Zaro'), ('JENNY', 'Jenny'), ('JONAK', 'Jonak'), ('EMUAUSTRALIA', 'EMU Australia'), ('SHABBIESAMSTERDAM', 'Shabbies Amsterdam'), ('COOLWAY', 'Coolway'), ('UNISA', 'Unisa'), ('LILIMILL', 'lilimill'), ('XTI', 'XTI'), ('COLORSOFCALIFORNIA', 'Colors of California'), ('KANGAROOS', 'KangaROOS'), ('LAUTRECHOSE', 'L’Autre Chose'), ('DIVINEFACTORY', 'Divine Factory'), ('PINTODIBLU', 'Pinto Di Blu'), ('KENTUCKYSWESTERN', "Kentucky's Western"), ('RAPISARDI', 'Rapisardi'), ('PONSQUINTANA', 'Pons Quintana'), ('EVERYBODY', 'Everybody'), ('LAMICA', 'Lamica'), ('DARKWOOD', 'Darkwood'), ('PRIMADONNACOLLECTION', 'Primadonna Collection'), ('OXITALY', 'Oxitaly'), ('SOFTCLOX', 'Softclox'), ('BENATURAL', 'Be Natural'), ('BEBO', 'BEBO'), ('SNEAKYSTEVE', 'Sneaky Steve'), ('HOMERS', 'Homers'), ('DNAFOOTWEARBV', 'DNA Footwear BV'), ('JEFFREYCAMPBELL', 'Jeffrey Campbell'), ('REFRESH', 'Refresh'), ('JANA', 'Jana'), ('HUNTER', 'Hunter'), ('ALMAENPENA', 'Alma en Pena'), ('ECCO', 'ecco'), ('KENNETHCOLENEWYORK', 'Kenneth Cole New York'), ('KAMIK', 'Kamik'), ('CASADEI', 'Casadei'), ('MALO', 'MA&LO'), ('PERLATO', 'PERLATO'), ('ELNATURALISTA', 'El Naturalista'), ('ANGULUS', 'ANGULUS'), ('GIOSEPPO', 'Gioseppo'), ('POLLINI', 'Pollini'), ('LAZAMANI', 'Lazamani'), ('NOCLAIM', 'Noclaim'), ('PURALOPEZ', 'Pura Lopez'), ('KICKERS', 'Kickers'), ('HUB', 'HUB'), ('TRUSSARDIJEANS', 'Trussardi Jeans'), ('CASHOTT', "Ca'Shott"), ('WEEKEND', 'Weekend'), ('DONNACAROLINA', 'Donna Carolina'), ('TAMARISHEARTSOLE', 'Tamaris Heart & Sole'), ('MARIP', 'Maripé'), ('AEYDE', 'Aeyde'), ('STEFFENSCHRAUT', 'Steffen Schraut'), ('LYSSS', 'Élysèss'), ('ANDRE', 'Andre'), ('BEONLY', 'Be Only'), ('CAFNOIR', 'CAFèNOIR'), ('FREDDELABRETONIERE', 'Fred de la Bretoniere'), ('MJUS', 'MJUS'), ('PEDROMIRALLES', 'Pedro Miralles'), ('CANDICECOOPER', 'Candice Cooper'), ('CTWLK', 'CTWLK'), ('SEEBYCHLO', 'See by Chloé'), ('VITTILOVE', 'Vitti Love'), ('DACHSTEIN', 'Dachstein'), ('MOONBOOT', 'Moon Boot'), ('AVECLESFILLES', 'Avec Les Filles'), ('NEOSENS', 'Neosens'), ('FERSENGOLD', 'Fersengold'), ('HARLEYDAVIDSON', 'Harley Davidson'), ('KEEN', 'Keen'), ('NINEWEST', 'Nine West'), ('SCAPA', 'Scapa'), ('BIRKENSTOCK', 'Birkenstock'), ('SCHUTZ', 'Schutz'), ('TOSCABLU', 'Tosca Blu'), ('CASSISCTEDAZUR', "Cassis côte d'azur"), ('SHELLYSLONDON', 'Shellys London'), ('MISSKG', 'Miss KG'), ('SANITA', 'Sanita'), ('PAVEMENT', 'Pavement'), ('FRANCORUSSONAPOLI', 'Franco Russo Napoli'), ('JESSICASIMPSON', 'Jessica Simpson'), ('HELIA', 'Helia'), ('SHOETHEBEAR', 'Shoe The Bear'), ('FITFLOP', 'FitFlop'), ('UMAPARKER', 'UMA PARKER'), ('TATAITALIA', 'Tata Italia'), ('PALOMABARCEL', 'Paloma Barceló'), ('LAURABIAGIOTTI', 'Laura Biagiotti'), ('COSMOPARIS', 'Cosmoparis'), ('ERIKAROCCHI', 'Erika Rocchi'), ('LIPSY', 'Lipsy'), ('DOCKERSBYGERLI', 'Dockers by Gerli'), ('MARCELOSTERTAGXTAMARIS', 'Marcel Ostertag x Tamaris'), ('JCPLAY', 'JC Play'), ('JOSHUASANDERS', 'Joshua Sanders'), ('FRANCESCOMILANO', 'Francesco Milano'), ('SIGERSONMORRISON', 'Sigerson Morrison'), ('TOMS', 'TOMS'), ('HASSIA', 'HASSIA'), ('GARDENIA', 'Gardenia'), ('DUNELONDONWIDEFIT', 'Dune London WIDE FIT'), ('FIOREDILUCIAMILANO', 'Fiore di Lucia Milano'), ('FORNARINA', 'Fornarina'), ('POPA', 'POPA'), ('LOLARAMONA', 'Lola Ramona'), ('STYLESNOB', 'Stylesnob'), ('RAS', 'RAS'), ('LODI', 'Lodi'), ('YOSISAMRA', 'Yosi Samra'), ('MELISSA', 'Melissa'), ('GADEA', 'Gadea'), ('HIRSCHKOGEL', 'Hirschkogel'), ('SAMEDELMAN', 'Sam Edelman'), ('PARADOXLONDONPINK', 'Paradox London Pink'), ('NINASHOES', 'Nina Shoes'), ('CARVELA', 'Carvela'), ('IMAGINEVINCECAMUTO', 'Imagine Vince Camuto'), ('LUCAGROSSI', 'Luca Grossi'), ('TORAL', 'Toral'), ('ESPADRIJLORIGINALE', 'Espadrij l´originale'), ('EEIGHT', 'Eeight'), ('FRATELLIROSSETTI', 'Fratelli Rossetti'), ('RIVERISLANDWIDEFIT', 'River Island Wide Fit'), ('VICTORIASHOES', 'Victoria Shoes'), ('GHBASSCO', 'G. H. Bass & Co.'), ('PROENZASCHOULER', 'Proenza Schouler'), ('MCQALEXANDERMCQUEEN', 'McQ Alexander McQueen'), ('CASTAER', 'Castañer'), ('KIO', 'Kio'), ('STONEFLY', 'Stonefly'), ('ZADIGVOLTAIRE', 'Zadig & Voltaire'), ('VINCECAMUTO', 'Vince Camuto'), ('MSGM', 'MSGM'), ('FLIPFLOP', 'flip*flop'), ('BENJAMINADAMS', 'Benjamin Adams'), ('MINNETONKA', 'Minnetonka'), ('LAURAVITA', 'LAURA VITA'), ('FLYLONDON', 'Fly London'), ('NONAME', 'No Name'), ('TKEES', 'Tkees'), ('IVYKIRZHNER', 'Ivy Kirzhner'), ('MABUBYMARIABK', 'MABU By Maria Bk'), ('CHINESELAUNDRY', 'Chinese Laundry'), ('IPANEMA', 'Ipanema'), ('KARSTON', 'Karston'), ('PAPILLIO', 'Papillio'), ('EMMAGO', 'Emma Go'), ('UZURII', 'Uzurii'), ('ISAPERAMYKONOS', 'Isapera Mykonos'), ('LOEFFLERRANDALL', 'Loeffler Randall'), ('PACOMENA', 'Paco Mena'), ('GENUINS', 'Genuins'), ('MENTOR', 'Mentor'), ('CIMARRON', 'Cimarron'), ('OPENINGCEREMONY', 'Opening Ceremony'), ('CORALBLUE', 'Coral Blue'), ('VIDORRETA', 'Vidorreta'), ('MELVINHAMILTON', 'Melvin & Hamilton'), ('ROYALREPUBLIQ', 'Royal RepubliQ'), ('NATURALWORLD', 'Natural World'), ('KEDS', 'Keds'), ('COLLEGE', 'COLLEGE'), ('SEVENBOOTLANE', 'Seven Boot Lane'), ('NATIVE', 'Native'), ('PAEZ', 'Paez'), ('MARUTI', 'Maruti'), ('HBYHUDSON', 'H by Hudson'), ('HUF', 'HUF'), ('SKECHERSSPORT', 'Skechers Sport'), ('TENPOINTS', 'Ten Points'), ('INUOVO', 'Inuovo'), ('JAMESPERSE', 'James Perse'), ('LOWA', 'Lowa'), ('MERRELL', 'Merrell'), ('HITEC', 'Hi-Tec'), ('NEWBALANCE', 'New Balance'), ('ADIDASGOLF', 'adidas Golf'), ('SANUK', 'Sanuk'), ('SHIMANO', 'Shimano'), ('VIBRAMFIVEFINGERS', 'Vibram Fivefingers'), ('LOTTO', 'Lotto'), ('INOV', 'Inov-8'), ('BOGS', 'Bogs'), ('DCSHOES', 'DC Shoes'), ('KEMPA', 'Kempa'), ('PUMAGOLF', 'Puma Golf'), ('ASICSTIGER', 'Asics Tiger'), ('SUPRA', 'Supra'), ('BRITISHKNIGHTS', 'British Knights'), ('BLEND', 'Blend'), ('LECOQSPORTIF', 'le coq sportif'), ('LEANDROLOPES', 'Leandro Lopes'), ('DIADORA', 'Diadora'), ('GARMENTPROJECT', 'GARMENT PROJECT'), ('PIOLA', 'Piola'), ('KSWISS', 'K-SWISS'), ('BOXFRESH', 'Boxfresh'), ('PLDMBYPALLADIUM', 'P-L-D-M by Palladium'), ('YELLOWCAB', 'Yellow Cab'), ('MICHALSKY', 'Michalsky'), ('WODEN', 'Woden'), ('MOAMASTEROFARTS', 'MOA - Master of Arts'), ('PROJECTDELRAY', 'Project Delray'), ('IPPONVINTAGE', 'Ippon Vintage'), ('BUGATTI', 'Bugatti')], max_length=255)),
                ('gender', models.CharField(choices=[('women', 'women'), ('men', 'men'), ('(trans', 'trans')], max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('product_description', models.CharField(max_length=255)),
                ('product_title', models.CharField(max_length=255)),
                ('source', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
                ('path', models.CharField(max_length=255)),
                ('checksum', models.CharField(max_length=255)),
                ('garment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Styling.Garments')),
            ],
        ),
        migrations.CreateModel(
            name='ImageURLs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=255)),
                ('garment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Styling.Garments')),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_category', models.CharField(choices=[('WOMENSCLOTHINGPLAYSUITSJUMPSUITS', 'womens-clothing-playsuits-jumpsuits'), ('WOMENSCLOTHINGJACKETSDENIMJACKETS', 'womens-clothing-jackets-denim-jackets'), ('WOMENSCLOTHINGDRESSES', 'womens-clothing-dresses'), ('WOMENSCLOTHINGLEGGINGS', 'womens-clothing-leggings'), ('WOMENSCLOTHINGJEANS', 'womens-clothing-jeans'), ('WOMENSCLOTHINGCOATS', 'womens-clothing-coats'), ('WOMENSCLOTHINGJACKETS', 'womens-clothing-jackets'), ('WOMENSCLOTHINGSWEATSHIRTS', 'womens-clothing-sweatshirts'), ('WOMENSCLOTHINGBLOUSESTUNICS', 'womens-clothing-blouses-tunics'), ('WOMENSCLOTHINGJACKETSLEATHERJACKETS', 'womens-clothing-jackets-leather-jackets'), ('WOMENSCLOTHINGSKIRTS', 'womens-clothing-skirts'), ('WOMENSSHOESBALLETPUMPS', 'womens-shoes-ballet-pumps'), ('WOMENSSHOESANKLEBOOTS', 'womens-shoes-ankle-boots'), ('WOMENSCLOTHINGTROUSERS', 'womens-clothing-trousers'), ('WOMENSSHOESBOOTS', 'womens-shoes-boots'), ('WOMENSCLOTHINGTOPS', 'womens-clothing-tops'), ('WOMENSSHOESFLATSLACEUPS', 'womens-shoes-flats-lace-ups'), ('WOMENSSHOESHEELS', 'womens-shoes-heels'), ('WOMENSSPORTSSHOES', 'womens-sports-shoes'), ('WOMENSSHOESSANDALS', 'womens-shoes-sandals'), ('WOMENSSHOESTRAINERS', 'womens-shoes-trainers')], max_length=255)),
                ('garment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Styling.Garments')),
            ],
        ),
    ]
