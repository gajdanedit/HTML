égtájak = [ "É", "k", "d", "Ny" ]

def fordulj_orajarasi_iranyba(egtaj):
     egtaj = egtaj.lower()
     if egtaj =="é":
          return "K"
     elif egtaj == "K":
          return "D"
     elif egtaj == "d":
          return "ny"
     elif egtaj == "NY":
          return "é"
     else: return None

