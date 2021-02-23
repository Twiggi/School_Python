#!python
import xlrd
import xlwt
import sys

class pomocnik:
    def __init__(self, meno):
        self.meno = meno
        self.kategoria = []
        self.behy_sobota = 0
        self.behy_nedela = 0


if __name__ == "__main__":
    pomocnici_sobota = {}
    pomocnici_nedela = {}
    pomocnici_sobota_small = []
    pomocnici_sobota_medium = []
    pomocnici_sobota_large = []
    pomocnici_nedela_small = []
    pomocnici_nedela_medium = []
    pomocnici_nedela_large = []
    pomocnici_sobota_all = []
    pomocnici_nedela_all = []

    pomocnici_sobota_all.append(pomocnici_sobota_small)
    pomocnici_sobota_all.append(pomocnici_sobota_medium)
    pomocnici_sobota_all.append(pomocnici_sobota_large)
    pomocnici_nedela_all.append(pomocnici_nedela_small)
    pomocnici_nedela_all.append(pomocnici_nedela_medium)
    pomocnici_nedela_all.append(pomocnici_nedela_large)

    # ZADAVANIE PARAMETROV PRE VYPOCET
    loc = str(input("Zadaj nazov suboru: "))
    if loc[-4:] != ".xls":
        loc = loc + ".xls"
    no_of_sheet = int(input("Kolko dni maju preteky: "))
    if no_of_sheet == 1:
        pocet_behov = int(input("Kolko je parkurov: "))
        min_pocet_pomocnikov = int(input("Kolko je minimalny pocet pomocnikov na parkure: "))
    elif no_of_sheet == 2:
        pocet_behov = int(input("Kolko je parkurov v sobotu: "))
        pocet_behov_nedela = int(input("Kolko je parkurov v nedelu: "))
        min_pocet_pomocnikov = int(input("Kolko je minimalny pocet pomocnikov na parkure v sobotu: "))
        min_pocet_pomocnikov_nedela = int(input("Kolko je minimalny pocet pomocnikov na parkure v nedelu: "))
    #maximalny_vyskyt = int(input("Kolko krat moze maximalne byt 1 clovek na parkure: "))


    for no_of_sheet in range(0,no_of_sheet):
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_index(no_of_sheet)
        #sheet.cell_value(0, 0)

        pocet_pomocnikov = sheet.nrows

        # ZISTI POCET MOZNYCH POMOCNIKOV NA KAZDY DEN
        for i in range(1, pocet_pomocnikov):
            if no_of_sheet == 0:
                p = pomocnik(sheet.cell_value(i, 1))
                tmp = str(sheet.cell_value(i,2))
                tmp1 = tmp.split(",")
                for t in tmp1:
                    p.kategoria.append(t)
                pomocnici_sobota[sheet.cell_value(i,0)] = p
            else:
                p = pomocnik(sheet.cell_value(i, 1))
                tmp = str(sheet.cell_value(i, 2))
                tmp1 = tmp.split(",")
                for t in tmp1:
                    p.kategoria.append(t)
                pomocnici_nedela[sheet.cell_value(i, 0)] = p

        #ROZDELI POMOCNIKOV PODLA DNI A KATEGORII
        for pom in pomocnici_sobota:
            if "SA" in pomocnici_sobota[pom].kategoria and "MA" not in pomocnici_sobota[pom].kategoria and "LA" not in pomocnici_sobota[pom].kategoria:
                pomocnici_sobota_large.append(pomocnici_sobota[pom])
                pomocnici_sobota_medium.append(pomocnici_sobota[pom])
            elif "SA" not in pomocnici_sobota[pom].kategoria and "MA" in pomocnici_sobota[pom].kategoria and "LA" not in pomocnici_sobota[pom].kategoria:
                pomocnici_sobota_large.append(pomocnici_sobota[pom])
                pomocnici_sobota_small.append(pomocnici_sobota[pom])
            elif "SA" not in pomocnici_sobota[pom].kategoria and "MA" not in pomocnici_sobota[pom].kategoria and "LA" in pomocnici_sobota[pom].kategoria:
                pomocnici_sobota_small.append(pomocnici_sobota[pom])
                pomocnici_sobota_medium.append(pomocnici_sobota[pom])
            elif "SA" in pomocnici_sobota[pom].kategoria and "MA" in pomocnici_sobota[pom].kategoria and "LA" not in pomocnici_sobota[pom].kategoria:
                pomocnici_sobota_large.append(pomocnici_sobota[pom])
            elif "SA" in pomocnici_sobota[pom].kategoria and "MA" not in pomocnici_sobota[pom].kategoria and "LA" in pomocnici_sobota[pom].kategoria:
                pomocnici_sobota_medium.append(pomocnici_sobota[pom])
            elif "SA" not in pomocnici_sobota[pom].kategoria and "MA" in pomocnici_sobota[pom].kategoria and "LA" in pomocnici_sobota[pom].kategoria :
                pomocnici_sobota_small.append(pomocnici_sobota[pom])
            elif "SA" in pomocnici_sobota[pom].kategoria and "MA" in pomocnici_sobota[pom].kategoria and "LA" in pomocnici_sobota[pom].kategoria:
                continue
            else:
                #min(pomocnici_sobota_all, key=len).append(pomocnici_sobota[pom])
                pomocnici_sobota_small.append(pomocnici_sobota[pom])
                pomocnici_sobota_medium.append(pomocnici_sobota[pom])
                pomocnici_sobota_large.append(pomocnici_sobota[pom])

        if pomocnici_nedela:
            for pom in pomocnici_nedela:
                if "SA" in pomocnici_nedela[pom].kategoria and "MA" not in pomocnici_nedela[pom].kategoria and "LA" not in pomocnici_nedela[pom].kategoria:
                    pomocnici_nedela_large.append(pomocnici_nedela[pom])
                    pomocnici_nedela_medium.append(pomocnici_nedela[pom])
                elif "SA" not in pomocnici_nedela[pom].kategoria and "MA" in pomocnici_nedela[pom].kategoria and "LA" not in pomocnici_nedela[pom].kategoria:
                    pomocnici_nedela_large.append(pomocnici_nedela[pom])
                    pomocnici_nedela_small.append(pomocnici_nedela[pom])
                elif "SA" not in pomocnici_nedela[pom].kategoria and "MA" not in pomocnici_nedela[pom].kategoria and "LA" in pomocnici_nedela[pom].kategoria:
                    pomocnici_nedela_small.append(pomocnici_nedela[pom])
                    pomocnici_nedela_medium.append(pomocnici_nedela[pom])
                elif "SA" in pomocnici_nedela[pom].kategoria and "MA" in pomocnici_nedela[pom].kategoria and "LA" not in pomocnici_nedela[pom].kategoria:
                    pomocnici_nedela_large.append(pomocnici_nedela[pom])
                elif "SA" in pomocnici_nedela[pom].kategoria and "MA" not in pomocnici_nedela[pom].kategoria and "LA" in pomocnici_nedela[pom].kategoria:
                    pomocnici_nedela_medium.append(pomocnici_nedela[pom])
                elif "SA" not in pomocnici_nedela[pom].kategoria and "MA" in pomocnici_nedela[pom].kategoria and "LA" in pomocnici_nedela[pom].kategoria:
                    pomocnici_nedela_small.append(pomocnici_nedela[pom])
                elif "SA" in pomocnici_nedela[pom].kategoria and "MA" in pomocnici_nedela[pom].kategoria and "LA" in pomocnici_nedela[pom].kategoria:
                    continue
                else:
                    # min(pomocnici_sobota_all, key=len).append(pomocnici_sobota[pom])
                    pomocnici_nedela_small.append(pomocnici_nedela[pom])
                    pomocnici_nedela_medium.append(pomocnici_nedela[pom])
                    pomocnici_nedela_large.append(pomocnici_nedela[pom])

        if no_of_sheet == 0:
            # print("SOBOTA")
            # print("SMALL")
            # for i in range(0, (min_pocet_pomocnikov * pocet_behov)):
            #     if i%min_pocet_pomocnikov == 0 and i != 0:
            #         print()
            #     print(pomocnici_sobota_small[i%len(pomocnici_sobota_small)].meno, end=", ")
            # print()
            # print()
            # print("MEDIUM")
            # for i in range(0, (min_pocet_pomocnikov * pocet_behov)):
            #     if i%min_pocet_pomocnikov == 0 and i != 0:
            #         print()
            #     print(pomocnici_sobota_medium[i%len(pomocnici_sobota_medium)].meno, end=", ")
            # print()
            # print()
            # print("LARGE")
            # for i in range(0, (min_pocet_pomocnikov * pocet_behov)):
            #     if i%min_pocet_pomocnikov == 0 and i != 0:
            #         print()
            #     print(pomocnici_sobota_large[i%len(pomocnici_sobota_large)].meno, end=", ")
            # print()
            wt = xlwt.Workbook()
            new_sheet = wt.add_sheet("PRIDELENIE_SO")
            new_sheet.write(0,0,"LOTW BLA BLA - 2042/69", xlwt.easyxf('font: name Times New Roman, bold 1, colour light_blue, height 400;''pattern: pattern solid_fill, fore_color yellow;'))
            new_sheet.write(3,0,"SOBOTA",xlwt.easyxf('font: bold 1, height 300'))
            for pretek in range(0,pocet_behov):
                new_sheet.write(5,2*pretek,"pretek"+str(pretek+1))
            #for p in range(pocet_behov):
            col = 0
            row = 7
            pretek = 0
            new_sheet.write(row,pretek,"SMALL", xlwt.easyxf('font: bold 1'))
            row += 1
            for i in range(0, (min_pocet_pomocnikov * pocet_behov)):
                if i%min_pocet_pomocnikov == 0 and i != 0:
                    col = col + 2
                    row = 8
                new_sheet.write(row,col,pomocnici_sobota_small[i%len(pomocnici_sobota_small)].meno, xlwt.easyxf('font: name Times New Roman, height 240;''border: left thin, right thin, top thin, bottom thin'))
                pomocnici_sobota_small[i % len(pomocnici_sobota_small)].behy_sobota += 1
                row += 1

            #for p in range(pocet_behov):
            col = 0
            row = 7 + min_pocet_pomocnikov + 2
            new_sheet.write(row,pretek,"MEDIUM", xlwt.easyxf('font: bold 1'))
            row += 1
            for i in range(0, (min_pocet_pomocnikov * pocet_behov)):
                if i%min_pocet_pomocnikov == 0 and i != 0:
                    col = col + 2
                    row = 8 + min_pocet_pomocnikov + 2
                new_sheet.write(row,col,pomocnici_sobota_medium[i%len(pomocnici_sobota_medium)].meno, xlwt.easyxf('font: name Times New Roman, height 240;''border: left thin, right thin, top thin, bottom thin'))
                pomocnici_sobota_medium[i % len(pomocnici_sobota_medium)].behy_sobota += 1
                row += 1

            #for p in range(pocet_behov):
            col = 0
            row = 7 + 2 * (min_pocet_pomocnikov + 2)
            new_sheet.write(row,pretek,"LARGE", xlwt.easyxf('font: bold 1'))
            row += 1
            for i in range(0, (min_pocet_pomocnikov * pocet_behov)):
                if i%min_pocet_pomocnikov == 0 and i != 0:
                    col = col + 2
                    row = 8 + 2 * (min_pocet_pomocnikov + 2)
                new_sheet.write(row,col,pomocnici_sobota_large[i%len(pomocnici_sobota_large)].meno, xlwt.easyxf('font: name Times New Roman, height 240;''border: left thin, right thin, top thin, bottom thin'))
                pomocnici_sobota_large[i % len(pomocnici_sobota_large)].behy_sobota += 1
                row += 1
            #wt.save("bruh.xls")


        else:
            # print()
            # print("NEDELA")
            # print("SMALL")
            # for i in range(0, (min_pocet_pomocnikov_nedela * pocet_behov_nedela)):
            #     if i % min_pocet_pomocnikov_nedela == 0 and i != 0:
            #         print()
            #     i = i % len(pomocnici_nedela_small)
            #     print(pomocnici_nedela_small[i].meno, end=", ")
            # print()
            # print()
            # print("MEDIUM")
            # for i in range(0, (min_pocet_pomocnikov_nedela * pocet_behov_nedela)):
            #     if i % min_pocet_pomocnikov_nedela == 0 and i != 0:
            #         print()
            #     i = i % len(pomocnici_nedela_medium)
            #     print(pomocnici_nedela_medium[i].meno, end=", ")
            # print()
            # print()
            # print("LARGE")
            # for i in range(0, (min_pocet_pomocnikov_nedela * pocet_behov_nedela)):
            #     if i % min_pocet_pomocnikov_nedela == 0 and i != 0:
            #         print()
            #     i = i % len(pomocnici_nedela_large)
            #     print(pomocnici_nedela_large[i].meno, end=", ")
            # print()
            new_sheet = wt.add_sheet("PRIDELENIE_NE")
            new_sheet.write(0, 0, "LOTW BLA BLA - 2042/69", xlwt.easyxf(
                'font: name Times New Roman, bold 1, colour light_blue, height 400;''pattern: pattern solid_fill, fore_color yellow;'))
            new_sheet.write(3, 0, "NEDELA", xlwt.easyxf('font: bold 1, height 300'))
            for pretek in range(0, pocet_behov_nedela):
                new_sheet.write(5, 2 * pretek, "pretek" + str(pretek + 1))
            # for p in range(pocet_behov):
            col = 0
            row = 7
            pretek = 0
            new_sheet.write(row, pretek, "SMALL", xlwt.easyxf('font: bold 1'))
            row += 1
            for i in range(0, (min_pocet_pomocnikov_nedela * pocet_behov_nedela)):
                if i % min_pocet_pomocnikov_nedela == 0 and i != 0:
                    col = col + 2
                    row = 8
                new_sheet.write(row, col, pomocnici_nedela_small[i % len(pomocnici_nedela_small)].meno, xlwt.easyxf('font: name Times New Roman, height 240;''border: left thin, right thin, top thin, bottom thin'))
                pomocnici_nedela_small[i % len(pomocnici_nedela_small)].behy_nedela += 1
                row += 1

            # for p in range(pocet_behov):
            col = 0
            row = 7 + min_pocet_pomocnikov_nedela + 2
            new_sheet.write(row, pretek, "MEDIUM", xlwt.easyxf('font: bold 1'))
            row += 1
            for i in range(0, (min_pocet_pomocnikov_nedela * pocet_behov_nedela)):
                if i % min_pocet_pomocnikov_nedela == 0 and i != 0:
                    col = col + 2
                    row = 8 + min_pocet_pomocnikov_nedela + 2
                new_sheet.write(row, col, pomocnici_nedela_medium[i % len(pomocnici_nedela_medium)].meno, xlwt.easyxf('font: name Times New Roman, height 240;''border: left thin, right thin, top thin, bottom thin'))
                pomocnici_nedela_medium[i % len(pomocnici_nedela_medium)].behy_nedela += 1
                row += 1

            # for p in range(pocet_behov):
            col = 0
            row = 7 + 2 * (min_pocet_pomocnikov_nedela + 2)
            new_sheet.write(row, pretek, "LARGE", xlwt.easyxf('font: bold 1'))
            row += 1
            for i in range(0, (min_pocet_pomocnikov_nedela * pocet_behov_nedela)):
                if i % min_pocet_pomocnikov_nedela == 0 and i != 0:
                    col = col + 2
                    row = 8 + 2 * (min_pocet_pomocnikov_nedela + 2)
                new_sheet.write(row, col, pomocnici_nedela_large[i % len(pomocnici_nedela_large)].meno, xlwt.easyxf('font: name Times New Roman, height 240;''border: left thin, right thin, top thin, bottom thin'))
                pomocnici_nedela_large[i % len(pomocnici_nedela_large)].behy_nedela += 1
                row += 1




    new_sheet = wt.add_sheet("Pomocnici")
    new_sheet.write(0,0,"MENO", xlwt.easyxf('font: bold 1'))
    new_sheet.write(0, 1, "POCET BEHOV V SOBOTU", xlwt.easyxf('font: bold 1'))
    new_sheet.write(0, 4, "MENO", xlwt.easyxf('font: bold 1'))
    new_sheet.write(0, 5, "POCET BEHOV V NEDELU", xlwt.easyxf('font: bold 1'))
    # for i in range(1,pocet_pomocnikov):
    #     new_sheet.write(i,0,str(pomocnici_sobota[i].meno), xlwt.easyxf('font: name Times New Roman, height 240;''border: left thin, right thin, top thin, bottom thin'))
    #     new_sheet.write(i,1,str(pomocnici_sobota[i].behy_sobota), xlwt.easyxf('font: name Times New Roman, height 240;''border: left thin, right thin, top thin, bottom thin'))
    #     if pomocnici_nedela:
    #         new_sheet.write(i,4, str(pomocnici_sobota[i].meno), xlwt.easyxf('font: name Times New Roman, height 240;''border: left thin, right thin, top thin, bottom thin'))
    #         new_sheet.write(i,5,str(pomocnici_nedela[i].behy_nedela), xlwt.easyxf('font: name Times New Roman, height 240;''border: left thin, right thin, top thin, bottom thin'))
    for p in pomocnici_sobota:
        new_sheet.write(int(p),0,str(pomocnici_sobota[p].meno), xlwt.easyxf('font: name Times New Roman, height 240;''border: left thin, right thin, top thin, bottom thin'))
        new_sheet.write(int(p),1,str(pomocnici_sobota[p].behy_sobota), xlwt.easyxf('font: name Times New Roman, height 240;''border: left thin, right thin, top thin, bottom thin'))
    for p in pomocnici_nedela:
        new_sheet.write(int(p),4, str(pomocnici_nedela[p].meno), xlwt.easyxf('font: name Times New Roman, height 240;''border: left thin, right thin, top thin, bottom thin'))
        new_sheet.write(int(p),5,str(pomocnici_nedela[p].behy_nedela), xlwt.easyxf('font: name Times New Roman, height 240;''border: left thin, right thin, top thin, bottom thin'))


    wt.save("Rozdelenie_preteky.xls")
    print("Rozpis pomocnikov je hotovy v subore Rozdelenie_preteky.xls")

