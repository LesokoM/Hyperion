if exist new_folder (mkdir if_folder) REM creating if_folder if new_folder exists
REM creating hyperionDev folder if if_folder exists else creating new-projects folder
if exist if_folder (mkdir hyperionDev) else (mkdir new-projects) 

