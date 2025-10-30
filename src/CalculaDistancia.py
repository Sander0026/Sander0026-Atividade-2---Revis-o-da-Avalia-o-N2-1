def CalculaDistancia(cliente, galpao):
  distância =  (cliente['Latitude'] - galpao['Latitude'])**2 + \
               (cliente['Longitude'] - galpao['Longitude'])**2
  return distância**0.5
