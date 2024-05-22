# Tim Doran, Evangelos Kontopantelis, Jose M Valderas, Stephen Campbell, Martin Roland, Chris Salisbury, David Reeves, 2024.

import sys, csv, re

codes = [{"code":"8808002","system":"gprdproduct"},{"code":"1636010","system":"gprdproduct"},{"code":"9381003","system":"gprdproduct"},{"code":"3253007","system":"gprdproduct"},{"code":"9229001","system":"gprdproduct"},{"code":"6469009","system":"gprdproduct"},{"code":"9228001","system":"gprdproduct"},{"code":"2879002","system":"gprdproduct"},{"code":"8809002","system":"gprdproduct"},{"code":"428001","system":"gprdproduct"},{"code":"8235001","system":"gprdproduct"},{"code":"9381001","system":"gprdproduct"},{"code":"5028001","system":"gprdproduct"},{"code":"2052007","system":"gprdproduct"},{"code":"11792001","system":"gprdproduct"},{"code":"8236001","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('bisphosphonates-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["bisphosphonates-015mg---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["bisphosphonates-015mg---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["bisphosphonates-015mg---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
