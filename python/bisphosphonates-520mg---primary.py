# Tim Doran, Evangelos Kontopantelis, Jose M Valderas, Stephen Campbell, Martin Roland, Chris Salisbury, David Reeves, 2024.

import sys, csv, re

codes = [{"code":"3642010","system":"gprdproduct"},{"code":"8780002","system":"gprdproduct"},{"code":"8610003","system":"gprdproduct"},{"code":"2281010","system":"gprdproduct"},{"code":"7070002","system":"gprdproduct"},{"code":"1353011","system":"gprdproduct"},{"code":"6596003","system":"gprdproduct"},{"code":"2628001","system":"gprdproduct"},{"code":"4759009","system":"gprdproduct"},{"code":"10642001","system":"gprdproduct"},{"code":"635009","system":"gprdproduct"},{"code":"636010","system":"gprdproduct"},{"code":"1300001","system":"gprdproduct"},{"code":"4783002","system":"gprdproduct"},{"code":"7186001","system":"gprdproduct"},{"code":"2906010","system":"gprdproduct"},{"code":"4407009","system":"gprdproduct"},{"code":"3166010","system":"gprdproduct"},{"code":"4782002","system":"gprdproduct"},{"code":"634010","system":"gprdproduct"},{"code":"1354011","system":"gprdproduct"},{"code":"8133001","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('bisphosphonates-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["bisphosphonates-520mg---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["bisphosphonates-520mg---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["bisphosphonates-520mg---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
