#!/bin/bash

import sys
import os
import openpyxl
import pandas as pd
import math
import numpy as np
import statistics


def list_subdirs(in_path):
    matches = []
    for root, dirnames, filenames in os.walk(in_path):
        row=[]
        if(os.path.join(root).count("/")==3):
            matches.append(os.path.join(root)) 
    return matches
    
   
#COMPUTATION OF THE EXPECTED OUTCOME
def compute_oracle(spo2, hr, temp, sys_bp, dias_bp, glu,profile,oxi_risk,ecg_risk,term_risk,abps_risk,abpd_risk,glc_risk):

      
    output=""

    all_sensors=[]
    all_sensors.append(spo2)
    all_sensors.append(hr)
    all_sensors.append(temp)
    all_sensors.append(sys_bp)
    all_sensors.append(dias_bp)
    all_sensors.append(glu)
    
    all_sensors_score=[]
    all_sensors_weight=[]
    

    for item in all_sensors:
         if(item=="low risk"):
             all_sensors_score.append(5) #5
         elif(item=="moderate risk"):
             all_sensors_score.append(20) #20
         elif(item=="high risk"):
             all_sensors_score.append(100) #100
         elif(item=="deactivated"):
             all_sensors_score.append(-9999)
    
    weight_high_risk_sensor=-9999
    
    if(profile=="Obesity3"):
    	weight_high_risk_sensor=2.0
    elif(profile=="Obesity2"):
        weight_high_risk_sensor=1.90
    elif(profile=="Obesity1"):
        weight_high_risk_sensor=1.85
    elif(profile=="Overweight" or profile=="Underweight"  ):
        weight_high_risk_sensor=1.75
    elif(profile=="Normalweight"):
        weight_high_risk_sensor=1.0
    else:
    	weight_high_risk_sensor=-9999
    	print("ERROR")   
    
    all_sensors_weight.append(1.0)
    all_sensors_weight.append(weight_high_risk_sensor)
    all_sensors_weight.append(1.0)
    all_sensors_weight.append(weight_high_risk_sensor)
    all_sensors_weight.append(weight_high_risk_sensor)
    all_sensors_weight.append(1.0)
    
    score=0.0
    sum_w=0.0

    for s, w in zip(all_sensors_score, all_sensors_weight):
        if(s!=-9999):
    	    score=score+(s*w)   
    score=score/5
    
    if (score<8): #8
        return "VERY LOW RISK"

    elif (score>=8 and score<11):#8
        return "LOW RISK"

    elif (score>=11 and score<=20):#11 20
        return "MODERATE RISK"

    elif (score>20 and score<=36):#20 36
        return "CRITICAL RISK"

    elif (score>36):#36
        return "VERY CRITICAL RISK"

    else: 
        return "ERROR!"
       


def read_output_prob_t2(j,resulting_file_name,patients_folder):

    content=[]
    
    # Create a new Excel workbook
    workbook = openpyxl.Workbook()
    # Select the default sheet (usually named 'Sheet')
    sheet = workbook.active

    result=[]
    sum_diff=[0,0,0,0,0]
    
    content.append(["Id","Patient","Oxi","Ecg","Term","Abps","Abpd","Glc","BSN Outcome","Expected Outcome","Difference","Oxi-Risk","Ecg-Risk","Term-Risk","Abps-Risk","Abpd-Risk","Glc-Risk","Oxi-Sens","Ecg-Sens","Term-Sens","Abps-Sens","Abpd-Sens","Glc-Sens","Timestamp"])

    term_sensor="0"
    ecg_sensor="0"
    oxi_sensor="0"
    abps_sensor="0"
    abpd_sensor="0"
    glc_sensor="0"
    sensor_values=False
    id=0
    
 
    id_outcome=0
    id_oracle=0
    id_difference=0
	    
	    
    directories = list_subdirs(patients_folder)
    #aux=0
    for path in directories:
            profile=""
    	    if(path.endswith("Normalweight")):
    	        profile="Normalweight"
    	    elif(path.endswith("Obesity1")):
    	        profile="Obesity1"
    	    elif(path.endswith("Obesity2")):
    	        profile="Obesity2"
    	    elif(path.endswith("Obesity3")):
    	        profile="Obesity3"
    	    elif(path.endswith("Overweight")):
    	        profile="Overweight"
    	    elif(path.endswith("Underweight")):
    	        profile="Underweight"
    
    
    	    BSN_output_folder=path+"/output_"+str(j)
            #print(path+"\n")
            term="deactivated"
	    ecg="deactivated"
	    oxi="deactivated"
	    abps="deactivated"
	    abpd="deactivated"
	    glc="deactivated"
    
            txt_files=[]
            for file in os.listdir(path):
               if file.endswith(".txt"):
                   txt_files.append(os.path.join(path, file))
                   
            for txt in txt_files:
               if (os.path.basename(txt)=="HR_mc.txt"):
		    ecg="unknown"
               elif(os.path.basename(txt)=="SaO2_mc.txt"):
		    oxi="unknown" 
               elif(os.path.basename(txt)=="Temp_mc.txt"):
		    term="unknown"
               elif(os.path.basename(txt)=="NISysABP_mc.txt"):
		    abps="unknown" 
               elif(os.path.basename(txt)=="NIDiasABP_mc.txt"):
		    abpd="unknown" 
               elif(os.path.basename(txt)=="zzzzzzzzz"):
		    glc="unknown"
            
			   

	    if(os.path.isfile(BSN_output_folder+'/g4t1_-1-stdout.log')):
	       with open(BSN_output_folder+'/g4t1_-1-stdout.log') as f:
		    term_sensor="0"
		    ecg_sensor="0"
		    oxi_sensor="0"
		    abps_sensor="0"
		    abpd_sensor="0"
		    glc_sensor="0"
		    sensor_values=False
	    	    id_outcome=0
		    id_oracle=0
		    id_difference=0

		    x = f.readline() 
		    for line in f: 

		        if(sensor_values==False):
		    	    if(term!="deactivated" and line.startswith("Term:")):
		        	    term=line[6:len(line)-1]
		    	    if(ecg!="deactivated" and line.startswith("Ecg:")):
		        	    ecg=line[5:len(line)-1]
		    	    if(oxi!="deactivated" and line.startswith("Oxi:")):
		        	    oxi=line[5:len(line)-1]
		    	    if(abps!="deactivated" and line.startswith("Abps:")):
		        	    abps=line[6:len(line)-1]
		    	    if(abpd!="deactivated" and line.startswith("Abpd:")):
		        	    abpd=line[6:len(line)-1]
		    	    if(glc!="deactivated" and line.startswith("Glc:")):
		        	    glc=line[5:len(line)-1]

		   	    if(line.startswith("| THERM_RISK: ")):
		        	    term_risk=line[14:len(line)-1]
		    	    if(line.startswith("| ECG_RISK: ")):
		        	    ecg_risk=line[12:len(line)-1]
		    	    if(line.startswith("| OXIM_RISK: ")):
		        	    oxi_risk=line[13:len(line)-1]
		   	    if(line.startswith("| ABPS_RISK: ")):
		        	    abps_risk=line[13:len(line)-1]
		    	    if(line.startswith("| ABPD_RISK: ")):
		        	    abpd_risk=line[13:len(line)-1]
		    	    if(line.startswith("| GLC_RISK: ")):
		        	    glc_risk=line[12:len(line)-1]
		            if(line.startswith("++++++++++++++++++++")):
		                    sensor_values=True
		        else:
			    if(line.startswith("Trm:")):
		        	    term_sensor=line[5:len(line)-1]
		    	    if(line.startswith("Ecg:")):
			            ecg_sensor=line[5:len(line)-1]
		    	    if(line.startswith("Oxi:")):
		       		    oxi_sensor=line[5:len(line)-1]
		    	    if(line.startswith("Abps:")):
		       		    abps_sensor=line[6:len(line)-1]
		    	    if(line.startswith("Abpd:")):
		        	    abpd_sensor=line[6:len(line)-1]
		    	    if(line.startswith("Glc:")):
		       		    glc_sensor=line[5:len(line)-1]
		            if(line.startswith("++++++++++++++++++++")):
		                    sensor_values=False           

		        if(line.startswith("MilliSeconds Since Epoch:")):
		            time=line[25:(len(line)-1)]

		        if(line.startswith("| PATIENT_STATE:")):
		            resultado=line[16:(len(line)-1)]
		            if(term!="unknown" and ecg!="unknown" and oxi!="unknown" and abps!="unknown" and abpd!="unknown" and glc!="unknown"):
		                oracle=compute_oracle(oxi,ecg,term,abps, abpd, glc,profile,oxi_risk,ecg_risk,term_risk,abps_risk,abpd_risk,glc_risk)
		                if (resultado=="VERY LOW RISK"):
		                   id_outcome=0
		                elif (resultado=="LOW RISK"):
		                   id_outcome=1
		                elif (resultado=="MODERATE RISK"):
		                   id_outcome=2
		                elif (resultado=="CRITICAL RISK"):
		                   id_outcome=3
		                elif (resultado=="VERY CRITICAL RISK"):
		                   id_outcome=4
		                else:
		                   id_outcome=9999999999999

		                if (oracle=="VERY LOW RISK"):
		                   id_oracle=0
		                elif (oracle=="LOW RISK"):
		                   id_oracle=1
		                elif (oracle=="MODERATE RISK"):
		                   id_oracle=2
		                elif (oracle=="CRITICAL RISK"):
		                   id_oracle=3
		                elif (oracle=="VERY CRITICAL RISK"):
		                   id_oracle=4
		                else:
		                   id_oracle=9999999999999
		                id_difference=abs(id_outcome-id_oracle)
		                content.append([str(id),os.path.basename(path),oxi,ecg,term,abps,abpd,glc,resultado,oracle,str(id_difference), oxi_risk,ecg_risk,term_risk,abps_risk,abpd_risk, glc_risk,oxi_sensor, ecg_sensor,term_sensor, abps_sensor, abpd_sensor,glc_sensor,time])
		                sum_diff[id_difference]=sum_diff[id_difference]+1
		                                      
				id=id+1

		               
	    
    tot_diff=sum_diff[0]+sum_diff[1]+sum_diff[2]+sum_diff[3]+sum_diff[4]
    tot_diff_perc=[]

    tot_diff_perc.append(sum_diff[0]*100/float(tot_diff))
    tot_diff_perc.append(sum_diff[1]*100/float(tot_diff))
    tot_diff_perc.append(sum_diff[2]*100/float(tot_diff))
    tot_diff_perc.append(sum_diff[3]*100/float(tot_diff))
    tot_diff_perc.append(sum_diff[4]*100/float(tot_diff))
	  
    content.append([])
    content.append(["","Absolute Amount","Percentage Amount"])
    content.append(["Difference 0", sum_diff[0],str(tot_diff_perc[0])+""])
    content.append(["Difference 1", sum_diff[1],str(tot_diff_perc[1])+"","","Passing TC Rate:"])
    content.append(["Difference 2", sum_diff[2],str(tot_diff_perc[2])+"","",str(float("{:.2f}".format(tot_diff_perc[0]+tot_diff_perc[1])))+""])
    content.append(["Difference 3", sum_diff[3],str(tot_diff_perc[3])+""])
    content.append(["Difference 4", sum_diff[4],str(tot_diff_perc[4])+""])
    content.append([])
    content.append([])
    content.append(["Sum",tot_diff,str(tot_diff_perc[0]+tot_diff_perc[1]+tot_diff_perc[2]+tot_diff_perc[3]+tot_diff_perc[4])+""])
  
    
    for row in content:
	sheet.append(row)
	    
    # Save the workbook to a file
    workbook.save("../Output_files/output"+str(j)+"_"+resulting_file_name)
    #print(tot_diff)
    print(str(float("{:.2f}".format(tot_diff_perc[0]+tot_diff_perc[1]))))
    return (tot_diff_perc[0]+tot_diff_perc[1])
 


def main(argv):
     
    if(len(sys.argv)==3):
       patients_folder= sys.argv[1]    
    elif(len(sys.argv)==1):
       patients_folder="../DTMCs"
    else:
       print("Error!")
       exit(0)
       

    number_of_executions=5    
    passing_tc_rate=[]
     
    for j in range(0,number_of_executions):
       print("Ex"+str(j)+":")
       passing_tc_rate.append(read_output_prob_t2(j,'output_sensor_readings.xlsx',patients_folder))
  

        
if __name__ == "__main__":
    main(sys.argv)
