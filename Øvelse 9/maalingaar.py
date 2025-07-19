class Maalinger_aar:
  def __init__(self, aar: int):
    self.aar = aar
    self.total_solflekker = 0
    self.antall_maalinger = 0
    self.maks_daglig = 0
    self.min_daglig = 1000

  def legge_maaling(self, antall_solflekker: int):
    self.total_solflekker += antall_solflekker
    self.antall_maalinger += 1

    if antall_solflekker > self.maks_daglig:
      self.maks_daglig = antall_solflekker

    if antall_solflekker < self.min_daglig:
      self.min_daglig = antall_solflekker

  def gjennomsnitt_solflekker(self) -> float:
    return self.total_solflekker / self.antall_maalinger