
%module dgtal

%{
#include "/home/florent/projet/DGtal/src/DGtal/arithmetic/LighterSternBrocot.h"
#include "/home/florent/projet/DGtal/src/DGtal/base/StdRebinders.h"
%}

%include "/home/florent/projet/DGtal/src/DGtal/arithmetic/LighterSternBrocot.h"
%include "/home/florent/projet/DGtal/src/DGtal/base/StdRebinders.h"

%template (LighterSternBrocoti64i64MapRebinder) LighterSternBrocot<DGTal::int64_t,DGTal::int64_t,StdMapRebinder>;
