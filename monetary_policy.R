setwd("/Users/Pedro/Desktop/monetary_policy") #Sets the working directory

#library(readxl) #Loads the necessary library to read excel files

#expectations_db <- read_excel("expectations_db.xlsx") #Imports original excel database of expectations

#expectations_db #Shows the recently imported database (expectations)

#save(expectations_db,file = "expectations_db.df") #Saves database

#inflation_db <- read_excel("inflation_db.xlsx") #Imports original inflation dataset

#inflation_db

#save(inflation_db,file = "inflation_db.df") #Saves inflation dataset

#interest_rate_db <- read_excel("interest_rate_db.xlsx") #Imports interest rate dataset

#interest_rate_db

#save(interest_rate_db,file = "interest_rate_db.df") #Saves interest rate dataset

###################### LOADS THE DATA AND ADDS NEW ROWS

load("expectations_db.df")

load("inflation_db.df")

load("interest_rate_db.df")

interest_rate_db <- rbind(interest_rate_db, c("Jan", "January", "01", "18", 2018, 3.00, 2, 3, 1)) #Code to add latest data on interest rate

save(interest_rate_db,file = "interest_rate_db.df")

expectations_db <- rbind(expectations_db, c("Jan", "January", "01", "18", 2018, 58.5, 70.7, 50, 2.23, NA, 2.4, 2.5)) #Code to add latest data on expectations

save(expectations_db,file = "expectations_db.df")

inflation_db <- rbind(inflation_db, c("Jan", "January", "01", "18", 2018, 0.127417107488597, 1.2531883694175, 0.127417107488597, -0.129632120477368, 1.97121356769657)) #Code to add latest data on inflation

save(inflation_db,file = "inflation_db.df")

######################## SAVE THE LATEST DATA (t = 0 and t = - 1)

#### LATEST INFLATION DATA

last_month_col <- inflation_db[, c(2)]
last_month <- tail(last_month_col, 1)
last_month_t1 <- head(tail(last_month_col, n=2), n=1)

last_inf_m_col <- inflation_db[, c(6)]
last_inf_m <- tail(last_inf_m_col, 1)
last_inf_m_t1 <- head(tail(last_inf_m_col, n=2), n=1)

last_inf_yoy_col <- inflation_db[,c(7)]
last_inf_yoy <- tail(last_inf_yoy_col, 1)
last_inf_yoy_t1 <- head(tail(last_inf_yoy_col, n=2), n=1)

last_inf_ytd_col <- inflation_db[,c(8)]
last_inf_ytd <- tail(last_inf_ytd_col, 1)
last_inf_ytd_t1 <- head(tail(last_inf_ytd_col, n=2), n=1)

last_cinf_m_col <- inflation_db[,c(9)]
last_cinf_m <- tail(last_cinf_m_col,1)
last_cinf_m_t1 <- head(tail(last_cinf_m_col, n=2), n=1)

last_cinf_yoy_col <- inflation_db[,c(10)]
last_cinf_yoy <- tail(last_cinf_yoy_col,1)
last_cinf_yoy_t1 <- head(tail(last_cinf_yoy_col, n=2), n=1)

#### LATEST EXPECTATIONS DATA

last_3m_col <- expectations_db[, c(6)]
last_3m <- tail(last_3m_col, 1)
last_3m_t1 <- head(tail(last_3m_col, n=2), n=1)

last_12m_col <- expectations_db[, c(7)]
last_12m <- tail(last_12m_col, 1)
last_12m_t1 <- head(tail(last_12m_col, n=2), n=1)

last_12m_e_col <- expectations_db[, c(9)]
last_12m_e <- tail(last_12m_e_col, 1)
last_12m_e_t1 <- head(tail(last_12m_e_col, n=2), n=1)

last_2018_ie_col <- expectations_db[, c(11)]
last_2018_ie <- tail(last_2018_ie_col, 1)
last_2018_ie_t1 <- head(tail(last_2018_ie_col, n=2), n=1)

last_2019_ie_col <- expectations_db[, c(12)]
last_2019_ie <- tail(last_2019_ie_col, 1)
last_2019_ie_t1 <- head(tail(last_2019_ie_col, n=2), n=1)

#### LATEST INFLATION RATES DATA

last_interest_rate_col <- interest_rate_db[, c(6)]
last_interest_rate <- tail(last_interest_rate_col, 1)
last_interest_rate_t1 <- head(tail(last_interest_rate_col, n=2), n=1)

######################## DATA FOR CHARTS

set_colors <- c(rgb(r=0.237,g=0.50,b=0.55), rgb(r=0.5,g=0.148,b=0.185), rgb(r=0.75,g=0.75,b=0.77))
graph_int_rt_dt <- interest_rate_db[-c(1:120), c(4)]
graph_int_rt <- interest_rate_db[-c(1:120), c(6)]
