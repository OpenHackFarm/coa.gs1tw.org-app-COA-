#!/usr/bin/env python
# encoding: utf-8

from bs4 import BeautifulSoup
import glob
import csv

with open('gs1.csv', 'w') as fp:
    csvfile = csv.writer(fp)

    # write header
    csvfile.writerow(("標準分類編碼", "行情代號(水產品代號)", "品種", "中文名稱", "英文名稱", "學名名稱", "俗名名稱"))

    files = glob.glob("*.htm")

    for file in files:
        with open(file, "r") as myfile:
            html_doc = myfile.read().replace('\n', '')

            soup = BeautifulSoup(html_doc, 'html.parser')

            table = soup.find('table', attrs={'width': "100%", 'border': "0", 'cellpadding': "4", 'cellspacing': "1"})
            rows = table.findAll('tr')

            del rows[0]
            for row in rows:
                cols = row.find_all('td')
                cols = [ele.text.strip().encode('utf-8') for ele in cols]

                csvfile.writerow(cols)

                print cols[0]
                print '\t' + cols[1]
                print '\t' + cols[2]
                print '\t' + cols[3]
                print '\t' + cols[4]
                print '\t' + cols[5]
                print '\t' + cols[6]
