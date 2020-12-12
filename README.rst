================================
PyramidでAPIサーバーを書くサンプル
================================

develop
-------

setup::

  $ python3.8 -m venv .env
  $ . .env/bin/activate
  (.env)$ pip install -r setup_requirements.txt
  (.env)$ pip install -c constraints.txt -e '.[develop]'

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

  $ rm -rf .env
  $ python3.8 -m venv .env
  $ . .env/bin/activate
  (.env)$ pip install -U pip setuptools wheel
  (.env)$ pip list -l --format freeze > setup_requirements.txt
  (.env)$ pip install --use-feature=2020-resolver -e '.[develop]'
  (.env)$ pip freeze -l --exclude-editable > constraints.txt

