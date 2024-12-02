# AdapTA_Paper_AST


# AdapTA - Adaptive Testing Approach

**Paper Title**: An Adaptive Testing Approach Based on Field Data

**Submitted to**: Automation of Software Test (AST) Conference

**Abstract**: The growing need to test systems post-release has led to extending testing activities into production environments, where uncertainty and dynamic conditions pose significant challenges. Field testing approaches, especially Self-Adaptive Testing in the Field (SATF), face hurdles like managing unpredictability, minimizing system overhead, and reducing human intervention, among others. 
Despite its importance, SATF remains underexplored in the literature. This work introduces AdapTA (Adaptive Testing Approach), a novel SATF strategy tailored for testing Body Sensor Networks (BSNs). BSNs are networks of wearable or implantable sensors designed to monitor physiological and environmental data. AdapTA employs an ex-vivo approach, using real-world data collected from the field to simulate patient behavior in in-house experiments. 
Field data are used to derive Discrete-Time Markov Chain (DTMC) models, which simulate patient profiles and generate test input data for the BSN. The BSN’s outputs are compared against a proposed oracle to evaluate test outcomes. AdapTA's adaptive logic continuously monitors the system under test and the simulated patient, triggering adaptations as needed. Results demonstrate that AdapTA achieves greater effectiveness compared to a non-adaptive version of the proposed approach across three adaptation scenarios, emphasizing the value of its adaptive logic.
  
## **Configure the SA-BSN**:
1. Download and install the [ROS Noetic for Ubuntu 20.04](http://wiki.ros.org/noetic/Installation/Ubuntu)
2. Download and install the [SA-BSN](https://github.com/lesunb/bsn/tree/1c45cd8f4c43e36fcf5665940d5ce7c66b907b31)


## **Clone this repository**:
```
$ curl -o AdapTA_Paper.zip https://anonymous.4open.science/api/repo/AdapTA_Paper_AST-3715/zip
$ unzip AdapTA_Paper.zip -d AdapTA_Paper/
$ cd AdapTA_Paper/
```

## **Unzip the DTMCs folders**:
```
$ unzip AdapTA/S1_SensorDeactivation/DTMCs/DTMCs.zip -d AdapTA/S1_SensorDeactivation/DTMCs/
$ rm AdapTA/S1_SensorDeactivation/DTMCs/DTMCs.zip
$ unzip AdapTA/S2_PatientProfile/DTMCs/DTMCs.zip -d AdapTA/S2_PatientProfile/DTMCs/
$ rm AdapTA/S2_PatientProfile/DTMCs/DTMCs.zip
$ unzip AdapTA/S3_CriticalCondition/DTMCs/DTMCs.zip -d AdapTA/S3_CriticalCondition/DTMCs/
$ rm AdapTA/S3_CriticalCondition/DTMCs/DTMCs.zip
$ unzip Baseline/Baseline_S1/DTMCs/DTMCs.zip -d Baseline/Baseline_S1/DTMCs/
$ rm Baseline/Baseline_S1/DTMCs/DTMCs.zip
$ unzip Baseline/Baseline_S2/DTMCs/DTMCs.zip -d Baseline/Baseline_S2/DTMCs/
$ rm Baseline/Baseline_S2/DTMCs/DTMCs.zip
$ unzip Baseline/Baseline_S3/DTMCs/DTMCs.zip -d Baseline/Baseline_S3/DTMCs/
$ rm Baseline/Baseline_S3/DTMCs/DTMCs.zip
```

Note: If you want to run the 

## 1. AdapTA
### **Scenario 1**:
1. Enter the folder with scripts:
```
$ cd AdapTA/S1_SensorDeactivation/Scripts/
```
2. Transform transition matrices into patients:
```
$ python 0_convert_tm_into_patient.py
```
3. Prepare the SA-BSN to AdapTA-S1:
```
$ python 1_copy_needed_files_s1.py
```
4. Run the SA-BSN:
```
$ bash 2_script_all_profiles.sh
```
5. Parse the log files:
```
$ python 3_script_read.py
```

### **Scenario 2**:
1. Enter the folder with scripts:
```
$ cd AdapTA/S2_PatientProfile/Scripts/
```
2. Transform transition matrices into patients:
```
$ python 0_convert_tm_into_patient.py
```
3. Prepare the SA-BSN to AdapTA-S1:
```
$ python 1_copy_needed_files_s2.py
```
4. Run the SA-BSN:
```
$ bash 2_script_all_profiles.sh
```
5. Parse the log files:
```
$ python 3_read_all_output.py
```

### **Scenario 3**:
1. Enter the folder with scripts:
```
$ cd AdapTA/S3_CriticalCondition/Scripts/
```
2. Transform transition matrices into patients:
```
$ python 0_convert_tm_into_patient.py
```
3. Prepare the SA-BSN to AdapTA-S1:
```
$ python 1_copy_needed_files_s3.py
```
4. Run the SA-BSN:
```
$ bash 2_script_all_profiles.sh
```
5. Parse the log files:
```
$ python 3_read_all_output.py
```
## 2. Baseline
### **Scenario 1**:
1. Enter the folder with scripts:
```
$ cd Baseline/Baseline_S1/Scripts/
```
2. Transform transition matrices into patients:
```
$ python 0_convert_tm_into_patient.py
```
3. Prepare the SA-BSN to AdapTA-S1:
```
$ python 1_copy_needed_files_s1.py
```
4. Run the SA-BSN:
```
$ bash 2_script_all_profiles.sh
```
5. Parse the log files:
```
$ python 3_script_read_baseline.py
```

### **Scenario 2**:
1. Enter the folder with scripts:
```
$ cd Baseline/Baseline_S2/Scripts/
```
2. Transform transition matrices into patients:
```
$ python 0_convert_tm_into_patient.py
```
3. Prepare the SA-BSN to AdapTA-S1:
```
$ python 1_copy_needed_files_s2.py
```
4. Run the SA-BSN:
```
$ bash 2_script_all_profiles.sh
```
5. Parse the log files:
```
$ python 3_read_all_output.py
```

### **Scenario 3**:
1. Enter the folder with scripts:
```
$ cd Baseline/Baseline_S3/Scripts/
```
2. Transform transition matrices into patients:
```
$ python 0_convert_tm_into_patient.py
```
3. Prepare the SA-BSN to AdapTA-S1:
```
$ python 1_copy_needed_files_baseline.py
```
4. Run the SA-BSN:
```
$ bash 2_script_all_profiles.sh
```
5. Parse the log files:
```
$ python 3_read_all_output
```

