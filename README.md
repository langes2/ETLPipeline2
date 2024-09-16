Extract = {getR191.cs, getToken.cs, getR191Monthly.cs} Transform = {tpcleanone.py, tpcleantwo.py, findsimrows.py} Load = {sqlconnect.py}

Execute Transform and Load = {run_TPcleaningpipeline.bat} Execute Extract, then Transform and Load = {run_TPweeklypipeline.bat, run_TPmonthlypipeline.bat}
