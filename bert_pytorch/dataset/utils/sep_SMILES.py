import re
import pdb

#regex = '(\[[^\[\]]{1,6}\])'
test_string = 'cCCc[Na+].[Na+].[O-]C(=O)C1=C(C=CC=C1)C2=C3C=C(Br)C(=O)C(Br)=C3OC4=C2C=C(Br)C([O-])=C4'
test_string = 'CC(O)=O.CCNC(=O)[C@@H]1CCCN1C(=O)[C@H](CCCNC(N)=N)NC(=O)[C@H](CC(C)C)NC(=O)[C@@H](CC2=CNC3=C2C=CC=C3)NC(=O)[C@H](CC4=CC=C(O)C=C4)NC(=O)[C@H](CO)NC(=O)[C@H](CC5=CNC6=C5C=CC=C6)NC(=O)[C@H](CC7=CNC=N7)NC(=O)[C@@H]8CCC(=O)N8'

def tokenize_SMILES(input_string = test_string):
    regex = '([A-Z][a-z])'

    token_list = re.split(regex, input_string)

    if len(token_list)>1:
        two_letter_atom_ids=list(range(1,len(token_list),2))
        remainder_ids=list(range(0,len(token_list),2))

        for idx in two_letter_atom_ids:
            if token_list[idx]=='Cc' or token_list[idx]=='Oc':
                remainder_ids.append(idx)

        remainder_ids.sort(reverse = True)
        
        for idx in remainder_ids:
            token_list[idx:idx+1]=list(token_list[idx])

    else:
        token_list = list(input_string)

    return token_list


print(tokenize_SMILES())