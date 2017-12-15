load And3Way.hdl,
output-file And3Way.out,
compare-to And3Way.cmp,
output-list a%B3.1.3 b%B3.1.3 c%B3.1.3 out%B3.1.3;

set a 0,
set b 0,
set c 0,
eval,
output;

set a 0,
set b 1,
set c 0,
eval,
output;

set a 1,
set b 0,
set c 0,
eval,
output;

set a 1,
set b 1,
set c 0,
eval,
output;

set a 0,
set b 0,
set c 1,
eval,
output;

set a 0,
set b 1,
set c 1,
eval,
output;

set a 1,
set b 0,
set c 1,
eval,
output;

set a 1,
set b 1,
set c 1,
eval,
output;
