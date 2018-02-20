setwd("C:/Users/pportocarrero@mef.gob.pe/Desktop/monetary_policy") #Sets the working directory

library(readxl) #Loads the necessary library to read excel files

monetary_policy <- read_excel("monetary_policy.xlsx") #Imports original excel database

monetary_policy #Shows the recently imported database

save(monetary_policy,file = "monetary_policy_db.df") #Saves database

load("monetary_policy_db.df")

monetary_policy <- rbind(monetary_policy, c(Jan))