#include "component/CentralHub.hpp"
//#include <sstream>
#include <iostream>
#include <string>

//CHANGED
CentralHub::CentralHub(int &argc, char **argv, const std::string &name, const bool &active, const bsn::resource::Battery &battery) : Component(argc, argv, name), active(active), max_size(20), total_buffer_size(0), buffer_size({0,0,0,0,0,0}), battery(battery), data_buffer({{0},{0},{0},{0},{0},{0}}),raw_data_buffer({{0},{0},{0},{0},{0},{0}}) {}

CentralHub::~CentralHub() {}

int32_t CentralHub::run() {
	setUp();
    ros::NodeHandle nh;
    ros::Subscriber thermometerSub = nh.subscribe("thermometer_data", 10, &CentralHub::collect, this);
    ros::Subscriber oximeterSub = nh.subscribe("oximeter_data", 10, &CentralHub::collect, this);
    ros::Subscriber ecgSub = nh.subscribe("ecg_data", 10, &CentralHub::collect, this);
    ros::Subscriber abpsSub = nh.subscribe("abps_data", 10, &CentralHub::collect, this);
    ros::Subscriber abpdSub = nh.subscribe("abpd_data", 10, &CentralHub::collect, this);
    ros::Subscriber glucosemeterSub = nh.subscribe("glucosemeter_data", 10, &CentralHub::collect, this);
    ros::Subscriber reconfigSub = nh.subscribe("reconfigure_"+ros::this_node::getName(), 10, &CentralHub::reconfigure, this);

    ros::Subscriber eventSub = nh.subscribe("collect_event",10,&CentralHub::getEvent,this); //SAMIRA ADDED

    while(ros::ok()) {
        ros::Rate loop_rate(rosComponentDescriptor.getFreq());
        try {
            body();
        } catch (const std::exception& e) {
            sendStatus("fail");
        }
        loop_rate.sleep();
    }

    return 0;
}


void CentralHub::getEvent(const archlib::Event::ConstPtr& msg) { //SAMIRA ADDED
        std::string source=msg->source;
        std::string sensor_name;
        //std::cout<<source<<std::endl;
        if(source=="/g3t1_1"){
            sensor_name="Oxi";
        }else if(source=="/g3t1_2"){
            sensor_name="Ecg";
        }else if(source=="/g3t1_3"){
            sensor_name="Trm";
        }else if(source=="/g3t1_4"){
            sensor_name="Abps";     
        }else if(source=="/g3t1_5"){
            sensor_name="Abpd";
        }else if(source=="/g3t1_6"){
            sensor_name="Glc";
        }else{
            sensor_name=source;
        }
		std::cout<<sensor_name<<" "<<msg->content<<"!!!!!!!!!!!!!!!!!!!!"<<std::endl;	
}
	


void CentralHub::body() {
    ros::spinOnce(); //calls collect() if there's data in the topics

    if (!isActive() && battery.getCurrentLevel() > 90){
        turnOn();
    } else if (isActive() && battery.getCurrentLevel() < 2){
        turnOff();        
    }
    
    if(isActive()) {
        if(total_buffer_size > 0){
            apply_noise();
            process();
            transfer();
            sendStatus("success");
        }
    } else {
        recharge();
        throw std::domain_error("out of charge");
    }
}

void CentralHub::apply_noise() {}


void CentralHub::reconfigure(const archlib::AdaptationCommand::ConstPtr& msg) {
    std::string action = msg->action.c_str();

    std::vector<std::string> pairs = bsn::utils::split(action, ',');

    for (std::vector<std::string>::iterator it = pairs.begin(); it != pairs.end(); ++it){
        std::vector<std::string> param = bsn::utils::split(action, '=');

        // Why does replicate_collect updates frequency?
        /*if(param[0]=="replicate_collect"){
            rosComponentDescriptor.setFreq(rosComponentDescriptor.getFreq()+stoi(param[1]));
        }*/
        if(param[0]=="freq"){
            double new_freq = stod(param[1]);
            rosComponentDescriptor.setFreq(new_freq);
            
        }
    }
}

bool CentralHub::isActive() {
    return active;
}

void CentralHub::turnOn() {
    active = true;
    activate();
}

void CentralHub::turnOff() {
    active = false;
    deactivate();
}

/*  battery will always recover in 20seconds
    *
    *  b/s = 100% / 20 seconds = 5 %/s 
    *      => recovers 5% battery per second
    *  if we divide by the execution frequency
    *  we get the amount of battery we need to
    *  recover per execution cycle to achieve the
    *  5 %/s battery recovery rate
    */
void CentralHub::recharge() {
    if(battery.getCurrentLevel() <= 100) 
        battery.generate((100.0/20.0)/rosComponentDescriptor.getFreq());
}   
