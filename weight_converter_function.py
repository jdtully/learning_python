#converts Lbs  to KGs in  a  function

def convert_weight(weight,scale):
    if scale.lower=="p":
        con_weight = weight * .45
        scale = "K"
    else:
        con_weight = weight / 0.45
        scale = "P" 
    return
    con_weight=float()
    print(con_weight.convert_weight(55,"k"))