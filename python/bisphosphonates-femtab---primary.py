# Tim Doran, Evangelos Kontopantelis, Jose M Valderas, Stephen Campbell, Martin Roland, Chris Salisbury, David Reeves, 2024.

import sys, csv, re

codes = [{"code":"6172009","system":"gprdproduct"},{"code":"1810001","system":"gprdproduct"},{"code":"9476001","system":"gprdproduct"},{"code":"13941001","system":"gprdproduct"},{"code":"2523001","system":"gprdproduct"},{"code":"8809003","system":"gprdproduct"},{"code":"10530001","system":"gprdproduct"},{"code":"1107001","system":"gprdproduct"},{"code":"8576001","system":"gprdproduct"},{"code":"13074001","system":"gprdproduct"},{"code":"5780001","system":"gprdproduct"},{"code":"13949001","system":"gprdproduct"},{"code":"11457001","system":"gprdproduct"},{"code":"8134001","system":"gprdproduct"},{"code":"780001","system":"gprdproduct"},{"code":"8621001","system":"gprdproduct"},{"code":"6389009","system":"gprdproduct"},{"code":"2436001","system":"gprdproduct"},{"code":"1823001","system":"gprdproduct"},{"code":"1804001","system":"gprdproduct"},{"code":"4662001","system":"gprdproduct"},{"code":"5226001","system":"gprdproduct"},{"code":"6421001","system":"gprdproduct"},{"code":"779002","system":"gprdproduct"},{"code":"2879001","system":"gprdproduct"},{"code":"8140001","system":"gprdproduct"},{"code":"2525001","system":"gprdproduct"},{"code":"13401001","system":"gprdproduct"},{"code":"1102001","system":"gprdproduct"},{"code":"1914002","system":"gprdproduct"},{"code":"1271001","system":"gprdproduct"},{"code":"13168001","system":"gprdproduct"},{"code":"12648001","system":"gprdproduct"},{"code":"8648001","system":"gprdproduct"},{"code":"1802001","system":"gprdproduct"},{"code":"397011","system":"gprdproduct"},{"code":"3254001","system":"gprdproduct"},{"code":"1636009","system":"gprdproduct"},{"code":"2297001","system":"gprdproduct"},{"code":"14135001","system":"gprdproduct"},{"code":"5288001","system":"gprdproduct"},{"code":"1806001","system":"gprdproduct"},{"code":"5254001","system":"gprdproduct"},{"code":"10600001","system":"gprdproduct"},{"code":"2329001","system":"gprdproduct"},{"code":"1821001","system":"gprdproduct"},{"code":"6680001","system":"gprdproduct"},{"code":"7514001","system":"gprdproduct"},{"code":"1816001","system":"gprdproduct"},{"code":"5723009","system":"gprdproduct"},{"code":"6684001","system":"gprdproduct"},{"code":"1812001","system":"gprdproduct"},{"code":"6218001","system":"gprdproduct"},{"code":"4661001","system":"gprdproduct"},{"code":"2543001","system":"gprdproduct"},{"code":"13533001","system":"gprdproduct"},{"code":"779003","system":"gprdproduct"},{"code":"6101001","system":"gprdproduct"},{"code":"5754009","system":"gprdproduct"},{"code":"5841001","system":"gprdproduct"},{"code":"7428001","system":"gprdproduct"},{"code":"4269009","system":"gprdproduct"},{"code":"963001","system":"gprdproduct"},{"code":"2533001","system":"gprdproduct"},{"code":"7317001","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('bisphosphonates-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["bisphosphonates-femtab---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["bisphosphonates-femtab---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["bisphosphonates-femtab---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
