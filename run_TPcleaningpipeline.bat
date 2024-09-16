@echo off
python "C:\Users\Public\Documents\TenantPrepaysPipeline\tpcleanone.py" > "C:\Users\Public\Documents\TenantPrepaysPipeline\TPcleaninglogs\cleanup1.log" 2>&1
python "C:\Users\Public\Documents\TenantPrepaysPipeline\tpcleantwo.py" > "C:\Users\Public\Documents\TenantPrepaysPipeline\TPcleaninglogs\cleanup2.log" 2>&1
python "C:\Users\Public\Documents\TenantPrepaysPipeline\findsimrows.py" > "C:\Users\Public\Documents\TenantPrepaysPipeline\TPcleaninglogs\cleanup3.log" 2>&1
python "C:\Users\Public\Documents\TenantPrepaysPipeline\sqlconnect.py" > "C:\Users\Public\Documents\TenantPrepaysPipeline\TPcleaninglogs\dbconnect.log" 2>&1