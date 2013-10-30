#!/usr/bin/python
# Copyright (c) Universal Technical Resource Services, Inc.
# Version 2.0
# CGrimes.Oct 28 2013

import cgi
import datetime
from datetime import datetime
import os
import sys
import re

ext = None

def init_ext():
  global ext
  ext = ext

# Note: The following line should be commented-out for production.
# import cgitb ; cgitb.enable()

# ShortnameUrlPathPrefix = cgi.escape("/isis")
ShortnameUrlPathPrefix = cgi.escape("")

MQ1TailNumberOptions = [
    ["Not Listed", "NONL"],
    ["01003079", "01003079"],
    ["07003211", "07003211"],
    ["07003212", "07003212"],
    ["07003215", "07003215"],
    ["07003216", "07003216"],
    ["07003217", "07003217"],
    ["07003218", "07003218"],
    ["07003222", "07003222"],
    ["08003226", "08003226"],
    ["08003227", "08003227"],
    ["02003090", "02003090"],
    ["03033115", "03033115"],
    ["05003140", "05003140"],
    ["05003150", "05003150"],
    ["05003153", "05003153"],
    ["06003157", "06003157"],
    ["06003167", "06003167"],
    ["06003176", "06003176"],
    ["07003180", "07003180"],
    ["07003183", "07003183"],
    ["07003185", "07003185"],
    ["98003047", "98003047"],
    ["00003066", "00003066"],
    ["00003067", "00003067"],
    ["00003068", "00003068"],
    ["00003069", "00003069"],
    ["00003071", "00003071"],
    ["01003074", "01003074"],
    ["01003075", "01003075"],
    ["01003076", "01003076"],
    ["01003077", "01003077"],
    ["01003078", "01003078"],
    ["02003081", "02003081"],
    ["02003088", "02003088"],
    ["02003091", "02003091"],
    ["02003096", "02003096"],
    ["02003097", "02003097"],
    ["02003098", "02003098"],
    ["02003100", "02003100"],
    ["02003102", "02003102"],
    ["03003104", "03003104"],
    ["03003107", "03003107"],
    ["03003110", "03003110"],
    ["03003111", "03003111"],
    ["03033116", "03033116"],
    ["03033117", "03033117"],
    ["03033118", "03033118"],
    ["03033119", "03033119"],
    ["03033120", "03033120"],
    ["03033122", "03033122"],
    ["04003125", "04003125"],
    ["04003126", "04003126"],
    ["04003128", "04003128"],
    ["04003129", "04003129"],
    ["04003132", "04003132"],
    ["04003133", "04003133"],
    ["04003134", "04003134"],
    ["05003136", "05003136"],
    ["05003137", "05003137"],
    ["05003138", "05003138"],
    ["05003142", "05003142"],
    ["05003143", "05003143"],
    ["05003144", "05003144"],
    ["05003148", "05003148"],
    ["05003149", "05003149"],
    ["05003154", "05003154"],
    ["05003156", "05003156"],
    ["05033146", "05033146"],
    ["05033147", "05033147"],
    ["06003159", "06003159"],
    ["06003160", "06003160"],
    ["06003161", "06003161"],
    ["06003162", "06003162"],
    ["06003164", "06003164"],
    ["06003166", "06003166"],
    ["06003168", "06003168"],
    ["06003170", "06003170"],
    ["06003172", "06003172"],
    ["06003175", "06003175"],
    ["06003177", "06003177"],
    ["07003179", "07003179"],
    ["07003181", "07003181"],
    ["07003182", "07003182"],
    ["07003184", "07003184"],
    ["07003187", "07003187"],
    ["07003188", "07003188"],
    ["07003189", "07003189"],
    ["07003190", "07003190"],
    ["07003191", "07003191"],
    ["07003192", "07003192"],
    ["07003193", "07003193"],
    ["07003194", "07003194"],
    ["07003195", "07003195"],
    ["07003196", "07003196"],
    ["07003197", "07003197"],
    ["07003198", "07003198"],
    ["07003199", "07003199"],
    ["07003201", "07003201"],
    ["07003202", "07003202"],
    ["07003203", "07003203"],
    ["07003205", "07003205"],
    ["07003206", "07003206"],
    ["07003207", "07003207"],
    ["07003208", "07003208"],
    ["07003209", "07003209"],
    ["07003210", "07003210"],
    ["07003213", "07003213"],
    ["07003214", "07003214"],
    ["07003219", "07003219"],
    ["07003220", "07003220"],
    ["07003221", "07003221"],
    ["07003223", "07003223"],
    ["08003234", "08003234"],
    ["08003235", "08003235"],
    ["08003236", "08003236"],
    ["08003237", "08003237"],
    ["08003238", "08003238"],
    ["08003240", "08003240"],
    ["08003241", "08003241"],
    ["08003243", "08003243"],
    ["08003245", "08003245"],
    ["08003513", "08003513"],
    ["08003514", "08003514"],
    ["09003251", "09003251"],
    ["09003253", "09003253"],
    ["09003257", "09003257"],
    ["09003259", "09003259"],
    ["09003260", "09003260"],
    ["09003268", "09003268"],
    ["97003037", "97003037"],
    ["98003040", "98003040"],
    ["98003041", "98003041"],
    ["98003042", "98003042"],
    ["98003044", "98003044"],
    ["98003051", "98003051"],
    ["99003055", "99003055"],
    ["99003057", "99003057"],
    ["99003058", "99003058"],
    ["99003059", "99003059"],
    ["99003060", "99003060"],
    ["99003063", "99003063"],
    ["05033145", "05033145"],
    ["07003200", "07003200"],
    ["09003261", "09003261"],
    ["09003262", "09003262"],
    ["09003263", "09003263"],
    ["09003264", "09003264"],
    ["02003101", "02003101"],
    ["03003106", "03003106"],
    ["03033123", "03033123"],
    ["05003139", "05003139"],
    ["08003225", "08003225"],
    ["08003229", "08003229"],
    ["08003230", "08003230"],
    ["08003231", "08003231"],
    ["08003232", "08003232"],
    ["08003233", "08003233"],
    ["08003247", "08003247"],
    ["08003248", "08003248"],
    ["09003254", "09003254"],
    ["09003255", "09003255"],
    ["09003256", "09003256"],
    ["09003258", "09003258"],
    ["09003266", "09003266"],
    ["07003250", "07003250"],
    ["09003252", "09003252"],
    ["04003131", "04003131"],
    ["07003224", "07003224"],
    ["08003242", "08003242"],
    ["08003244", "08003244"],
    ["08003246", "08003246"],
    ["ANYMQ001", "ANYMQ001"]
]

MQ9TailNumberOptions = [
    ["Not Listed", "NONL"],
    ["04004010","04004010"],
    ["04004011","04004011"],
    ["04004012","04004012"],
    ["04004013","04004013"],
    ["04004014","04004014"],
    ["05004015","05004015"],
    ["05004016","05004016"],
    ["05004018","05004018"],
    ["05044102","05044102"],
    ["06004020","06004020"],
    ["06004105","06004105"],
    ["07004023","07004023"],
    ["07004025","07004025"],
    ["07004026","07004026"],
    ["07004027","07004027"],
    ["07004028","07004028"],
    ["07004029","07004029"],
    ["07004030","07004030"],
    ["07004031","07004031"],
    ["07004032","07004032"],
    ["07004033","07004033"],
    ["07004039","07004039"],
    ["08004035","08004035"],
    ["08004036","08004036"],
    ["08004037","08004037"],
    ["08004038","08004038"],
    ["08004039","08004039"],
    ["08004040","08004040"],
    ["08004041","08004041"],
    ["08004042","08004042"],
    ["08004043","08004043"],
    ["08004044","08004044"],
    ["08004045","08004045"],
    ["08004047","08004047"],
    ["08004048","08004048"],
    ["08004049","08004049"],
    ["08004050","08004050"],
    ["08004051","08004051"],
    ["08004052","08004052"],
    ["08004053","08004053"],
    ["08004084","08004084"],
    ["08004085","08004085"],
    ["08004086","08004086"],
    ["08004087","08004087"],
    ["09004054","09004054"],
    ["09004060","09004060"],
    ["09004062","09004062"],
    ["09004063","09004063"],
    ["09004064","09004064"],
    ["09004066","09004066"],
    ["09004067","09004067"],
    ["09004068","09004068"],
    ["09004069","09004069"],
    ["09004072","09004072"],
    ["09004073","09004073"],
    ["09004075","09004075"],
    ["10004079","10004079"],
    ["10004085","10004085"],
    ["10004088","10004088"],
    ["10004089","10004089"],
    ["10004090","10004090"],
    ["10004091","10004091"],
    ["10004098","10004098"],
    ["10004099","10004099"],
    ["10004100","10004100"],
    ["10004101","10004101"],
    ["10004103","10004103"],
    ["10004104","10004104"],
    ["10004113","10004113"],
    ["10004114","10004114"],
    ["11004120","11004120"],
    ["11004121","11004121"],
    ["11004123","11004123"],
    ["11004124","11004124"],
    ["11004125","11004125"],
    ["11004126","11004126"],
    ["11004128","11004128"],
    ["11004129","11004129"],
    ["4855TRCK","4855TRCK"],
    ["TRCK4855","TRCK4855"]
]

MQ1BaseOptions = [
   ["Not Listed",              "NONL"],
   ["Cannon AFB (NM)",         "KCVS"],
   ["Ellington FLD ANG (TX)",  "KEFD"],
   ["Hector FLD (ND)",         "KFAR"],
   ["Holloman AFB (NM)",       "KHMN"],
   ["March ANG (CA)",          "KRIV"],
   ["Creech AFB (NV)",         "KINS"]
]

MQ9BaseOptions = [
   ["Not Listed",              "NONL"],
   ["Cannon AFB (NM)",         "KCVS"],
   ["Hancock FLD (NY)",        "KSYR"],
   ["Holloman AFB (NM)",       "KHMN"],
   ["Creech AFB (NV)",         "KINS"],
   ["Deployed Location",       "ZZZZ"]
]

C130JTailNumberOptions = [
  ["0000000 (0000)", "0000"],
  ["9408151 (5413)", "5413"],
  ["9408152 (5415)", "5415"],
  ["9605300 (5451)", "5451"],
  ["9605301 (5452)", "5452"],
  ["9605302 (5453)", "5453"],
  ["9608153 (5454)", "5454"],
  ["9608154 (5455)", "5455"],
  ["9701351 (5469)", "5469"],
  ["9701352 (5470)", "5470"],
  ["9701353 (5471)", "5471"],
  ["9701354 (5472)", "5472"],
  ["9705303 (5473)", "5473"],
  ["9705304 (5474)", "5474"],
  ["9705305 (5475)", "5475"],
  ["9705306 (5476)", "5476"],
  ["9701931 (5477)", "5477"],
  ["9805307 (5486)", "5486"],
  ["9805308 (5487)", "5487"],
  ["9801932 (5490)", "5490"],
  ["9801355 (5491)", "5491"],
  ["9801356 (5492)", "5492"],
  ["9801357 (5493)", "5493"],
  ["9801358 (5494)", "5494"],
  ["9905309 (5501)", "5501"],
  ["9901933 (5502)", "5502"],
  ["9901431 (5517)", "5517"],
  ["9901432 (5518)", "5518"],
  ["9901433 (5519)", "5519"],
  ["0001934 (5522)", "5522"],
  ["0101461 (5525)", "5525"],
  ["0101462 (5526)", "5526"],
  ["0101935 (5532)", "5532"],
  ["0200314 (5545)", "5545"],
  ["0208155 (5546)", "5546"],
  ["0201434 (5547)", "5547"],
  ["0201463 (5551)", "5551"],
  ["0201464 (5552)", "5552"],
  ["0308154 (5557)", "5557"],
  ["0403142 (5558)", "5558"],
  ["0403143 (5559)", "5559"],
  ["0403144 (5560)", "5560"],
  ["0408153 (5561)", "5561"],
  ["0508152 (5566)", "5566"],
  ["0503146 (5567)", "5567"],
  ["0503147 (5568)", "5568"],
  ["0503145 (5569)", "5569"],
  ["0508157 (5570)", "5570"],
  ["0508156 (5571)", "5571"],
  ["0501435 (5572)", "5572"],
  ["0508158 (5573)", "5573"],
  ["0501465 (5574)", "5574"],
  ["0501436 (5575)", "5575"],
  ["0501466 (5576)", "5576"],
  ["0608159 (5581)", "5581"],
  ["0604631 (5582)", "5582"],
  ["0601438 (5584)", "5584"],
  ["0601467 (5585)", "5585"],
  ["0601437 (5586)", "5586"],
  ["0604632 (5587)", "5587"],
  ["0604633 (5588)", "5588"],
  ["0604634 (5589)", "5589"],
  ["0701468 (5594)", "5594"],
  ["0704635 (5595)", "5595"],
  ["0704636 (5596)", "5596"],
  ["0704637 (5597)", "5597"],
  ["0704638 (5598)", "5598"],
  ["0704639 (5599)", "5599"],
  ["0746310 (5600)", "5600"],
  ["0746311 (5608)", "5608"],
  ["0808601 (5609)", "5609"],
  ["0746312 (5610)", "5610"],
  ["0808602 (5611)", "5611"],
  ["0808604 (5612)", "5612"],
  ["0808603 (5613)", "5613"],
  ["0808606 (5614)", "5614"],
  ["0808605 (5615)", "5615"],
  ["0808607 (5616)", "5616"],
  ["0608611 (5619)", "5619"],
  ["0608612 (5620)", "5620"],
  ["0608610 (5621)", "5621"],
  ["0708608 (5622)", "5622"],
  ["0708609 (5623)", "5623"],
  ["0708613 (5624)", "5624"],
  ["0708614 (5625)", "5625"],
  ["0703170 (5628)", "5628"],
  ["0900108 (5633)", "5633"],
  ["0900109 (5634)", "5634"],
  ["0603171 (5641)", "5641"],
  ["0803172 (5642)", "5642"],
  ["0803173 (5643)", "5643"],
  ["0803174 (5648)", "5648"],
  ["0906207 (5656)", "5656"],
  ["0906208 (5657)", "5657"],
  ["0906209 (5658)", "5658"],
  ["0906210 (5659)", "5659"],
  ["0803175 (5670)", "5670"],
  ["0803176 (5671)", "5671"],
  ["0803177 (5672)", "5672"],
  ["0803178 (5673)", "5673"],
  ["0803179 (5674)", "5674"],
  ["0805675 (5675)", "5675"],
  ["0805678 (5678)", "5678"],
  ["0805679 (5679)", "5679"],
  ["0806201 (5680)", "5680"],
  ["0806202 (5681)", "5681"],
  ["0806203 (5682)", "5682"],
  ["0805683 (5683)", "5683"],
  ["0805684 (5684)", "5684"],
  ["0805685 (5685)", "5685"],
  ["0805686 (5686)", "5686"],
  ["0805691 (5691)", "5691"],
  ["0805692 (5692)", "5692"],
  ["0805693 (5693)", "5693"],
  ["0806204 (5694)", "5694"],
  ["0806205 (5695)", "5695"],
  ["0806206 (5696)", "5696"],
  ["0805697 (5697)", "5697"],
  ["1005700 (5700)", "5700"],
  ["1005701 (5701)", "5701"],
  ["0805705 (5705)", "5705"],
  ["0905706 (5706)", "5706"],
  ["0905707 (5707)", "5707"],
  ["0905708 (5708)", "5708"],
  ["0905709 (5709)", "5709"],
  ["0905710 (5710)", "5710"],
  ["0905711 (5711)", "5711"],
  ["0805712 (5712)", "5712"],
  ["0905713 (5713)", "5713"],
  ["1005714 (5714)", "5714"],
  ["0805715 (5715)", "5715"],
  ["1005716 (5716)", "5716"],
  ["1005717 (5717)", "5717"],
  ["1105719 (5719)", "5719"],
  ["0805724 (5724)", "5724"],
  ["1105725 (5725)", "5725"],
  ["0805726 (5726)", "5726"],
  ["1105727 (5727)", "5727"],
  ["1005728 (5728)", "5728"],
  ["1105729 (5729)", "5729"],
  ["1105731 (5731)", "5731"],
  ["1105733 (5733)", "5733"],
]


C130JBaseOptions = [
  ["Not Listed", "UNKWN"],
  ["Baltimore ANG (MD) (135th)", "KMTN1"],
  ["Cannon AFB (NM) (AC-130J)", "KCVS2"],
  ["Cannon AFB (NM)(MC-130J)", "KCVS1"],
  ["Channel Island AGB (CA) (146 AW)", "KNTD1"],
  ["Davis-Monthan AFB (NM) (563 RQG)", "KDMA1"],
  ["Dyess AFB (TX) (317 AG)", "KDYS1"],
  ["Eglin AFB (FL) (9 SOS)", "KVPS1"],
  ["Harrisburg IAP (PA) (193 SOW)", "KMDT1"],
  ["Hurlburt (7 SOS)", "KHRT1"],
  ["Kadena AB (1 SOS)", "RODN1"],
  ["Kadena AB (17 SOS)", "RODN2"],
  ["Keesler AFB (MS) (53 WRS)", "KBIX1"],
  ["Keesler AFB (MS) (815 AS)", "KBIX2"],
  ["Kirtland AFB (NM) (HC-130J)", "KABQ1"],
  ["Kirtland AFB (NM) (MC-130J)", "KABQ2"],
  ["Little Rock AFB (AR) (19 AW)", "KLRF1"],
  ["Little Rock AFB (AR)(314 AW)", "KLRF2"],
  ["RAF Mildenhall (67 SOS)", "EGUN2"],
  ["RAF Mildenhall (MC-130J)", "EGUN1"],
  ["Moody AFB (GA) (347 RQG)", "KVAD1"],
  ["Ramstein AB (86 AW)", "ETAR1"],
  ["Quonset Point AGB (RI) (143 AW)", "KOQU1"],
  ["Yokota AB (374 AW)", "RJTY1"]
]

B1TailNumberOptions = [
    ["Not Listed", "NONL"],
    ["84000049", "84000049"],
    ["85000068", "85000068"],
    ["85000075", "85000075"],
    ["86000122", "86000122"],
    ["85000059", "85000059"],
    ["85000061", "85000061"],
    ["85000064", "85000064"],
    ["85000065", "85000065"],
    ["85000069", "85000069"],
    ["85000072", "85000072"],
    ["85000073", "85000073"],
    ["85000074", "85000074"],
    ["85000077", "85000077"],
    ["85000080", "85000080"],
    ["85000088", "85000088"],
    ["85000089", "85000089"],
    ["85000090", "85000090"],
    ["86000097", "86000097"],
    ["86000098", "86000098"],
    ["86000100", "86000100"],
    ["86000101", "86000101"],
    ["86000103", "86000103"],
    ["86000105", "86000105"],
    ["86000107", "86000107"],
    ["86000108", "86000108"],
    ["86000109", "86000109"],
    ["86000110", "86000110"],
    ["86000112", "86000112"],
    ["86000117", "86000117"],
    ["86000119", "86000119"],
    ["86000120", "86000120"],
    ["86000123", "86000123"],
    ["86000124", "86000124"],
    ["86000126", "86000126"],
    ["86000132", "86000132"],
    ["86000133", "86000133"],
    ["86000135", "86000135"],
    ["86000136", "86000136"],
    ["86000140", "86000140"],
    ["85000060", "85000060"],
    ["85000066", "85000066"],
    ["85000079", "85000079"],
    ["85000081", "85000081"],
    ["85000083", "85000083"],
    ["85000084", "85000084"],
    ["85000085", "85000085"],
    ["85000087", "85000087"],
    ["85000091", "85000091"],
    ["86000093", "86000093"],
    ["86000094", "86000094"],
    ["86000095", "86000095"],
    ["86000099", "86000099"],
    ["86000102", "86000102"],
    ["86000104", "86000104"],
    ["86000111", "86000111"],
    ["86000113", "86000113"],
    ["86000115", "86000115"],
    ["86000118", "86000118"],
    ["86000121", "86000121"],
    ["86000125", "86000125"],
    ["86000127", "86000127"],
    ["86000129", "86000129"],
    ["86000130", "86000130"],
    ["86000134", "86000134"],
    ["86000137", "86000137"],
    ["86000138", "86000138"],
    ["86000139", "86000139"]
]

B1BaseOptions = [
  ["Not Listed",        "UNKWN"],
  ["Ellsworth AFB (SD)","KRCA"],
  ["Dyess AFB (TX)",    "KDYS"],
  ["Deployed Location", "ZZZZ"]
]

def GetScriptUrl():
    return os.getenv("SCRIPT_NAME")

def UploadWhatToTitle(uploadWhat):
    if uploadWhat == "c130j":
        return "C130J File Upload"
    elif uploadWhat == "mq1":
        return "MQ1 File Upload"
    elif uploadWhat == "mq9":
        return "MQ9 File Upload"
    elif uploadWhat == "b1":
        return "B1 File Upload"        
    else:
        return ("Upload " + uploadWhat)

def WritePrologueHtml(uploadWhat):
    print "Content-type: text/html\r"
    print "\r"
    print "<html>"
    print "<head>"
    print ("<title>" + cgi.escape(UploadWhatToTitle(uploadWhat)) + "</title>")
    print "<link rel=\"stylesheet\" type=\"text/css\" href=\"{ShortnameUrlPathPrefix}/css/dialog.css\">".format(ShortnameUrlPathPrefix = ShortnameUrlPathPrefix)
    if uploadWhat == "c130j" or uploadWhat == "mq1" or uploadWhat == "mq9" or uploadWhat == "b1":
        print """
<link rel="stylesheet" type="text/css" href="{ShortnameUrlPathPrefix}/css/smoothness/jquery-ui-1.8.16.custom.css" />
<script type="text/javascript" src="{ShortnameUrlPathPrefix}/js/jquery-1.6.3.min.js"></script>
<script type="text/javascript" src="{ShortnameUrlPathPrefix}/js/jquery-ui-1.8.16.custom.min.js"></script>
<script type="text/javascript" src="{ShortnameUrlPathPrefix}/js/jquery.timeentry.min-1.4.9.js"></script>
<link rel="stylesheet" type="text/css" href="http://code.jquery.com/ui/1.10.3/themes/smoothness/jquery-ui.css" />
<script type="text/javascript" src="http://code.jquery.com/ui/1.10.3/jquery-ui.js"></script>
<script type="text/javascript" src="http://code.jquery.com/jquery-1.9.1.js"></script>
<link rel="stylesheet" type="text/css" href="/resources/demos/style.css" />



""".format(ShortnameUrlPathPrefix = ShortnameUrlPathPrefix)
        print """

<script type="text/javascript">

<!--
$(document).ready(function () {
$("#DownloadDateInput").datepicker({ maxDate: "0d",
                                     buttonText: "Choose Date",
                                     showOn: "both"});
});
$("form").submit(function () {
    $("input[type=submit]", this).click(function () {
        return false;
    });
    return true;
});
-->
</script>
"""
# In javascript above...added 'space' after 3 x function arguments - Lines 585, 590, Line 591
# In Javascript above...line 593-moved brackets to column 5 vice 9, line 594-move return to column 5 vice 9
    print "</head>"
    print "<body>"

def WriteEpilogueHtml():
    print "</body>"
    print "</html>"

def WriteSelectHtml(name, options, haveBlankOption = True, fieldStorage = None):
    defaultValue = ""
    if not fieldStorage is None:
        defaultValue = fieldStorage.getfirst(name, "")
    print ("<select name=\"" + cgi.escape(name) + "\">")
    if haveBlankOption:
        print "<option value=\"\"></option>"
    for option in options:
        value = option[1]
        selectedString = ""
        if value == defaultValue:
            selectedString = " selected"
        print ("<option value=\"" +
               cgi.escape(value) +
               "\"" +
               selectedString +
               ">" +
               cgi.escape(option[0]) +
               "</option>")
    print "</select>"

def WriteDefaultFormHtml(uploadWhat, formInfoHtml, fieldStorage = None):
    # Note: The "fieldStorage" argument is for when we implement the form for
    # the C-130J, which has fields other than just the file one.
    if uploadWhat == "c130j":
        print """
<form name="form" action="{scriptUrlAttrVal}" method="POST" enctype="multipart/form-data">
<center>
<h2 style=color:blue> C-130J Uploads</h2>
</center>
<br>
  <p>Tail Number (LHSN):
""".format(scriptUrlAttrVal = GetScriptUrl())
        WriteSelectHtml(name         = "tail-number", 
                        options      = C130JTailNumberOptions,
                        fieldStorage = fieldStorage)
        print """
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

        Base you are uploading from: 

"""
        WriteSelectHtml(name         = "base",
                        options      = C130JBaseOptions,
                        fieldStorage = fieldStorage)
        print """

</p>
<br>

  <p>Date file downloaded from aircraft (be as accurate as possible):
     <input type="text" name="download-date" id="DownloadDateInput"></p>
     <p style=color:blue;> <i>Use Date from DTADS File Name </i> </p>
<br>
  <p>Select File for Upload &nbsp;&nbsp; <input type="file" name="upload_file" size="30" maxlength="80"></p>
<br>
  <p align="center"><input type="submit" label="Upload" value="Upload">
                    &nbsp;&nbsp;
                    <input type="reset" label="Reset" value="Reset"></p>

</form>
"""
    elif uploadWhat == "mq1":
        print """
<form name="form" action="{scriptUrlAttrVal}" method="POST" enctype="multipart/form-data">

<center>
<h2 style=color:blue> MQ-1 Uploads</h2>
</center>
<br>

  <p>Tail Number:
""".format(scriptUrlAttrVal = GetScriptUrl())
        WriteSelectHtml(name         = "tail-number", 
                        options      = MQ1TailNumberOptions,
                        fieldStorage = fieldStorage)
        print """
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

        Base you are uploading from: 
"""
        WriteSelectHtml(name         = "base",
                        options      = MQ1BaseOptions,
                        fieldStorage = fieldStorage)
        print """
</p>
<br>
  <p>Date of Flight (From Folder Name:  MMDDYY):
     <input type="text" name="download-date" id="DownloadDateInput"><br></p>
<br>
  <p>Select File for Upload &nbsp;&nbsp; <input type="file" name="upload_file" size="30" maxlength="80"></p>
<br>
  <p align="center"><input type="submit" label="Upload" value="Upload">
                    &nbsp;&nbsp;
                    <input type="reset" label="Reset" value="Reset"></p>


</form>
"""
    elif uploadWhat == "mq9":
        print """
<form name="form" action="{scriptUrlAttrVal}" method="POST" enctype="multipart/form-data">

<center>
<h2 style=color:blue> MQ-9 Uploads</h2>
</center>
<br>

  <p>Tail Number:
""".format(scriptUrlAttrVal = GetScriptUrl())
        WriteSelectHtml(name         = "tail-number", 
                        options      = MQ9TailNumberOptions,
                        fieldStorage = fieldStorage)
        print """
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

        Base you are uploading from: 
"""
        WriteSelectHtml(name         = "base",
                        options      = MQ9BaseOptions,
                        fieldStorage = fieldStorage)
        print """
</p>
<br>
  <p>Date of Flight (From Folder Name:  MMDDYY):
     <input type="text" name="download-date" id="DownloadDateInput"><br></p>
<br>
  <p>Select File for Upload &nbsp;&nbsp; <input type="file" name="upload_file" size="30" maxlength="80"></p>
<br>
  <p align="center"><input type="submit" label="Upload" value="Upload">
                    &nbsp;&nbsp;
                    <input type="reset" label="Reset" value="Reset"></p>
</form>
"""
    elif uploadWhat == "b1":
        print """
<form name="form" action="{scriptUrlAttrVal}" method="POST" enctype="multipart/form-data">

<center>
<h2 style=color:blue> B-1 Uploads</h2>
</center>
<br>

  <p>Tail Number:
""".format(scriptUrlAttrVal = GetScriptUrl())
        WriteSelectHtml(name         = "tail-number", 
                        options      = B1TailNumberOptions,
                        fieldStorage = fieldStorage)
        print """
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

        Base you are uploading from: 
"""
        WriteSelectHtml(name         = "base",
                        options      = B1BaseOptions,
                        fieldStorage = fieldStorage)
        print """
</p>
<br>
  <p>Date file downloaded from aircraft (be as accurate as possible):
     <input type="text" name="download-date" id="DownloadDateInput"><br></p>
<br>
  <p>Select File for Upload &nbsp;&nbsp; <input type="file" name="upload_file" size="30" maxlength="80"></p>
<br>
  <p align="center"><input type="submit" label="Upload" value="Upload">
                    &nbsp;&nbsp;
                    <input type="reset" label="Reset" value="Reset"></p>
</form>
"""
    else:
        print """
<center>
  <table border="2" class="tblSection" cellpadding=5 cellspacing=3 style="border-collapse: collapse" frame="box" rules="none">
    <form name="form" action="{scriptUrlAttrVal}" method="POST" enctype="multipart/form-data">
      <tr class="section-header">
        <td colspan="2" align="center">
          <span class="section-header">
            {formTitleHtml}
          </span>
        </td>
      </tr>
      <tr class="section-header">
        <td colspan="2" align="left">
          <span class="section-info">
            {formInfoHtml}
          </span>
        </td>
      </tr>
      <tr class="section-row">
        <td align="right">
          Upload file:
        </td>
        <td>
          <input type="file" name="upload_file" size="30" maxlength="80"> 
        </td>
      </tr>
      <tr class="section-header">
        <td colspan=2 align="center"><br>
          <input type="submit" label="Upload" value="Upload">
                &nbsp;&nbsp;
          <input type="reset" label="Reset" value="Reset">
        </td>
      </tr>
    </form>
  </table>
</center>
""".format(scriptUrlAttrVal = GetScriptUrl(),
           formTitleHtml    = cgi.escape("Upload " + uploadWhat),
           formInfoHtml     = (formInfoHtml or ""))

def WriteErrorAndFormAndEpilogueHtml(html, uploadWhat, formInfoHtml, fieldStorage):
    WriteDefaultFormHtml(uploadWhat   = uploadWhat,
                         formInfoHtml = formInfoHtml,
                         fieldStorage = fieldStorage)
    print """
<center>
  <hr noshade size=1 width="80%%">
  <table border=0 bgcolor="#000000" cellpadding=0 cellspacing=0>
    <tr>
      <td>
        <table border=0 width="100%%" cellpadding=5 cellspacing=1>
          <tr>
            <td bgcolor="#ffefd5" width="100%%">
              <font color="#ff0000"><b>Error -</b></font>
              {html}
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</center>
""".format(html = html)
    WriteEpilogueHtml()

def HandleShowFormRequest(uploadWhat, formInfoHtml):
    WritePrologueHtml(uploadWhat = uploadWhat)
    WriteDefaultFormHtml(uploadWhat   = uploadWhat,
                         formInfoHtml = formInfoHtml)
    WriteEpilogueHtml()

def SanitizeStoreFilename(filename):
    # TODO: We could "re.compile" these regexps.

    # Strip off any leading Unix-like or Windows-like file path directory.
    m = re.search("[^/\\\\]*$", filename)
    if m is None:
        return ""
    filename = m.group()

    # Remove any contiguous non-alphanumeric characters from the start.
    filename = re.sub("^[^a-zA-Z0-9]+", "", filename)

    # Remove any contiguous non-alphanumeric characters from the end
    filename = re.sub("[^a-zA-Z0-9]+$", "", filename)

    # Replace each substring of non-{alpha,num,dot,underscore} with minus.
    filename = re.sub("[^_.a-zA-Z0-9]+", "-", filename)

    # Replace any trailing ".flag" with "-flag", to avoid conflicting with the
    # ".flag" files used by this setup.
    filename = re.sub("\\.flag$", "-flag", filename)

    return filename
    splitfilename = filename
    root, ext = os.path.splitext(splitfilename)

    ext = ext.lower()

def GetValidFormSelectValue(name, options, fieldStorage, defaultValue = ""):
    if fieldStorage is None:
        return defaultValue
    value = fieldStorage.getfirst(name, defaultValue)
    for option in options:
        if option[1] == value:
            return value
    return defaultValue

def GetValidFormDateValue(name, fieldStorage, defaultValue = None):
    dateString = fieldStorage.getfirst(name, None)
    if dateString is None:
        return defaultValue
    try:
        # datetime.datetime threw exception-trying as just datetime
        #dt = datetime.datetime.strptime(dateString, "%m/%d/%Y")
        dt = datetime.strptime(dateString, "%m/%d/%Y")
    except ValueError:
        return defaultValue
    if (dt.year < 1900) or (dt.year > 9999):
        return defaultValue
    return dt.strftime("%Y%m%d")

def HandleProcessFormRequest(uploadWhat,
                             uploadPath,
                             formInfoHtml,
                             fieldStorage):
    WritePrologueHtml(uploadWhat = uploadWhat)

    uploadFileitem = fieldStorage["upload_file"]
    if ((uploadFileitem == None)        or
        (not uploadFileitem.filename)   or
        (uploadFileitem.filename == "") or
        (not uploadFileitem.file)):
        WriteErrorAndFormAndEpilogueHtml(
            html = "You must specify the upload file.",
            uploadWhat   = uploadWhat,
            formInfoHtml = formInfoHtml,
            fieldStorage = fieldStorage)
        return

    storeFilename = ""
    if uploadWhat == "c130j":
        tailNumber = GetValidFormSelectValue(
            name         = "tail-number",
            options      = C130JTailNumberOptions,
            fieldStorage = fieldStorage)
        if tailNumber == "":
            WriteErrorAndFormAndEpilogueHtml(
                html         = "You must specify a valid tail number.",
                uploadWhat   = uploadWhat,
                formInfoHtml = formInfoHtml,
                fieldStorage = fieldStorage)
            return
        base = GetValidFormSelectValue(
            name         = "base",
            options      = C130JBaseOptions,
            fieldStorage = fieldStorage)
        if base == "":
            WriteErrorAndFormAndEpilogueHtml(
                html         = "You must specify a valid base.",
                uploadWhat   = uploadWhat,
                formInfoHtml = formInfoHtml,
                fieldStorage = fieldStorage)
            return

        downloadDate = GetValidFormDateValue(
            name         = "download-date",
            fieldStorage = fieldStorage,
            defaultValue = None)
        if (downloadDate is None) or (downloadDate == ""):
            WriteErrorAndFormAndEpilogueHtml(
                html         = "You must specify a valid download date.",
                uploadWhat   = uploadWhat,
                formInfoHtml = formInfoHtml,
                fieldStorage = fieldStorage)
            return
        extList = [".fdr", ".fdt", ".dat"]
        if ext not in extList:
            WriteErrorAndFormAndEpilogueHtml(
                html         = "You may only upload fdr / fdt / dat files",
                uploadWhat   = uploadWhat,
                formInfoHtml = formInfoHtml,
                fieldStorage = fieldStorage)
            return
        storeFilename = ("c130j-" +
                         tailNumber +
                         "-" +
                         base +
                         "-" +
                         downloadDate +
                         "-" +
                         #datetime discriminator to allow identical tailnumber uploads
                         datetime.utcnow().strftime("%j.%H%M%f") +
                         ext) 
        sanitizedFilename = SanitizeStoreFilename(storeFilename)
        if storeFilename != sanitizedFilename:
            WriteErrorAndFormAndEpilogueHtml(
                html         = ("Internal Error: Invalid filename: <code>" +
                                cgi.escape(storeFilename) +
                                "</code>"),
                uploadWhat   = uploadWhat,
                formInfoHtml = formInfoHtml,
                fieldStorage = fieldStorage)
            return
    elif uploadWhat == "mq1":
        tailNumber = GetValidFormSelectValue(
            name         = "tail-number",
            options      = MQ1TailNumberOptions,
            fieldStorage = fieldStorage)
        if tailNumber == "":
            WriteErrorAndFormAndEpilogueHtml(
                html         = "You must specify a valid tail number.",
                uploadWhat   = uploadWhat,
                formInfoHtml = formInfoHtml,
                fieldStorage = fieldStorage)
            return
        base = GetValidFormSelectValue(
            name         = "base",
            options      = MQ1BaseOptions,
            fieldStorage = fieldStorage)
        if base == "":
            WriteErrorAndFormAndEpilogueHtml(
                html         = "You must specify a valid base.",
                uploadWhat   = uploadWhat,
                formInfoHtml = formInfoHtml,
                fieldStorage = fieldStorage)
            return

        downloadDate = GetValidFormDateValue(
            name         = "download-date",
            fieldStorage = fieldStorage,
            defaultValue = None)
        if (downloadDate is None) or (downloadDate == ""):
            WriteErrorAndFormAndEpilogueHtml(
                html         = "You must specify a valid download date.",
                uploadWhat   = uploadWhat,
                formInfoHtml = formInfoHtml,
                fieldStorage = fieldStorage)
            return
        extList = [".zip"]
        if ext not in extList:
            WriteErrorAndFormAndEpilogueHtml(
                html         = "You may only upload zip files",
                uploadWhat   = uploadWhat,
                formInfoHtml = formInfoHtml,
                fieldStorage = fieldStorage)
            return
        storeFilename = ("mq1-" +
                         tailNumber +
                         "-" +
                         base +
                         "-" +
                         downloadDate +
                         ext)
        sanitizedFilename = SanitizeStoreFilename(storeFilename)
        if storeFilename != sanitizedFilename:
            WriteErrorAndFormAndEpilogueHtml(
                html         = ("Internal Error: Invalid filename: <code>" +
                                cgi.escape(storeFilename) +
                                "</code>"),
                uploadWhat   = uploadWhat,
                formInfoHtml = formInfoHtml,
                fieldStorage = fieldStorage)
            return
    elif uploadWhat == "mq9":
        tailNumber = GetValidFormSelectValue(
            name         = "tail-number",
            options      = MQ9TailNumberOptions,
            fieldStorage = fieldStorage)
        if tailNumber == "":
            WriteErrorAndFormAndEpilogueHtml(
                html         = "You must specify a valid tail number.",
                uploadWhat   = uploadWhat,
                formInfoHtml = formInfoHtml,
                fieldStorage = fieldStorage)
            return
        base = GetValidFormSelectValue(
            name         = "base",
            options      = MQ9BaseOptions,
            fieldStorage = fieldStorage)
        if base == "":
            WriteErrorAndFormAndEpilogueHtml(
                html         = "You must specify a valid base.",
                uploadWhat   = uploadWhat,
                formInfoHtml = formInfoHtml,
                fieldStorage = fieldStorage)
            return

        downloadDate = GetValidFormDateValue(
            name         = "download-date",
            fieldStorage = fieldStorage,
            defaultValue = None)
        if (downloadDate is None) or (downloadDate == ""):
            WriteErrorAndFormAndEpilogueHtml(
                html         = "You must specify a valid download date.",
                uploadWhat   = uploadWhat,
                formInfoHtml = formInfoHtml,
                fieldStorage = fieldStorage)
            return
        extList = [".zip"]
        if ext not in extList:
            WriteErrorAndFormAndEpilogueHtml(
                html         = "You may only upload zip files",
                uploadWhat   = uploadWhat,
                formInfoHtml = formInfoHtml,
                fieldStorage = fieldStorage)
            return    
        storeFilename = ("mq9-" +
                         tailNumber +
                         "-" +
                         base +
                         "-" +
                         downloadDate +
                         "-" +
                         #datetime discriminator to allow PSO1 & PSO2 uploads
                         datetime.utcnow().strftime("%j.%H%M%f") +
                         ext)
        sanitizedFilename = SanitizeStoreFilename(storeFilename)
        if storeFilename != sanitizedFilename:
            WriteErrorAndFormAndEpilogueHtml(
                html         = ("Internal Error: Invalid filename: <code>" +
                                cgi.escape(storeFilename) +
                                "</code>"),
                uploadWhat   = uploadWhat,
                formInfoHtml = formInfoHtml,
                fieldStorage = fieldStorage)
            return
    elif uploadWhat == "b1":
        tailNumber = GetValidFormSelectValue(
            name         = "tail-number",
            options      = B1TailNumberOptions,
            fieldStorage = fieldStorage)
        if tailNumber == "":
            WriteErrorAndFormAndEpilogueHtml(
                html         = "You must specify a valid tail number.",
                uploadWhat   = uploadWhat,
                formInfoHtml = formInfoHtml,
                fieldStorage = fieldStorage)
            return
        base = GetValidFormSelectValue(
            name         = "base",
            options      = B1BaseOptions,
            fieldStorage = fieldStorage)
        if base == "":
            WriteErrorAndFormAndEpilogueHtml(
                html         = "You must specify a valid base.",
                uploadWhat   = uploadWhat,
                formInfoHtml = formInfoHtml,
                fieldStorage = fieldStorage)
            return
        downloadDate = GetValidFormDateValue(
            name         = "download-date",
            fieldStorage = fieldStorage,
            defaultValue = None)
        if (downloadDate is None) or (downloadDate == ""):
            WriteErrorAndFormAndEpilogueHtml(
                html         = "You must specify a valid download date.",
                uploadWhat   = uploadWhat,
                formInfoHtml = formInfoHtml,
                fieldStorage = fieldStorage)
            return
        extList = [".mfq"]
        if ext not in extList:
            WriteErrorAndFormAndEpilogueHtml(
                html         = "You may only upload mfq files",
                uploadWhat   = uploadWhat,
                formInfoHtml = formInfoHtml,
                fieldStorage = fieldStorage)
            return
        storeFilename = ("b1-" +
                         tailNumber +
                         "-" +
                         base +
                         "-" +
                         downloadDate +
                         "-" +
                         #datetime discriminator to allow PSO1 & PSO2 uploads
                         datetime.utcnow().strftime("%j.%H%M%f") +
                         #Need to add actual CITS file format extension
                         ext)
        sanitizedFilename = SanitizeStoreFilename(storeFilename)
        if storeFilename != sanitizedFilename:
            WriteErrorAndFormAndEpilogueHtml(
                html         = ("Internal Error: Invalid filename: <code>" +
                                cgi.escape(storeFilename) +
                                "</code>"),
                uploadWhat   = uploadWhat,
                formInfoHtml = formInfoHtml,
                fieldStorage = fieldStorage)            
    else:
        providedFilePath = uploadFileitem.filename
        storeFilename = SanitizeStoreFilename(providedFilePath)
        
        if storeFilename == "":
            WriteErrorAndFormAndEpilogueHtml(
                html = ("The provided file path, <code>" + 
                        cgi.escape(providedFilePath) + 
                        "<code>, is sanitized to a blank file name."),
                uploadWhat   = uploadWhat,
                formInfoHtml = formInfoHtml,
                fieldStorage = fieldStorage)
            return
    
    storeFilePath = os.path.join(uploadPath, storeFilename);
    flagFilePath  = (storeFilePath + ".flag")
    
    if (os.path.exists(storeFilePath)):
        WriteErrorAndFormAndEpilogueHtml(
            html = ("A file named <code>" +
                    cgi.escape(storeFilename) +
                    "</code> has already been uploaded."),
            uploadWhat   = uploadWhat,
            formInfoHtml = formInfoHtml,
            fieldStorage = fieldStorage)
        return
        
    fileSize = 0
    try:
        storeFile = file(storeFilePath, "wb")
        while True:
            block = uploadFileitem.file.read(2048)
            if block:
                storeFile.write(block)
                fileSize += len(block)
            else:
                break
        storeFile.close()

        flagFile = file(flagFilePath, "wb")
        flagFile.write("");
        flagFile.close();

    except Exception:
        WriteErrorAndFormAndEpilogueHtml(
#            html = "The upload could not be stored.  Please notify the webmaster.",
            html = "The upload could not be stored, contact the ISIS Webmaster", 
            href = "mailto:webmaster@usaf-mfoqa.com?,?Subject=Data File Upload Error" + 
                   "&body=A flight data file upload attempt failed and the file could not be stored.",
            uploadWhat   = uploadWhat,
            formInfoHtml = formInfoHtml,
            fieldStorage = fieldStorage)
        try:
            flagFile.close()
        except Exception:
            pass
        try:
            os.remove(flagFilePath)
        except Exception:
            pass
        try:
            storeFile.close()
        except Exception:
            pass
        try:
            os.remove(storeFilePath)
        except Exception:
            pass
        return
        
    WriteDefaultFormHtml(uploadWhat   = uploadWhat,
                         formInfoHtml = formInfoHtml,
                         fieldStorage = None)
    print """
<center>
  <hr noshade size="1" width="90%%">
  <table border="0" bgcolor="#c0c0c0" cellpadding="0" cellspacing="0">
    <tr>
      <td>
        <table border="0" width="100%%" cellpadding="10" cellspacing="2">
          <tr align="center">
            <td bgcolor="#000099" width="100%%">
              <font color="#ffffff">
                <h2>{uploadWhatHtml} Upload Status</h2> 
              </font>
            </td>
          </tr>
          <tr align="center">
            <td bgcolor="#000099" width="100%%">
              <font color="#ffffff">
                File 
                <font color="#00ffff"><b>{filenameHtml}</b></font> of size 
                <font color="#00ffff"><b>{sizeHtml}</b></font> bytes is 
                uploaded successfully!
                <br>
                <br>
                You may upload additional files or close browser if done...
              </font>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</center>
""".format(uploadWhatHtml = cgi.escape(uploadWhat),
           filenameHtml   = cgi.escape(storeFilename),
           sizeHtml       = cgi.escape(str(fileSize)))
    WriteEpilogueHtml()

def HandleRequest(uploadWhat,
                  uploadPath,
                  formInfoHtml = ""):
    fieldStorage = cgi.FieldStorage() 
    if fieldStorage.has_key("upload_file"):
        HandleProcessFormRequest(uploadWhat   = uploadWhat,
                                 uploadPath   = uploadPath,
                                 formInfoHtml = formInfoHtml,
                                 fieldStorage = fieldStorage)
    else:
        HandleShowFormRequest(uploadWhat   = uploadWhat,
                              formInfoHtml = formInfoHtml)

#EOF
if __name__ == "__main__":
    import doctest
    doctest.testmod()
