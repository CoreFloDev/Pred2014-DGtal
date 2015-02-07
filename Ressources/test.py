import dgtal
from ctypes import c_int as ll

print dir(dgtal)

#fraction = dgtal.LightSternBrocot_fraction(3,5);

fraction = dgtal.Fraction

print dir(fraction)

f = dgtal.Fraction(3,5)
print f.p()
print f.q()
print f.k()
print f.u()
inv = f.inverse()
print inv.p()
print inv.q()
print f.partial(2).p()

#//! [approximation-types]
#  typedef DGtal::int64_t Integer;
#  typedef DGtal::int64_t Quotient;
#  typedef LighterSternBrocot<Integer, Quotient> SB; // the type of the Stern-Brocot tree
#  typedef SB::Fraction Fraction; // the type for fractions
#  typedef std::back_insert_iterator< Fraction > OutputIterator;
#  //! [approximation-types]

#  //! [approximation-process]
#  long double epsilon = 1e-14;
#  long double number0 = strtold( argv[ 1 ], 0 );
#  long double number = number0;
#  ASSERT( number >= 0.0 );
#  Fraction f;
#  OutputIterator itback = std::back_inserter( f );
#  Quotient i = 0;
#  while ( true )
#    {
#      long double int_part = floorl( number );
#      Quotient u = NumberTraits<long double>::castToInt64_t( int_part );
#      *itback++ = std::make_pair( u, i++ );
#      long double approx =
#        ( (long double) NumberTraits<Integer>::castToDouble( f.p() ) )
#        / ( (long double) NumberTraits<Integer>::castToDouble( f.q() ) );
#      std::cout << "z = " << f.p() << " / " << f.q()
#                << " =~ " << std::setprecision( 16 ) << approx << std::endl;
#      number -= int_part;
#      if ( ( (number0 - epsilon ) < approx )
#           && ( approx < (number0 + epsilon ) ) ) break;
#      number = 1.0 / number;
#    }
#  std::cout << "z = " << f.p() << " / " << f.q() << std::endl;
#  //! [approximation-process]
#  return 0;

print "Mec j'arrive au bout :D"
