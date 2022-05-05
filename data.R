getwd()
setwd("C:/users/francisco")
getwd()

df = read.csv2(file = "hola.csv", header = TRUE, encoding = "UTF-8-BOM")
head(df)
