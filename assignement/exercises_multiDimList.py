# TCDD = [
#     "Sirkeci",
#     "Alsancak",
#     "Ankara"
# ]
# print(TCDD)

#JSON VERİ TİPİ ÇOK BOYUTLU DİZİLER

TCDD = { # json tipinin python şekli
    "sirkeci":["doğu ekspresi","Ankara mavi"],
    # "Ankara",
    "Ankara":{
        "doğu ekspresi":{
            "vagon1":["Sevilay","Engin","Seçilay"],
            "vagon2":["Yağız","Dağhan"]
        },
        "izmir mavi":{
            "vagon1":["Caner","Elif","Fatih"],
            "vagon2":{
                "5566":{
                    "adi":"Erdinç",
                    "TC":"335544"
                }
            }
        }
        },
    "İzmir":""
}
print(TCDD)
print("=============")
print("Ankaradaki trenler:",TCDD["Ankara"])
print("=============")
print("İzmirdeki trenler:",TCDD["İzmir"])
print("=============")
print("sirkecideki trenler:",TCDD["sirkeci"])
print("=============")
print("Ankaradaki trenler:",TCDD["Ankara"])
print("=============")
print("Ankara garı, izmir mavi:",TCDD["Ankara"]["izmir mavi"])
print("=============")
print("Ankara garı, izmir mavi, vagon2:",TCDD["Ankara"]["izmir mavi"]["vagon2"])
print("Ankara garı, izmir mavi, vagon2:",TCDD["Ankara"]["izmir mavi"]["vagon2"]["5566"]["adi"])
