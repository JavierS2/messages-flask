#!/bin/bash

mysql -u root -p -e 'CREATE DATABASE ejemplo'
mysql -u root -p ejemplo < ejemplo_DB.sql

exit 0
