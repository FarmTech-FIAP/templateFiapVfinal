# ============================================================
# g. Aplicação em R para calcular dados estatísticos básicos
# FarmTech Solutions - Análise Estatística
# ============================================================

# 1. Carregar os dados exportados pelo Python
dados <- read.csv("dados_farmtech.csv")

# 2. Visualizar os dados carregados
cat("========================================\n")
cat("  FARMTECH - Dados Importados\n")
cat("========================================\n\n")
print(dados)

# 3. Estatísticas Básicas para Área (hectares)
media_area <- mean(dados$area_ha, na.rm = TRUE)
desvio_area <- sd(dados$area_ha, na.rm = TRUE)

# 4. Estatísticas Básicas para Insumo Total (kg)
media_insumo <- mean(dados$insumo_total_kg, na.rm = TRUE)
desvio_insumo <- sd(dados$insumo_total_kg, na.rm = TRUE)

# 5. Estatísticas Básicas para Quantidade de Ruas
media_ruas <- mean(dados$ruas, na.rm = TRUE)
desvio_ruas <- sd(dados$ruas, na.rm = TRUE)

# 6. Estatísticas Básicas para Quantidade de Plantas
media_plantas <- mean(dados$plantas, na.rm = TRUE)
desvio_plantas <- sd(dados$plantas, na.rm = TRUE)

# 7. Impressão do Relatório Estatístico
cat("\n========================================\n")
cat("  RELATÓRIO ESTATÍSTICO DA FAZENDA\n")
cat("========================================\n\n")

cat("Area Plantada (ha):\n")
cat("  - Media:        ", round(media_area, 4), "ha\n")
cat("  - Desvio Padrao:", round(desvio_area, 4), "ha\n\n")

cat("Insumo Total (kg):\n")
cat("  - Media:        ", round(media_insumo, 2), "kg\n")
cat("  - Desvio Padrao:", round(desvio_insumo, 2), "kg\n\n")

cat("Quantidade de Ruas:\n")
cat("  - Media:        ", round(media_ruas, 2), "\n")
cat("  - Desvio Padrao:", round(desvio_ruas, 2), "\n\n")

cat("Quantidade de Plantas:\n")
cat("  - Media:        ", round(media_plantas, 2), "\n")
cat("  - Desvio Padrao:", round(desvio_plantas, 2), "\n\n")

# 8. Gráficos

# Histograma da Área
hist(dados$area_ha,
     main = "Histograma - Area Plantada (ha)",
     xlab = "Area (ha)",
     ylab = "Frequencia",
     col = "lightgreen",
     border = "darkgreen")

# Boxplot do Insumo Total
boxplot(dados$insumo_total_kg,
        main = "Boxplot - Insumo Total (kg)",
        ylab = "Insumo (kg)",
        col = "lightyellow",
        border = "orange")

# Gráfico de dispersão: Área vs Insumo
plot(dados$area_ha, dados$insumo_total_kg,
     main = "Area (ha) x Insumo Total (kg)",
     xlab = "Area (ha)",
     ylab = "Insumo Total (kg)",
     col = "blue",
     pch = 19)

# Boxplot comparativo de área por cultura
boxplot(area_ha ~ cultura, data = dados,
        main = "Area por Cultura",
        xlab = "Cultura",
        ylab = "Area (ha)",
        col = c("gold", "lightblue"))
