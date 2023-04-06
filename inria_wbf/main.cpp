#include <chrono>
#include <ctime>
#include <iostream>
#include <map>
#include <stdio.h>
#include <vector>

#include <boost/filesystem.hpp>
#include <boost/program_options.hpp>

#include <robot_dart/robot.hpp>
#include <robot_dart/robot_dart_simu.hpp>
#include <robot_dart/sensor/force_torque.hpp>
#include <robot_dart/sensor/imu.hpp>
#include <robot_dart/sensor/torque.hpp>

#include <yaml-cpp/yaml.h>

#include "controller.hpp"
#include "inria_wbc/behaviors/behavior.hpp"
#include "inria_wbc/robot_dart/cmd.hpp"

#ifdef GRAPHIC
#include <robot_dart/gui/magnum/graphics.hpp>
#endif

using namespace robot_dart;
using namespace robot_dart::sensor;
using namespace robot_dart::gui;
using namespace robot_dart::magnum;
using namespace std::chrono_literals;

int main()
{
    // Set up the simulation and the world
    auto simu = std::make_shared<RobotDARTSimu>();
    auto world = simu->world();
    
    // Create the robot from the URDF file
    auto robot = std::make_shared<Robot>("path/to/your/urdf/file.urdf");

    // Add the robot to the simulation and set the gravity
    simu->add_robot(robot);
    simu->set_gravity(Eigen::Vector3d(0, 0, -9.81));
    
    // Create the controller for the robot
    auto controller = std::make_shared<Controller>(robot);

    // Add the controller to the simulation
    simu->add_controller(controller);

    // Create the behavior for the robot
    auto behavior = std::make_shared<inria_wbc::behaviors::Behavior>(
        "path/to/your/behavior/file.yaml",
        controller
    );

    // Add the behavior to the simulation
    simu->add_behavior(behavior);

    // Create the sensors for the robot
    auto ft_sensor = std::make_shared<ForceTorqueSensor>("ft_sensor");
    auto imu_sensor = std::make_shared<IMUSensor>("imu_sensor");
    auto torque_sensor = std::make_shared<TorqueSensor>("torque_sensor");
    
    // Add the sensors to the simulation
    robot->add_sensor(ft_sensor);
    robot->add_sensor(imu_sensor);
    robot->add_sensor(torque_sensor);

    // Set up the simulation parameters (time step, duration, etc.)
    double dt = 0.001;
    double duration = 10.0;
    int steps = static_cast<int>(duration / dt);
    
    // Run the simulation
    for (int i = 0; i < steps; i++) {
        // Update the sensors and the controller
        simu->step(dt);

        // Output the command to the robot
        inria_wbc::robot_dart::set_commands(*robot, controller->commands());
    }
    
    return 0;
}