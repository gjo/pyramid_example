========================================
PyramidでAPIサーバーを書くサンプル
========================================

develop
-------

setup::

  $ python3.10 -m venv env310
  $ . env310/bin/activate
  (env310)$ pip install -r setup_requirements.txt
  (env310)$ pip install -c constraints.txt -e '.[develop]'

create databases::

  $ mysql
  mysql> CREATE DATABASE dev_example_app CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;
  mysql> CREATE USER dev_example_app_adm@'%' IDENTIFIED BY 'dev_example_app_adm_pw';
  mysql> GRANT ALL ON dev_example_app.* TO dev_example_app_adm@'%';
  mysql> CREATE USER dev_example_app_ro@'%' IDENTIFIED BY 'dev_example_app_ro_pw';
  mysql> GRANT SELECT ON dev_example_app.* TO dev_example_app_ro@'%';
  mysql> CREATE USER dev_example_app_rw@'%' IDENTIFIED BY 'dev_example_app_rw_pw';
  mysql> GRANT SELECT,INSERT,UPDATE,DELETE ON dev_example_app.* TO dev_example_app_rw@'%';
  mysql> CREATE DATABASE test_example_app CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;
  mysql> CREATE USER test_example_app@'%' IDENTIFIED BY 'test_example_app_pw';
  mysql> GRANT ALL ON test_example_app.* TO test_example_app@'%';
  mysql> quit
  $ . .env/bin/activate
  (.env)$ alembic -c development.ini upgrade head

run tests::

  $ . .env/bin/activate
  (.env)$ tox

run server::

  $ . .env/bin/activate
  (.env)$ pserve --reload development.ini

update deps::

  $ rm -rf env310
  $ python3.10 -m venv env310
  $ . env310/bin/activate
  (env310)$ pip install -U pip setuptools wheel
  (env310)$ pip list --format freeze > setup_requirements.txt

  [EDIT pyproject.toml]

  (env310)$ pip install -e '.[develop]'
  (env310)$ pip list --format freeze --exclude-editable > constraints.txt

