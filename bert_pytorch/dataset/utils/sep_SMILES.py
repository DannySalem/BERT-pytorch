import re
import pdb

two_letter_atoms = ['He','Li', 'Be', 'Ne', 'Na', 'Mg','Al','Si','Cl','Ar','Ca','Sc','Ti','Cr','Mn','Fe','Co','Ni',
'Cu','Zn','Ga','Ge','As','Se','Br','Kr','Rb','Sr','Zr','Nb','Mo','Tc','Ru','Rh','Pd','Ag','Cd',
'In','Sn','Sb','Te','Xe','Cs','Ba','La','Xe','Pr','Nd','Pm','Sm','Eu','Gd','Tb','Dy','Ho','Er',
'Tm','Yb','Lu','Hf','Ta','Re','Os','Ir','Pt','Au','Hg','Tl','Pb','Bi','Po','At','Rn','Fr','Ra',
'Ac','Th','Pa','Np','Pu','Am','Cm','Bk','Cf','Es','Fm','Md','No','Lr','Rf','Db','Sg','Hs','Mt',
'Ds','Rg','Cn','Nh','Fl','Mc','Lv','Ts','Og']

#regex = '(\[[^\[\]]{1,6}\])'
test_string = 'cCCc[Na+].[Na+].[O-]C(=O)C1=C(C=CC=C1)C2=C3C=C(Br)C(=O)C(Br)=C3OC4=C2C=C(Br)C([O-])=C4'
test_string = 'CC(O)=O.CCNC(=O)[C@@H]1CCCN1C(=O)[C@H](CCCNC(N)=N)NC(=O)[C@H](CC(C)C)NC(=O)[C@@H](CC2=CNC3=C2C=CC=C3)NC(=O)[C@H](CC4=CC=C(O)C=C4)NC(=O)[C@H](CO)NC(=O)[C@H](CC5=CNC6=C5C=CC=C6)NC(=O)[C@H](CC7=CNC=N7)NC(=O)[C@@H]8CCC(=O)N8'

def tokenize_SMILES(input_string = test_string):
    regex = '([A-Z][a-z])'
    #print(input_string)
    token_list = re.split(regex, input_string)

    if len(token_list)>1:
        two_letter_atom_ids=list(range(1,len(token_list),2))
        remainder_ids=list(range(0,len(token_list),2))

        for idx in two_letter_atom_ids:
            if token_list[idx] not in two_letter_atoms:
                remainder_ids.append(idx)

        remainder_ids.sort(reverse = True)
        
        for idx in remainder_ids:
            token_list[idx:idx+1]=list(token_list[idx])

    else:
        token_list = list(input_string)

    e_indices = [i for i, x in enumerate(token_list) if x == "e"]
    e_indices.reverse()
    for j in e_indices:
        #if token_list[j+1] != ']':
        token_list[j-1:j+1] = [''.join(token_list[j-1:j+1])]

    a_indices = [i for i, x in enumerate(token_list) if x == "a"]
    a_indices.reverse()
    for j in a_indices:
        if token_list[j+1] != ']':
            token_list[j:j+2] = [''.join(token_list[j:j+2])]

    return token_list


#print(tokenize_SMILES())