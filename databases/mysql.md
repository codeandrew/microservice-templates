# MYSQL
```
mysql -u root -p
```

**RESET ROOT PASSWORD**
```bash
sudo systemctl stop mysql
sudo mysqld_safe --skip-grant-tables &
mysql -u root
```
once in
```sql
FLUSH PRIVILEGES;
ALTER USER 'root'@'localhost' IDENTIFIED BY 'new_password';
FLUSH PRIVILEGES;
```

```bash
sudo systemctl start mysql
```



## CONNECTION SETTINGS
sudo vi /etc/mysql/mysql.conf.d/mysqld.cnf

Change the bind-address
Look for the line that says bind-address and change its value from 127.0.0.1 to 0.0.0.0 to listen on all interfaces, or to your specific server IP if you want to be more restrictive.

css
Copy code
bind-address = 0.0.0.0
Restart MySQL

After saving the changes, restart MySQL to apply them:

bash
Copy code
sudo systemctl restart mysql

**FIREWALL SETTINGS**
```
sudo ufw allow 3306
sudo ufw enable
sudo ufw status
```

**MYSQL USER PERMISSIONS**

```
GRANT ALL PRIVILEGES ON *.* TO 'username'@'remote_host' IDENTIFIED BY 'password';
FLUSH PRIVILEGES;
```
> Note: It's recommended to specify the exact database and permissions rather than using *.* and ALL PRIVILEGES for security reasons.

