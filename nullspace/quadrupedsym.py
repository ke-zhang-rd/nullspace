from sympy import symbols, simplify

q_sym = symbols('q0:12')

x0, y0, z0 = symbols('x0, y0, z0', real=True)
x1, y1, z1 = symbols('x1, y1, z1', real=True)
x2, y2, z2 = symbols('x2, y2, z2', real=True)
x3, y3, z3 = symbols('x3, y3, z3', real=True)

x0, y0, z0 = symbols('x0, y0, z0', real=True)
x0, y0, z0 = symbols('x0, y0, z0', real=True)
x0, y0, z0 = symbols('x0, y0, z0', real=True)

x0, y0, z0 = symbols('x0, y0, z0', real=True)
x0, y0, z0 = symbols('x0, y0, z0', real=True)
x0, y0, z0 = symbols('x0, y0, z0', real=True)

x0, y0, z0 = symbols('x0, y0, z0', real=True)
x0, y0, z0 = symbols('x0, y0, z0', real=True)
x0, y0, z0 = symbols('x0, y0, z0', real=True)

x0, y0, z0 = symbols('x0, y0, z0', real=True)
x0, y0, z0 = symbols('x0, y0, z0', real=True)
x0, y0, z0 = symbols('x0, y0, z0', real=True)


r0 = Matrix([x0, y0, z0])
r1 = Matrix([x0, y0, z0])
r2 = Matrix([x0, y0, z0])
r3 = Matrix([x0, y0, z0])

r6 = Matrix([x0, y0, z0])
r7 = Matrix([x0, y0, z0])
r8 = Matrix([x0, y0, z0])
r9 = Matrix([x0, y0, z0])
r10 = Matrix([x0, y0, z0])
r11 = Matrix([x0, y0, z0])
r12 = Matrix([x0, y0, z0])
r13 = Matrix([x0, y0, z0])

r14 = Matrix([x0, y0, z0])
r15 = Matrix([x0, y0, z0])
r16 = Matrix([x0, y0, z0])
r17 = Matrix([x0, y0, z0])

XJ = [SXForm(Ex(q_sym[0]), ZeroMatrix(3, 1)),
      SXForm(Ey(q_sym[1]), ZeroMatrix(3, 1)),
      SXForm(Ey(q_sym[2]), ZeroMatrix(3, 1)),
      SXForm(Ex(q_sym[3]), ZeroMatrix(3, 1)),
      SXForm(Ey(q_sym[4]), ZeroMatrix(3, 1)),
      SXForm(Ey(q_sym[5]), ZeroMatrix(3, 1)),
      SXForm(Ex(q_sym[6]), ZeroMatrix(3, 1)),
      SXForm(Ey(q_sym[7]), ZeroMatrix(3, 1)),
      SXForm(Ey(q_sym[8]), ZeroMatrix(3, 1)),
      SXForm(Ex(q_sym[9]), ZeroMatrix(3, 1)),
      SXForm(Ey(q_sym[10]), ZeroMatrix(3, 1)),
      SXForm(Ey(q_sym[11]), ZeroMatrix(3, 1))]
      
Xtree = [None, #0
         None, #1
         None, #2
         None, #3
         None, #4
         None, #5
         SXForm(eye(3), r6),
         SXForm(perfect_Ez_pi, r7),
         SXForm(eye(3), r8),
         SXForm(eye(3), r9),
         SXForm(perfect_EZ_pi, r10),
         SXForm(eye(3), r11)
         SXForm(eye(3), r12),
         SXForm(perfect_EZ_pi, r13),
         SXForm(eye(3), r14),
         SXForm(eye(3), r15),
         SXForm(perfect_EZ_pi, r16),
         SXForm(eye(3), r17)

gcLocation = [SXForm(eye(3), r0),
              SXForm(eye(3), r1),
              SXForm(eye(3), r2),
              SXForm(eye(3), r3)]
  
Abad0_SX = Xtree[6]
Abad1_SX = Xtree[9]
Abad2_SX = Xtree[12]
Abad3_SX = Xtree[15]

Abad0_SX = simplify(Abad0_SX)
Abad1_SX = simplify(Abad1_SX)
Abad2_SX = simplify(Abad2_SX)
Abad3_SX = simplify(Abad3_SX)

abad0 = getr(Abad0_SX)
abad1 = getr(Abad1_SX)
abad2 = getr(Abad2_SX)
abad3 = getr(Abad3_SX)

abad0 = simplify(abad0)
abad1 = simplify(abad1)
abad2 = simplify(abad2)
abad3 = simplify(abad3)


Hip0_SX = Xtree[7] * XJ[0] * Abad0_SX
Hip1_SX = Xtree[10] * XJ[3] * Abad1_SX
Hip2_SX = Xtree[13] * XJ[6] * Abad2_SX
Hip3_SX = Xtree[16] * XJ[9] * Abad3_SX

Hip0_SX = simplify(Hip0_SX)
Hip1_SX = simplify(Hip1_SX)
Hip2_SX = simplify(Hip2_SX)
Hip3_SX = simplify(Hip3_SX)

hip0 = getr(Hip0_SX)
hip1 = getr(Hip1_SX)
hip2 = getr(Hip2_SX)
hip3 = getr(Hip3_SX)

hip0 = simplify(hip0)
hip1 = simplify(hip1)
hip2 = simplify(hip2)
hip3 = simplify(hip3)


Knee0_SX = Xtree[8] * XJ[1] * Hip0_SX
Knee1_SX = Xtree[11] * XJ[4] * Hip1_SX
Knee2_SX = Xtree[14] * XJ[7] * Hip2_SX
Knee3_SX = Xtree[17] * XJ[10] * Hip3_SX

Knee0_SX = simplify(Knee0_SX)
Knee1_SX = simplify(Knee1_SX)
Knee2_SX = simplify(Knee2_SX)
Knee3_SX = simplify(Knee3_SX)

knee0 = getr(Knee0_SX)
knee1 = getr(Knee1_SX)
knee2 = getr(Knee2_SX)
knee3 = getr(Knee3_SX)

knee0 = simplify(knee0)
knee1 = simplify(knee1)
knee2 = simplify(knee2)
knee3 = simplify(knee3)

T0 = gcLocation[0] * XJ[2] * knee0_SX
T1 = gcLocation[1] * XJ[5] * knee1_SX
T2 = gcLocation[2] * XJ[8] * knee2_SX
T3 = gcLocation[3] * XJ[11] * knee3_SX

T0 = simplify(T0)
T1 = simplify(T1)
T2 = simplify(T2)
T3 = simplify(T3)

foot0 = getr(T0)
foot1 = getr(T1)
foot2 = getr(T2)
foot3 = getr(T3)

foot0 = simplify(foot0)
foot1 = simplify(foot1)
foot2 = simplify(foot2)
foot3 = simplify(foot3)
