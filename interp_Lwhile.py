from ast import *
from interp_Lif import InterpLif
from utils import *

class InterpLwhile(InterpLif):

  def interp_stmts(self, ss, env):
    if len(ss) == 0:
      return
    match ss[0]:
      case While(test, body, []):
        while self.interp_exp(test, env):
            self.interp_stmts(body, env)
        return self.interp_stmts(ss[1:], env)
      case _:
        return super().interp_stmts(ss, env)
    
