import pymysql
pymysql.version_info = (1, 4, 13, "final", 0)  # 加了这行就管用了, 离谱
pymysql.install_as_MySQLdb()
# C:\Users\Administrator\Envs\djangohomework\Scripts\python.exe|C:\inetpub\wwwroot\djangohomework\wfastcgi.py