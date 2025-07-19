import matplotlib.pyplot as pt
import pandas as pd
from maalingaar import Maalinger_aar


def main():
  data = {}
  maalinger = pd.read_csv("F:/IcyWorep/Øvelse 9/solflekkaktivitet_daglig.csv", header=None, sep=";")


  for _, maaling in maalinger.iterrows():
    aar = int(maaling[0])
    antall_solflekker = int(maaling[4])

    if aar not in data:
      data[aar] = Maalinger_aar(aar)

    if antall_solflekker != -1:
      data[aar].legge_maaling(antall_solflekker)

  x = list(data.keys())
  gjennomsnitt_solflekker = []
  maksimum = []
  minimum = []

  for i in range(len(x)):
    maaling = data[x[i]]
    gjennomsnitt = maaling.gjennomsnitt_solflekker()
    
    gjennomsnitt_solflekker.append(gjennomsnitt)
    maksimum.append(maaling.maks_daglig)
    minimum.append(maaling.min_daglig)

  topp_x = []
  topp_y = []

  for i in range(5, len(x) - 5):
    if gjennomsnitt_solflekker[i] >= max(gjennomsnitt_solflekker[i-5:i+5]):
      topp_x.append(x[i])
      topp_y.append(gjennomsnitt_solflekker[i])

  forskjell = [topp_x[i+1] - topp_x[i] for i in range(len(topp_x) - 1)]
  gjennomsnitt_forskjell = round(sum(forskjell) / len(forskjell), 1)

  print(f"Gjennomsnittlige avstanden mellom toppene: {gjennomsnitt_forskjell} år")

  pt.plot(x, gjennomsnitt_solflekker, color="black")
  pt.plot(x, maksimum, ls="dashed", color="red")
  pt.plot(x, minimum, ls="dashed", color="blue")
  pt.scatter(topp_x, topp_y, color="red", zorder=2)
  pt.title("Solflekkaktivitet hvert år")
  pt.legend(["Gjennomsnitt", "Maksimum", "Minimum", "Topper"])
  pt.show()
  
if __name__ == "__main__":
  main()