import os
import shutil


home_directory = os.path.expanduser("~")
print(home_directory)

def replace_file(target_path, replacement_file):
    try:
        # Copy the replacement file to the target location, overwriting the existing file
        shutil.copy(replacement_file, target_path)
        print("File replaced successfully")
    except Exception as e:
        print("Error replacing file")

# Usage example
if __name__ == "__main__":
   	#target_file = home_directory+"/Documentos/Imprimir.pdf"  # The destination where the file will be replaced
   	#replacement_file = "./Imprimir_Samira.pdf"  # The source file to copy
    
    	#replace_file(target_file, replacement_file)
    
    
    	replace_file(home_directory+"/sa-bsn/src/sa-bsn/target_system/components/component/src/CentralHub.cpp","../Files_to_Replace/CentralHub.cpp")
	replace_file(home_directory+"/sa-bsn/src/sa-bsn/target_system/components/component/include/component/CentralHub.hpp","../Files_to_Replace/CentralHub.hpp")
	replace_file(home_directory+"/sa-bsn/src/libbsn/src/generator/DataGenerator.cpp","../Files_to_Replace/DataGenerator.cpp")
	replace_file(home_directory+"/sa-bsn/src/libbsn/include/libbsn/generator/DataGenerator.hpp","../Files_to_Replace/DataGenerator.hpp")
	replace_file(home_directory+"/sa-bsn/src/sa-bsn/target_system/components/component/src/g3t1_1/G3T1_1.cpp","../Files_to_Replace/G3T1_1.cpp")
	replace_file(home_directory+"/sa-bsn/src/sa-bsn/target_system/components/component/src/g3t1_2/G3T1_2.cpp","../Files_to_Replace/G3T1_2.cpp")
	replace_file(home_directory+"/sa-bsn/src/sa-bsn/target_system/components/component/src/g3t1_3/G3T1_3.cpp","../Files_to_Replace/G3T1_3.cpp")
	replace_file(home_directory+"/sa-bsn/src/sa-bsn/target_system/components/component/src/g3t1_4/G3T1_4.cpp","../Files_to_Replace/G3T1_4.cpp")
	replace_file(home_directory+"/sa-bsn/src/sa-bsn/target_system/components/component/src/g3t1_5/G3T1_5.cpp","../Files_to_Replace/G3T1_5.cpp")
	replace_file(home_directory+"/sa-bsn/src/sa-bsn/target_system/components/component/src/g3t1_6/G3T1_6.cpp","../Files_to_Replace/G3T1_6.cpp")
	replace_file(home_directory+"/sa-bsn/src/sa-bsn/target_system/components/component/include/component/g4t1/G4T1.hpp","../Files_to_Replace/G4T1.hpp")
	replace_file(home_directory+"/sa-bsn/src/sa-bsn/target_system/components/component/src/g4t1/G4T1.cpp","../Files_to_Replace/G4T1.cpp")
	replace_file(home_directory+"/sa-bsn/src/sa-bsn/environment/patient/src/PatientModule.cpp","../Files_to_Replace/PatientModule.cpp")
	replace_file(home_directory+"/sa-bsn/src/libbsn/src/processor/Processor.cpp","../Files_to_Replace/Processor.cpp")	
	replace_file(home_directory+"/sa-bsn/src/sa-bsn/target_system/components/component/src/Sensor.cpp","../Files_to_Replace/Sensor.cpp")
	replace_file(home_directory+"/sa-bsn/run.sh","../Files_to_Replace/run.sh")
    		
    	
        replace_file(home_directory+"/sa-bsn/src/sa-bsn/configurations/target_system/g4t1.launch","../Files_to_Replace/g4t1.launch")
        replace_file(home_directory+"/sa-bsn/src/sa-bsn/configurations/target_system/g3t1_1.launch","../Files_to_Replace/g3t1_1.launch")
        replace_file(home_directory+"/sa-bsn/src/sa-bsn/configurations/target_system/g3t1_2.launch","../Files_to_Replace/g3t1_2.launch")
        replace_file(home_directory+"/sa-bsn/src/sa-bsn/configurations/target_system/g3t1_3.launch","../Files_to_Replace/g3t1_3.launch")
        replace_file(home_directory+"/sa-bsn/src/sa-bsn/configurations/target_system/g3t1_4.launch","../Files_to_Replace/g3t1_4.launch")
        replace_file(home_directory+"/sa-bsn/src/sa-bsn/configurations/target_system/g3t1_5.launch","../Files_to_Replace/g3t1_5.launch")
        replace_file(home_directory+"/sa-bsn/src/sa-bsn/configurations/target_system/g3t1_6.launch","../Files_to_Replace/g3t1_6.launch")
        
        
        
    	# Execute a shell command
	os.system("cd "+home_directory+"/sa-bsn/; catkin_make; cd -")

    	

    
