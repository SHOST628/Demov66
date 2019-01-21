-- Create table
create table XF_PAGELOCATION
(
  xf_functionid   VARCHAR2(100),
  xf_functionname VARCHAR2(1000),
  xf_locationid     VARCHAR2(100) primary key not null,
  xf_locationname   VARCHAR2(1000),
  xf_locationdesc   VARCHAR2(4000),
  xf_location VARCHAR2(4000) not null
)
tablespace DATA01
  pctfree 10
  initrans 1
  maxtrans 255
  storage
  (
    initial 64K
    next 1M
    minextents 1
    maxextents unlimited
  );


--用例表
-- Create table
create table XF_TESTCASE
(
  xf_caseid   VARCHAR2(100) not null,
  xf_casedesc VARCHAR2(4000),
  xf_tsid     VARCHAR2(100) not null,
  xf_tsdesc   VARCHAR2(4000),
  xf_action   VARCHAR2(100) not null,
  xf_locationid VARCHAR2(100),
  xf_opvalues VARCHAR2(1000),
  xf_ifmix    integer
)
tablespace DATA01
  pctfree 10
  initrans 1
  maxtrans 255
  storage
  (
    initial 64K
    next 1M
    minextents 1
    maxextents unlimited
  );

--用例组合表
-- Create table
create table XF_MIXCASE
(
  xf_mixid    VARCHAR2(100) not null,
  xf_mixcasedesc VARCHAR2(4000),
  xf_caseid   VARCHAR2(100) not null
)
tablespace DATA01
  pctfree 10
  initrans 1
  maxtrans 255
  storage
  (
    initial 64K
    next 1M
    minextents 1
    maxextents unlimited
  );

--指定要执行的用例
-- Create table
create table XF_CASEDEBUG
(
  xf_caseid       VARCHAR2(100),
  xf_mixid VARCHAR2(100),
  xf_executeuser     VARCHAR2(50)
)
tablespace DATA01
  pctfree 10
  initrans 1
  maxtrans 255
  storage
  (
    initial 64K
    next 1M
    minextents 1
    maxextents unlimited
  );