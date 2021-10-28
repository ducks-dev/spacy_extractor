directions = ['n',  'north',
              'ne', 'northeast',
              'nw', 'northwest',
              'e',  'east',
              's',  'south',
              'se', 'southeast',
              'sw', 'southwest',
              'w', 'west']
#removed 'is' 'cv' 'cvs' 'club' 'i'
usps_abbr = ["allee", "alley", "ally", "aly", "anex", "annex", "annx",
             "anx", "arc", "arcade", "av", "ave", "aven", "avenu",
             "avenue", "avn", "avnue", "bayoo", "bayou", "bch",
             "beach", "bend", "bg", "bgs", "blf", "blfs", "bluf",
             "bluff", "bluffs", "blvd", "bnd", "bot", "bottm",
             "bottom", "boul", "boulevard", "boulv", "br", "branch",
             "brdge", "brg", "bridge", "brk", "brks", "brnch", "brook",
             "brooks","btm", "burg", "burgs", "byp", "bypa", "bypas",
             "bypass", "byps", "byu", "camp", "canyn", "canyon",
             "cape", "causeway", "causway", "cen", "cent", "center",
             "centers", "centr", "centre", "cir", "circ", "circl",
             "circle", "circles", "cirs", "ck", "clb", "clf", "clfs",
             "cliff", "cliffs", "cmn", "cmp", "cnter", "cntr",
             "cnyn", "common", "cor", "corner", "corners", "cors",
             "course", "court", "courts", "cove", "coves", "cp",
             "cpe", "cr", "crcl", "crcle", "crecent", "creek", "cres",
             "crescent", "cresent", "crest", "crk", "crossing",
             "crossroad", "crscnt", "crse", "crsent", "crsnt", "crssing",
             "crssng", "crst", "crt", "cswy", "ct", "ctr", "ctrs", "cts",
             "curv", "curve", "cyn", "dale", "dam", "div",
             "divide", "dl", "dm", "dr", "driv", "drive", "drives",
             "drs", "drv", "dv", "dvd", "est", "estate", "estates",
             "ests", "exp", "expr", "express", "expressway", "expw",
             "expy", "ext", "extension", "extensions", "extn", "extnsn",
             "exts", "fall", "falls", "ferry", "field", "fields", "flat",
             "flats", "fld", "flds", "fls", "flt", "flts", "ford",
             "fords", "forest", "forests", "forg", "forge", "forges",
             "fork", "forks", "fort", "frd", "frds", "freeway", "freewy",
             "frg", "frgs", "frk", "frks", "frry", "frst", "frt", "frway",
             "frwy", "fry", "ft", "fwy", "garden", "gardens", "gardn",
             "gateway", "gatewy", "gatway", "gdn", "gdns", "glen",
             "glens", "gln", "glns", "grden", "grdn", "grdns", "green",
             "greens", "grn", "grns", "grov", "grove", "groves", "grv",
             "grvs", "gtway", "gtwy", "harb", "harbor", "harbors",
             "harbr", "haven", "havn", "hbr", "hbrs", "height",
             "heights", "hgts", "highway", "highwy", "hill", "hills",
             "hiway", "hiwy", "hl", "hllw", "hls", "hollow", "hollows",
             "holw", "holws", "hrbor", "ht", "hts", "hvn", "hway",
             "hwy", "ia", "inlet", "inlt", "island",
             "islands", "isle", "isles", "islnd", "iss", "jct", "jction",
             "jctn", "jctns", "jcts", "junction", "junctions", "junctn",
             "juncton", "key", "keys", "knl", "knls", "knol", "knoll",
             "knolls", "ky", "kys", "la", "lake", "lakes", "land",
             "landing", "lane", "lanes", "lck", "lcks", "ldg", "ldge",
             "lf", "lgt", "lgts", "light", "lights", "lk", "lks", "ln",
             "lndg", "lndng", "loaf", "lock", "locks", "lodg", "lodge",
             "loop", "loops", "mall", "manor", "manors", "mdw", "mdws",
             "meadow", "meadows", "medows", "mews", "mill", "mills",
             "mission", "missn", "ml", "mls", "mnr", "mnrs", "mnt",
             "mntain", "mntn", "mntns", "motorway", "mount", "mountain",
             "mountains", "mountin", "msn", "mssn", "mt", "mtin", "mtn",
             "mtns", "mtwy", "nck", "neck", "opas", "orch", "orchard",
             "orchrd", "oval", "overpass", "ovl", "park", "parks",
             "parkway", "parkways", "parkwy", "pass", "passage", "path",
             "paths", "pike", "pikes", "pine", "pines", "pk", "pkway",
             "pkwy", "pkwys", "pky", "pl", "place", "plain", "plaines",
             "plains", "plaza", "pln", "plns", "plz", "plza", "pne",
             "pnes", "point", "points", "port", "ports", "pr", "prairie",
             "prarie", "prk", "prr", "prt", "prts", "psge", "pt", "pts",
             "rad", "radial", "radiel", "radl", "ramp", "ranch",
             "ranches", "rapid", "rapids", "rd", "rdg", "rdge", "rdgs",
             "rds", "rest", "ridge", "ridges", "riv", "river", "rivr",
             "rnch", "rnchs", "road", "roads", "route", "row", "rpd",
             "rpds", "rst", "rte", "rue", "run", "rvr", "shl", "shls",
             "shoal", "shoals", "shoar", "shoars", "shore", "shores",
             "shr", "shrs", "skwy", "skyway", "slnds", "smt", "spg",
             "spgs", "spng", "spngs", "spring", "springs", "sprng",
             "sprngs", "spur", "spurs", "sq", "sqr", "sqre", "sqrs",
             "sqs", "squ", "square", "squares", "ss", "st", "sta",
             "station", "statn", "stn", "str", "stra", "strav",
             "strave", "straven", "stravenue", "stravn", "stream",
             "street", "streets", "streme", "strm", "strt", "strvn",
             "strvnue", "sts", "sumit", "sumitt", "summit", "ter",
             "terr", "terrace", "throughway", "tpk", "tpke", "tr",
             "trace", "traces", "track", "tracks", "trafficway",
             "trail", "trails", "trak", "trce", "trfy", "trk", "trks",
             "trl", "trls", "trnpk", "trpk", "trwy", "tunel", "tunl",
             "tunls", "tunnel", "tunnels", "tunnl", "turnpike",
             "turnpk", "un", "underpass", "union", "unions", "uns",
             "upas", "valley", "valleys", "vally", "vdct", "via",
             "viadct", "viaduct", "view", "views", "vill", "villag",
             "village", "villages", "ville", "villg", "villiage", "vis",
             "vist", "vista", "vl", "vlg", "vlgs", "vlly", "vly", "vlys",
             "vst", "vsta", "vw", "vws", "walk", "walks", "wall", "way",
             "ways", "well", "wells", "wl", "wls", "wy", "xing", "xrd",

             "allee.","alley.","ally.","aly.","anex.","annex.","annx.",
             "anx.","arc.","arcade.","av.","ave.","aven.","avenu.",
             "avenue.","avn.","avnue.","bayoo.","bayou.","bch.",
             "beach.","bend.","bg.","bgs.","blf.","blfs.","bluf.",
             "bluff.","bluffs.","blvd.","bnd.","bot.","bottm.",
             "bottom.","boul.","boulevard.","boulv.","br.","branch.",
             "brdge.","brg.","bridge.","brk.","brks.","brnch.","brook.",
             "brooks.","btm.","burg.","burgs.","byp.","bypa.","bypas.",
             "bypass.","byps.","byu.","camp.","canyn.","canyon.",
             "cape.","causeway.","causway.","cen.","cent.","center.",
             "centers.","centr.","centre.","cir.","circ.","circl.",
             "circle.","circles.","cirs.","ck.","clb.","clf.","clfs.",
             "cliff.","cliffs.","club.","cmn.","cmp.","cnter.","cntr.",
             "cnyn.","common.","cor.","corner.","corners.","cors.",
             "course.","court.","courts.","cove.","coves.","cp.",
             "cpe.","cr.","crcl.","crcle.","crecent.","creek.","cres.",
             "crescent.","cresent.","crest.","crk.","crossing.",
             "crossroad.","crscnt.","crse.","crsent.","crsnt.","crssing.",
             "crssng.","crst.","crt.","cswy.","ct.","ctr.","ctrs.","cts.",
             "curv.","curve.","cv.","cvs.","cyn.","dale.","dam.","div.",
             "divide.","dl.","dm.","dr.","driv.","drive.","drives.",
             "drs.","drv.","dv.","dvd.","est.","estate.","estates.",
             "ests.","exp.","expr.","express.","expressway.","expw.",
             "expy.","ext.","extension.","extensions.","extn.","extnsn.",
             "exts.","fall.","falls.","ferry.","field.","fields.","flat.",
             "flats.","fld.","flds.","fls.","flt.","flts.","ford.",
             "fords.","forest.","forests.","forg.","forge.","forges.",
             "fork.","forks.","fort.","frd.","frds.","freeway.","freewy.",
             "frg.","frgs.","frk.","frks.","frry.","frst.","frt.","frway.",
             "frwy.","fry.","ft.","fwy.","garden.","gardens.","gardn.",
             "gateway.","gatewy.","gatway.","gdn.","gdns.","glen.",
             "glens.","gln.","glns.","grden.","grdn.","grdns.","green.",
             "greens.","grn.","grns.","grov.","grove.","groves.","grv.",
             "grvs.","gtway.","gtwy.","harb.","harbor.","harbors.",
             "harbr.","haven.","havn.","hbr.","hbrs.","height.",
             "heights.","hgts.","highway.","highwy.","hill.","hills.",
             "hiway.","hiwy.","hl.","hllw.","hls.","hollow.","hollows.",
             "holw.","holws.","hrbor.","ht.","hts.","hvn.","hway.",
             "hwy.","i.","ia.","inlet.","inlt.","is.","island.",
             "islands.","isle.","isles.","islnd.","iss.","jct.","jction.",
             "jctn.","jctns.","jcts.","junction.","junctions.","junctn.",
             "juncton.","key.","keys.","knl.","knls.","knol.","knoll.",
             "knolls.","ky.","kys.","la.","lake.","lakes.","land.",
             "landing.","lane.","lanes.","lck.","lcks.","ldg.","ldge.",
             "lf.","lgt.","lgts.","light.","lights.","lk.","lks.","ln.",
             "lndg.","lndng.","loaf.","lock.","locks.","lodg.","lodge.",
             "loop.","loops.","mall.","manor.","manors.","mdw.","mdws.",
             "meadow.","meadows.","medows.","mews.","mill.","mills.",
             "mission.","missn.","ml.","mls.","mnr.","mnrs.","mnt.",
             "mntain.","mntn.","mntns.","motorway.","mount.","mountain.",
             "mountains.","mountin.","msn.","mssn.","mt.","mtin.","mtn.",
             "mtns.","mtwy.","nck.","neck.","opas.","orch.","orchard.",
             "orchrd.","oval.","overpass.","ovl.","park.","parks.",
             "parkway.","parkways.","parkwy.","pass.","passage.","path.",
             "paths.","pike.","pikes.","pine.","pines.","pk.","pkway.",
             "pkwy.","pkwys.","pky.","pl.","place.","plain.","plaines.",
             "plains.","plaza.","pln.","plns.","plz.","plza.","pne.",
             "pnes.","point.","points.","port.","ports.","pr.","prairie.",
             "prarie.","prk.","prr.","prt.","prts.","psge.","pt.","pts.",
             "rad.","radial.","radiel.","radl.","ramp.","ranch.",
             "ranches.","rapid.","rapids.","rd.","rdg.","rdge.","rdgs.",
             "rds.","rest.","ridge.","ridges.","riv.","river.","rivr.",
             "rnch.","rnchs.","road.","roads.","route.","row.","rpd.",
             "rpds.","rst.","rte.","rue.","run.","rvr.","shl.","shls.",
             "shoal.","shoals.","shoar.","shoars.","shore.","shores.",
             "shr.","shrs.","skwy.","skyway.","slnds.","smt.","spg.",
             "spgs.","spng.","spngs.","spring.","springs.","sprng.",
             "sprngs.","spur.","spurs.","sq.","sqr.","sqre.","sqrs.",
             "sqs.","squ.","square.","squares.","ss.","st.","sta.",
             "station.","statn.","stn.","str.","stra.","strav.",
             "strave.","straven.","stravenue.","stravn.","stream.",
             "street.","streets.","streme.","strm.","strt.","strvn.",
             "strvnue.","sts.","sumit.","sumitt.","summit.","ter.",
             "terr.","terrace.","throughway.","tpk.","tpke.","tr.",
             "trace.","traces.","track.","tracks.","trafficway.",
             "trail.","trails.","trak.","trce.","trfy.","trk.","trks.",
             "trl.","trls.","trnpk.","trpk.","trwy.","tunel.","tunl.",
             "tunls.","tunnel.","tunnels.","tunnl.","turnpike.",
             "turnpk.","un.","underpass.","union.","unions.","uns.",
             "upas.","valley.","valleys.","vally.","vdct.","via.",
             "viadct.","viaduct.","view.","views.","vill.","villag.",
             "village.","villages.","ville.","villg.","villiage.","vis.",
             "vist.","vista.","vl.","vlg.","vlgs.","vlly.","vly.","vlys.",
             "vst.","vsta.","vw.","vws.","walk.","walks.","wall.","way.",
             "ways.","well.","wells.","wl.","wls.","wy.","xing.","xrd."]



states = ["alabama", "ala.", "ala", "al",
          "alaska", "alaska", "ak",
          "arizona", "ariz.", "ariz", "az",
          "arkansas", "ark.", "ark", "ar",
          "california", "calif.", "calif", "ca",
          "canalzone", "c.z.", "cz",
          "colorado", "colo.", "colo", "co",
          "connecticut", "conn.", "conn", "ct",
          "delaware", "del.", "del", "de",
          "district of columbia", "d.c.", "dc",
          "florida", "fla.", "fla", "fl",
          "georgia", "ga.", "ga",
          "guam", "guam", "gu",
          "hawaii", "hawaii", "hi",
          "idaho", "idaho", "id",
          "illinois", "ill.", "ill", "il",
          "indiana", "ind.", "ind", "in",
          "iowa", "iowa", "ia",
          "kansas", "kan.", "kan", "ks",
          "kentucky", "ky.", "ky",
          "louisiana", "la.", "la",
          "maine", "maine", "me",
          "maryland", "md.", "md",
          "massachusetts", "mass.", "mass", "ma",
          "michigan", "mich.", "mich", "mi",
          "minnesota", "minn.", "minn", "mn",
          "mississippi", "miss.", "miss", "ms",
          "missouri", "mo.", "mo",
          "montana", "mont.", "mont", "mt",
          "nebraska", "neb.", "neb", "ne",
          "nevada", "nev.", "nev", "nv",
          "newhampshire", "n.h.", "nh",
          "newjersey", "n.j.", "nj",
          "newmexico", "n.m.", "nm",
          "newyork", "n.y.", "ny",
          "northcarolina", "n.c.", "nc",
          "northdakota", "n.d.", "nd",
          "ohio", "ohio", "oh",
          "oklahoma", "okla.", "ok",
          "oregon", "ore.", "ore", "or",
          "pennsylvania", "pa.", "pa",
          "puertorico", "p.r.", "pr",
          "rhodeisland", "r.i.", "ri",
          "southcarolina", "s.c.", "sc",
          "southdakota", "s.d.", "sd",
          "tennessee", "tenn.", "tenn", "tn",
          "texas", "texas", "tx",
          "utah", "utah", "ut",
          "vermont", "vt.", "vt",
          "virginislands", "v.i.", "vi",
          "virginia", "va.", "va",
          "washington", "wash.", "wa",
          "westvirginia", "w.va.", "wv",
          "wisconsin", "wis.", "wis", "wi",
          "wyoming", "wyo.", "wyo", "wy"]

phone_r1 = [
    {"label": "PHONE_NUMBER", "pattern":
     [{'SHAPE': 'ddddddd'}]},
    {"label": "PHONE_NUMBER", "pattern":
     [{'SHAPE': 'dddddddddd'}]},
    {"label": "PHONE_NUMBER", "pattern":
     [{'SHAPE': 'ddddddddddd'}]},
    {"label": "PHONE_NUMBER", "pattern":
     [{'SHAPE': 'd'},
      {'ORTH': '('},
      {'SHAPE': 'ddd'},
      {'ORTH': ')'},
      {'SHAPE': 'ddd'},
      {'ORTH': '-', 'OP': '?'},
      {'SHAPE': 'dddd'}]},
    {"label": "PHONE_NUMBER", "pattern":
     [{'SHAPE': 'd'},
      {'ORTH': '-', 'OP': '?'},
      {'SHAPE': 'ddd'},
      {'ORTH': '-', 'OP': '?'},
      {'SHAPE': 'ddd'},
      {'ORTH': '-', 'OP': '?'},
      {'SHAPE': 'dddd'}]},   ]


phone_r2 = [
    {"label": "PHONE_NUMBER", "pattern":
     [{'ORTH': '('},
      {'SHAPE': 'ddd'},
      {'ORTH': ')'},
      {'SHAPE': 'ddd'},
      {'ORTH': '-', 'OP': '?'},
      {'SHAPE': 'dddd'}]},
    {"label": "PHONE_NUMBER", "pattern":
     [{'SHAPE': 'ddd'},
      {'ORTH': '-', 'OP': '?'},
      {'SHAPE': 'ddd'},
      {'ORTH': '-', 'OP': '?'},
      {'SHAPE': 'dddd'}]},   ]

phone_r3 = [
    {"label": "PHONE_NUMBER", "pattern":
     [{'SHAPE': 'ddd'},
      {'ORTH': '-', 'OP': '?'},
      {'SHAPE': 'dddd'}]},
]

email_r1 = [
    {"label": "EMAIL", "pattern":
    # [{"TEXT" : {"REGEX": "[\w\.-]+@[\w\.-]+"}}]}
     [{"LIKE_EMAIL": True}]}
]

to_replace_ents = ["PERSON", "ADDRESS", "EMAIL", "PHONE_NUMBER"]

person_r1 = [
    {"label": "PERSON", "pattern":
     [{"POS": "PROPN"},]}
]


street_r1 = [
    {"label": "ADDRESS", "pattern":
     [{"LIKE_NUM": True, 'OP': '?'},
      {"lower": {"IN": directions}, 'OP': '?'},
      {"TEXT": {"REGEX": "[\w]{0-3}"}},
      {"lower": {"IN": usps_abbr}},
      {"IS_PUNCT": True},
      {"TEXT": {"REGEX": "[\w]"}, 'OP': '*'},
      {"IS_PUNCT": True},
      {"lower": {"IN": states}}
      ]},
]

# street_r2 = [
#     {"label": "ADDRESS", "pattern":
#      [{"LIKE_NUM": True, 'OP': '?'},
#       {"lower": {"IN": directions}, 'OP': '?'},
#       {"TEXT": {"REGEX": "[\w]{0-3}"}},
#       {"lower": {"IN": usps_abbr}},
#       {"IS_PUNCT": True},
#       {"TEXT": {"REGEX": "[\w]"}, 'OP': '*'},
#       {"IS_PUNCT": True},
#       {"lower": {"IN": states}, 'OP': '?'}
#       ]},
# ]

street_r2 = [
    {"label": "ADDRESS", "pattern":
     [{"LIKE_NUM": True, 'OP': '?'},
      {"lower": {"IN": directions}, 'OP': '?'},
      {"TEXT": {"REGEX": "[\w]+"}},
      {"lower": {"IN": usps_abbr}}
      ]},
]
