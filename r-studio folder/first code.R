#Basic time plots:
#load necessary packages
library(tidyverse)
library(ggplot2)
#view timeplots of closing price of MSFT
ggplot(data = WQU_Econometrics_Module1_Data) + 
  geom_point(mapping = aes(x = Date, y = MSFT),
             color = "darkblue") +
  labs(x = "year",y = "Microsoft - Daily Closing Price")
ggsave("C:/Users/samar/Desktop/econometrics/Microsoft_closing_price.png")
#generate plots for each of the log return graphs of the four assets 
ggplot(data = WQU_Econometrics_Module1_Data) + 
  geom_line(mapping = aes(x = Date,y = APPL_lr), 
            color = "darkred") + 
  labs(x = "year",y = "Apple - Log Daily Return") 
ggsave("C:/Users/samar/Desktop/econometrics/Apple_log_returns.png") 
ggplot(data = WQU_Econometrics_Module1_Data) +
  geom_line(mapping = aes(x = Date,y = INTC_lr), 
            color ="darkgreen") +
  labs(x = "year",y = "Intel - Log Daily Return") 
ggsave("C:/Users/samar/Desktop/econometrics/Intel_log_returns.png") 
ggplot(data = WQU_Econometrics_Module1_Data) + 
  geom_line(mapping = aes(x = Date, y = IBM_lr), 
            color = "darkcyan") +
  labs(x = "year",y = "IBM - Log Daily Return") 
ggsave("C:/Users/samar/Desktop/econometrics/IBM_log_returns.png")
