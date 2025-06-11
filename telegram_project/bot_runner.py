from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
    ConversationHandler,
)
import os
from dotenv import load_dotenv
load_dotenv()
# === Hardcoded user data ===
USERS = {
    "123456789": {"username": "liam", "password": "liam21", "balance": 1425, "referrals": [], "verified_by": None},
    "224567550": {"username": "olivia", "password": "wom##bat99", "balance": 320, "referrals": [], "verified_by": None},
    "342278901": {"username": "noah", "password": "tfgfyptus47", "balance": 750, "referrals": [], "verified_by": None},
    "456789012": {"username": "ava", "password": "43oala33", "balance": 45, "referrals": [], "verified_by": None},
    "567110120": {"username": "william", "password": "ridoo889", "balance": 980, "referrals": [], "verified_by": None},
    "678901234": {"username": "sophia", "password": "sophia12", "balance": 200, "referrals": [], "verified_by": None},
    "789099345": {"username": "james", "password": "billabong", "balance": 1350, "referrals": [], "verified_by": None},
    "899123006": {"username": "isabella", "password": "isabellareef54", "balance": 65, "referrals": [], "verified_by": None},
    "901200567": {"username": "ethan", "password": "merang//,", "balance": 510, "referrals": [], "verified_by": None},
    "011345670": {"username": "mia", "password": "mia77", "balance": 1200, "referrals": [], "verified_by": None},
    "192322678": {"username": "alexander", "password": "aus//sie3", "balance": 15, "referrals": [], "verified_by": None},
    "023488789": {"username": "charlotte", "password": "bour22///", "balance": 890, "referrals": [], "verified_by": None},
    "331167890": {"username": "benjamin", "password": "cooral//", "balance": 430, "referrals": [], "verified_by": None},
    "445868901": {"username": "amelia", "password": "43sman55", "balance": 720, "referrals": [], "verified_by": None},
    "551089012": {"username": "jack", "password": "emu76", "balance": 105, "referrals": [], "verified_by": None},
    "669990123": {"username": "harper", "password": "luru31", "balance": 950, "referrals": [], "verified_by": None},
    "778901234": {"username": "thomas", "password": "ndi64", "balance": 280, "referrals": [], "verified_by": None},
    "189010645": {"username": "evelyn", "password": "daintree90", "balance": 1300, "referrals": [], "verified_by": None},
    "990121156": {"username": "oliver", "password": "peooth11", "balance": 370, "referrals": [], "verified_by": None},
    "199234507": {"username": "emma", "password": "bri86654544", "balance": 3820, "referrals": [], "verified_by": None},#
    "214445670": {"username": "lucas", "password": "28lucas", "balance": 60, "referrals": [], "verified_by": None},
    "323446780": {"username": "grace", "password": "kakadu73", "balance": 1100, "referrals": [], "verified_by": None},
    "431267800": {"username": "henry", "password": "3566342", "balance": 490, "referrals": [], "verified_by": None},
    "543378901": {"username": "lily", "password": "rferhfc19", "balance": 230, "referrals": [], "verified_by": None},
    "656009012": {"username": "jackson", "password": "platypus87", "balance": 1450, "referrals": [], "verified_by": None},
    "997890129": {"username": "Alinta", "password": "shark53", "balance": 340, "referrals": [], "verified_by": None},
    "879301134": {"username": "mason", "password": "102gumtree", "balance": 670, "referrals": [], "verified_by": None},
    "999012345": {"username": "ruby", "password": "w65allaby15", "balance": 920, "referrals": [], "verified_by": None},
    "122123456": {"username": "levi", "password": "81levi", "balance": 125, "referrals": [], "verified_by": None},
    "210234737": {"username": "chloe", "password": "harbour62", "balance": 780, "referrals": [], "verified_by": None},
    "321348978": {"username": "max", "password": "joey49", "balance": 410, "referrals": [], "verified_by": None},
    "434456789": {"username": "ella", "password": "22ralreef23", "balance": 1050, "referrals": [], "verified_by": None},
    "549867890": {"username": "harry", "password": "27harryy", "balance": 190, "referrals": [], "verified_by": None},
    "654670101": {"username": "zoe", "password": "9zooe4", "balance": 1360, "referrals": [], "verified_by": None},
    "005789002": {"username": "samuel", "password": "samuelbat68", "balance": 850, "referrals": [], "verified_by": None},
    "876470123": {"username": "kakadu", "password": "%654ptus41", "balance": 620, "referrals": [], "verified_by": None},
    "987901234": {"username": "ethan", "password": "la6575", "balance": 1150, "referrals": [], "verified_by": None},
    "098102385": {"username": "scarlett", "password": "didgeridoo", "balance": 260, "referrals": [], "verified_by": None},
    "669234507": {"username": "joshua", "password": "bong89", "balance": 870, "referrals": [], "verified_by": None},
    "276345698": {"username": "matilda", "password": "reef17", "balance": 430, "referrals": [], "verified_by": None},
    "321411789": {"username": "daniel", "password": "//trang56", "balance": 990, "referrals": [], "verified_by": None},
    "432727890": {"username": "hannah", "password": "ydneyyt83", "balance": 700, "referrals": [], "verified_by": None},
    "543670701": {"username": "luke", "password": "6aunssie29", "balance": 1240, "referrals": [], "verified_by": None},
    "654773012": {"username": "georgia", "password": "meljshne65", "balance": 310, "referrals": [], "verified_by": None},
    "765890123": {"username": "ryan", "password": "cooral92", "balance": 680, "referrals": [], "verified_by": None},
    "876951234": {"username": "eva", "password": "65sman..?", "balance": 145, "referrals": [], "verified_by": None},
    "987052345": {"username": "nathan", "password": "emu14", "balance": 930, "referrals": [], "verified_by": None},
    "098003456": {"username": "lucy", "password": "65332379", "balance": 400, "referrals": [], "verified_by": None},
    "109345678": {"username": "cooper", "password": "bdi55626", "balance": 1071, "referrals": [], "verified_by": None},
    "210836789": {"username": "emily", "password": "daintree63", "balance": 220, "referrals": [], "verified_by": None},
    "321567890": {"username": "oscar", "password": "8perth8", "balance": 1350, "referrals": [], "verified_by": None},
    "432748901": {"username": "madison", "password": "3676##91", "balance": 5, "referrals": [], "verified_by": None},
    "543789012": {"username": "jyura", "password": "jordan@34", "balance": 760, "referrals": [], "verified_by": None},
    "654822013": {"username": "aria", "password": "kakadu57", "balance": 1230, "referrals": [], "verified_by": None},
    "765901284": {"username": "zachary", "password": "heep82", "balance": 180, "referrals": [], "verified_by": None},
    "876012115": {"username": "violet", "password": "surfer16", "balance": 890, "referrals": [], "verified_by": None},
    "987123456": {"username": "finn", "password": "platypus93", "balance": 350, "referrals": [], "verified_by": None},
    "098924567": {"username": "layla", "password": "663528231", "balance": 1014, "referrals": [], "verified_by": None},
    "109456789": {"username": "gabriel", "password": "tree24####", "balance": 470, "referrals": [], "verified_by": None},
    "210447890": {"username": "piper", "password": "llaby2##4", "balance": 130, "referrals": [], "verified_by": None},
    "321678901": {"username": "elijah", "password": "Qpera45", "balance": 820, "referrals": [], "verified_by": None},
    "432779012": {"username": "sienna", "password": "73868671", "balance": 290, "referrals": [], "verified_by": None},
    "543890123": {"username": "archie", "password": "##76337", "balance": 1150, "referrals": [], "verified_by": None},
    "654881334": {"username": "freya", "password": "//ralreef", "balance": 640, "referrals": [], "verified_by": None},
    "765012345": {"username": "lachlan", "password": "outback59", "balance": 90, "referrals": [], "verified_by": None},
    "876113456": {"username": "imogen", "password": "83aroo25", "balance": 970, "referrals": [], "verified_by": None},
    "987234567": {"username": "harrison", "password": "wombat80", "balance": 428, "referrals": [], "verified_by": None},
    "098175678": {"username": "elsie", "password": "coolptus22.", "balance": 1080, "referrals": [], "verified_by": None},
    "109567890": {"username": "xavier", "password": "kla1265", "balance": 250, "referrals": [], "verified_by": None},
    "219478901": {"username": "willow", "password": "willow//96", "balance": 880, "referrals": [], "verified_by": None},
    "321789012": {"username": "dacma", "password": "abong65555543", "balance": 110, "referrals": [], "verified_by": None},
    "438390123": {"username": "Tali", "password": "reef69", "balance": 1260, "referrals": [], "verified_by": None},
    "543901234": {"username": "toby", "password": "rang///33", "balance": 385, "referrals": [], "verified_by": None},
    "654883345": {"username": "audrey", "password": "audrey94", "balance": 730, "referrals": [], "verified_by": None},
    "765123456": {"username": "flynn", "password": "au//ssi51", "balance": 140, "referrals": [], "verified_by": None},
    "879134567": {"username": "rose", "password": "melZournerose", "balance": 910, "referrals": [], "verified_by": None},
    "987345678": {"username": "carter", "password": "cral...35", "balance": 460, "referrals": [], "verified_by": None},
    "090056089": {"username": "ivy", "password": "sman602", "balance": 1190, "referrals": [], "verified_by": None},
    "109248901": {"username": "sebastian", "password": "emu19", "balance": 270, "referrals": [], "verified_by": None},
    "210965902": {"username": "mila", "password": "uluru84", "balance": 850, "referrals": [], "verified_by": None},
    "321120123": {"username": "lincoln", "password": "ivyyi41", "balance": 100, "referrals": [], "verified_by": None},
    "432631234": {"username": "clara", "password": "daintree27", "balance": 1320, "referrals": [], "verified_by": None},
    "543932345": {"username": "ashton", "password": "36563564", "balance": 390, "referrals": [], "verified_by": None},
    "654913456": {"username": "stella", "password": "11ane10", "balance": 940, "referrals": [], "verified_by": None},
    "765954567": {"username": "declan", "password": "declan", "balance": 210, "referrals": [], "verified_by": None},
    "879835678": {"username": "aurora", "password": "kakadu53", "balance": 1070, "referrals": [], "verified_by": None},
    "998456789": {"username": "caleb", "password": "sh5eep29", "balance": 340, "referrals": [], "verified_by": None},
    "009567890": {"username": "esme", "password": "urfer95", "balance": 1210, "referrals": [], "verified_by": None},
    "112789012": {"username": "theo", "password": "platypus71", "balance": 87, "referrals": [], "verified_by": None},
    "282890123": {"username": "hazel", "password": "reefshark", "balance": 900, "referrals": [], "verified_by": None},
    "384901234": {"username": "leo", "password": "7646743pan", "balance": 433, "referrals": [], "verified_by": None},
    "432041235": {"username": "eliza", "password": "allaby92", "balance": 1160, "referrals": [], "verified_by": None},
    "543863456": {"username": "arthur", "password": "opera69", "balance": 260, "referrals": [], "verified_by": None},
    "654724567": {"username": "penelope", "password": "loe1236", "balance": 830, "referrals": [], "verified_by": None},
    "760665678": {"username": "felix", "password": "felix87654", "balance": 150, "referrals": [], "verified_by": None},
    "876456789": {"username": "warra", "password": "coraaalreef61", "balance": 1091, "referrals": [], "verified_by": None},
    "987777890": {"username": "judit", "password": "ovalblank//", "balance": 370, "referrals": [], "verified_by": None},
    "098888901": {"username": "luna", "password": "garoo23", "balance": 968, "referrals": [], "verified_by": None},
    "170990123": {"username": "elliot", "password": "wom9asgh0", "balance": 227, "referrals": [], "verified_by": None},
    "210901234": {"username": "maeve", "password": "45343..58", "balance": 1280, "referrals": [], "verified_by": None},
    "109923456": {"username": "Murrung", "password": "garoo22231", "balance": 1425, "referrals": [], "verified_by": None},
    "106634567": {"username": "olivia", "password": "wombat99", "balance": 3320, "referrals": [], "verified_by": None},#
    "100345678": {"username": "noah", "password": "76574547", "balance": 750, "referrals": [], "verified_by": None},
    "109956789": {"username": "ava", "password": "koala33", "balance": 45, "referrals": [], "verified_by": None},
    "100567890": {"username": "william", "password": "didgeridoo88", "balance": 986, "referrals": [], "verified_by": None},
    "100907801": {"username": "silvia", "password": "sophiabackout", "balance": 204, "referrals": [], "verified_by": None},
    "176690125": {"username": "james", "password": "valabong??", "balance": 1354, "referrals": [], "verified_by": None},
    "100880123": {"username": "Kipara", "password": "reef54", "balance": 65, "referrals": [], "verified_by": None},
    "100121234": {"username": "ethan", "password": "boofookng29", "balance": 510, "referrals": [], "verified_by": None},
    "101972345": {"username": "mia", "password": "sydney77", "balance": 1200, "referrals": [], "verified_by": None},
    "101963456": {"username": "alexander", "password": "a//ussie4/", "balance": 15, "referrals": [], "verified_by": None},
    "101784567": {"username": "charlotte", "password": "tmelbourne//", "balance": 897, "referrals": [], "verified_by": None},
    "101125678": {"username": "benjamin", "password": "coral18", "balance": 430, "referrals": [], "verified_by": None},
    "101756789": {"username": "amelia", "password": "tasman55", "balance": 720, "referrals": [], "verified_by": None},
    "101887890": {"username": "jack", "password": "emu76", "balance": 105, "referrals": [], "verified_by": None},
    "101238901": {"username": "harper", "password": "uluru31", "balance": 952, "referrals": [], "verified_by": None},
    "101819012": {"username": "thomas", "password": "di64746", "balance": 280, "referrals": [], "verified_by": None},
    "101090123": {"username": "evelyn", "password": "daintree90", "balance": 1300, "referrals": [], "verified_by": None},
    "101661234": {"username": "oliver", "password": "6734653211", "balance": 370, "referrals": [], "verified_by": None},
    "102442345": {"username": "emma", "password": "bane###44", "balance": 820, "referrals": [], "verified_by": None},
    "102333456": {"username": "lucas", "password": "lucas@28", "balance": 600, "referrals": [], "verified_by": None},
    "102564567": {"username": "Ngarra", "password": "kakadu73", "balance": 1100, "referrals": [], "verified_by": None},
    "102625678": {"username": "henry", "password": "Henryhenry", "balance": 499, "referrals": [], "verified_by": None},
    "102096789": {"username": "lily", "password": "@@urfer19", "balance": 230, "referrals": [], "verified_by": None},
    "102877890": {"username": "jackson", "password": "platypus87", "balance": 1450, "referrals": [], "verified_by": None},
    "102008901": {"username": "sophie", "password": "reefshark53", "balance": 340, "referrals": [], "verified_by": None},
    "102649012": {"username": "mason", "password": "6378736", "balance": 670, "referrals": [], "verified_by": None},
    "102980123": {"username": "ruby", "password": "ruby1005", "balance": 920, "referrals": [], "verified_by": None},
    "102891234": {"username": "levi", "password": "opera81", "balance": 125, "referrals": [], "verified_by": None},
    "103122345": {"username": "chloe", "password": "harbour62", "balance": 2780, "referrals": [], "verified_by": None},#
    "103763456": {"username": "max", "password": "maxmax??.", "balance": 410, "referrals": [], "verified_by": None},
    "103994567": {"username": "ella", "password": "mooralreef23", "balance": 1050, "referrals": [], "verified_by": None},
    "103309568": {"username": "harry", "password": "back2777", "balance": 190, "referrals": [], "verified_by": None},
    "103477789": {"username": "zoe", "password": "aroo9454", "balance": 1360, "referrals": [], "verified_by": None},
    "103533890": {"username": "samuel", "password": "wombat68", "balance": 85, "referrals": [], "verified_by": None},
    "103688901": {"username": "isabelle", "password": "calyptus41", "balance": 624, "referrals": [], "verified_by": None},
    "103712012": {"username": "ethan", "password": "k$#oala75", "balance": 1150, "referrals": [], "verified_by": None},
    "103895123": {"username": "scarlett", "password": "didgeridoo32", "balance": 261, "referrals": [], "verified_by": None},
    "103901234": {"username": "joshua", "password": "67r8363389", "balance": 872, "referrals": [], "verified_by": None},
    "104099345": {"username": "matilda", "password": "reef17", "balance": 433, "referrals": [], "verified_by": None},
    "104100456": {"username": "daniel", "password": "poomerang56", "balance": 994, "referrals": [], "verified_by": None},
    "104277567": {"username": "hannah", "password": "hannah5009", "balance": 75, "referrals": [], "verified_by": None},
    "104366678": {"username": "luke", "password": "ausbvie29", "balance": 1240, "referrals": [], "verified_by": None},
    "104433789": {"username": "georgia", "password": "megeorgia", "balance": 315, "referrals": [], "verified_by": None},
    "104576890": {"username": "ryan", "password": "coal9002", "balance": 684, "referrals": [], "verified_by": None},
    "104677901": {"username": "eva", "password": "tasman38", "balance": 145, "referrals": [], "verified_by": None},
    "102189012": {"username": "nathan", "password": "emu14", "balance": 938, "referrals": [], "verified_by": None},
    "109890123": {"username": "lucy", "password": "uluru79", "balance": 4200, "referrals": [], "verified_by": None},#
    "100601234": {"username": "cooper","password": "267643", "balance": 1070, "referrals": [], "verified_by": None},
    "109812345": {"username": "emily", "password": "daintree63", "balance": 220, "referrals": [], "verified_by": None},
    "100923456": {"username": "oscar", "password": "peytew6548", "balance": 1356, "referrals": [], "verified_by": None},
    "107634567": {"username": "madison", "password": "bane..91", "balance": 95, "referrals": [], "verified_by": None},
    "100945678": {"username": "jordan", "password": "crocs@@@", "balance": 760, "referrals": [], "verified_by": None},
    "100056789": {"username": "aria", "password": "kakadu57", "balance": 1230, "referrals": [], "verified_by": None},
    "109967890": {"username": "zachary", "password": "Zachary82", "balance": 187, "referrals": [], "verified_by": None},
    "105678901": {"username": "Djamarrkuli", "password": "s6536516", "balance": 893, "referrals": [], "verified_by": None},
    "105772312": {"username": "finn", "password": "platypus93", "balance": 350, "referrals": [], "verified_by": None},
    "105891223": {"username": "layla", "password": "reefshark61", "balance": 1010, "referrals": [], "verified_by": None},
    "105901234": {"username": "gabriel", "password": "tree24555", "balance": 470, "referrals": [], "verified_by": None},
    "106011245": {"username": "piper", "password": "2006piper", "balance": 136, "referrals": [], "verified_by": None},
    "106126556": {"username": "elijah", "password": "opera45", "balance": 820, "referrals": [], "verified_by": None},
    "106234867": {"username": "sienna", "password": "harbour71", "balance": 290, "referrals": [], "verified_by": None},
    "106345098": {"username": "archie", "password": "archiearchie", "balance": 1150, "referrals": [], "verified_by": None},
    "106456089": {"username": "freya", "password": "freyaeef13", "balance": 640, "referrals": [], "verified_by": None},
    "106568820": {"username": "lachlan", "password": "lachlan6235", "balance": 6906, "referrals": [], "verified_by": None},#
    "106998901": {"username": "imogen", "password": "imogenroo", "balance": 970, "referrals": [], "verified_by": None},
    "106999012": {"username": "harrison", "password": "wombat80", "balance": 423, "referrals": [], "verified_by": None},
    "108890123": {"username": "elsie", "password": "elsieptus..", "balance": 1080, "referrals": [], "verified_by": None},
    "108801234": {"username": "xavier", "password": "koghala12", "balance": 250, "referrals": [], "verified_by": None},
    "103312345": {"username": "willow", "password": "didgeridoo96", "balance": 885, "referrals": [], "verified_by": None},
    "104423456": {"username": "hunter", "password": "billmonk13", "balance": 110, "referrals": [], "verified_by": None},
    "105534567": {"username": "Kurrbid", "password": "reef69", "balance": 1266, "referrals": [], "verified_by": None},
    "106645678": {"username": "toby", "password": "boom43rang28", "balance": 384, "referrals": [], "verified_by": None},
    "107756789": {"username": "audrey", "password": "ydney9oo4", "balance": 730, "referrals": [], "verified_by": None},
    "108867890": {"username": "flynn", "password": "aussie51", "balance": 140, "referrals": [], "verified_by": None},
    "109978901": {"username": "rose", "password": "bourne7008", "balance": 910, "referrals": [], "verified_by": None},
    "100089012": {"username": "carter", "password": "ggsoral35", "balance": 460, "referrals": [], "verified_by": None},
    "109890123": {"username": "ivy", "password": "tasman62", "balance": 1197, "referrals": [], "verified_by": None},
    "108701234": {"username": "sebastian", "password": "emu19", "balance": 270, "referrals": [], "verified_by": None},
    "108712345": {"username": "mila", "password": "uluru84", "balance": 850, "referrals": [], "verified_by": None},
    "107623456": {"username": "lincoln", "password": "blacki41", "balance": 100, "referrals": [], "verified_by": None},
    "106534567": {"username": "clara", "password": "daintree27", "balance": 1325, "referrals": [], "verified_by": None},
    "105445678": {"username": "ashton", "password": "perth64", "balance": 390, "referrals": [], "verified_by": None},
    "105456789": {"username": "jirra", "password": "bright10", "balance": 940, "referrals": [], "verified_by": None},
    "104367890": {"username": "declan", "password": "dile...##", "balance": 2316, "referrals": [], "verified_by": None},#
    "104378901": {"username": "aurora", "password": "kakadu53", "balance": 1070, "referrals": [], "verified_by": None},
    "108789012": {"username": "caleb", "password": "Calebcaleb2", "balance": 340, "referrals": [], "verified_by": None},
    "107890123": {"username": "esme", "password": "3746763495", "balance": 1218, "referrals": [], "verified_by": None},
    "103201234": {"username": "theo", "password": "platypus71", "balance": 80, "referrals": [], "verified_by": None},
    "109012345": {"username": "hazel", "password": "reefshark48", "balance": 901, "referrals": [], "verified_by": None},
    "103223456": {"username": "leo", "password": "leoleoleo??", "balance": 430, "referrals": [], "verified_by": None},
    "102134567": {"username": "eliza", "password": "@@eliza@@", "balance": 1160, "referrals": [], "verified_by": None},
    "109945678": {"username": "arthur", "password": "opera69", "balance": 260, "referrals": [], "verified_by": None},
    "100056789": {"username": "Biyux", "password": "harbour36", "balance": 835, "referrals": [], "verified_by": None},
    "109067890": {"username": "felix", "password": "joey84felix", "balance": 4150, "referrals": [], "verified_by": None},#
    "096678901": {"username": "ada", "password": "coralreef61", "balance": 1090, "referrals": [], "verified_by": None},
    "109889012": {"username": "jude", "password": "judejude$$", "balance": 370, "referrals": [], "verified_by": None},
    "109660123": {"username": "luna", "password": "48539876523", "balance": 962, "referrals": [], "verified_by": None},
    "109551234": {"username": "elliot", "password": "wombat90", "balance": 220, "referrals": [], "verified_by": None},
    "110442345": {"username": "maeve", "password": "meavetus58", "balance": 1280, "referrals": [], "verified_by": None},
    "110333456": {"username": "angus", "password": "di76565562", "balance": 304, "referrals": [], "verified_by": None},
    "110224567": {"username": "isla", "password": "reef45", "balance": 1050, "referrals": [], "verified_by": None},
    "110225678": {"username": "finnley", "password": "finnley19", "balance": 480, "referrals": [], "verified_by": None},
    "110166789": {"username": "sienna", "password": "kangaroo67", "balance": 925, "referrals": [], "verified_by": None},
    "110967890": {"username": "jett", "password": "wombat34", "balance": 130, "referrals": [], "verified_by": None},
    "119878901": {"username": "phoebe", "password": "eucalyptus91", "balance": 870, "referrals": [], "verified_by": None},
    "119800012": {"username": "ryder", "password": "kohghala28", "balance": 416, "referrals": [], "verified_by": None},
    "110866123": {"username": "elise", "password": "didgeridoo56", "balance": 1190, "referrals": [], "verified_by": None},
    "110909234": {"username": "connor", "password": "connorcon", "balance": 250, "referrals": [], "verified_by": None},
    "111054345": {"username": "delilah", "password": "delilah17", "balance": 980, "referrals": [], "verified_by": None},
    "111983456": {"username": "logan", "password": "zossie84", "balance": 3361, "referrals": [], "verified_by": None},#
    "111544567": {"username": "evie", "password": "bourne2##9", "balance": 1120, "referrals": [], "verified_by": None},
    "111235678": {"username": "jaxon", "password": "voral65", "balance": 190, "referrals": [], "verified_by": None},
    "111786789": {"username": "alice", "password": "tasman42", "balance": 850, "referrals": [], "verified_by": None},
    "111997890": {"username": "flynn", "password": "emu78", "balance": 430, "referrals": [], "verified_by": None},
    "111128901": {"username": "harriet", "password": "uluru15", "balance": 1270, "referrals": [], "verified_by": None},
    "111459012": {"username": "milo", "password": "b654593", "balance": 290, "referrals": [], "verified_by": None},
    "111090123": {"username": "daisy", "password": "daintree36", "balance": 960, "referrals": [], "verified_by": None},
    "111091234": {"username": "oscar", "password": "penbmytt81", "balance": 140, "referrals": [], "verified_by": None},
    "112002345": {"username": "lola", "password": "brisbaness", "balance": 1030, "referrals": [], "verified_by": None},
    "112443456": {"username": "hudson", "password": "hudson24", "balance": 384, "referrals": [], "verified_by": None},
    "112224567": {"username": "bella", "password": "kakadu69", "balance": 890, "referrals": [], "verified_by": None},
    "112655678": {"username": "kai", "password": "Lackkia", "balance": 210, "referrals": [], "verified_by": None},
    "112236789": {"username": "amelie", "password": "amelie", "balance": 1145, "referrals": [], "verified_by": None},
    "112887890": {"username": "asher", "password": "platypus39", "balance": 4470, "referrals": [], "verified_by": None},#
    "112558901": {"username": "violette", "password": "reefshark96", "balance": 930, "referrals": [], "verified_by": None},
    "112449012": {"username": "roman", "password": "nnmtree53?", "balance": 160, "referrals": [], "verified_by": None},
    "112220123": {"username": "lilyana", "password": "lilyanana", "balance": 1080, "referrals": [], "verified_by": None},
    "112331234": {"username": "ezra", "password": "opera74", "balance": 340, "referrals": [], "verified_by": None},
    "113112345": {"username": "Yulyan", "password": "harbour19", "balance": 990, "referrals": [], "verified_by": None},
    "113003456": {"username": "nolan", "password": "8nolan6", "balance": 3230, "referrals": [], "verified_by": None},#
    "113994567": {"username": "savannah", "password": "zalreef42", "balance": 1160, "referrals": [], "verified_by": None},
    "113875678": {"username": "rhys", "password": "declanrhys", "balance": 400, "referrals": [], "verified_by": None},
    "113766789": {"username": "pippa", "password": "Zoobuggg?", "balance": 876, "referrals": [], "verified_by": None},
    "113657890": {"username": "declan", "password": "wombat91", "balance": 120, "referrals": [], "verified_by": None},
    "113665891": {"username": "estelle", "password": "leucalyptus", "balance": 1050, "referrals": [], "verified_by": None},
    "113789012": {"username": "beau", "password": "ko//ala14", "balance": 490, "referrals": [], "verified_by": None},
    "113000123": {"username": "sadie", "password": "didgeridoo81", "balance": 920, "referrals": [], "verified_by": None},
    "113551234": {"username": "callum", "password": "callumm", "balance": 266, "referrals": [], "verified_by": None},
    "114092345": {"username": "milla", "password": "milla234", "balance": 1110, "referrals": [], "verified_by": None},
    "114123456": {"username": "atticus", "password": "atticus222", "balance": 385, "referrals": [], "verified_by": None},
    "114454567": {"username": "esther", "password": "mele2005born", "balance": 970, "referrals": [], "verified_by": None},
    "114125678": {"username": "lachie", "password": "567ral12", "balance": 150, "referrals": [], "verified_by": None},
    "114896789": {"username": "annie", "password": "tasman69", "balance": 1080, "referrals": [], "verified_by": None},
    "114117890": {"username": "ronan", "password": "emu35", "balance": 2437, "referrals": [], "verified_by": None},#
    "114568901": {"username": "elsa", "password": "uluru92", "balance": 990, "referrals": [], "verified_by": None},
    "114129012": {"username": "jettson", "password": "5653348", "balance": 220, "referrals": [], "verified_by": None},
    "114850123": {"username": "lillian", "password": "daintree15", "balance": 1040, "referrals": [], "verified_by": None},
    "114091234": {"username": "silas", "password": "erth81", "balance": 370, "referrals": [], "verified_by": None},
    "115892345": {"username": "cecilia", "password": "vonbane46", "balance": 5900, "referrals": [], "verified_by": None},#
    "115113456": {"username": "levi", "password": "76365223", "balance": 180, "referrals": [], "verified_by": None},
    "115134567": {"username": "adele", "password": "kakadu79", "balance": 1150, "referrals": [], "verified_by": None},
    "115675678": {"username": "tobias", "password": "tobiasjunk", "balance": 410, "referrals": [], "verified_by": None},
    "119056789": {"username": "cora", "password": "fer9ew3", "balance": 960, "referrals": [], "verified_by": None},
    "115567890": {"username": "edward", "password": "platypus49", "balance": 130, "referrals": [], "verified_by": None},
    "110078901": {"username": "lydia", "password": "reefshark16", "balance": 1070, "referrals": [], "verified_by": None},
    "117789012": {"username": "vincent", "password": "gumeree82", "balance": 290, "referrals": [], "verified_by": None},
    "112290123": {"username": "beatrice", "password": "beatrice38", "balance": 920, "referrals": [], "verified_by": None},
    "111201234": {"username": "miles", "password": "opera75", "balance": 340, "referrals": [], "verified_by": None},
    "114412345": {"username": "flora", "password": "harbour21", "balance": 3980, "referrals": [], "verified_by": None},#
    "116902356": {"username": "elliott", "password": "e6543652", "balance": 200, "referrals": [], "verified_by": None},
    "116239967": {"username": "june", "password": "caloohreef54", "balance": 1107, "referrals": [], "verified_by": None},
    "116347778": {"username": "jude", "password": "junemark00", "balance": 460, "referrals": [], "verified_by": None},
    "116453389": {"username": "martha", "password": "aroomartha7", "balance": 1030, "referrals": [], "verified_by": None},
    "116561290": {"username": "otis", "password": "wombat24", "balance": 186, "referrals": [], "verified_by": None},
    "116671201": {"username": "veronica", "password": "5463us81", "balance": 950, "referrals": [], "verified_by": None},
    "116785512": {"username": "percy", "password": "k//goala8", "balance": 270, "referrals": [], "verified_by": None},
    "1168903230": {"username": "matilda", "password": "didgeridoo95", "balance": 1127, "referrals": [], "verified_by": None},
    "116901994": {"username": "theodore", "password": "theodorere", "balance": 391, "referrals": [], "verified_by": None}
}
# === States for conversation ===
ASK_ID, ASK_USERNAME, ASK_PASSWORD = range(3)

# === Track verified users (Telegram user_id) ===
VERIFIED_USERS = {}

# === Bot Token ===
BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_USERNAME = "WestPac_helpBot"  # For referral link

# === Start command ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if user_id in VERIFIED_USERS:
        await update.message.reply_text("You are already verified.")
        return await show_buttons(update, context)

    await update.message.reply_text("Enter 9-digit TFN:")
    return ASK_ID

async def ask_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    id_number = update.message.text.strip()

    if id_number not in USERS:
        await update.message.reply_text("ID not found. Verification cancelled.")
        return ConversationHandler.END

    if USERS[id_number]["verified_by"] is not None:
        await update.message.reply_text("A user has already verified this account.")
        return ConversationHandler.END

    context.user_data["id_number"] = id_number
    await update.message.reply_text("Enter your username:")
    return ASK_USERNAME

async def ask_username(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.message.text.strip()
    id_number = context.user_data["id_number"]

    if USERS[id_number]["username"] != username:
        await update.message.reply_text("Username does not match. Verification cancelled.")
        return ConversationHandler.END

    context.user_data["username"] = username
    await update.message.reply_text("Enter your password:")
    return ASK_PASSWORD

async def ask_password(update: Update, context: ContextTypes.DEFAULT_TYPE):
    password = update.message.text.strip()
    id_number = context.user_data["id_number"]

    user = USERS[id_number]

    if user["password"] != password:
        await update.message.reply_text("Password incorrect. Verification cancelled.")
        return ConversationHandler.END

    telegram_id = update.effective_user.id
    user["verified_by"] = telegram_id
    VERIFIED_USERS[telegram_id] = id_number

    await update.message.reply_text("Verification successful.")
    return await show_buttons(update, context)

# === Show menu buttons ===
async def show_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["Withdraw", "Balance"], ["Referral", "Make Payment"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Choose an option:", reply_markup=reply_markup)
    return ConversationHandler.END

# === Helper to check verification ===
def is_verified(user_id):
    return user_id in VERIFIED_USERS

# === Withdraw handler ===
async def withdraw(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_verified(update.effective_user.id):
        await update.message.reply_text("Please verify first using /start.")
        return

    await update.message.reply_text("Invalid payment proof upholded or payment was made during site mantainance and was added to your account balance we advised you wait for 30-40 days or make new payment")

async def handle_photo(update:Update,
    context: ContextTypes. DEFAULT_TYPE):
    await update.message.reply_text("Payment proof successfully uploaded. Thank you!")

# === Balance handler ===
async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if not is_verified(user_id):
        await update.message.reply_text("Please verify first using /start.")
        return

    id_number = VERIFIED_USERS[user_id]
    balance = USERS[id_number]["balance"]
    await update.message.reply_text(f"Your current balance is ${balance}")

# === Make payment handler ===
async def make_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_verified(update.effective_user.id):
        await update.message.reply_text("Please verify first using /start.")
        return

    await update.message.reply_text("Make payment to this tag westpac")

# === Referral handler ===
async def referral(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if not is_verified(user_id):
        await update.message.reply_text("Please verify first using /start.")
        return

    id_number = VERIFIED_USERS[user_id]

    if context.args:
        ref_id = context.args[0]
        if ref_id in USERS and user_id not in USERS[ref_id]["referrals"]:
            USERS[ref_id]["referrals"].append(user_id)
            USERS[ref_id]["balance"] += 20

    ref_link = f"https://t.me/{BOT_USERNAME}?start={id_number}"
    ref_count = len(USERS[id_number]["referrals"])
    await update.message.reply_text(f"Share your referral link:\n{ref_link}\n\nReferrals: {ref_count}\nBonus: ${ref_count * 20:.2f}")

# === Fallback handler ===
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Invalid Input. Use the buttons or /start.") #"I didn’t understand that. Use the buttons or /start."

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            ASK_ID: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_id)],
            ASK_USERNAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_username)],
            ASK_PASSWORD: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_password)],
        },
        fallbacks=[],
    )

    app.add_handler(conv_handler)
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    app.add_handler(MessageHandler(filters.Regex("^Withdraw$"), withdraw))
    app.add_handler(MessageHandler(filters.Regex("^Balance$"), balance))
    app.add_handler(MessageHandler(filters.Regex("^Make Payment$"), make_payment))
    app.add_handler(MessageHandler(filters.Regex("^Referral$"), referral))
    app.add_handler(MessageHandler(filters.COMMAND, unknown))
    app.add_handler(MessageHandler(filters.TEXT, unknown))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()