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
$ git clone https://github.com/fedebotu/clone-anonymous-github.git && cd clone-anonymous-github
$ python3 src/download.py --url https://anonymous.4open.science/r/AdapTA_Paper_AST-3715/
$ cd AdapTA_Paper_AST-3715/

