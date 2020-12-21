from c3ga_py import *
from clifford.g3c import layout as g3c


def test_basics():
  # Garamon version
  mv1 = Mvec();
  mv1[scalar] = 1.0;
  mv1[E0] = 42.0;
  print("mv1 garamon: ", mv1 )
  
  # Clifford version
  mv1_clifford  = 1.0 + g3c.stuff.eo*42.0
  print("mv1 clifford: ", mv1_clifford)
  
  # Garamon version
  mv2 = Mvec()
  mv2[E0] = 1.0;
  mv2[E1] = 2.0;
  mv2 += e0123i() + 2*e01();
  print("mv2 : " , mv2 );
  
  # Clifford version
  mv2_clifford  = 1.0 + g3c.blades['e1']*2.0 + g3c.blades['e12345'] + 2*g3c.stuff.eo*g3c.blades['e1']
  print("mv2 clifford: ", mv2_clifford)

  # some products
  print("outer product     : ", (mv1 ^ mv2) )
  print("inner product     : ", (mv1 | mv2) )
  print("geometric product     : ", (mv1 * mv2) )


  # some tools
  print("grade : ", mv1.grade())
  print("norm : ", mv1.norm())
  print("norm : ", mv2.grade())

  
if __name__ == '__main__':
  test_basics()
