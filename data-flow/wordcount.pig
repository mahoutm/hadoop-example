a = load '/flume/events/*';
b = foreach a generate flatten(TOKENIZE((chararray)$0)) as word;
c = group b by word;
d = foreach c generate COUNT(b) as cnt, group as wd;
store d into 'koala' using org.apache.hcatalog.pig.HCatStorer();
