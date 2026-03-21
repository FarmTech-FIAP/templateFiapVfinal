# ============================================================
# g. Aplicação em R para calcular dados estatísticos básicos
# FarmTech Solutions - Análise Estatística
# ============================================================
pasta_projeto <- file.path(getwd(), "FIAP", "src", "cap1_agritura_digital")
caminho_csv <- file.path(pasta_projeto, "dados_farmtech_sao_paulo.csv")

if (dir.exists(pasta_projeto)) {
  cat("Arquivos na pasta:\n")
  print(list.files(pasta_projeto))
}

dados <- read.csv(caminho_csv, stringsAsFactors = FALSE)

colunas_necessarias <- c("area_ha", "insumo_total_kg", "ruas", "plantas", "cultura")
faltando <- setdiff(colunas_necessarias, names(dados))

if (length(faltando) > 0) {
  stop(paste("Colunas ausentes no CSV:", paste(faltando, collapse = ", ")))
}

cat("========================================\n")
cat("   FARMTECH - DADOS IMPORTADOS\n")
cat("========================================\n\n")

# Estatisticas gerais
media_area <- mean(dados$area_ha, na.rm = TRUE)
desvio_area <- sd(dados$area_ha, na.rm = TRUE)

media_insumo <- mean(dados$insumo_total_kg, na.rm = TRUE)
desvio_insumo <- sd(dados$insumo_total_kg, na.rm = TRUE)

media_ruas <- mean(dados$ruas, na.rm = TRUE)
desvio_ruas <- sd(dados$ruas, na.rm = TRUE)

media_plantas <- mean(dados$plantas, na.rm = TRUE)
desvio_plantas <- sd(dados$plantas, na.rm = TRUE)

cat("\n========================================\n")
cat("   RELATORIO ESTATISTICO GERAL\n")
cat("========================================\n\n")

cat("Area Plantada (ha):\n")
cat("  Media: ", round(media_area, 2), "\n")
cat("  Desvio:", round(desvio_area, 2), "\n\n")

cat("Insumo Total (kg):\n")
cat("  Media: ", round(media_insumo, 2), "\n")
cat("  Desvio:", round(desvio_insumo, 2), "\n\n")

cat("Quantidade de Ruas:\n")
cat("  Media: ", round(media_ruas, 2), "\n")
cat("  Desvio:", round(desvio_ruas, 2), "\n\n")

cat("Quantidade de Plantas:\n")
cat("  Media: ", round(media_plantas, 2), "\n")
cat("  Desvio:", round(desvio_plantas, 2), "\n\n")

cat("========================================\n")
cat("   ESTATISTICAS POR CULTURA\n")
cat("========================================\n\n")

culturas <- unique(dados$cultura)

for (c in culturas) {
  sub <- dados[dados$cultura == c, ]
  
  cat("Cultura:", c, "\n")
  cat("  Media area (ha): ", round(mean(sub$area_ha, na.rm = TRUE), 2), "\n")
  cat("  Desvio area:     ", round(sd(sub$area_ha, na.rm = TRUE), 2), "\n")
  cat("  Media insumo:    ", round(mean(sub$insumo_total_kg, na.rm = TRUE), 2), "\n")
  cat("  Desvio insumo:   ", round(sd(sub$insumo_total_kg, na.rm = TRUE), 2), "\n\n")
}

hist(dados$area_ha,
     main = "Histograma - Area Plantada (ha)",
     xlab = "Area (ha)",
     ylab = "Frequencia",
     col = "lightgreen",
     border = "darkgreen")

boxplot(dados$insumo_total_kg,
        main = "Boxplot - Insumo Total (kg)",
        ylab = "Insumo (kg)",
        col = "lightyellow",
        border = "orange")

plot(dados$area_ha, dados$insumo_total_kg,
     main = "Area (ha) x Insumo Total (kg)",
     xlab = "Area (ha)",
     ylab = "Insumo Total (kg)",
     col = "blue",
     pch = 19)

boxplot(area_ha ~ cultura, data = dados,
        main = "Area por Cultura",
        xlab = "Cultura",
        ylab = "Area (ha)",
        col = c("gold", "lightblue"))
