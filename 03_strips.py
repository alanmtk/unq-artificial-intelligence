class StripsGraph:
  def init(self, operadores)
    self.graph = dict()
    self._operadores()

  def getItem(self, state):
    if state not in self.graph:
      vecinos = dict()
      for o in self._operadores:
        if o.esAplicable(state):
          vecinos[o.name] = o.aplicar(state)

      self.graph[state] = vecinos

    return self.graph[state]


Nombre, Pre, EFF-, EFF+
Pre: precondicion
EFF-: cosas que dejan de valer
EFF+: cosas que valen

PickUpA = operador('pickup(A)', {'clear(A)', 'empty'}, {'empty', 'onTable(A)', 'on(A,B)', 'on(A,C)', 'clear(A)'}, {'holding(A)'})

PutDownA = operador('putdown(A)', {'holding(A)'}, {'holding(A)'}, {'empty', 'clear(A)', 'onTable(A)'})


initial = {'empty', 'onTable(A)', 'onTable(B)', 'onTable(C)', 'clear(A)', 'clear(B)', 'clear(C)'}
goal = {'on(A,B)', 'on(B,C)'}