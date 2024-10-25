import rendeles
import etlap
#####return-ből#####
rend_lev = [1]
rend_lev_ar = [1000]
rend_fo = [3]
rend_fo_ar = [1800]
####################

def nyugta(kiir):
    etlap.kiir2(); etlap.kiir2("|           NYUGTA:          |", 1); etlap.kiir2()
    etlap.kiir(rend_lev, rend_lev_ar, rend_fo, rend_fo_ar)


