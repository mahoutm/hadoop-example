A = load '<input files>' using PigStorage(',') as (tm:chararray,lat:double,lon:double,z:int,tem:double,sat:double,u:double,v:double,dep:double,ele:double);
T = FILTER A BY ( tem > -999 and z < 3);
C = GROUP T ALL;
D = FOREACH C GENERATE group as key, MAX(T.tem) as tem_max, MIN(T.tem) as tem_min, AVG(T.tem) as tem_avg, MAX(T.sat) as sat_max, MIN(T.sat)as sat_min, AVG(T.sat) as sat_avg, AVG(T.u) as u_avg, AVG(T.v) as v_avg, COUNT(T);
DUMP D;
