drop table if exists twitter_account;
create table twitter_account (
    id text primary key not null,
    credential text not null
);
insert into twitter_account (id, credential) values (
'lukasz+challenge@uchicago.edu', 'sekretnehaslo123'
);