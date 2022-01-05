import sys

sys.path.append("../../common")
from env_indigo import *

indigo = Indigo()

# Reactions
r = indigo.loadReaction("C>>C")
print(r.grossFormula())

r = indigo.loadReaction("CC.C>>C.CC")
print(r.grossFormula())

r = indigo.loadReaction(
    """$RXN



  1  1  0
$MOL

  Ketcher 11071614152D 1   1.00000     0.00000     0

 18 17  0     0  0            999 V2000
   -6.9282    0.0000    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   -6.0622   -0.5000    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   -5.1961    0.0000    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   -4.3301   -0.5000    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   -3.4641    0.0000    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   -2.5981   -0.5000    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   -1.7321    0.0000    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   -0.8660   -0.5000    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    0.0000    0.0000    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    0.8660   -0.5000    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    1.7321    0.0000    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    2.5981   -0.5000    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    3.4641    0.0000    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    4.3301   -0.5000    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    5.1961    0.0000    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    6.0622   -0.5000    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    6.9282    0.0000    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    7.7942   -0.5000    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
  1  2  1  0     0  0
  2  3  1  0     0  0
  3  4  1  0     0  0
  4  5  1  0     0  0
  5  6  1  0     0  0
  6  7  1  0     0  0
  7  8  1  0     0  0
  8  9  1  0     0  0
  9 10  1  0     0  0
 10 11  1  0     0  0
 11 12  1  0     0  0
 12 13  1  0     0  0
 13 14  1  0     0  0
 14 15  1  0     0  0
 15 16  1  0     0  0
 16 17  1  0     0  0
 17 18  1  0     0  0
M  STY  1   1 SRU
M  SLB  1   1   1
M  SCN  1   1 HT 
M  SMT   1 n
M  SAL   1  2   4   5
M  SBL   1  2   3   5
M  SDI   1  4   -4.7631   -1.0000   -4.7631    0.5000
M  SDI   1  4   -3.0311    0.5000   -3.0311   -1.0000
M  STY  1   2 SRU
M  SLB  1   2   2
M  SCN  1   2 HT 
M  SMT   2 k
M  SAL   2  3  11  12  13
M  SBL   2  2  10  13
M  SDI   2  4    1.2990   -1.0000    1.2990    0.5000
M  SDI   2  4    3.8971    0.5000    3.8971   -1.0000
M  STY  1   3 SRU
M  SLB  1   3   3
M  SCN  1   3 HT 
M  SMT   3 n
M  SAL   3  1   8
M  SBL   3  2   7   8
M  SDI   3  4   -1.2990   -1.0000   -1.2990    0.5000
M  SDI   3  4   -0.4330    0.5000   -0.4330   -1.0000
M  END
$MOL

  Ketcher 11071614152D 1   1.00000     0.00000     0

 18 17  0     0  0            999 V2000
   11.9888    0.1500    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   12.8548   -0.3500    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   13.7209    0.1500    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   14.5869   -0.3500    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   15.4529    0.1500    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   16.3189   -0.3500    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   17.1849    0.1500    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   18.0510   -0.3500    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   18.9170    0.1500    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   19.7829   -0.3500    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   20.6490    0.1500    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   21.5150   -0.3500    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   22.3810    0.1500    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   23.2470   -0.3500    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   24.1130    0.1500    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   24.9791   -0.3500    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   25.8451    0.1500    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   26.7112   -0.3500    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
  1  2  1  0     0  0
  2  3  1  0     0  0
  3  4  1  0     0  0
  4  5  1  0     0  0
  5  6  1  0     0  0
  6  7  1  0     0  0
  7  8  1  0     0  0
  8  9  1  0     0  0
  9 10  1  0     0  0
 10 11  1  0     0  0
 11 12  1  0     0  0
 12 13  1  0     0  0
 13 14  1  0     0  0
 14 15  1  0     0  0
 15 16  1  0     0  0
 16 17  1  0     0  0
 17 18  1  0     0  0
M  END
"""
)
print(r.grossFormula())
