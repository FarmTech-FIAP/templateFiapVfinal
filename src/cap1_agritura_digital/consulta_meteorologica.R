# ============================================================
# Aplicacao em R - Consulta de dados meteorologicos via API
# FarmTech Solutions - Monitoramento Climatico
# ============================================================

if (!require(jsonlite)) install.packages("jsonlite", repos = "https://cloud.r-project.org")
library(jsonlite)

cidade <- "Sao Paulo"
pais <- "Brazil"

cat("========================================\n")
cat("   FARMTECH - CONSULTA METEOROLOGICA\n")
cat("========================================\n\n")

url_geo <- paste0(
  "https://geocoding-api.open-meteo.com/v1/search?name=",
  URLencode(cidade),
  "&count=1&language=pt&format=json"
)

geo <- fromJSON(url_geo)

if (is.null(geo$results) || length(geo$results) == 0) {
  stop("Nao foi possivel localizar a cidade informada na API.")
}

latitude <- geo$results$latitude[1]
longitude <- geo$results$longitude[1]
nome_local <- geo$results$name[1]
estado <- if ("admin1" %in% names(geo$results)) geo$results$admin1[1] else ""
pais_encontrado <- geo$results$country[1]

#Consulta
url_meteo <- paste0(
  "https://api.open-meteo.com/v1/forecast?",
  "latitude=", latitude,
  "&longitude=", longitude,
  "&current=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,wind_speed_10m",
  "&daily=temperature_2m_max,temperature_2m_min,precipitation_sum",
  "&timezone=America%2FSao_Paulo",
  "&forecast_days=3"
)

meteo <- fromJSON(url_meteo)

if (is.null(meteo$current)) {
  stop("Nao foi possivel obter os dados meteorologicos.")
}

#Processando dados atuais
temp_atual <- meteo$current$temperature_2m
umidade_atual <- meteo$current$relative_humidity_2m
sensacao <- meteo$current$apparent_temperature
chuva_atual <- meteo$current$precipitation
vento_atual <- meteo$current$wind_speed_10m
hora_leitura <- meteo$current$time


cat("========================================\n")
cat("   CLIMA ATUAL\n")
cat("========================================\n")
cat("Horario da leitura:        ", hora_leitura, "\n")
cat("Temperatura atual:         ", temp_atual, "C\n")
cat("Umidade relativa do ar:    ", umidade_atual, "%\n")
cat("Sensacao termica:          ", sensacao, "C\n")
cat("Precipitacao atual:        ", chuva_atual, "mm\n")
cat("Velocidade do vento:       ", vento_atual, "km/h\n\n")

# Proximos 3 dias
cat("========================================\n")
cat("   PREVISAO PARA OS PROXIMOS 3 DIAS\n")
cat("========================================\n")

previsao <- data.frame(
  data = meteo$daily$time,
  temp_max = meteo$daily$temperature_2m_max,
  temp_min = meteo$daily$temperature_2m_min,
  chuva_dia = meteo$daily$precipitation_sum
)

for (i in 1:nrow(previsao)) {
  cat("Data: ", previsao$data[i], "\n")
  cat("  Temperatura maxima: ", previsao$temp_max[i], "C\n")
  cat("  Temperatura minima: ", previsao$temp_min[i], "C\n")
  cat("  Precipitacao total: ", previsao$chuva_dia[i], "mm\n\n")
}