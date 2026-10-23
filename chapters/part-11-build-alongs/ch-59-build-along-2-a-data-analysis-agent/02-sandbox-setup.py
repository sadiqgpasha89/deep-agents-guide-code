# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part XI: Build-Alongs
# Chapter 59: Build-Along 2: A Data Analysis Agent
# Section: Sandbox setup
# Snippet 2 of this chapter.

import csv, io
data = [["Date","Product","Units Sold","Revenue"],
        ["2025-08-01","Widget A",10,250], ["2025-08-02","Widget B",5,125],
        ["2025-08-03","Widget A",7,175],  ["2025-08-04","Widget C",3,90],
        ["2025-08-05","Widget B",8,200]]
buf = io.StringIO(); csv.writer(buf).writerows(data)
backend.upload_files([("/root/data/sales_data.csv", buf.getvalue().encode("utf-8"))])
