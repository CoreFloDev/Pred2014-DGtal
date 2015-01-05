
long double epsilon = 1e-14;
long double number0 = strtold( argv[ 1 ], 0 );
long double number = number0;
ASSERT( number >= 0.0 );
Fraction f;
OutputIterator itback = std::back_inserter( f );
Quotient i = 0;
while ( true )
  {
    long double int_part = floorl( number );
    Quotient u = NumberTraits<long double>::castToInt64_t( int_part );
    *itback++ = std::make_pair( u, i++ );
    long double approx =
      ( (long double) NumberTraits<Integer>::castToDouble( f.p() ) )
      / ( (long double) NumberTraits<Integer>::castToDouble( f.q() ) );
    std::cout << "z = " << f.p() << " / " << f.q()
              << " =~ " << std::setprecision( 16 ) << approx << std::endl;
    number -= int_part;
    if ( ( (number0 - epsilon ) < approx )
         && ( approx < (number0 + epsilon ) ) ) break;
    number = 1.0 / number;
  }
