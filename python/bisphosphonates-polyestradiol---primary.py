# Tim Doran, Evangelos Kontopantelis, Jose M Valderas, Stephen Campbell, Martin Roland, Chris Salisbury, David Reeves, 2024.

import sys, csv, re

codes = [{"code":"5837001","system":"gprdproduct"},{"code":"10196001","system":"gprdproduct"},{"code":"10787001","system":"gprdproduct"},{"code":"10417001","system":"gprdproduct"},{"code":"8692002","system":"gprdproduct"},{"code":"2374002","system":"gprdproduct"},{"code":"5838001","system":"gprdproduct"},{"code":"8587003","system":"gprdproduct"},{"code":"8124001","system":"gprdproduct"},{"code":"8649003","system":"gprdproduct"},{"code":"11668002","system":"gprdproduct"},{"code":"9165002","system":"gprdproduct"},{"code":"10641001","system":"gprdproduct"},{"code":"7037001","system":"gprdproduct"},{"code":"8611002","system":"gprdproduct"},{"code":"10599001","system":"gprdproduct"},{"code":"1088001","system":"gprdproduct"},{"code":"3252002","system":"gprdproduct"},{"code":"1531009","system":"gprdproduct"},{"code":"7748001","system":"gprdproduct"},{"code":"4342002","system":"gprdproduct"},{"code":"8649001","system":"gprdproduct"},{"code":"8125001","system":"gprdproduct"},{"code":"10640001","system":"gprdproduct"},{"code":"6303002","system":"gprdproduct"},{"code":"1531011","system":"gprdproduct"},{"code":"8530001","system":"gprdproduct"},{"code":"2374003","system":"gprdproduct"},{"code":"2240002","system":"gprdproduct"},{"code":"5838002","system":"gprdproduct"},{"code":"1531010","system":"gprdproduct"},{"code":"3253001","system":"gprdproduct"},{"code":"8649002","system":"gprdproduct"},{"code":"8453001","system":"gprdproduct"},{"code":"10639001","system":"gprdproduct"},{"code":"8692001","system":"gprdproduct"},{"code":"8520001","system":"gprdproduct"},{"code":"7828001","system":"gprdproduct"},{"code":"8611003","system":"gprdproduct"},{"code":"3252001","system":"gprdproduct"},{"code":"9382001","system":"gprdproduct"},{"code":"8123001","system":"gprdproduct"},{"code":"1088002","system":"gprdproduct"},{"code":"8587001","system":"gprdproduct"},{"code":"4342001","system":"gprdproduct"},{"code":"6303001","system":"gprdproduct"},{"code":"9164003","system":"gprdproduct"},{"code":"9916001","system":"gprdproduct"},{"code":"1088003","system":"gprdproduct"},{"code":"8587002","system":"gprdproduct"},{"code":"8913001","system":"gprdproduct"},{"code":"11087001","system":"gprdproduct"},{"code":"8611001","system":"gprdproduct"},{"code":"2374001","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('bisphosphonates-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["bisphosphonates-polyestradiol---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["bisphosphonates-polyestradiol---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["bisphosphonates-polyestradiol---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
