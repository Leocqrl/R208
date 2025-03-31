import re

def dep(cdc):
    reg=r'[0-8][0-9][0-9][0-9][0-9]|9[0-5][0-9][0-9][0-9]'
    if re.match(reg, cdc):
        return(f'{cdc} : OK')
    else :
        return(f'{cdc} : PAS OK')

dep('94999')

assert dep('94999') == '94999 : OK'