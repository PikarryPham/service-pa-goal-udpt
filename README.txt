Hướng dẫn chạy và cài đặt app Python flask:
B1: Gõ câu lệnh: pip install flask
If cannot install, please use the word "--user" after the command. vD:
pip install flask --user
See more details here: https://www.codegrepper.com/code-examples/shell/ERROR%3A+Could+not+install+packages+due+to+an+OSError%3A+%5BWinError+2%5D+The+system+cannot+find+the+file+specified%3A+%27C%3A%5C%5CPython310%5C%5CScripts%5C%5Cpipenv.exe%27+-%3E+%27C%3A%5C%5CPython310%5C%5CScripts%5C%5Cpipenv.exe.deleteme%27
B2: Install packages and install python flask (python báo lỗi thiếu package nào thì tải đúng package đó)
B3: Sử dụng command "python -m flask run" để chạy ứng dụng

Note: 
If you meet the problem 
"Python MySQL OperationalError: 1045, "Access denied for user root@'localhost'", use the command

    GRANT all privileges on <name of database>.* to '<name of your computer user>'@'localhost' WITH GRANT OPTION;
    SHOW GRANTS FOR '<name of your computer user>'@'localhost';

Một số link hướng dẫn khắc phục lỗi: nếu có:
https://stackoverflow.com/questions/54915276/mysqldb-exceptions-operationalerror-1046-no-database-selected-flask-to-m
https://stackoverflow.com/questions/33241924/importerror-no-module-named-flask-ext-mysql
https://stackoverflow.com/questions/58675081/why-does-running-flask-run-on-windows-result-in-flask-is-not-recognized-as-an
https://www.codegrepper.com/code-examples/python/ERROR%3A+Could+not+install+packages+due+to+an+EnvironmentError%3A+%5BWinError+2%5D+The+system+cannot+find+the+file+specified%3A+%27c%3A%5C%5Cpython38%5C%5CScripts%5C%5Csqlformat.exe%27+-%3E+%27c%3A%5C%5Cpython38%5C%5CScripts%5C%5Csqlformat.exe.deleteme%27
