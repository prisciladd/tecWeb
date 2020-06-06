-- esquema.sql
-- Toda definição de banco deverá ser feita nesse arquivo

drop table if exists posts;
create table posts (
  id integer primary key autoincrement,
  titulo string not null,
  autor string not null,
  texto string not null
);

drop table if exists presenca;
create table presenca (
  email string not null,
  presenca string not null,
  resposta string not null,
  comentarios string not null
);