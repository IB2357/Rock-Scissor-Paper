from random import choice


RSP = {'P':'S','S':'R','R':'P'}
l = list(RSP.keys())
m,u = None,None
m_points, u_points = 0, 0

for i in range(6):
    m = choice(l)
    print(m)
    u = input("Enter R or P or S:\n")
    if u == m:
       u_points +=1
       m_points +=1

    elif u == RSP[m]:
        u_points +=1

    else:
        m_points +=1
    print(f" user's points {u_points}\n machine's points {m_points}")


print(f"end of the game\n\tuser's points {u_points}\n\tmachine's points {m_points}")
