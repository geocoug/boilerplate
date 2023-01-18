drop table if exists d_samples cascade;
create table d_samples (
    study character varying(20),
    sample_id character varying(80),
    sample_no character varying(80),
    sample_type character varying(2),
    matrix character varying(20),
    description text,
    sample_date timestamp without time zone,
    constraint pk_sample unique(study, sample_id, sample_no)
);
