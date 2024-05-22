# Tim Doran, Evangelos Kontopantelis, Jose M Valderas, Stephen Campbell, Martin Roland, Chris Salisbury, David Reeves, 2024.

import sys, csv, re

codes = [{"code":"7414001","system":"gprdproduct"},{"code":"9242001","system":"gprdproduct"},{"code":"9437001","system":"gprdproduct"},{"code":"5482001","system":"gprdproduct"},{"code":"5480001","system":"gprdproduct"},{"code":"9180001","system":"gprdproduct"},{"code":"6926001","system":"gprdproduct"},{"code":"7846001","system":"gprdproduct"},{"code":"9433001","system":"gprdproduct"},{"code":"9164002","system":"gprdproduct"},{"code":"9443001","system":"gprdproduct"},{"code":"1914001","system":"gprdproduct"},{"code":"9296002","system":"gprdproduct"},{"code":"11164001","system":"gprdproduct"},{"code":"11112002","system":"gprdproduct"},{"code":"9296001","system":"gprdproduct"},{"code":"2240003","system":"gprdproduct"},{"code":"2240001","system":"gprdproduct"},{"code":"8319001","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('bisphosphonates-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["bisphosphonates-750mcg---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["bisphosphonates-750mcg---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["bisphosphonates-750mcg---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
