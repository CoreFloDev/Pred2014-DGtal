%module dgtal

%{

#include "/home/florent/projet/DGtal/src/DGtal/arithmetic/LighterSternBrocot.h"

using namespace DGtal;
%}


%include "/home/florent/projet/DGtal/src/DGtal/base/BasicTypes.h"
%include "/home/florent/projet/DGtal/src/DGtal/arithmetic/LighterSternBrocot.h"

%template (LightSternBrocot) DGtal::LighterSternBrocot<DGtal::int64_t,DGtal::int64_t>;
%rename (Fraction) LightSternBrocot::Fraction;
%rename (Node) LightSternBrocot::Node;
