-- Create table
--用例表
create table XF_TESTCASE
(
  xf_caseid     VARCHAR2(100) not null,
  xf_tsid     VARCHAR2(100) not null,
  xf_tsdesc   VARCHAR2(4000),
  xf_action   VARCHAR2(300) not null,
  xf_opvalues VARCHAR2(3000)
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




-- Create table
--用例组合表
create table XF_MIXCASE
(
  xf_mixid    VARCHAR2(100) not null,
  xf_casedesc  VARCHAR2(4000),
  xf_caseid    VARCHAR2(4000) not null,
  xf_runmode VARCHAR2(10)
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
