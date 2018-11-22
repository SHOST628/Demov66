-- Create table
--用例表
-- Create table
create table XF_TESTCASE
(
  xf_caseid   VARCHAR2(50) not null,
  xf_casedesc VARCHAR2(4000),
  xf_tsid     VARCHAR2(50) not null,
  xf_tsdesc   VARCHAR2(4000),
  xf_action   VARCHAR2(50) not null,
  xf_opvalues VARCHAR2(500),
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

-- Create table
--用例组合表
-- Create table
create table XF_MIXCASE
(
  xf_mixid    VARCHAR2(50) not null,
  xf_mixcasedesc VARCHAR2(4000),
  xf_caseid   VARCHAR2(50) not null,
  xf_runmode  VARCHAR2(5) not null
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


--控制testcase是否执行
-- Create table
create table XF_CASECONTROL
(
  xf_caseid       VARCHAR2(50),
  xf_mixid        VARCHAR2(50),
  xf_casedesc VARCHAR2(4000),
  xf_runmode     VARCHAR2(5)
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
  xf_caseid       VARCHAR2(50),
  xf_mixid VARCHAR2(50),
  xf_executeuser     VARCHAR2(20)
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

--公共操作模块,供用例调用
--Create table
create table XF_COMONMODULE
(
  xf_moduleid       VARCHAR2(50) not null,
  xf_mdesc VARCHAR2(4000),
  xf_tsid     VARCHAR2(50) not null,
  xf_tsdesc   VARCHAR2(4000),
  xf_action VARCHAR2(50),
  xf_opvalues VARCHAR2(500)
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